from fastapi import APIRouter
import uuid

router = APIRouter()


@router.post("/create-conversation")
async def create_conversation():

    conversation_id = str(
        uuid.uuid4()
    )

    return {
        "conversation_id":
            conversation_id,

        "conversation_url":
            f"https://tavus.example/{conversation_id}"
    }