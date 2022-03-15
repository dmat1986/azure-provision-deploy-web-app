# Provisioning and deploying a web app with the Azure SDK for Python

This is a Python script that utilizes Azure SDK libraries to provision on Azure App Service and deploy an app from a Giyhub repository.

To run the script, download the project and cd into the project directory. Then, run:

`pip install -r requirements.txt`

This installs the necessary libraries.

Fork this repository:

`https://github.com/Azure-Samples/python-docs-hello-world`

Create the following environment variable:

`export REPO_URL=url_of_your_fork`

Create the `WEB_APP_NAME` environment variable:

`WEB_APP_NAME=azure-provision-deploy`

Make sure your settings in Azure allow you to deploy and build code from your preferred source and build provider - Github, in this case. Go to the Deployment Center in the Azure Portal to set this up.

Run the script:

`python provision_deploy_web_app.py`

Followed by:

`az webapp up --resource-group PythonAzureExample-WebApp-rg --sku B1 -n azure-provision-deploy`

Requirements:

- azure-mgmt-resource

- azure-mgmt-web

- azure-identity
