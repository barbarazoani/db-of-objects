import os
import boto3
from dotenv import load_dotenv

load_dotenv(".env.development")

class Settings:
    def __init__(self):
        #AWS
        self.s3_bucket_name = os.getenv('S3_BUCKET_NAME', 'glacier-ml-training')
        self.aws_region = os.getenv('AWS_REGION', 'us-east-1')
        self.aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

        # Pinecone services
        self.api_key = os.getenv('PINECONE_API_KEY')
        self.index_name = os.getenv('PINECONE_INDEX_NAME')
        self.k = int(os.getenv("PINECONE_TOP_K", 20))
    
    def get_s3_client(self):
        return boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )
settings = Settings()
