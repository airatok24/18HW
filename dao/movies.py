# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.movies import Movies, MoviesSchema


class MoviesDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies = Movies.query.all()
        result = MoviesSchema(many=True).dump(movies)
        return result, 200
