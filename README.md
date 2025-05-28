# 🚗 Parking Lot App Deployment with Pulumi (AWS EC2 + FastAPI + MongoDB)

This project deploys a complete parking lot backend system built with **FastAPI** and **MongoDB** on a single **AWS EC2** instance using [Pulumi](https://www.pulumi.com/) and Python.

It:
- Provisions an EC2 instance
- Installs MongoDB locally on the instance
- Clones your FastAPI project from GitHub
- Installs Python dependencies
- Starts the server with `uvicorn`

---

## 🧰 Requirements

Before using this deployment, make sure you have:

- An [AWS account](https://aws.amazon.com/)
- Python 3.9 or newer
- [Pulumi CLI](https://www.pulumi.com/docs/get-started/install/)
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- `git`

---

## 🔧 Setup Instructions

### 1. Clone this deployment repository

```bash
git clone https://github.com/YOUR_USERNAME/parkingLotDeploy.git
cd parkingLotDeploy
