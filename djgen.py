import os
import sys
from system.calls import *
from generators.main import *

# first check if we are in a django app. this is a quick fix though
try:
	os.path.isfile('./manage.py')
except Exception as e:
	print "file check error: "
	print e

generate_app('ddd')