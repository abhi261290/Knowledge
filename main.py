from fastapi import FastAPI, Depends
from pydantic import BaseModel
from openai import AzureOpenAI
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from app.settings import settings
from app.auth import verify_token

app = FastAPI(title="Internal Chatbot")

client = AzureOpenAI(
    api_key=settings.OPENAI_KEY,
    azure_endpoint=settings.OPENAI_ENDPOINT,
    api_version="2024-02-01"
)

search_client = SearchClient(
    endpoint=settings.SEARCH_ENDPOINT,
    index_name=settings.SEARCH_INDEX,
    credential=AzureKeyCredential(settings.SEARCH_KEY)
)

class ChatRequest(BaseModel):
    question: str

@app.post("/chat", dependencies=[Depends(verify_token)])
def chat(req: ChatRequest):
    results = search_client.search(req.question, top=3)
    context = "\n".join([r["content"] for r in results])

    prompt = f"""
You are an internal company assistant.
Answer ONLY using the context below.
If not found, say "Information not available".

Context:
{context}

Question:
{req.question}
"""

    response = client.chat.completions.create(
        model=settings.OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}]
    )

    return {
        "answer": response.choices[0].message.content.strip()
    }
