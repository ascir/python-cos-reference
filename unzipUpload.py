import ibm_boto3
from ibm_botocore.client import Config, ClientError
import zipfile
import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

with zipfile.ZipFile('./selfhosted_test.zip', 'r') as zip_ref:
    zip_ref.extractall()
    extracted = zip_ref.namelist()
    # extracted_file = os.path.join(extract_dir, extracted[0])

print(extracted[0])



COS_ENDPOINT = os.getenv("COS_ENDPOINT")
COS_API_KEY_ID = os.getenv("COS_API_KEY_ID") # eg "W00YiRnLW4a3fTjMB-odB-2ySfTrFBIQQWanc--P3byk"

COS_SERVICE_CRN= os.getenv("COS_SERVICE_CRN")

BUCKET= os.getenv("BUCKET")

cos = ibm_boto3.client("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_SERVICE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT)

directory = extracted[0]

# iterate over files in
# that directory
c = 1
for subdir, dirs, files in os.walk(directory):
    for file in files:
        print(c)
        c+=1
        filename= os.path.join(subdir, file)
        cos.upload_file(Filename=filename,Bucket=BUCKET, Key= filename)
        print(f"Uploaded {filename}")
