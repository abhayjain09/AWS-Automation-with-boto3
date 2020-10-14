import boto3
import os

aws_mag_con=boto3.session.Session(profile_name="Abhay-Personal")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

s3_con_res = aws_mag_con.resource('s3')
s3_con_cli = aws_mag_con.client(service_name="s3",region_name="us-east-1")
bucketname="test-abhay"

for key in s3_con_cli.list_objects(Bucket=bucketname)['Contents']:
    print(key['Key'])
    
