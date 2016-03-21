from functools import wraps
from flask import jsonify, abort
from flask.ext.login import current_user
from models import Permission

def api_login_required(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		if not current_user.is_authenticated():
			return jsonify({'statecode': 403}) 
		return f(*args, **kwargs)
	return decorator
		
def permission_required(permission):
	def decorator(f):
		@wraps(f)
		def decorator_function(*args, **kwargs):
			if not current_user.can(permission):
				abort(403)
			return f(*args, **kwargs)
		return decorator_function
	return decorator

def admin_required(f):
	return permission_required(Permission.ADMINISTER)(f)