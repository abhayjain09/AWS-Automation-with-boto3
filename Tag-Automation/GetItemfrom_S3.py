import boto3

aws_mag_con=boto3.session.Session(profile_name="Abhay-Personal")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

s3 = aws_mag_con.resource('s3')
bucketname="test-abhay"
itemname="Uat_tag.json"
obj = s3.Object(bucketname, itemname)
body = obj.get()['Body'].read()
print(body)