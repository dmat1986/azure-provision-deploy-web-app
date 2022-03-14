import random, os
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient

#Aquire a credential object
credential = AzureCliCredential()

#Get subscription ID from environment variable
subscription_id = os.environ["AZURE_SUBSCRIPTION_ID"]

#Set resource group name and location in which to provision resources
RESOURCE_GROUP_NAME = 'PythonAzureExample-WebApp-rg'
LOCATION = "centralus"

#Provision the resource group
resource_client = ResourceManagementClient(credential,subscription_id)
rg_result = resource_client.resource_groups.create_or_update(RESOURCE_GROUP_NAME,
	{"location":LOCATION})

print(f"Provisioned resource group {rg_result.name}")

#Provision the app service plan; define the underlying virtual machine
#for the web app
SERVICE_PLAN_NAME = 'PythonAzureExample-WebApp-plan'
WEB_APP_NAME = os.environ["WEB_APP_NAME"]

#Get the client object
app_service_client = WebSiteManagementClient(credential,subscription_id)

#Provision the plan
poller = app_service_client.app_service_plans.begin_create_or_update(RESOURCE_GROUP_NAME,
	SERVICE_PLAN_NAME,
	{
		"location":LOCATION,
		"reserved":True,
		"sku":{"name":"B1"}
	})

plan_result = poller.result()

print(f"Provisioned app service plan {plan_result.name}")

#Provision the web app
poller = app_service_client.web_apps.begin_create_or_update(RESOURCE_GROUP_NAME,
	WEB_APP_NAME,
	{
		"location":LOCATION,
		"server_farm_id":plan_result.id,
		"site_config":{
			"linux_fx_version":"python|3.8"
		}
	})

web_app_result = poller.result()

print(f"Provisioned web app {web_app_result.name} at {web_app_result.default_host_name}")

#Deploy code from Github repository
REPO_URL = os.environ["REPO_URL"]

poller = app_service_client.web_apps.begin_create_or_update_source_control(RESOURCE_GROUP_NAME,
    WEB_APP_NAME, 
    { 
        "location": "GitHub",
        "repo_url": REPO_URL,
        "branch": "master"
    }
)

sc_result = poller.result()

print(f"Set source control on web app to {sc_result.branch} branch of {sc_result.repo_url}")