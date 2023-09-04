from errors.custom_exceptions import ValidationError


class MovieValidator:
    @staticmethod
    def validate(movie):
        errors = ''
        if movie.id < 0:
            errors += "'{}' is not a valid movie ID.\n".format(movie.id)
        if movie.title == '':
            errors += 'Invalid movie title.\n'
        if movie.description == '':
            errors += 'Invalid movie description.\n'
        if movie.genre == '':
            errors += 'Invalid movie genre.\n'
        if len(errors) > 0:
            raise ValidationError(errors)
