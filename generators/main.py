
import os
import sys
sys.path.append('../system/')
from system.calls import *

def generate_urls_py(app_name):
    value="from django.conf.urls import url\nfrom . import views\n\n\nurlpatterns = [\n\turl(r\'^$\', views.index, name=\'index\'),\n]"
    file_write('./'+app_name+'/urls.py',value)


def generate_template(app_name,file_name):
    directory = './'+app_name+'/'+'templates/'+app_name
    if not os.path.exists(directory):
        os.makedirs(directory)
    html = open(os.path.abspath('generators/resources/index.html'))
    value= html.read()
    template_path = directory+'/'+file_name+'.html'
    file_write(template_path,value)      
    return template_path


def generate_app(name):
    try:
        cmdline("django-admin.py startapp "+name)
        generate_urls_py(name)
        generate_template(name,'index.html')
    except Exception as e:
        print e


def generate_view(app_name,view_name):
    view_template = view_name
    template_path = generate_template(app_name,view_template)
    #now we append to the view file
    view_code = "\n\ndef "+view_name+"(request):\n\treturn render(request, \'"+template_path+"\')\n"
    with open(app_name+'/views.py', "a") as myfile:
        myfile.write(view_code)


def generate_project(project_name):
    try:
        cmdline("django-admin.py startproject "+project_name+' .')
    except Exception as e:
        print e