import boto3
import json

aws_mag_con=boto3.session.Session(profile_name="UAT-AWS")
ec2_con_res = aws_mag_con.resource('ec2')
ec2_con_cli =aws_mag_con.client(service_name="ec2",region_name="us-east-1")
s3_con_res = aws_mag_con.resource('s3')
s3_con_cli = aws_mag_con.client(service_name="s3",region_name="us-east-1")
c = 0



#fil = [{'Name': 'owner-id', 'Values': ['274138180186']}]

'''   
np_sers_ids = []   
for each_item in ec2_con_cli.describe_security_groups()['SecurityGroups']:
         print(each_item['GroupId'])
         c=c+1
         
           

print(c)
         
       
 '''        
#ec2_con_res.create_tags(Resources= np_sers_ids , Tags=[{'Key': 'India_name', 'Value': "abhay jain"}, ])

#print(co)


#bucketname="test-abhay"
np_sers_ids = []

#for key in s3_con_cli.list_objects(Bucket=bucketname)['Contents']:
#     np_sers_ids = []
#     itemname=(key['Key'])
 #    obj = s3_con_res.Object(bucketname, itemname)
  #   body = obj.get()['Body'].read().decode() 
     #print((body))
 #    json_load =json.loads(body)
 #    print(json_load)
 #    Company_var=(json_load['Company'])
 #    print(Company_var)
 #    Tag_var = (json_load['Tag_List'])
 #    f1={"Name": "tag:Company", "Values":[Company_var]}
     #Logic for Get list of EC2 instanceID
for each_item in ec2_con_cli.describe_instances()['Reservations']:
    	     for each_in in each_item['Instances']:
 #            print(each_in['InstanceId'])
                 np_sers_ids.append(each_in['InstanceId'])

     #Logic for Get list of EC2 VPC_ID
for each_item in ec2_con_cli.describe_vpcs()['Vpcs']:
    	   np_sers_ids.append(each_item['VpcId'])

     #Logic for Get list of EIP AllocationID
for each_item in ec2_con_cli.describe_addresses()['Addresses']:
         np_sers_ids.append(each_item['AllocationId'])

     
     # Logic for Get list of EC2 Snapshot_ID
owner_id_filter = [{'Name': 'owner-id', 'Values': ['274138180186']}]
for each_item in ec2_con_cli.describe_snapshots(Filters = owner_id_filter)['Snapshots']:
         np_sers_ids.append(each_item['SnapshotId'])

     # Logic for Get list of EC2 AMI IDs
owner_id_filter = [{'Name': 'owner-id', 'Values': ['274138180186']}]
for each_item in ec2_con_cli.describe_images(Filters = owner_id_filter)['Images']:
         np_sers_ids.append(each_item['ImageId'])
     
     # Logic for Get list of EC2 KeyPairId
for each_item in ec2_con_cli.describe_key_pairs()['KeyPairs']:
         np_sers_ids.append(each_item['KeyPairId'])

     # Logic for Get list of EC2 NatGatewayId
for each_item in ec2_con_cli.describe_nat_gateways()['NatGateways']:
         np_sers_ids.append(each_item['NatGatewayId'])

     # Logic for Get list of EC2 FleetId "there is no fleet on US-east-1" "Need to check"
for each_item in ec2_con_cli.describe_fleets()['Fleets']:
         np_sers_ids.append(each_item['FleetId'])


     # Logic for Get list of EC2 NetworkAclId
for each_item in ec2_con_cli.describe_network_acls()['NetworkAcls']:
         np_sers_ids.append(each_item['NetworkAclId'])
 
     # Logic for Get list of EC2 InternetGatewayId
for each_item in ec2_con_cli.describe_internet_gateways()['InternetGateways']:
         np_sers_ids.append(each_item['InternetGatewayId'])

     # Logic for Get list of EC2 describe_security_groups GroupId
for each_item in ec2_con_cli.describe_security_groups()['SecurityGroups']:
         np_sers_ids.append(each_item['GroupId'])


for i in np_sers_ids:
   print(i)
