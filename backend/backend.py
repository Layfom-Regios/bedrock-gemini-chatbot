import boto3
import os
from dotenv import load_dotenv

load_dotenv()

bedrock_agent_runtime = boto3.client(
    "bedrock-agent-runtime",
    region_name=os.getenv("AWS_REGION")
)

def retrieve_context(query):
    response = bedrock_agent_runtime.retrieve(
        knowledgeBaseId=os.getenv("KNOWLEDGE_BASE_ID"),
        retrievalQuery={
            "text": query
        },
        retrievalConfiguration={
            "vectorSearchConfiguration": {
                "numberOfResults": 3
            }
        }
    )

    chunks = []
    for result in response["retrievalResults"]:
        chunks.append(result["content"]["text"])

    return chunks