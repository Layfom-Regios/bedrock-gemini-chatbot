import boto3
import os
from dotenv import load_dotenv

load_dotenv()

client = boto3.client("bedrock-agent", region_name=os.getenv("AWS_REGION"))

def sync_kb(data_source_id):
    response = client.start_ingestion_job(
        knowledgeBaseId=os.getenv("KNOWLEDGE_BASE_ID"),
        dataSourceId=data_source_id
    )
    print(response)

# Replace with your data source ID
sync_kb("your_data_source_id")