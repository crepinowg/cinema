#####################################################################
#
#
#
#
#
#
#####################################################################


def login():
	response.view = "reservation/auth/login.html"
	return dict(form=auth.login())

def register(): 
	response.view = "reservation/auth/register.html"
	return dict(form=auth.register())

