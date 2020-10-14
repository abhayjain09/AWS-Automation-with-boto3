import boto3
import json


aws_mag_con=boto3.session.Session(profile_name="Abhay-Personal")
ec2_con_res = aws_mag_con.resource('ec2')
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
s3_con_res = aws_mag_con.resource('s3')
s3_con_cli = aws_mag_con.client(service_name="s3",region_name="us-east-1")

bucketname="test-abhay"

for key in s3_con_cli.list_objects(Bucket=bucketname)['Contents']:
     itemname=(key['Key'])
     obj = s3_con_res.Object(bucketname, itemname)
     body = obj.get()['Body'].read().decode() 
     #print((body))
     json_load =json.loads(body)
     print((json_load))
     a=(json_load['key'])
     b=(json_load['Values'])
     print (a)
     print (b)
     print(type(a))
     print(type(b))
     for instance in ec2_con_res.instances.all():
       print (instance.id)
  #     for each in str1:
   #           print(type(each))
       ec2_con_res.create_tags(Resources=[instance.id, ], Tags= [{'Key': a , 'Value': b}, ], )
