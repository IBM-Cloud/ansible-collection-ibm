# IBM Cloud Ansible: IBM APP-ID INSTANCE CREATION

This example shows how to setup App-ID service instance.
In this example, an app-id instance is created in given region

## Configuration Parameters

The following parameters can be set by the user:

* `name:`: used for the instance name.
* `service`: service used for the service info.
* `plan:`: plan opted by the used in IBM cloud
* `location:`: IBM Cloud resource location

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

1. To create all resources and test public SSH connection to the VM, run the
   'create' playbook:

    ```
    ansible-playbook create.yml
    ```

### Destroy

1. To destroy all resources run the 'destroy' playbook:

    ```
    ansible-playbook destroy.yml
    ```
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/iam?topic=iam-userapikey
