# coding: utf8
from ipcheck import runscan

@auth.requires_login()
def index():
    response.subtitle = 'Let\'s see how we\'re doin\' here...'
    servers, switches = runscan(db)
    return dict(servers=servers,switches=switches)

def user():
    response.subtitle = 'What\'s the Secret Password?'
    return dict(form=auth())
