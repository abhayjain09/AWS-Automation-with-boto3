import boto3

aws_mag_con=boto3.session.Session(profile_name="Abhay-Personal")
"""
iam_con=aws_mag_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)
    
#aws_mag_con=boto3.session.Session(profile_name="root")
s3_con=aws_mag_con.resource('s3')

for each in s3_con.buckets.all():
    print(each.name)
"""    
ec2 = aws_mag_con.resource('ec2')
for instance in ec2.instances.all():
   print (instance.id)
   ec2.create_tags(Resources=[instance.id, ], Tags=[{'Key': 'India_name', 'Value': "abhay jain"}, {'Key': 'Name', 'Value': "abhay jain"}])