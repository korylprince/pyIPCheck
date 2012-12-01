# coding: utf8
from ipcheck import runscan

def json():
    if request.vars['username'] is None or request.vars['password'] is None:
        raise HTTP(400, "Bad Request")
    if not auth.settings.login_methods[0](request.vars['username'],request.vars['password']):
        raise HTTP(403, "Permission Denied") 
    servers,switches = runscan(db)
    return dict(servers=servers,switches=switches)
