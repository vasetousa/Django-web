from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')
    return None


# in Mb
def image_size_validator(max_size):
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))

    return validate


@deconstructible
class MinDateValidator:
    def __int__(self, min_date):
        self.min_date = min_date

    def __call__(self, value):
        if value < self.min_date:
            raise ValidationError(f'Date must be greater than {self.min_date}')


@deconstructible
class MaxDateValidator:
    def __int__(self, max_date):
        self.min_date = max_date

    def __call__(self, value):
        if value > self.max_date:
            raise ValidationError(f'Date must be earlier than {self.max_date}')
