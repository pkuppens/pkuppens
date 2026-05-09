# install-superpowers

Install and enable the `superpowers` plugin in Cursor, without overriding Cursor’s official `/add-plugin` command.

## Install

- Recommended (Cursor Plugins):
  - Run: `/add-plugin superpowers`
  - If prompted, reload Cursor.

- Open the **Extensions** view (usually `Ctrl+Shift+X`).
- Search for **"superpowers"**.
- Install the extension published by **Cursor** (often shown as `cursor-public`).
- If Cursor prompts you, click **Reload**.

If Marketplace search is flaky, open the plugin page and install from there:

- `https://cursor.com/marketplace/superpowers`

## Verify it is active

- Start a **new Agent chat**.
  - If Superpowers registers a `sessionStart` hook, you should see a **session-start prompt**.
  - On **Windows**, select a **Bash** shell:
    - **Git Bash** (recommended if you have Git for Windows installed), or
    - **WSL Bash** (if you use WSL).
- Then ask: **"Do you have superpowers?"**
- If it does not work:
  - Note: Superpowers is a **Cursor Plugin**. It may not show up in the **Extensions** list even when installed.
  - Ensure the extension is **enabled** for this workspace.
  - Reload Cursor once more.
  - Close and re-open the chat panel (rarely needed).

## Hooks (how they run)

Superpowers may register hooks (for example `sessionStart`). These hooks run **locally inside Cursor** when their event happens.

- You do **not** run hooks in Chrome.
- You usually do **not** run hooks manually in a terminal.
- To trigger a `sessionStart`-type hook, start a **new Agent chat** (or reload Cursor).

## Update or remove

- **Update**:
  - Open **Extensions** (`Ctrl+Shift+X`), then update **Superpowers** if an update is available.
  - Or use the command palette: **Extensions: Check for Extension Updates**.
- **Remove**:
  - Open **Extensions** (`Ctrl+Shift+X`) → **Superpowers** → **Uninstall** (or **Disable**).
  - Reload Cursor when prompted.

