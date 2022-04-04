import dj_database_url 

from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

DATABASES ['default'] = dj_database_url.config('postgres://vfdkukbkivpjzp:b72e1bed07a219cd6d972a21d1c3ecbc7eb73c4cdb1ba90ca7e3c840191b28c9@ec2-176-34-211-0.eu-west-1.compute.amazonaws.com:5432/d4m8c8m6rfp347')

SECRET_KEY = 'n+rayy91un9ruz2p)s$zy%6w_n*adx(3ma(5-hfw_@!=b_j3b_'

ALLOWED_HOSTS = ['galleries-app.herokuapp.com']