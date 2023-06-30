# Mockingjay Process Injection Vulnerable DLL Finder

This tool helps you find potential DLL candidates vulnerable to the recently discovered Mockingjay Process Injection Technique by Security Joes (https://www.securityjoes.com/post/process-mockingjay-echoing-rwx-in-userland-to-achieve-code-execution).

The tool looks out for DLL file having a default permission set of RWX (Read-Write-Executable)

### Usage: 
python rwx_dll_finder.py directory_name

**directory_name** : the directory you wish to scan against

Example: Scans the current directory
- python rwx_dll_finder.py directory_name .

Example: Scans the entire C:\ drive
- python rwx_dll_finder.py directory_name C:\


## Disclaimer: Use at Your Own Risk 

This tool is provided as-is and without any warranty or guarantee of its effectiveness or suitability for any specific purpose. It is intended to be used for educational and informational purposes only. However, it is essential to acknowledge that this tool has the potential to be misused or abused.

The creators and contributors of this tool cannot be held responsible for any damages, losses, or consequences resulting from the use or misuse of this tool. Users are solely responsible for ensuring compliance with all applicable laws and regulations while utilizing this tool.

We strongly advise against using this tool for any illegal activities, unauthorized access, or malicious purposes. Any such use is strictly prohibited, and the responsibility lies solely with the user.

By downloading, installing, or using this tool, you agree that the creators and contributors shall not be liable for any direct, indirect, incidental, special, or consequential damages or losses arising from its use.

Proceed with caution, exercise responsible and ethical behavior, and respect the privacy and security of others. Always obtain proper authorization before using this tool on any system or network that you do not own or have explicit permission to access.

Remember, knowledge and tools can be powerful, but it is the responsibility of the user to utilize them in a lawful and ethical manner.
