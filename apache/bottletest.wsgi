import bottle, os, sys
from beaker.middleware import SessionMiddleware

cur_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.dirname(os.path.dirname(cur_dir)))

bottle.TEMPLATE_PATH.append(os.path.join(os.path.dirname(cur_dir), 'templates'))
from bottletest.hello import *

session_opts = {
    'session.type': 'ext:database',
    'session.url': 'postgresql+psycopg2://postgres:abc@127.0.0.1/bottletest',
    'session.cookie_expires': True,
    'session.lock_dir': '/tmp',
    'session.auto': True
}
application = SessionMiddleware(bottle.default_app(), session_opts)
