import os

s3_bucket_name = os.environ["s3_bucket_name"] if "s3_bucket_name" in os.environ else ""
s3_region_name = os.environ["s3_region_name"] if "s3_region_name" in os.environ else ""
s3_access_key_id = os.environ["s3_access_key_id"] if "s3_access_key_id" in os.environ else ""
s3_access_key = os.environ["s3_access_key"] if "s3_access_key" in os.environ else ""

bucket = {
    'access-key-id': s3_access_key_id,
    'secret-access-key': s3_access_key,
    'region': s3_region_name
}
