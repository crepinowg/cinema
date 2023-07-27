#####################################################################
#
#
#
#
#
#
#####################################################################


@auth.requires_login()
def profile(): 
	response.view = "reservation/user/profile.html"
	return dict(form=auth.profile())

def not_authorized(): 
	response.view = "reservation/error/403.html"
	return dict()
