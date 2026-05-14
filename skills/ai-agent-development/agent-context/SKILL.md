---
name: agent-context
description: >-
  Guides context management for AI agents: RAG pipelines, knowledge graphs,
  embeddings, conversation memory, and context window strategies. Use when
  adding external knowledge to agents or managing long conversations.
---

# Agent Context

Patterns for providing agents with knowledge beyond the LLM's training data. Covers retrieval-augmented generation (RAG), knowledge graphs, embedding strategies, conversation memory, and context window management.

## When to use

- Building a RAG pipeline (document ingestion → chunking → embedding → retrieval → generation)
- Integrating a knowledge graph as a context source
- Managing conversation history that exceeds the context window
- Choosing between vector search, BM25, and hybrid retrieval
- Designing the chunking strategy for a document corpus

## RAG pipeline

```text
Documents → Ingestion → Chunking → Embedding → Vector Store
                                                     │
User query → Embedding → Similarity search ──────────┘
                                  │
                           Retrieved chunks
                                  │
                    System prompt + chunks + query → LLM → Response
```

### Ingestion

- Support multiple file types: PDF, DOCX, Markdown, HTML, plain text
- Extract metadata (title, author, date, source URL) for filtering
- Track document versions for re-indexing

### Chunking strategies

| Strategy | Description | Best for |
|----------|-------------|----------|
| Fixed-size | Split by character/token count with overlap | General purpose, predictable chunk sizes |
| Recursive | Split by structure (paragraphs, sentences, words) with fallback | Structured documents |
| Semantic | Group by topic similarity using embeddings | Topic-coherent retrieval |
| Document-aware | Respect headings, sections, tables | Technical documentation |

- **Overlap** — 10-20% overlap between chunks prevents splitting mid-sentence
- **Chunk size** — 256-1024 tokens is typical; smaller for precision, larger for context

### Embedding models

| Model | Dimensions | On-premises | Notes |
|-------|-----------|-------------|-------|
| `all-MiniLM-L6-v2` | 384 | Yes (sentence-transformers) | Fast, good baseline |
| `nomic-embed-text` | 768 | Yes (Ollama) | Strong open-source option |
| `text-embedding-3-small` | 1536 | No (OpenAI API) | High quality, cloud-only |
| `text-embedding-3-large` | 3072 | No (OpenAI API) | Highest quality, cloud-only |

### Retrieval strategies

| Strategy | Mechanism | Strengths |
|----------|-----------|-----------|
| Dense (vector) | Cosine similarity on embeddings | Semantic matching |
| Sparse (BM25) | Term frequency–inverse document frequency | Exact keyword matches |
| Hybrid | Weighted combination of dense + sparse | Best of both approaches |
| Re-ranking | Score initial results with a cross-encoder | Higher precision at retrieval time |

## Knowledge graphs

Use a knowledge graph when relationships between entities matter more than text similarity.

- **Triple store** — (subject, predicate, object) facts; query with SPARQL or Cypher
- **Graph RAG** — combine graph traversal with text retrieval for relationship-aware answers
- **Entity extraction** — extract entities from documents and link them to the graph
- **Tools:** Neo4j, Amazon Neptune, Apache Jena, or in-memory graphs (NetworkX)

### When to prefer a knowledge graph over vector search

- Domain has well-defined entities and relationships (medical ontologies, org charts)
- Questions involve multi-hop reasoning ("Who reports to the manager of project X?")
- Factual accuracy matters more than semantic similarity
- Data changes frequently and must be updated without re-embedding

## Conversation memory

| Pattern | Description | Use when |
|---------|-------------|----------|
| Full history | Include all messages in prompt | Short conversations, small context windows |
| Sliding window | Keep last N messages | Long conversations with recent-context focus |
| Summarisation | Periodically summarise older messages | Very long sessions, memory-constrained |
| Semantic memory | Store and retrieve relevant past messages by similarity | Agents that recall across sessions |

## Context window management

- **Token counting** — count tokens before sending to avoid truncation (use `tiktoken` for OpenAI, model-specific tokenisers for others)
- **Priority ordering** — system prompt > retrieved context > conversation history > user message
- **Truncation strategy** — drop oldest messages first; never truncate the system prompt or current user message
- **Compression** — summarise retrieved documents before injection to fit more sources

## Integration with other skills

- [agent-types](../agent-types/SKILL.md) — RAG agent pattern
- [agent-llm-providers](../agent-llm-providers/SKILL.md) — embedding model selection per provider
- [fair-data-principles](../../fair-data-principles/SKILL.md) — FAIR-aligned metadata for retrieved documents
- [design-data-model](../../design/design-data-model/SKILL.md) — document and chunk data models
