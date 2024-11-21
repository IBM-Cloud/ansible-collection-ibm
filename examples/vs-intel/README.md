# Example Ansible Playbook: IBM Cloud Virtual Server

This is an example for instance provision of an IBM Cloud Virtual Server.

An existing Resource Group must be provided, if an SSH Key pair or VPC network and VPC Subnet does not exist then it will be created during provision. For example purposes only, a Floating Public IP Address is attached to the IBM Cloud Virtual Server and a login connectivity test is performed (show MOTD).

As defaults:
- OS Image selected is Linux, which can be amended to Windows.
- Virtual Server Profile size is 4 vCPU and 16GiB DRAM.
- Virtual Network Interface (VNI) is attached to the Virtual Server with auto-delete
- no storage is attached
- Instance Metadata service is enabled

## Execution

1. [Create an IBM Cloud User API Key].
2. Edit the input variables of the Ansible Playbook `create.yml`. Input variables can be extracted into separate files, or environment variables etc - please see [Ansible User guide]
3. Execute the Ansible Playbook example to gather data and create service instances or resources using the IBM Cloud API endpoints
    ```shell
    ansible-playbook create.yml
    ```
4. In addition, an example `destroy.yml` is included.
    - To avoid potential mistaken removal, the SSH Key pair VPC network, and VPC Subnet are not destroyed as these are re-used or optionally created in the example.

[Create an IBM Cloud User API Key]: https://cloud.ibm.com/docs/account?topic=account-userapikey
[Ansible User guide]: https://docs.ansible.com/ansible/latest/user_guide/index.html
