# IBM Cloud Ansible: IBM Transit-Gateway

This example illustrates how to use the Transit gateway and connection resources to import a certificate and to order a certificate.

## Configuration Parameters

The following parameters can be set by the user:
* `name` - The unique user-defined name for this gateway. Example: myGateway
* `location` - Transit Gateway location. Example: us-south
* `global_` - Gateways with global routing (true) can connect to networks outside their associated region.
* `resource_group` - The resource group ID where the transit gateway to be created.
* `gateway` -  The Transit Gateway identifier.
* `name` - The user-defined name for the transit gateway connection. If unspecified, the name will be the network name (the name of the VPC in the case of network type 'vpc', and the word Classic, in the case of network type 'classic').
* `network_type` - Defines what type of network is connected via this connection.Allowable values: [classic,vpc]. Example: vpc
* `network_id` -he ID of the network being connected via this connection. This field is required for some types, such as 'vpc'. For network type 'vpc' this is the CRN of the VPC to be connected. This field is required to be unspecified for network type 'classic'. Example: crn:v1:bluemix:public:is:us-south:a/123456::vpc:4727d842-f94f-4a2d-824a-9bc9b02c523b   
* `network_account_id` - The ID of the account which owns the network that is being connected. Generally only used if the network is in a different account than the gateway.

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

1. To create all resources, run the
   'create' playbook:

    ```
    ansible-playbook create.yml

### Destroy

1. To destroy all resources run the 'destroy' playbook:

    ```
    ansible-playbook destroy.yml
    ```
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/iam?topic=iam-userapikey
