
import os
import sys
from system.calls import *

def generate_urls_py(app_name):
    value="from django.conf.urls import url\nfrom . import views\n\n\nurlpatterns = [\n\turl(r\'^$\', views.index, name=\'index\'),\n]"
    file_write('./'+app_name+'/urls.py',value)


def generate_view_py(app_name,file_name):
    directory = './'+app_name+'/'+'templates/'+app_name
    if not os.path.exists(directory):
        os.makedirs(directory)
    html = open('./generators/resources/index.html')
    value= html.read()
    file_write(directory+'/'+file_name,value)      


def generate_app(name):
    try:
        cmdline("django-admin.py startapp "+name)
        generate_urls_py(name)
        generate_view_py(name,'index.html')
    except Exception as e:
        print e



