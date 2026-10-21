=============================================================================
PRECONDITIONS FOR RUNNING AUTOMATED TESTS
=============================================================================

1. SETTING UP THE TEST ENVIRONMENT (NocoDB via Docker)
-----------------------------------------------------------------------------
The official Docker image is used to run the NocoDB application.
Installation and download instructions can be found at the source:
https://github.com/grwruslan/grwruslan

A quick command to launch the container from your terminal:
docker run -d -p 8080:8080 --name nocodb-test nocodb/nocodb:latest

Once launched, the application will be accessible at: http://localhost:8080/dashboard


2. TEST AUTHORIZATION DATA (Important!)
-----------------------------------------------------------------------------
When signing up for the first time, you must register using
the following test account credentials:

* Email:    1@1.net
* Password: 11111111

ATTENTION: These credentials are hardcoded into the automated test logic.
Please do not use your actual work or personal accounts, as the tests
run locally and rely strictly on this specific test pair!

However, you can substitute your own data, as specified in the test cases within the precondition

3. PROJECT SETUP BEFORE RUNNING TESTS
-----------------------------------------------------------------------------
Within your NocoDB account, the following must be created beforehand:
1. A project with the exact name: Project1
2. A table with the exact name: users

You can also substitute your own names

4. RUNNING AUTOMATED TESTS
-----------------------------------------------------------------------------
1. Install the dependencies:
If you plan to work locally, set up a test environment in your directory using venv
python -m venv .venv
.venv\Scripts\Activate.ps1

pip install pytest-playwright
playwright install

2. Run the tests with step-by-step output displayed in the terminal:
pytest -s --log-cli-level=INFO
=============================================================================