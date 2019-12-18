from netmiko import Netmiko
from getpass import getpass
from ntc_templates.parse import parse_output

# creds
import os
import creds

swi_host = input('\nSwitch IP: ')
username = creds.username
password = creds.password
ftp_server = creds.ip_address
ios_name = 'c2960x-universalk9-mz.152-7.E0a.bin'
# ios_size = '26534912'

print (f'\nConnecting to {swi_host} now...')
myDevice = {
    'host': swi_host,
    'username': username,
    'password': password,
    'device_type': 'cisco_ios'
}
net_connect = Netmiko(**myDevice)
net_connect.enable()

# print('Copying files over to switch...')
# net_connect.send_command(f'copy ftp://user:user@{ftp_server}/{ios_name} flash:/{ios_name}', expect_string=']?')

# config_command = f'boot system switch all flash:/{ios_name}'
# print('Done!')
# print('Setting boot system path...')

# net_connect.send_config_set(config_command)
# print('Done! Exiting now..')
sh_dir = net_connect.send_command('dir')

parse_dir = parse_output(platform='cisco_ios', command='dir', data=sh_dir)

print(parse_dir)

# output sh boot
# dir each flash
# if statements if file is not on flash
# wait for confirmation to reboot

# holt strong elizabeth