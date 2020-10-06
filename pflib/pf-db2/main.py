# TODO: FIGURE OUT HOW TO USE THE GITHUB SECRETS FOR LIKE PASSWORDS N SHIT
import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser
from configparser import ConfigParser

config = ConfigParser()
print(config.read("x.ini"))
home = expanduser('~')
sql_hostname = config["SSH_tunneled_MySQL"]["sql_hostname"]
sql_username = config["SSH_tunneled_MySQL"]["sql_username"]
sql_password = config["SSH_tunneled_MySQL"]["sql_password"]
sql_main_database = config["SSH_tunneled_MySQL"]["sql_main_database"]
sql_port = int(config["SSH_tunneled_MySQL"]["sql_port"])
ssh_host = config["SSH_tunneled_MySQL"]["ssh_host"]
ssh_user = config["SSH_tunneled_MySQL"]["ssh_user"]
ssh_port = int(config["SSH_tunneled_MySQL"]["ssh_port"])
ssh_password = config["SSH_tunneled_MySQL"]["ssh_password"]
sql_ip = config["SSH_tunneled_MySQL"]["sql_ip"]



with SSHTunnelForwarder(
		(ssh_host, ssh_port),
		ssh_username=ssh_user,
		ssh_password=ssh_password,
		remote_bind_address=(sql_hostname, sql_port)) as tunnel:
	conn = pymysql.connect(host='127.0.0.1', user=sql_username, passwd=sql_password, db=sql_main_database, port=tunnel.local_bind_port)
	query = '''SELECT * from dailyASN;'''
	data = pd.read_sql_query(query, conn)
	print(data)
	conn.close()
