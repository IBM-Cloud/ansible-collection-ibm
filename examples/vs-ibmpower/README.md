# Example Ansible Playbook: IBM Power Virtual Server in IBM Cloud

This is an example for instance provision of an IBM Power Virtual Server, using an IBM Power Virtual Server Workspace (public) at an IBM Power Virtual Server Location that is collocated with IBM Cloud.

An existing IBM Power Virtual Server Workspace must be provided, if an SSH Key pair or network (VLAN Subnet) does not exist then it will be created during provision. For example purposes only, a Floating Public IP Address is attached to the IBM Power Virtual Server and a login connectivity test is performed (show MOTD).

As defaults:
- machine type is IBM Power 9 hardware `s922` which can be amended to `e980`, or IBM Power 10 hardware `s1022` and `e1080` etc.
- OS Image selected is for Linux, which can be amended to AIX or IBMi.
- virtual server size is 0.25 CPU Core at SMT-8 (thereby 4 vCPU) and 8GiB DRAM.
- no storage is attached

## Execution

1. [Create an IBM Cloud User API Key].
2. Edit the input variables of the Ansible Playbook `create.yml`. Input variables can be extracted into separate files, or environment variables etc - please see [Ansible User guide]
3. Execute the Ansible Playbook example to gather data and create service instances or resources using the [IBM Power Virtual Server (`power-cloud`) API endpoints](https://cloud.ibm.com/apidocs/power-cloud)
    ```shell
    ansible-playbook create.yml
    ```
4. In addition, an example `destroy.yml` is included.
    - To avoid potential mistaken removal, the SSH Key pair and network (VLAN Subnet) are not destroyed as these are re-used or optionally created in the example.

[Create an IBM Cloud User API Key]: https://cloud.ibm.com/docs/account?topic=account-userapikey
[Ansible User guide]: https://docs.ansible.com/ansible/latest/user_guide/index.html
