import datetime

from domain.client import Client
from domain.movie import Movie
from domain.rental import Rental


class EntityDataAccess:
    """
    Abstract entity data access class
    """
    @staticmethod
    def read_from(line):
        pass

    @staticmethod
    def write_to(file, entity):
        pass

    @staticmethod
    def get_line(self, entity):
        pass


class MovieDataAccess(EntityDataAccess):
    """
        Abstract movie data access class
    """
    def read_from(self, line):
        tokens = line.split(';')
        movie = Movie(tokens[1], tokens[2], tokens[3])
        movie.id = int(tokens[0])
        return movie

    def write_to(self, file, movie):
        movie_string = self.get_line(movie)
        file.write(movie_string)

    def get_line(self, movie):
        return str(movie.id) + ';' + movie.title + ';' + movie.description + ';' + movie.genre + ';\n'


class ClientDataAccess(EntityDataAccess):
    """
        Abstract movie data access class
    """
    def read_from(self, line):
        tokens = line.split(';')
        client = Client(tokens[1])
        client.id = int(tokens[0])
        return client

    def write_to(self, file, client):
        client_string = self.get_line(client)
        file.write(client_string)

    def get_line(self, client):
        return str(client.id) + ';' + client.name + ';\n'


class RentalDataAccess(EntityDataAccess):
    """
        Abstract movie data access class
    """
    def read_from(self, line):
        tokens = line.split(';')
        rented_date = datetime.datetime.strptime(tokens[3], '%Y-%m-%d').date()
        due_date = datetime.datetime.strptime(tokens[4], '%Y-%m-%d').date()
        returned_date = datetime.datetime.strptime(tokens[5], '%Y-%m-%d').date()
        rental = Rental(int(tokens[1]), int(tokens[2]), rented_date, due_date, returned_date)
        rental.id = int(tokens[0])
        return rental

    def write_to(self, file, rental):
        rental_string = self.get_line(rental)
        file.write(rental_string)

    def get_line(self, rental):
        return str(rental.id) + ';' + str(rental.movie_id) + ';' + str(rental.client_id) + ';' + str(rental.rented_date) + ';' + str(rental.due_date) + \
                        ';' + str(rental.returned_date) + ';\n'
