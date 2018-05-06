from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('go9sn)w)g@90uqsx3kfrj&54%fdl1v10p5nl^5l(jh9h&kzpxj')

DEBUG = env.bool('DJANGO_DEBUG', default=True)