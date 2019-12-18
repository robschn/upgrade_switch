from netmiko import Netmiko
from getpass import getpass
from ntc_templates.parse import parse_output

# creds
import creds

# swi_host = input('\nSwitch IP: ')
swi_host = '172.21.225.115'
username = creds.username
password = creds.password
ftp_server = creds.ip_address
ios_name = 'c2960x-universalk9-mz.152-7.E0a.bin'\
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

print('Gathering switch information...')
sh_dir = net_connect.send_command('dir all')
parse_dir = parse_output(platform='cisco_ios', command='dir all', data=sh_dir)

flash_numbers = []
for x in parse_dir:
    flash_numbers.append(x['file_system'])

print(f'Found: {" ".join(str(x) for x in flash_numbers)}')

for flash_num in flash_numbers:
    print(f'Sending command to copy {ios_name} to {flash_num}...')
    net_connect.send_command(f'copy ftp://user:user@{ftp_server}/{ios_name} {flash_num}{ios_name}', expect_string=']?')

print('Please wait for the copying to finsh.')
# config_command = f'boot system switch all flash:/{ios_name}'

# net_connect.send_config_set(config_command)
print('Done!')
# print('Boot path set, exiting now..')





# output sh boot
# dir each flash
# if statements if file is not on flash
# wait for confirmation to reboot

# holt strong elizabeth