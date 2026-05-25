#!/usr/bin/env bash
# Validate SKILL.md frontmatter against the agentskills.io specification.
# https://agentskills.io/specification
#
# Usage: bash scripts/validate-skill-frontmatter.sh [skills-directory]
#   Default directory: skills/
#
# Exit codes:
#   0 — all skills passed
#   1 — one or more skills failed validation

set -euo pipefail

SKILLS_DIR="${1:-skills}"
passed=0
failed=0
failed_files=()

# Extract the raw value after "key:" from frontmatter text.
# Handles both bare values and quoted values (single or double quotes).
extract_field() {
  local frontmatter="$1"
  local key="$2"
  local line
  line=$(echo "$frontmatter" | grep -m1 "^${key}:" || true)
  if [[ -z "$line" ]]; then
    echo ""
    return
  fi
  local value="${line#*: }"
  # Strip surrounding quotes if present
  value="${value#\"}"
  value="${value%\"}"
  value="${value#\'}"
  value="${value%\'}"
  # Trim leading/trailing whitespace
  value="$(echo "$value" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')"
  echo "$value"
}

validate_skill() {
  local file="$1"
  local errors=()

  # --- Frontmatter extraction ---
  # Read the file content and check for --- delimiters
  local content
  content=$(cat "$file")

  local first_line
  first_line=$(head -n1 "$file" | tr -d '\r')
  if [[ "$first_line" != "---" ]]; then
    errors+=("missing YAML frontmatter (file does not start with ---)")
    printf "  FAIL  %s\n" "$file"
    for err in "${errors[@]}"; do
      printf "        - %s\n" "$err"
    done
    return 1
  fi

  # Extract frontmatter between first and second --- (strip \r for CRLF files)
  local frontmatter
  frontmatter=$(awk 'NR==1 && /^---\r?$/{found=1; next} found && /^---\r?$/{exit} found{print}' "$file" | tr -d '\r')

  if [[ -z "$frontmatter" ]]; then
    errors+=("empty YAML frontmatter")
    printf "  FAIL  %s\n" "$file"
    for err in "${errors[@]}"; do
      printf "        - %s\n" "$err"
    done
    return 1
  fi

  # --- name validation ---
  local name
  name=$(extract_field "$frontmatter" "name")

  if [[ -z "$name" ]]; then
    errors+=("missing required field: name")
  else
    local name_len=${#name}
    if (( name_len > 64 )); then
      errors+=("name exceeds 64 characters (got ${name_len})")
    fi

    if ! echo "$name" | grep -qE '^[a-z0-9]([a-z0-9-]*[a-z0-9])?$'; then
      errors+=("name '${name}' does not match pattern: lowercase alphanumeric + hyphens, no leading/trailing/consecutive hyphens")
    fi

    if echo "$name" | grep -q '\-\-'; then
      errors+=("name '${name}' contains consecutive hyphens")
    fi

    # name must match parent directory
    local parent_dir
    parent_dir=$(basename "$(dirname "$file")")
    if [[ "$name" != "$parent_dir" ]]; then
      errors+=("name '${name}' does not match parent directory '${parent_dir}'")
    fi
  fi

  # --- description validation ---
  local description
  description=$(extract_field "$frontmatter" "description")

  if [[ -z "$description" ]]; then
    errors+=("missing required field: description")
  else
    local desc_len=${#description}
    if (( desc_len > 1024 )); then
      errors+=("description exceeds 1024 characters (got ${desc_len})")
    fi
  fi

  # --- compatibility validation (optional, max 500 chars) ---
  local compatibility
  compatibility=$(extract_field "$frontmatter" "compatibility")
  if [[ -n "$compatibility" ]]; then
    local compat_len=${#compatibility}
    if (( compat_len > 500 )); then
      errors+=("compatibility exceeds 500 characters (got ${compat_len})")
    fi
  fi

  # --- Report ---
  if [[ ${#errors[@]} -eq 0 ]]; then
    printf "  OK    %s\n" "$file"
    return 0
  else
    printf "  FAIL  %s\n" "$file"
    for err in "${errors[@]}"; do
      printf "        - %s\n" "$err"
    done
    return 1
  fi
}

# --- Main ---
if [[ ! -d "$SKILLS_DIR" ]]; then
  echo "Error: directory '${SKILLS_DIR}' does not exist." >&2
  exit 1
fi

echo "Validating SKILL.md frontmatter in ${SKILLS_DIR}/ ..."
echo ""

while IFS= read -r -d '' skill_md; do
  if validate_skill "$skill_md"; then
    passed=$(( passed + 1 ))
  else
    failed=$(( failed + 1 ))
    failed_files+=("$skill_md")
  fi
done < <(find "$SKILLS_DIR" -name 'SKILL.md' -print0 | sort -z)

echo ""
echo "--- Summary ---"
echo "Passed: ${passed}"
echo "Failed: ${failed}"
echo "Total:  $(( passed + failed ))"

if [[ "$failed" -gt 0 ]]; then
  echo ""
  echo "Failed files:"
  for f in "${failed_files[@]}"; do
    echo "  - ${f}"
  done
  exit 1
fi
