from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from expensesTracker.web.constants import constants as con


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError(
            con.VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE
        )


@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):  # same as 'validate_only_letters', but
        # we can provide the value dynamically
        filesize = value.file.size
        if filesize > self.__megabytes_to_bytes(self.max_size):  # in Mb
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * con.MB  # MB = 1024 * 1024 from constants

    def __get_exception_message(self):
        return f"Max file size is {self.max_size:.2f} MB"
