from netmiko import Netmiko
from getpass import getpass
from ntc_templates.parse import parse_output

# creds
import creds

swi_host = input('\nSwitch IP: ')
username = creds.username
password = creds.password
ftp_server = creds.ip_address
ios_name = 'c2960x-universalk9-mz.152-7.E0a.bin'
# old_ios_name = 'c2960x-universalk9-mz.152-4.E6.bin'
# ios_size = '26534912'

print (f'Connecting now..')
myDevice = {
    'host': swi_host,
    'username': username,
    'password': password,
    'device_type': 'cisco_ios',
    'timeout': 35 * 60
}
net_connect = Netmiko(**myDevice)
net_connect.enable()

print('Gathering switch information..')
sh_swi = net_connect.send_command('show switch detail')
parse_swi = parse_output(platform='cisco_ios', command='show switch detail', data=sh_swi)

swi_numbers = []
for x in parse_swi:
    swi_numbers.append(x['switch'])

print(f'Found found {swi_numbers[-1]} switch(es) in the stack!')
# ftp the file to flash1:
net_connect.send_command(f'copy ftp://user:user@{ftp_server}/{ios_name} flash:/', expect_string=']?')
net_connect.send_command('\n', expect_string='#')

# copy from flash1: to flash#:
for swi_num in swi_numbers:
    print(f'Copying {ios_name} to flash{swi_num}. Please wait...')
    if swi_num != 1
        net_connect.send_command(f'copy flash:/{ios_name} flash{swi_num}:/', expect_string=']?')
        net_connect.send_command('\n', expect_string='#')

print('\nSetting boot path and writing memory.')
net_connect.send_config_set(f'boot system switch all flash:/{ios_name}')
net_connect.send_command('write mem')

print('Here is the current switch priority\n')
sh_swi = net_connect.send_command('show switch')
print(sh_swi)

reload_prompt = input('Would you like to proceed with a reload? [y/n]: ')
if reload_prompt == 'y':
    reload_time = input('Enter reload time HH:MM. If now, press "enter": ')
    if reload_time == '':
        print('Reloading now!')
        net_connect.send_command('reload', expect_string='[confirm]')
        net_connect.send_command('\n')
        
    else:
        print(f'Reload set for {reload_time}')
        net_connect.send_command(f'reload at {reload_time}')
        net_connect.send_command('reload', expect_string='[confirm]')
        net_connect.send_command('\n')
        

print('Update finished! Exiting now..')
exit()

