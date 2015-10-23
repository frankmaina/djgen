import os
import sys
from system.calls import *
from generators.main import *
from system.commands import *
import logging

#some basic configs
logging.basicConfig(filename='djgen.log',level=logging.DEBUG)
app_version = "0.3.0"



#we initiate options that are available through the command line
import argparse
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
parser.add_argument("--new", help="Start a new Django Project.",
                    type=str)
parser.add_argument("--app", help="Create a new Django App.",
                    type=str)
parser.add_argument("--view", help="Generate an app View.",
                    type=str)
parser.add_argument("--template", help="Generate a Template to a specific app.",
                    type=str)
parser.add_argument("--urls", help="Generate an app urls.py file.",
                    type=str)
group.add_argument("--version","-v", help="App version.",action='store_true')
args = parser.parse_args()



# first check if we are in a django app. this is a quick fix though
def check_folder():
	if not os.path.isfile('./manage.py'):
		logging.debug("\nAttempted action on a non-django direcotry.\n")
		sys.exit("This is not a django folder!")



# then process the arguements passed
try:
	if args.new:
		generate_project(args.new)
		print "The Project "+args.new+" has been generated."
	elif args.app and not args.view and not args.template and not args.urls:
		check_folder()
		generate_app(args.app)
		print "The app "+args.app+" has been generated."
	elif args.view and args.app:
		check_folder()
		generate_view(args.app,args.view)
		print "The view has been generated for the app: " + args.app
	elif args.template and args.app:
		check_folder()
		generate_template(args.app,args.template)
		print "The template file has been generated for the app: " + args.app
	elif args.urls and args.app:
		check_folder()
		generate_urls_py(args.app)
		print "A urls.py file has been generated for the app: " + args.app
	elif sys.argv[1]=="version" or "-v":	
		print "Djgen Version: "+ app_version
	else:
		print "An error occurred parsing command line arguements."
		logging.debug("An error occurred parsing command line arguements.")
except Exception as e:
	logging.debug('\n\n'+e)
