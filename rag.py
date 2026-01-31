from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from prompts import QUERY_REWRITE_PROMPT, ANSWER_PROMPT
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)

load_dotenv()

DB_PATH = "vectorstore"

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
db = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

rewrite_prompt = PromptTemplate.from_template(QUERY_REWRITE_PROMPT)
answer_prompt = PromptTemplate.from_template(ANSWER_PROMPT)

def ask(question: str):
    rewritten = llm.invoke(
        rewrite_prompt.format(question=question)
    ).content

    logging.info(f"Rewritten query: {rewritten}")

    docs = db.similarity_search(rewritten, k=6)
    logging.info(f"Retrieved {len(docs)} chunks")

    context = "\n\n".join([d.page_content for d in docs])
    sources = list(set(d.metadata.get("source", "Unknown") for d in docs))

    answer = llm.invoke(
        answer_prompt.format(context=context, question=question)
    ).content

    return {"answer": answer, "sources": sources}
