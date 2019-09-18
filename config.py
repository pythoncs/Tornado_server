# -*- coding: UTF-8 -*-
#coding=utf-8
import os
# Tornado app configuration
settings = {
    'template_path': os.path.join(os.path.dirname('__file__'), 'temp'),
    'static_path': os.path.join(os.path.dirname('__file__'), 'statics'),
    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies':False,
    'login_url':'/login',
    'debug':True,
}

# log
log_path = os.path.join(os.path.dirname('__file__'), 'logs/log')
