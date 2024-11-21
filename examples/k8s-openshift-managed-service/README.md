# Example Ansible Playbook: IBM Cloud managed-service for Red Hat OpenShift (ROKS) cluster with VPC networking

This is an example for creation of a Red Hat OpenShift (ROKS) cluster managed-service instance (managed by IBM Cloud), connected to an existing Virtual Private Cloud (VPC) Subnet.

The default is `3` worker nodes in the cluster, and requires an IBM Cloud Virtual Private Cloud (VPC) and IBM Cloud Object Storage (COS) service instance - which are not created by this Ansible Playbook example.

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
