import os
import sys
from system.calls import *
from generators.main import *
from system.commands import *
# first check if we are in a django app. this is a quick fix though
'''try:
	os.path.isfile('./manage.py')
except Exception as e:
	print "this is not a django folder: "
	print e'''


if sys.argv[1]=='new':
	if sys.argv[2]=='project':
		generate_project(sys.argv[3])
	elif sys.arg[2]=='app':
		generate_app(sys.argv[3])
	elif sys.arg[2]=='view':
		generate_view(sys.argv[3],sys.argv[4])
	elif sys.arg[2]=='template':
		generate_template(sys.argv[3],sys.argv[4])
	elif sys.arg[2]=='urls':
		generate_urls_py(sys.argv[3],sys.argv[4])
	else:
		print "An error occurred parsing command line arguements."
elif sys.argv[1]=='run':
	runserver_command()
elif sys.argv[1]=='version':
	print "0.2.0"
else:
	print "Welcome to djgen."
	print "Would you like to generate a new app?(Y/N)"
	next_command = raw_input()
	if next_command=='y':
		generate_project
	elif next_command=='n':
		print "thanks!"
