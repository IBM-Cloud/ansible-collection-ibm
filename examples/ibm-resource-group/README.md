# IBM Cloud Ansible: IBM Resource Group Example

This example shows creation and destruction of ibmcloud resource group

In this example a resource group is 
- created by create.yml playbook.
- destoyed by delete.yml playbook.

## Configuration Parameters

The following parameters can be set by the user:

* `resource_group_name`: Name of the resource group.

## Running

### Set API Key and Region

1. [Obtain an IBM Cloud API key].

2. Export your API key to the `IC_API_KEY` environment variable:

    ```
    export IC_API_KEY=<YOUR_API_KEY_HERE>
    ```

    Note: Modules also support the 'ibmcloud_api_key' parameter, but it is
    recommended to only use this when encrypting your API key value.

### Create

1. To create resource group, run the
   'create' playbook:

    ```
    ansible-playbook create.yml
    ```

### Destroy

1. To destroy resource group run the 'destroy' playbook:

    ```
    ansible-playbook destroy.yml
    ```
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui
