from fastapi import FastAPI
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

app = FastAPI()

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

@app.post("/chat")
async def chat(user_message: str):
    response = client.complete(
        messages=[
            SystemMessage("You are a helpful assistant."),
            UserMessage(user_message),
        ],
        temperature=1.0,
        top_p=1.0,
        model=model
    )
    return {"response": response.choices[0].message.content}
