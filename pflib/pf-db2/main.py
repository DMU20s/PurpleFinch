import pymysql
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
from os.path import expanduser

home = expanduser('~')
# mypkey = paramiko.RSAKey.from_private_key_file(home + pkeyfilepath)
# if you want to use ssh password use - ssh_password='your ssh password', bellow

sql_hostname = ''
sql_username = ''
sql_password = ''
sql_main_database = 'pfdb1'
sql_port = 3306
ssh_host = ''
ssh_user = ''
ssh_port = 22
ssh_password = ''
sql_ip = '127.0.0.1'

with SSHTunnelForwarder(
		(ssh_host, ssh_port),
		ssh_username=ssh_user,
		ssh_pkey=ssh_password,
		remote_bind_address=(sql_hostname, sql_port)) as tunnel:
	conn = pymysql.connect(host='127.0.0.1', user=sql_username, passwd=sql_password, db=sql_main_database, port=tunnel.local_bind_port)
	query = '''SELECT VERSION();'''
	data = pd.read_sql_query(query, conn)
	conn.close()

# TODO: DBeaver
# TODO: MQTT EXPLORER
# TODO: MAKE DUMMYGUIDE FOR HOW TO DO THE SQL THING
# TODO: FIGURE OUT HOW TO USE THE GITHUB SECRETS FOR LIKE PASSWORDS N SHIT
