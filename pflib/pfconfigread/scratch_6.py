from configparser import ConfigParser
from os import environ
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser
from configparser import ConfigParser
config = ConfigParser()
config.read(environ.get('PFCONPATH'))   # Get the path of the config file from environment variable


# print('SSH_tuneled_MySQL' in config)


home = expanduser('~')
sql_hostname = config["SSH_tunneled_MySQL"]["sql_hostname"]
sql_username = config["SSH_tunneled_MySQL"]["sql_username"]
sql_password = config["SSH_tunneled_MySQL"]["sql_password"]
sql_database = config["SSH_tunneled_MySQL"]["sql_database"]
sql_port = int(config["SSH_tunneled_MySQL"]["sql_port"])
ssh_host = config["SSH_tunneled_MySQL"]["ssh_host"]
ssh_user = config["SSH_tunneled_MySQL"]["ssh_user"]
ssh_port = int(config["SSH_tunneled_MySQL"]["ssh_port"])
ssh_password = config["SSH_tunneled_MySQL"]["ssh_password"]
sql_ip = config["SSH_tunneled_MySQL"]["sql_ip"]

