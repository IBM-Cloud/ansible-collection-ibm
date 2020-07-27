# IBM Cloud Ansible: IBM API-Gateway 

This example illustrates how to use the API Gateway Endpoint and Subscription resources to create an endpoint for a given OpenAPI definition and to create a subscription for this endpoint.It allows the user to input a single openAPI document or a directory of documents.

## Configuration Parameters

The following parameters can be set by the user:

`region`: The region where the resource has to be provisioned. Default: us-south
`service_name`: The name of the API Gateway Service Instance.
`endpoint_name`: The name of the API Gateway Endpoint resource.
`managed`: Indicates whether endpoint is online or not. Default: false
`file_path`: The API document name that represents the endpoint. It is required when a single endpoint is created
`action_type`: The type of action that is performed on the API endpoint. Supported values are [share], [unshare], [manage], and [unmanage].To manage API to offline and online action_type has to be set. The default value is [unshare]. Note that endpoint actions are performed by using the type parameter after the endpoint is created. As a consequence, endpoint actions are invoked during an endpoint update only.
`dir_path`: The directory name of API documents that represents multiple endpoint. It is required when a multipple endpoints are created
`subscription_name`: The name of the subscription resource indicates the name for an API key
`subscription_type`: The type of the subscription resource indicates the type of API key sharing. Supported values are [external], and [internal].
`secret`: The secret of the API key.
`generate_secret`: It conflicts with secret. If generate_secret- true, secret is auto generated.

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
    ```

### Destroy

1. To destroy all resources run the 'destroy' playbook:

    ```
    ansible-playbook destroy.yml
    ```
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/iam?topic=iam-userapikey
