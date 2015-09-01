#!/usr/bin/env python
import os
import sys
from subprocess import call,Popen,check_output,PIPE

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

def generate_app(name):
	try:
		cmdline("django-admin.py startapp "+name)
		value="from django.conf.urls import url\nfrom . import views\n\n\nurlpatterns = [\n\turl(r\'^$\', views.index, name=\'index\'),\n]"
		file_write('./'+name+'/urls.py',value)
		directory = './'+name+'/'+'templates/'+name
		if not os.path.exists(directory):
			os.makedirs(directory)
		value="<html>\n</html>"
		file_write(directory+'/index.html',value)	
	except Exception as e:
		print e



def generate_urls_py(app_name):
	value="from django.conf.urls import url\nfrom . import views\n\n\nurlpatterns = [\n\turl(r\'^$\', views.index, name=\'index\'),\n]"
	file_write('./'+app_name+'/urls.py',value)



    

# first check if we are in a django app. this is a quick fix though
try:
	os.path.isfile('./manage.py')
except Exception as e:
	print "file check error: "
	print e

generate_app('ddd')