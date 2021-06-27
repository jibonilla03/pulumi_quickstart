"""Deploy a Webserver to AWS EC2"""

import pulumi
import pulumi_aws as aws

# Define variable to and get AMI
size = 't2.micro'
ami = aws.ec2.getAmi(most_recent="true",
                  owners=["137112412989"],
                  filters=[{"name":"name","values":["amzn-ami-hvm-*"]}])

# Add security group to allow SSH access
group = aws.ec2.SecurityGroup('webserver-secgrp',
    description='Enable SSH access',
    ingress=[
        {'protocol': 'tcp', 'from_port' : 22, 'to_port': 22, 'cidr_blocks': ['0.0.0.0/0']}
    ])

# Provision EC2 instance
server = aws.ec2.Instance('webserver-www',
    isinstance_type=size,
    vpc_security_group_ids=[group.id], # reference security group from above
    ami=ami.id)

pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
    