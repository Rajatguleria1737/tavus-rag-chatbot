from app.prompts.system_prompt import SYSTEM_PROMPT
from app.services.elastic_service import vector_search
from app.services.llm_service import (
    create_embedding,
    stream_completion,
)


def run_rag(question):

    embedding = create_embedding(question)

    docs = vector_search(embedding)

    context = "\n\n".join(docs)

    prompt = SYSTEM_PROMPT.format(
        context=context,
        question=question,
    )

    return stream_completion(prompt)