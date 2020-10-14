import boto3
aws_mag_con=boto3.session.Session(profile_name="Abhay-Personal")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
"""
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)
    
#aws_mag_con=boto3.session.Session(profile_name="root")
s3_con=aws_mag_con.resource('s3')

for each in s3_con.buckets.all():
    print(each.name)
"""  
"""  
ec2 = aws_mag_con.resource('ec2')
for instance in ec2.instances.all():
   print (instance.id)
  # ec2.create_tags(Resources=[instance.id, ], Tags=[{'Key': 'India_name', 'Value': "abhay jain"}, ])
"""

f1={"Name": "tag:Company", "Values":['Guru']}
print(type(f1))
np_sers_ids=[]

for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
    	for each_in in each_item['Instances']:
	    	np_sers_ids.append(each_in['InstanceId'])

for e in np_sers_ids:
 print(e)

'''
ec2 = aws_mag_con.resource('ec2')
for each_tag in np_sers_ids:
 ec2.create_tags(Resources=[each_tag], Tags=[{'Key': 'Name', 'Value': "Sucseess jain"}, ]
'''