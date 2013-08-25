import sys
import os
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'libs'))
sys.path.insert(1, os.path.join(os.path.abspath('.'), 'app'))

from app.flask_app import app
