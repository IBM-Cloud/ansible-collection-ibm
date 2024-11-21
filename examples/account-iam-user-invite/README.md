# Example Ansible Playbook: IBM Cloud IAM User invite example

This is an example for IBM Cloud IAM User invitations, and adding the users to an IAM Access Group.

## Execution

1. [Create an IBM Cloud User API Key].
2. Edit the input variables of the Ansible Playbook `create.yml`. Input variables can be extracted into separate files, or environment variables etc - please see [Ansible User guide]
3. Execute the Ansible Playbook example to gather data and create service instances or resources using the IBM Cloud API endpoints
    ```shell
    ansible-playbook create.yml
    ```

[Create an IBM Cloud User API Key]: https://cloud.ibm.com/docs/account?topic=account-userapikey
[Ansible User guide]: https://docs.ansible.com/ansible/latest/user_guide/index.html
