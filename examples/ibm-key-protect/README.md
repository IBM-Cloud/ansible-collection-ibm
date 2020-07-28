# IBM Cloud Ansible: IBM KEY PROTECT

This example shows how to Create a Key protect instance, generate a key and integrate that key with cos-bucket

This sample configuration will create the key protect instance, cos-bucket instance, root key, and integrate the key with a cos bucket after creating the bucket.

## Configuration Parameters

The following parameters can be set by the user:

| Name | Description | Type | Required |
|------|-------------|------|---------|
| kp\_plan | The key protect plan to provision| `string` | yes |
| kp\_name_ | The name of the keyprotect instance| `string` | yes |
| key\_name | The name of the kp key. | `string` | yes |
| standard\_key | Set to true to create a standard key, to create a root key set this flag to false. Default: `false` . | `bool` | no |
| plan | The cos instance plan to provision| `string` | yes |
| kp\_location | The location where key protect instance will be created| `string` | yes |
| location | The location where cos instance will be created| `string` | yes |
| cos\_name | The name of the cos instance to be provisioned| `string` | yes |
| cos\_bucket_name | The name of the cos ibucket| `string` | yes |

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
