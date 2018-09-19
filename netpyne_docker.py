import sys
from subprocess import Popen

try:
    label, github = sys.argv[1], sys.argv[2]
except Exception as e:
    print("A label for the container and a github repository URL for the NetPyNE model must be provided")

script = 'docker build -t %s --build-arg GITHUB=%s -f ./dockerfile .'%(label, github)

with open('./cmd.sh', 'w') as f:
    f.write(script)

with open('out.log', 'w') as stdout, open('err.log', 'w') as stderr:
    Popen(['/bin/bash', '../cmd.sh'], stdout=stdout, stderr=stderr, cwd='./docker')

