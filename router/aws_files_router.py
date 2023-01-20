import boto3
import botocore
from botocore.config import Config
from boto3.s3.transfer import TransferConfig
import os

from sqlalchemy.orm import Session
from fastapi import File, UploadFile
from fastapi import APIRouter, Depends
from database import get_db
from models import Files
from datetime import datetime
from schemas import AWS_Form

from dotenv import load_dotenv
load_dotenv()

# S3 Bucket Resource
s3 = boto3.resource(
    service_name='s3', region_name='ap-southeast-1',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

bucket = s3.Bucket(os.getenv('AWS_BUCKET_NAME'))
bucket_name = os.getenv('AWS_BUCKET_NAME')

# S3 Bucket Client
S3 = boto3.client(
    's3', region_name='ap-southeast-1',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)


router = APIRouter(
    prefix='/aws_files',
    tags=['AWS_Files']
)


@router.get('/{obj_name}')
async def get_one(obj_name: str):
    # Check if file exists in the bucket. Prefix = filename
    result = S3.list_objects_v2(Bucket=bucket_name, Prefix=obj_name)

    if 'Contents' in result:
        url = boto3.client('s3').generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': obj_name},
            ExpiresIn=3600
        )
        return url

    else:
        return 'File does not exist'



@router.delete('/')
async def delete_file(req: AWS_Form):
    S3.delete_object(Bucket=bucket_name, Key=req.filename)
    return {
        'msg': 'File Deleted',
        'filename': req.filename
    }


@router.post('/')
async def post(pdf_file: UploadFile = File(...), db: Session = Depends(get_db)):
    if pdf_file is not None:
        bucket.upload_fileobj(
            pdf_file.file,
            pdf_file.filename,
            ExtraArgs={
                'ContentType': pdf_file.content_type
            })

        data = Files(
            file_name=pdf_file.filename,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )

        db.add(data)
        db.commit()
        data = "File Uploaded to S3 Bucket"

    else:
        data = 'Please select a file.'

    return data

