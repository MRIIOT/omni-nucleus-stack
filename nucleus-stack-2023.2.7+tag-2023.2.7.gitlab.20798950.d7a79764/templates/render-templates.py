#!/usr/bin/env python3.10

import os
import sys
from pprint import pprint

bin_path = os.path.dirname(os.path.realpath(__file__))

stack_template_file = 'nucleus-stack.template.yml'
env_template_file = 'nucleus-stack.template.env'

ssl_stack_out = f'{bin_path}/../base_stack/nucleus-stack-ssl.yml'
base_stack_out = f'{bin_path}/../base_stack/nucleus-stack-no-ssl.yml'
env_file_out = f'{bin_path}/../base_stack/nucleus-stack.env'

from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader(bin_path),
                   trim_blocks=True,
                   lstrip_blocks=True)



# Render base stack template

template = env.get_template(stack_template_file)

with open(ssl_stack_out, 'w') as h:
  h.write(template.render(ssl=True))

with open(base_stack_out, 'w') as h:
  h.write(template.render(ssl=False))

# Render env template

template = env.get_template(env_template_file)

defaults = {
       'eula_accepted': 0, 
       'security_reviewed': 0, 
       ##### END

       'instance_name': 'my_omniverse',
       'server_ip_or_host': 'hostname-or-ip-here', 
       'ssl_ingress_host': 'my-nucleus.my-company.com', 
       'ssl_ingress_port': 443, 

       'master_password': '',
       'service_password': '',
       #### END

       'container_subnet': '192.168.2.0/26',
       'data_root': '/var/lib/omni/nucleus-data',
       'coredumps_root': '${DATA_ROOT}/empty',

       'lft_compression': 0,
       'auth_root_of_trust_pub': './secrets/auth_root_of_trust.pub',
       'auth_root_of_trust_pri': './secrets/auth_root_of_trust.pem',
       'auth_root_of_trust_long_term_pub': './secrets/auth_root_of_trust_lt.pub',
       'auth_root_of_trust_long_term_pri': './secrets/auth_root_of_trust_lt.pem',
       'pwd_salt': './secrets/pwd_salt',
       'lft_salt': './secrets/lft_salt',
       'discovery_registration_token': "./secrets/svc_reg_token",

       'ports_web': 8080, 

       'ssl_cert': '',
       'ssl_cert_key': '',
    }

dev_env = {
       'eula_accepted': 1, 
       'security_reviewed': 1, 
       'server_ip_or_host': 'stagevm-3.ov.nvidia.com', 
       'ssl_ingress_host': 'stagevm-3.ov.nvidia.com', 
       'master_password': '123',
       'service_password': '123',
       'container_subnet': '192.168.22.0/26',
       'coredumps_root': '/var/lib/omni/_crashdumps',
       'ssl_cert': '/etc/letsencrypt/live/stagevm-3.ov.nvidia.com/fullchain.pem',
       'ssl_cert_key': '/etc/letsencrypt/live/stagevm-3.ov.nvidia.com/privkey.pem',
    }

v = dict(defaults.items())
if(int(os.getenv('DEV', 0))):
  v = v | dev_env

with open(env_file_out, 'w') as h:
  h.write(template.render(values=v))
