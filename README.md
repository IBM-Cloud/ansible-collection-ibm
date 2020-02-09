# IBM Cloud Ansible Collections

Ansible modules for IBM cloud.

## Getting Started
Below steps are follwed to install ansible modules for IBM Cloud resources. All the resources are documented under
the [docs](docs) directory.

## Prerequisites

1. Install [Python3]

2. [RedHat Ansible] 2.8+

    ```
    pip install "ansible>=2.8.0"
    ```


## Install

1. Download modules collection

    ```
    git clone https://github.com/IBM-Cloud/ansible-collection-ibm.git
    ```

2. Add modules and module_utils to the [Ansible search path]. E.g.:

    ```
    cd ansible-collection-ibm
    cp modules/* $HOME/.ansible/plugins/modules/.
    cp module_utils/* $HOME/.ansible/plugins/module_utils/.

    ```

### Example Projects

1. [VPC Virtual Server Instance](examples/simple-vm-ssh)

2. [Power Virtual Server Instance](examples/simple-vm-power-vs)


[IBM Cloud Terraform Provider]: https://github.com/IBM-Cloud/terraform-provider-ibm
[Python3]: https://www.python.org/downloads/
[RedHat Ansible]: https://www.ansible.com/
[Ansible search path]: https://docs.ansible.com/ansible/latest/dev_guide/overview_architecture.html#ansible-search-path
[release page]:https://github.com/IBM-Cloud/terraform-provider-ibm/releases
