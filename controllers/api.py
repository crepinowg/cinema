#####################################################################
#
#
#
#
#
#
#####################################################################

import datetime

#[START] Gestion des films
@request.restful()
@auth.requires_login()
def films():
    print("Request ", request.vars, request.post_vars)

    def POST(*args, **kwargs):
        """
    		Save a new film
        """
        #TODO
        titre = str(request.vars.titre)
        realisateur = str(request.vars.realisateur)
        duree = str(request.vars.duree)

        db.film.insert(titre=titre, realisateur=realisateur, duree=duree)
        return response.json({})

    def GET(*args, **kwargs):
        """
        	Get films by pagination or a single.
            
            @args contains the rest of the url.
                exemple: api/films/test -> args will contains test as first element
            @param kwargs will contains our page value
        """
        print(args, kwargs, request.vars)
        if request.vars.page != None: #kwargs['page']
            #Want to get mulptile film
            page = int(request.vars.page)
            start = (page-1)*100
            end = page*10

            rows = db().select(db.film.ALL, limitby=(start, end))
            for row in rows:
                print(row)
            return response.json(rows)
        else:
    		#Want to get a single fiilm
            #TODO check the length of the @param args
            #before accessing the first element
            film_id = int(args[0]) #TODO use try catch here
            film = db(db.film.id==film_id).select()

            if (len(film) == 0):
                raise HTTP(404)

            return response.json(film[0])
            
        raise HTTP(403)
    def PUT(*args, **kwargs):
        """
            Update a film
        """
        print("Request PUT", args, list(args), kwargs);
        film_id = int(list(args)[0])
        print("Film Id", film_id)
        film_query = db(db.film.id==film_id)

        film = film_query.select()
        if (len(film) == 0):
            raise HTTP(404)

        #We can now update the film
        titre = str(request.vars.titre)
        realisateur = str(request.vars.realisateur)
        duree = str(request.vars.duree)

        film_query.update(titre=titre, realisateur=realisateur, duree=duree)
        return response.json({})

    def DELETE(*args, **kwargs):
        """
            Update a film
        """
        film_id = int(args[0])
        film_query = db(db.film.id==film_id)

        film = db(db.film.id==film_id).select()
        if (len(film) == 0):
            raise HTTP(404)

        #Delete the film
        #TODO review the cascade
        film_query.delete()
        return response.json({})

    #Unsupported method, return locals
    return locals()



#[START] Gestion des affiches
@request.restful()
#@auth.requires_login() to authorize users to go through films
def affiches():
    print("Affiche Request ", request.vars, request.post_vars)

    @auth.requires_membership('administrators')
    def POST(*args, **kwargs):
        """
            Save a new film
        """
        #TODO
        currDate = datetime.datetime.now()
        film_id = int(request.vars.film)
        db.affiche.insert(film=film_id, created=str(currDate), image=request.vars.image)

        return response.json({})

    def GET(*args, **kwargs):
        """
            Get affiche by pagination or a single.
            
            @args contains the rest of the url.
                exemple: api/affiche/test -> args will contains test as first element
            @param kwargs will contains our page value
        """
        print(args, kwargs, request.vars)
        if request.vars.page != None: #kwargs['page']
            #Want to get mulptile film
            page = int(request.vars.page)
            start = (page-1)*5
            end = page*100

            rows = db(db.affiche).select( 
                join=db.film.on(db.affiche.film == db.film.id), 
                limitby=(start, end)
            )

            for row in rows:
                print(row)
            return response.json(rows)
        else:
            #Want to get a single fiilm
            #TODO check the length of the @param args
            #before accessing the first element
            affiche_id = int(args[0]) #TODO use try catch here
            affiche = db(db.affiche.id==affiche_id).select(
                join=db.film.on(db.affiche.film == db.film.id)
            )

            if (len(affiche) == 0):
                raise HTTP(404)

            return response.json(affiche[0])
            
        raise HTTP(403)

    @auth.requires_membership('administrators')
    def PUT(*args, **kwargs):
        """
            Update a film
        """
        print("Request PUT", args, list(args), kwargs);
        affiche_id = int(list(args)[0])
        print("Affiche Id", affiche_id)
        affiche_query = db(db.affiche.id==affiche_id)

        affiche = affiche_query.select()
        if (len(affiche) == 0):
            raise HTTP(404)

        #We can now update the film
        currDate = datetime.datetime.now()
        film_id = int(request.vars.film)

        film_query.update(film=film_id, created=str(currDate), image=request.vars.image)

        return response.json({})

    @auth.requires_membership('administrators')
    def DELETE(*args, **kwargs):
        """
            Update a film
        """
        affiche_id = int(args[0])
        affiche_query = db(db.affiche.id==affiche_id)

        affiche = affiche_query.select()
        if (len(affiche) == 0):
            raise HTTP(404)

        #Delete the film
        #TODO review the cascade
        affiche_query.delete()
        return response.json({})

    #Unsupported method, return locals
    return locals()


#[START] Gestion des reservations
@request.restful()
@auth.requires_login()
def reservations():
    print("Reservations Request ", request.vars, request.post_vars)

    def POST(*args, **kwargs):
        """
            Save a new film
        """
        #TODO
        places = int(request.vars.place)
        affiche_id = int(request.vars.affiche_id)
        
        db.reservation.insert(places=places, affiche=affiche_id, user=auth.user_id)

        return response.json({})

    def GET(*args, **kwargs):
        """
            Get reservation by pagination or a single.
            
            @args contains the rest of the url.
                exemple: api/affiche/test -> args will contains test as first element
            @param kwargs will contains our page value
        """
        print(args, kwargs, request.vars)
        if request.vars.page != None: #kwargs['page']
            #Want to get mulptile film
            page = int(request.vars.page)
            start = (page-1)*5
            end = page*100

            rows = db(db.affiche.film == db.film.id).select( 
                join=db.affiche.on(db.reservation.affiche == db.affiche.id), 
                limitby=(start, end)
            )

            for row in rows:
                print(row)
            return response.json(rows)
        else:
            return response.json({})

    return locals()
