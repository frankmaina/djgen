from subprocess import call,Popen,check_output,PIPE
import os
import sys
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]



def file_write(file_name,value):
	f = open(file_name,'w')
	f.write(value+'\n')
	f.close() 
	return 0