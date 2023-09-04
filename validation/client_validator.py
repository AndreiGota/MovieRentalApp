from errors.custom_exceptions import ValidationError


class ClientValidator:
    @staticmethod
    def validate(client):
        errors = ''
        if client.id < 0:
            errors += "'{}' is not a valid client ID.\n".format(client.id)
        if client.name == '':
            errors += 'Invalid client name.\n'
        if len(errors) > 0:
            raise ValidationError(errors)
