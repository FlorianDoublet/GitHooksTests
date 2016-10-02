import pexpect
import subprocess

proc = subprocess.Popen(['/usr/bin/git', 'push'], stdout=subprocess.PIPE)

stdout_value = proc.communicate()[0].decode("utf-8")
if stdout_value == "" :
	print("ya rien dedans :( ")
else :
	print("ya un truc " + stdout_value)

