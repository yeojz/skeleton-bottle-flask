from functools import wraps
from google.appengine.api import users
from flask import redirect, request, abort

def requireLogin(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not users.get_current_user():
            return redirect(users.create_login_url(request.url))
        elif not users.is_current_user_admin():
            #return redirect(users.create_logout_url(request.url))
            return abort(403)
        return func(*args, **kwargs)
    return decorated_view
