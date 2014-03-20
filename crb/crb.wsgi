import os, sys
sys.path.append(os.path.abspath(os.path.split(__file__)[0]))
sys.path.append("C:\\project\\crb")
sys.path.insert(0, "C:\\project\\CRB2\\src\\django-mssql")

#print sys.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'crb.settings'

import sqlserver_ado
import sqlserver_ado.base
#print sqlserver_ado.base

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()