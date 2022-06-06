from flask_restx import Resource, Namespace

from implemented import movies_service

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = movies_service.get_all()
        return movies, 200
