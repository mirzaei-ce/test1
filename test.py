from subprocess import Popen,PIPE
import subprocess
import os,time
from github import Github

p = Popen(["ssh-keygen","-t","rsa","-b","4096","-C","test@gmail.com"], stdout=PIPE, stdin=PIPE,)
p.communicate("id_rsa")

subprocess.call("ssh-add id_rsa",shell=True)

g = Github("mirzaei-ce","Mahdi@1993")
key = open("id_rsa.pub").read()
print g.get_user().create_key("server",key)


print g.get_user().create_repo("test1")

subprocess.call("git init", shell=True)
subprocess.call("git config user.name mirzaei-ce", shell=True)
subprocess.call("git config user.email mirzaei@ce.sharif.edu", shell=True)
subprocess.call("git add .", shell=True)
subprocess.call("git commit -m 'init'", shell=True)
subprocess.call("git remote add origin git@github.com:mirzaei-ce/test1.git",shell=True)

p1 = Popen(["git","push","-u","origin","master"], stdout=PIPE, stdin=PIPE,)

p1.communicate()