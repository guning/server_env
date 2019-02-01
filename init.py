#!/usr/bin/python

from ConfigParser import ConfigParser
from string import Template
import os


def replace_docker_compose(variables):
    pass

env_file_path = './.env.tpl'
conf_file_path = './env.conf'

conf_parser = ConfigParser()
# read keys case sensitive
conf_parser.optionxform=str

conf_parser.read(conf_file_path)

confs = conf_parser._sections['variables']

if not os.path.exists(confs['WEB_CODE_DIR']):
    os.makedirs(confs['WEB_CODE_DIR'])

if not os.path.exists(confs['WEB_LOG_DIR']):
    os.makedirs(confs['WEB_LOG_DIR'])

if not os.path.exists(confs['DB_DATA_DIR']):
    os.makedirs(confs['DB_DATA_DIR'])

env_file = open(env_file_path, 'r')
env_content = env_file.read()
env_file.close()

tmplate = Template(env_content)
env = tmplate.substitute(confs)

_env_file = open('./dockerCompose/.env', 'w')
_env_file.write(env)
_env_file.close()

