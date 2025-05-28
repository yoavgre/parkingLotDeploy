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
git clone https://github.com/YOUR_USERNAME/parkingLotDeploy.git
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

Open the **url** in your browser (append `/docs` for Swagger UI) to see your live API! 🎉

---

## 🔁 Updating Code

Push new commits to **fastApiProject1** and redeploy:

```bash
pulumi up
```

---

## 🧹 Tear‑down

Delete all AWS resources to stop billing:

```bash
pulumi destroy
```

---

## 📁 Project Structure

```
Pulumi.yaml           # Project metadata
Pulumi.dev.yaml       # Stack config (exclude if it contains secrets)
__main__.py           # Pulumi Python deployment script
requirements.txt      # Python dependencies
.gitignore
README.md             # This file
```

---

## 📦 FastAPI App Expectations

Your FastAPI GitHub repo should:

* Be public or cloneable via HTTPS
* Contain `main.py` (or similar) defining `app = FastAPI()`
* Use `mongodb://localhost:27017/` as the DB URL

Example `main.py`:

```python
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["parking_db"]

@app.get("/")
async def root():
    return {"status": "API running"}
```

---

## 🛑 Do NOT Commit Sensitive Files

Add these to `.gitignore`:

```
.venv/
.env
*.pem
Pulumi.*.yaml
```

---

## 📝 License

MIT
