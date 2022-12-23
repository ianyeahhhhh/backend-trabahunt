import boto3
from botocore.config import Config
from boto3.s3.transfer import TransferConfig
import os

from sqlalchemy.orm import Session
from fastapi import File, UploadFile
from fastapi import APIRouter, Depends
from database import get_db
from models import Files
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

# S3 Bucket Resource 
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-southeast-1',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)

bucket = s3.Bucket(os.getenv('AWS_BUCKET_NAME'))
bucket_name = os.getenv('AWS_BUCKET_NAME')


# S3 Bucket Client
S3 = boto3.client(
    's3',
    region_name='ap-southeast-1',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
)


router = APIRouter(
    prefix='/aws_files',
    tags=['AWS_Files']
)

@router.post('/')
async def post(pdf_file: UploadFile = File(...)):

    if pdf_file.content_type == 'application/pdf':
        if pdf_file is not None:
            bucket.upload_fileobj(pdf_file.file, pdf_file.filename, ExtraArgs={'ContentType': pdf_file.content_type})

        data = Files(
            file_name = pdf_file.filename,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
    else:
        data = 'Please select a PDF file.'


    return data