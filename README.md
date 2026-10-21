# 🚀 NocoDB Automated Testing Project

This project contains automated tests for NocoDB built with **Pytest** and **Playwright**. Follow the guide below to set up the environment and run the tests locally.

---

## 📦 1. NocoDB Deployment (Docker)

The official Docker image is used to run the NocoDB application. Installation and download instructions can be found at the source repository: [NocoDB](https://github.com/nocodb).

Also, my contribution to the [NocoDB](https://github.com/grwruslan/grwruslan) project as a QA Engineer

Run the following command in your terminal to quickly launch the container:
```powershell
docker run -d -p 8080:8080 --name nocodb-test nocodb/nocodb:latest
```

Once launched, the application will be accessible at: 
👉 **[http://localhost:8080/dashboard](http://localhost:8080/dashboard)**

---

## 🔐 2. Test Authorization Data (Important!)

When signing up for the first time, you must register using the following test account credentials:

* **Email:** `1@1.net`
* **Password:** `11111111`

> ⚠️ **ATTENTION:** These credentials are hardcoded into the automated test logic. Please do not use your actual work or personal accounts, as the tests run locally and rely strictly on this specific test pair!
> 
> *However, you can substitute your own data, as specified in the test cases within the precondition.*

---

## ⚙️ 3. Project Setup Before Running Tests

Within your NocoDB account, the following must be created beforehand:
1. A project with the exact name: **`Project1`**
2. A table with the exact name: **`users`**

*Note: You can also substitute your own names if needed.*

---

## 🛠️ 4. Running Automated Tests

### Step 1: Initialize the Environment & Install Dependencies
Set up a local test environment in your directory using `venv` and install the required packages via PowerShell:

```powershell
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment in PowerShell
.venv\Scripts\Activate.ps1

# Install Playwright and its dependencies
pip install pytest-playwright
playwright install
```

### Step 2: Execute the Tests
Run the tests with step-by-step output displayed directly in the terminal:

```powershell
pytest -s --log-cli-level=INFO
```
