"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('my-bucket',
    website=s3.BucketWebsiteArgs(
        index_document="index.html",
    ))

# Create a new bucket object 
# Add an ACL of public-read so that it can be accessed anonymously over the Internet, and a content type so that it is served as HTML
bucketObject = s3.BucketObject(
    'index.html',
    acl='public-read',
    content_type='text/html',
    bucket=bucket,
    source=pulumi.FileAsset('index.html'),
)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Export the resulting bucket’s endpoint URL so you can easily access it
pulumi.export('bucket_endpoint', pulumi.Output.concat('http://', bucket.website_endpoint))