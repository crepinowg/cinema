#####################################################################
#
#
#
#
#
#
#####################################################################


def films():
    response.view = "reservation/cinema/index.html"
    return dict()

@auth.requires_login()
def reservations():
	"""
		Fournit la liste des réservations 
		de l'utilisatuer courant
	"""
	rows = db((db.reservation.user == auth.user_id ) & (db.affiche.film == db.film.id)).select( 
            join=db.affiche.on(db.reservation.affiche == db.affiche.id), 
            orderby=db.reservation.id
        )
	response.view = "reservation/cinema/reservations.html"
	return dict(reservations=rows)

@auth.requires_login()
def reserve():
	"""
		La page qui permet d'enrégistrer une réservation
	"""
	print(request.args)
	if len(request.args) == 0:
		return films()


	affiche_id = int(request.args[0])
	affiche = db(db.affiche.id==affiche_id).select(
		join=db.film.on(db.affiche.film == db.film.id)
	)

	if (len(affiche) == 0):
		return films()
	
	response.view = "reservation/cinema/reserve.html"
	return dict(affiche=affiche[0])