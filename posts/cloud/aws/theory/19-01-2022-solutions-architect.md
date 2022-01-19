# AWS Exploration

## Setting up a S3 Bucket


## Setting up an EC2 Instance

1. 
2. Choose an Instance type
3. 
4. 
5. 

```
aws configure
AWS Access Key ID: 
AWS Secret Access Key:
Default region name [selected-region-name]:
Default output format [None]:
```


```
chmod 0400 KEYPAIR.pem 
shh -i KEYPAIR.pem ec2-user@IPV4address
```
If you selected Amazon Linux, you should now be able to see: 

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|



```
whoami
```
The whoami command should give the output: ec2-user

### Setting up an EBS volume

Select Instance> Storage> Select Volume ID> Create Volume > GiB size (2)> Availability Zone (same as instance name)> Create Volume

### Setting up an EBS Snapshot


### AMI: Amazon Machine Image
