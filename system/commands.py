
import os
import sys
from system.calls import *



def runserver_command():
    try:
        cmdline("python manage.py runserver")
    except Exception as e:
        print e