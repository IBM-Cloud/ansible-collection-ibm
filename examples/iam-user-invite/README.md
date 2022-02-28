# IBM Cloud Ansible: IBM IAM User invite example

This example shows how to invite a batch of users to an account and also add the users to one more access groups

The users within an account can be able to invite, retrieve, update, or removed.

In this example a list of users are invited to the inviting account and added to a an newly created access group.

## Configuration Parameters

The following parameters can be set by the user:

* `ibm_space`: space details to be inserted by the user.
* `ibm_org`: org details to be inserted by the user.
* `user`: user details to be inserted by the user.

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
[Obtain an IBM Cloud API key]:https://cloud.ibm.com/docs/account?topic=account-userapikey&interface=ui
