from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.chains.rag_chain import run_rag

router = APIRouter()


@router.post("/conversation")
async def conversation(payload: dict):

    user_message = payload.get(
        "message",
        ""
    )

    stream = run_rag(user_message)

    async def generate():

        for chunk in stream:

            if chunk.choices:

                delta = (
                    chunk.choices[0]
                    .delta
                    .content
                )

                if delta:
                    yield delta

    return StreamingResponse(
        generate(),
        media_type="text/plain",
    )