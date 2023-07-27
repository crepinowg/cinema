#####################################################################
#
#
#
#
#
#
#####################################################################

@auth.requires_membership('administrators')
def films():
    #films_data = db().select(db.film.ALL)
    response.view = "reservation/backOffice/films.html"
    #return dict(method=request.method, films_grid=SQLFORM.grid(db.film), films=films_data)
    return dict()

@auth.requires_membership('administrators')
def affiches():
    films_data = db().select(db.film.ALL)
    response.view = "reservation/backOffice/affiches.html"
    return dict(films=films_data)

@auth.requires_membership('administrators')
def reservations():
    """
        Récupérer la liste de tous les utilsateurs confondu
    """
    rows = db((db.affiche.film == db.film.id) & (db.reservation.user == db.auth_user.id)).select( 
            join=db.affiche.on(db.reservation.affiche == db.affiche.id), 
            orderby=db.reservation.id
        )
    response.view = "reservation/backOffice/reservations.html"
    return dict(reservations=rows)