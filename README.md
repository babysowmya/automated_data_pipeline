# Automated Data Pipeline using Terraform, Docker & GitHub Actions

##  Project Overview

This project demonstrates a complete automated data pipeline using:

- Terraform (Infrastructure as Code)
- LocalStack (AWS simulation)
- Amazon S3 (for storage)
- Docker (for containerized ETL)
- GitHub Actions (CI/CD automation)

The pipeline:

1. Creates an S3 bucket using Terraform
2. Uploads a CSV file to S3
3. Runs a Dockerized Python ETL process
4. Processes the file
5. Uploads the transformed output back to S3
6. Runs automatically on every push to the main branch

---

## 🏗️ Project Architecture

User Push → GitHub Actions →  
Terraform creates S3 bucket →  
Upload input.csv →  
Docker runs ETL →  
Processed file stored in S3

---

## 📂 Project Structure

```

automated-data-pipeline/
│
├── terraform/              # Terraform configuration
├── etl/                    # Python ETL code + Dockerfile
├── docker-compose.yml      # Local container setup
├── .github/workflows/      # CI/CD pipeline
└── README.md

````

---

## 🛠️ Technologies Used

- Python
- Docker
- Terraform
- LocalStack
- AWS CLI
- GitHub Actions

---

## 🚀 How to Run Locally

### 1️⃣ Start LocalStack

```bash
docker-compose up -d
````

### 2️⃣ Initialize Terraform

```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### 3️⃣ Upload Sample File

```bash
aws --endpoint-url=http://localhost:4566 s3 cp input.csv s3://demo-data-bucket/raw/input.csv
```

### 4️⃣ Build Docker Image

```bash
docker build -t etl ./etl
```

### 5️⃣ Run ETL Container

```bash
docker run --network host \
-e AWS_ENDPOINT_URL=http://localhost:4566 \
-e BUCKET_NAME=demo-data-bucket \
etl
```

### 6️⃣ Verify Output

```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://demo-data-bucket/processed/
```

---

## 🔄 CI/CD Automation

The project includes a GitHub Actions workflow that:

* Starts LocalStack
* Applies Terraform
* Uploads test CSV
* Builds Docker image
* Runs ETL
* Verifies output

The pipeline runs automatically on every push to the `main` branch.

---

## Expected Output

After successful execution:

* `input.csv` is stored in `raw/`
* `output.csv` is stored in `processed/`
* GitHub Actions shows a green check mark

## 📌 Author
Sunkara Sowmya