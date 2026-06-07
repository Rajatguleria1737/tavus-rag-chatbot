from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.conversation import router
from app.routes.tavus import router as rag_router

app = FastAPI(
    title="Tavus RAG Chatbot"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(rag_router)