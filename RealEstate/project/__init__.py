from flask import *

app = Flask(__name__)

app.secret_key = app.config['SECRET_KEY'] = 'abc'

#login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'loadLogin'

import project.com.controller