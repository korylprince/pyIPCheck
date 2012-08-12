# coding: utf8

@auth.requires_login()
def index():
    response.subtitle = 'Let\'s see how we\'re doin\' here...'
    servers, switches = runscan()
    return dict(servers=servers,switches=switches)

def user():
    response.subtitle = 'What\'s the Secret Password?'
    return dict(form=auth())
