# Example Ansible Playbook: IBM Cloud Resource Group Example

This is an example for IBM Cloud Resource Group creation.

## Execution

1. [Create an IBM Cloud User API Key].
2. Edit the input variables of the Ansible Playbook `create.yml`. Input variables can be extracted into separate files, or environment variables etc - please see [Ansible User guide]
3. Execute the Ansible Playbook example to gather data and create service instances or resources using the IBM Cloud API endpoints
    ```shell
    ansible-playbook create.yml
    ```
4. In addition, an example `destroy.yml` is included.

[Create an IBM Cloud User API Key]: https://cloud.ibm.com/docs/account?topic=account-userapikey
[Ansible User guide]: https://docs.ansible.com/ansible/latest/user_guide/index.html
