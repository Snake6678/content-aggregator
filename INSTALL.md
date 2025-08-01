# Setup and Installation Guide

This guide provides step-by-step instructions to set up and run the Automated Content Aggregator project on your local machine and deploy it to your own GitHub account.

---
## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Git**: For version control and cloning the repository.
* **Python 3**: The programming language the project is written in.
* A **GitHub account**.

---
## Local Setup Instructions

These steps will guide you through setting up the project for local testing.

### 1. Clone the Repository
First, clone this repository to your local machine using the following command:

```sh
git clone https://github.com/Snake6678/content-aggregator.git
```

### 2. Navigate to the Project Directory
Change your current directory to the newly cloned folder:

```sh
cd content-aggregator
```

### 3. Create and Activate a Virtual Environment
It is a best practice to use a virtual environment to manage project-specific dependencies.

```sh
# Create the environment
python3 -m venv venv

# Activate the environment
source venv/bin/activate
```
Your terminal prompt should now be prefixed with `(venv)`.

### 4. Install Dependencies
Install the required Python libraries from the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

### 5. Run the Script Locally
You can now run a test to confirm everything is working. This will update the `README.md` file in your local directory.

```sh
python aggregator.py
```
You should see output confirming that the file was fetched and updated successfully.

---
## How the Automation Works

This project is designed to be automated. The **GitHub Action** workflow included in the `.github/workflows/` directory will automatically run on the schedule defined within the file. Once the code is present in a GitHub repository, no further steps are needed to enable the automation.
