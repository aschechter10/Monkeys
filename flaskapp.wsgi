#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/FlaskApp")
sys.path.append("/var/www/FlaskApp/FlaskApp/app/")

# from FlaskApp import db_manager
from FlaskApp import app as application
# application.secret_key = 'Add your secret key'
