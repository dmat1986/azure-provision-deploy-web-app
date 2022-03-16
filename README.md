# Provisioning and deploying a web app with the Azure SDK for Python

This is a Python script that utilizes Azure SDK libraries to provision on Azure App Service and deploy an app from a Github repository.

Provisioning refers to the process of allocating the resources required within Azure to deploy your code and data. The Azure SDK libraries allow you to do this programmatically within Python. 

Within the Azure resource model, there are 3 levels of hierarchy used to organize the resources: 

1. Subscriptions. A subscription outlines the various features available for an application.
2. Resource groups. A resource group is a container - packages of software that contain all of the necessary elements like files, libraries and environment variables, to run in an environment - for other resources which you can manage as a group, and it is always associated with a specific Azure region, which is the location of that data center.
3. Naming of the resource.  

To run the script, download the project and cd into the project directory. Then, run:

`pip install -r requirements.txt`

This installs the necessary libraries.

Fork this repository:

`https://github.com/Azure-Samples/python-docs-hello-world`

Create the following environment variable:

`export REPO_URL=url_of_your_fork`

Create the `WEB_APP_NAME` environment variable:

`WEB_APP_NAME=name_of_your_app`

Make sure your settings in Azure allow you to deploy and build code from your preferred source and build provider - Github, in this case. Go to the Deployment Center in the Azure Portal to set this up. For more details on this, see the links provided here: https://docs.microsoft.com/en-us/azure/developer/github/deploy-to-azure

Run the script:

`python provision_deploy_web_app.py`

Followed by:

`az webapp up --resource-group PythonAzureExample-WebApp-rg --sku B1 -n name_of_your_app`

Requirements:

- azure-mgmt-resource

- azure-mgmt-web

- azure-identity
