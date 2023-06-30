import os
import sys
import pefile

VULN_DLL_LIST = []

def verify_default_rwx(filename):
    pe = pefile.PE(filename)
    for section in pe.sections:
        if hex(section.Characteristics) == hex(0xe0000020):
            print('Default Section with RWX Found : ', bytearray.fromhex(section.Name.hex()).decode(), hex(section.Characteristics))
            VULN_DLL_LIST.append(filename)

if len(sys.argv) - 1 < 1:
    print('Usage: '+ sys.argv[0] + ' directory_path')
    exit(0)

print('### Mockingjay Process Injection Vulnerable DLL Finder ###\n')

for root, dirs, files in os.walk(sys.argv[1], topdown=True):
   for name in files:
    filename = os.path.join(root, name)
    if os.path.splitext(filename)[1] == '.dll':
        print('Analyzing : ', filename)
        verify_default_rwx(filename)
if len(VULN_DLL_LIST) > 0:
    print('Scanning Completed')
    print(VULN_DLL_LIST)
else:
    print('No Vulnerable DLL Found')