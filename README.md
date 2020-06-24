# IBM Cloud Ansible Collections

Ansible modules collection for IBM cloud.

## Getting Started
Below steps are follwed to install ansible collections for the IBM Cloud resources. All the resources are documented under the [Docs] directory.

## Prerequisites

1. Install [Python3]

2. [RedHat Ansible] 2.9+

    ```
    pip install "ansible>=2.9.2"
    ```


## Install

1. Download and Install collection

    ```
    ansible-galaxy collection install ibm.cloudcollection
    ```

### Example Projects

1. [VPC Virtual Server Instance](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/simple-vm-ssh)

2. [Power Virtual Server Instance](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/simple-vm-power-vs)

3. [IAM User Invite](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/iam-user-invite)

4. [APP ID instance creation](https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/examples/appid-instance-creation)


[IBM Cloud Terraform Provider]: https://github.com/IBM-Cloud/terraform-provider-ibm
[Python3]: https://www.python.org/downloads/
[Docs]: https://github.com/IBM-Cloud/ansible-collection-ibm/tree/master/docs