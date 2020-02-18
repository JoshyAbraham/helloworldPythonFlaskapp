from functools import wraps
from flask import request, abort

def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):

        # can figure out how to manage the keys later
        if request.args.get('key') and request.args.get('key') == 'APPKEY_HERE':
            return view_function(*args, **kwargs)
        else:
            abort(401)
    return decorated_function