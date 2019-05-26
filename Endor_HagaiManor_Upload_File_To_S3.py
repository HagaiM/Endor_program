import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = None
SECRET_KEY = None

local_file = '/Users/hagaimanor/Downloads/ETH_USD_agg.csv'
bucket_name = 'athena-dev-task'
s3_file_name = 'hagaimanor/ETH_USD_agg.csv'

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except NoCredentialsError:
        print("Credentials not available")
        return False



uploaded = upload_to_aws(local_file, bucket_name, s3_file_name)

##cli command
#aws s3 cp /Users/hagaimanor/Downloads/ETH_USD_agg.csv s3://s3-eu-west-1.amazonaws.com/athena-dev-task/hagai-manor/ETH_USD_agg.csv
#Err ->#upload failed: Downloads/ETH_USD_agg.csv to s3://s3-eu-west-1.amazonaws.com/athena-dev-task/hagaimanor/ETH_USD_agg.csv Unable to locate credentials

