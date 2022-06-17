from django.core.exceptions import ValidationError

'''
Unit tests -> concrete isolated peace of code.
Integration tests -> integration of coupled pieces of code
'''

'''
Unit tests
'''


def validate_greater_than_zero(value):
    if value <= 0:
        raise ValidationError('Value must be greater than 0')


'''
- check for negative value -> Error
- check for 0 value (corner case) -> Error
- check for positive value -> No error
'''


def get_only_positive_values(values):
    positive_values = []
    for value in values:
        try:
            validate_greater_than_zero(value)
            positive_values.append(value)
        except:
            pass

    return positive_values


'''
# With unit tests:
Mock validate_greater_than_zero
- check for empty list
- check for list with positives
- check for list with negatives


# With integration tests:
- No mocking
'''
