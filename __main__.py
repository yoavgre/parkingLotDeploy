import pulumi
import pulumi_aws as aws

# Get the latest Amazon Linux
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
        {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]},
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}
    ]
)

# EC2 startup script
user_data = """#!/bin/bash
# Update and install required packages
sudo yum update -y
sudo yum install -y python3 git docker

# Start and enable Docker
sudo systemctl start docker
sudo systemctl enable docker

# Run MongoDB in Docker
sudo docker run -d --name mongodb -p 27017:27017 mongo:6

# Install pip and Python dependencies
sudo python3 -m ensurepip --upgrade
pip3 install fastapi uvicorn motor python-dotenv

# Clone the FastAPI app from GitHub
cd /home/ec2-user
git clone https://github.com/yoavgre/parkingLotManager.git
cd parkingLotManager

# Run FastAPI app (assumes app/main.py contains `app = FastAPI()`)
sudo nohup /usr/local/bin/uvicorn app.main:app --host 0.0.0.0 --port 80 &
"""

# Create the EC2 instance
instance = aws.ec2.Instance("fastapi-instance",
    instance_type="t2.micro",
    ami=ami.id,
    vpc_security_group_ids=[security_group.id],
    user_data=user_data,
    tags={"Name": "ParkingLotManager"}
)

# Output the public IP and URL
pulumi.export("public_ip", instance.public_ip)
pulumi.export("url", pulumi.Output.concat("http://", instance.public_dns))
pulumi.export("swagger_ui", pulumi.Output.concat("http://", instance.public_dns, "/docs"))
