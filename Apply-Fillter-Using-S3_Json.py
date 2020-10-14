import boto3
import json

aws_mag_con=boto3.session.Session(profile_name="Abhay-Personal")
ec2_con_res = aws_mag_con.resource('ec2')
ec2_con_cli =aws_mag_con.client(service_name="ec2",region_name="us-east-1")
s3_con_res = aws_mag_con.resource('s3')
s3_con_cli = aws_mag_con.client(service_name="s3",region_name="us-east-1")

bucketname="test-abhay"
np_sers_ids = []

for key in s3_con_cli.list_objects(Bucket=bucketname)['Contents']:
     np_sers_ids = []
     itemname=(key['Key'])
     obj = s3_con_res.Object(bucketname, itemname)
     body = obj.get()['Body'].read().decode() 
     #print((body))
     json_load =json.loads(body)
     print(json_load)
     Company_var=(json_load['Company'])
     print(Company_var)
     Tag_var = (json_load['Tag_List'])
     f1={"Name": "tag:Company", "Values":[Company_var]}
     #Logic for Get list of EC2 instanceID
     for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
    	 for each_in in each_item['Instances']:
             print(each_in['InstanceId'])
             np_sers_ids.append(each_in['InstanceId'])

     #Logic for Get list of EC2 VPC_ID
     for each_item in ec2_con_cli.describe_vpcs(Filters=[f1])['Vpcs']:
    	   (each_item['VpcId'])

     #Logic for Get list of EIP AllocationID
     for each_item in ec2_con_cli.describe_addresses(Filters=[f1])['Addresses']:
         np_sers_ids.append(each_item['AllocationId'])



     ec2_con_res.create_tags(Resources= np_sers_ids, Tags= Tag_var, )
  
     
    
     

