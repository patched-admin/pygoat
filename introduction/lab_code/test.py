'''
import subprocess, json


cmd_str = "pwd; ls"
process = subprocess.Popen(
    cmd_str,
    shell=True,
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
data = stdout.decode('utf-8')
stderr = stderr.decode('utf-8')
# res = json.loads(data)
# print("Stdout\n" + data)
print(data + stderr)
'''
import subprocess

import yaml

try:
    with open('/home/fox/test.yaml', 'r') as stream:
        data = yaml.safe_load(stream)
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")
    exit(1)
except IOError as e:
    print(f"Error reading file: {e}")
    exit(1)

'''
stdout, stderr = data.communicate()
stdout = stdout.decode('utf-8')
stderr = stderr.decode('utf-8')
'''
print(data + "\n")
# print(stdout + "\n")
# print(stderr + "\n")