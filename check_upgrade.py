from getpass import getpass

from netmiko import Netmiko
from ntc_templates.parse import parse_output

# creds
import creds

# definitions
swi_host = input('\nSwitch IP: ')
username = creds.username
password = creds.password
ios_name = 'c2960x-universalk9-mz.152-7.E0a.bin'
old_ios_name = 'c2960x-universalk9-mz.152-4.E6.bin'
ios_size = '26534912'

# lists
swi_numbers = []
swi_priority = []
check_num = 0

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


for x in parse_swi:
    swi_numbers.append(x['switch'])
    swi_priority.append(x['priority'])

swi_num_prior = list(zip(swi_numbers, swi_priority))

print(f'Found {swi_numbers[-1]} switch(es) in the stack!\n')

print('Checking for corrupt IOS images..')

sh_dir = net_connect.send_command('dir all')
parse_dir = parse_output(platform='cisco_ios', command='dir all', data=sh_dir)

for x in parse_dir:
    if 'flash' in x['file_system']:
        if x['name'] == ios_name:
            check_num += 1
            if x['size'] == ios_size:
                print(f"All good! {x['file_system']}{x['name']} is equal to {x['size']}!")
            else:
                print(f"ERROR! {x['file_system']}{x['name']} is equal to {x['size']}!")

# net_connect.send_config_set(f"boot system switch all flash:/{ios_name}")

for x in range(swi_num_prior)
swi_prio_num[0][1] > swi_prio_num[1][1]

if int(swi_numbers[-1]) != check_num:
    print(f"Only {check_num} out of {swi_numbers[-1]} have {ios_name}!")

mylist = [('1', '14'), ('2', '1'), ('3', '10'), ('4', '15')]

for i in range(0, len(mylist)):
    try:
        mylist[i][1] > mylist[i+1][1]
    except IndexError:
        print("done")
