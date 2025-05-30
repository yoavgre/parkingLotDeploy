import pulumi
import pulumi_aws as aws

# Get the latest Amazon Linux 2 AMI
ami = aws.ec2.get_ami(
    most_recent=True,
    owners=["amazon"],
    filters=[{
        "name": "name",
        "values": ["amzn2-ami-hvm-*-x86_64-gp2"]
    }]
)

# Create a security group that allows HTTP and SSH access
security_group = aws.ec2.SecurityGroup("fastapi-sg",
    description="Allow SSH and FastAPI access",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
        {"protocol": "tcp", "from_port": 8000, "to_port": 8000, "cidr_blocks": ["0.0.0.0/0"]},
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}
    ]
)

# EC2 startup script
user_data = """#!/bin/bash
yum update -y
yum install -y python3 git

# Install MongoDB
cat > /etc/yum.repos.d/mongodb-org-6.0.repo <<EOF
[mongodb-org-6.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2/mongodb-org/6.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-6.0.asc
EOF

yum install -y mongodb-org
systemctl start mongod
systemctl enable mongod

# Install Python dependencies
pip3 install fastapi uvicorn motor python-dotenv

# Clone the FastAPI app from GitHub
cd /home/ec2-user
git clone https://github.com/yoavgre/parkingLotManager.git
cd YOUR_REPO

# Run FastAPI app
nohup uvicorn main:app --host 0.0.0.0 --port 80 &
"""

# Create EC2 instance
instance = aws.ec2.Instance("fastapi-instance",
    instance_type="t2.micro",
    ami=ami.id,
    vpc_security_group_ids=[security_group.id],
    user_data=user_data,
    tags={"Name": "FastAPIApp"}
)

# Output the public IP and URL
pulumi.export("public_ip", instance.public_ip)
pulumi.export("url", pulumi.Output.concat("http://", instance.public_dns))
