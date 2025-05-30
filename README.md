# 🚀 FastAPI + MongoDB Deployment with Pulumi (AWS EC2)

This project uses [Pulumi](https://www.pulumi.com/) to deploy a fully operational **FastAPI + MongoDB** backend onto an AWS EC2 instance.

It:

* Provisions an EC2 instance
* Installs MongoDB locally
* Installs Python and dependencies
* Clones your FastAPI project from GitHub
* Runs the FastAPI app with Uvicorn

---

## 🌐 Requirements

* An AWS account
* Python 3.9+
* [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
* [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* `git`

---

## 🛠 Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yoavgre/parkingLotDeploy.git
cd parkingLotDeploy
```

### 2. Set up a Python virtual environment

To isolate your dependencies, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:

```bash
pip install pulumi pulumi-aws
```

### 4. Configure AWS CLI

```bash
aws configure
```

Enter your:

* **AWS Access Key ID**
* **AWS Secret Access Key**
* **Default region** (e.g. `us-east-1`)

---

## 🚀 Deploy the FastAPI App to AWS

### 1. Login to Pulumi

```bash
pulumi login --local
```

Or use Pulumi Cloud (optional):

```bash
pulumi login
```

### 2. Deploy

```bash
pulumi up
```

* Review the preview
* Type `yes` to apply the changes

This will:

1. Launch an EC2 instance
2. Install MongoDB
3. Clone your FastAPI app
4. Run it with Uvicorn

---

## 🌍 Access the Running App

After deployment, Pulumi outputs something like:

```
Outputs:
    public_ip: "3.91.120.25"
    url      : "http://ec2-3-91-120-25.compute-1.amazonaws.com"
```

Open the **url** in your browser and append `/docs` for Swagger UI to see the live API! 🎉

---
