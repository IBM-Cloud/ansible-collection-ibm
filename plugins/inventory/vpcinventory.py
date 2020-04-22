#gpl v3
import os

from ansible.module_utils._text import to_native
from ansible.plugins.inventory import BaseInventoryPlugin
from ansible.utils.display import Display
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_vpc import VpcV1 # unreleased code woot

display = Display()

class InventoryModule(BaseInventoryPlugin):

    NAME = 'ibmcloud.ibmcollection.vpcinventory'  # used internally by Ansible, it should match the file name but not required



    def verify_file(self, path):
        ''' return true/false if this is possibly a valid file for this plugin to consume '''
        valid = False
        if super(InventoryModule, self).verify_file(path):
            # base class verifies that file exists and is readable by current user
            #if path.endswith(('cloud.yaml', 'ibmcloud.yml')):
            if path.endswith(('ibmcloud.yaml', 'cloud.yaml')):
                valid = True
        return valid


    def parse(self, inventory, loader, path, cache=True):

        self.loader = loader
        self.inventory = inventory
        self.set_options()


        ibmcloud_api_key = os.environ.get('IBMCLOUD_API_KEY')
        if ibmcloud_api_key is None:
            display.debug("Please set environment variable IBMCLOUD_API_KEY")
            display.debug("Instructions for getting an API Key are here:")
            display.debug("https://cloud.ibm.com/docs/iam?topic=iam-userapikey#create_user_key")
            raise AnsibleError('Error getting IBM Cloud credentials')


        try:
            authenticator = IAMAuthenticator(ibmcloud_api_key)
            client = VpcV1('2019-09-24', authenticator=authenticator)
            instances = client.list_instances()
        except Exception as e:
            raise AnsibleError('Error in connecting to IBM Cloud: %s' % to_native(e))


        #parse data and create inventory objects:
        for ins in instances.result['instances']:
            name = ins['name']
            vpc_name = ins['vpc']['name']
            ipv4 = ins['primary_network_interface']['primary_ipv4_address']
            display.debug("found host: %s %s %s" % (name, vpc_name, ipv4))
            self.inventory.add_host(name)
            self.inventory.set_variable(name, 'ansible_host', ipv4)
            self.inventory.set_variable(name, 'vpc_name', vpc_name)
