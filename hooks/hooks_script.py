#!/usr/bin/python

import sys
import os
import subprocess
from subprocess import Popen, PIPE
import time
import pexpect

hooked_commands = ["pull", "push", "commit"]
git_cmd = "/usr/bin/git"

def main(argv):
	
	if "pull" in argv :
		pull_hook(argv)
	elif "push" in argv :
		push_hook(argv)
	else :
		print("commande originale :")
		os.system(git_cmd + " " + array_to_string(argv))
	
	

def pull_hook(argv):
	#pre_pull (nothing to do here for the moment)
	
	#we execute the real git pull

	#built the array for the command and args
	full_cmd = argv
	full_cmd.insert(0, git_cmd)
	#create the proc
	proc = subprocess.Popen(full_cmd, stdout=subprocess.PIPE)
	#communicate with the proc
	stdout_value = proc.communicate()[0].decode("utf-8")
	print(stdout_value)
	#if it's already up to date we don't have to do anything anymore
	if "Already up-to-date" in stdout_value :
		return
	
	#post_pull 
	#Here we will refactor our class
	os.system('echo "test" >> f')
	
	#TODO : get list of modified file
	#git diff --name-only
	
	#on add les files
	proc = subprocess.Popen([git_cmd, 'add', 'f'], stdout=subprocess.PIPE)
	stdout_value = proc.communicate()[0].decode("utf-8")
	print(stdout_value)
	
	#on commit
	proc = subprocess.Popen([git_cmd, 'commit', '-m', '"user refactor (will be deleted)"'], stdout=subprocess.PIPE)
	stdout_value = proc.communicate()[0].decode("utf-8")
	print(stdout_value)
	

	
	
def push_hook(argv):
	print("push hook")
	

def commit_hook(argv):
	print("commit hook")
	
def array_to_string(argv):
	arg_string = ""
	for arg in argv :
		arg_string += arg + " "
	return arg_string
	
"""
will execute the cmd in the system.
the main cmd and each argument have to be in an element of the list
return the value of the command
"""
def execute_cmd(arg_list, print_it=True):
	#create the proc
	proc = subprocess.Popen(arg_list, stdout=subprocess.PIPE)
	#communicate with the proc and get the stdout value
	stdout_value = proc.communicate()[0].decode("utf-8")
	if print_it != False :
		print(stdout_value)
	return stdout_value

def check_if_pending_commit():
	arg_list = [ git_cmd, "cherry", "-v" ]
	res = execute_cmd(arg_list, print_it=False)
	if res == "" :
		return False
	elif res.startswith("+ ") :
		return True
	#there is a problem, for example we don't have this branch pushed in local
	else :
		print(res)
		return True
	


if __name__ == "__main__":
   main(sys.argv[1:])
