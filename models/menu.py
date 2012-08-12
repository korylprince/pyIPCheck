# -*- coding: utf-8 -*-

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################
if auth.is_logged_in():
    response.menu = [
        (SPAN('Scan', _style='color:#fff;font-size:13pt;'), False, URL('default','index'), [])
        ]
else:
    response.menu = []
