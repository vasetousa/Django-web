from django.core.exceptions import ValidationError


def only_letters_numbers_underscore_validator(value):
    message = 'Ensure this value contains only letters, numbers and underscore.'
    for char in value:
        if not char.isalpha() and not char.isdigit() and not char == '_':
            raise ValidationError(message)


def negative_number_validator(value):
    message = 'Age can not be a negative number!'
    if value < 0:
        raise ValidationError(message)
