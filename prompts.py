QUERY_REWRITE_PROMPT = """
Rewrite the user's question to be optimal for semantic vector search.
Do NOT answer the question.

Original question:
{question}

Rewritten query:
"""

ANSWER_PROMPT = """
You are an assistant answering questions ONLY using the provided context.

Context:
{context}

Question:
{question}

Instructions:
- Use only the context
- If unsure, say "I don't know"
- Cite sources

Answer:
"""
