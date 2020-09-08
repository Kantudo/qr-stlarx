from django.utils.deconstruct import deconstructible
from django.core.exceptions import ValidationError

@deconstructible
class FileSizeValidator:

    message = (
        'File size “%(size)s” is not allowed. '
        'Allowed size is: %(allowed_size)s.'
    )
    code = 'invalid_size'

    def __init__(self, allowed_size=2, message=None, code=None):

        self.allowed_size = allowed_size
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code

    def __call__(self, value):
        limit = self.allowed_size * 1024 * 1024
        size = value.size
        if value.size > limit:
            raise ValidationError(
                self.message,
                code=self.code,
                params={
                    'size': str(round(size/(1024**2), 2))+' MB',
                    'allowed_size': str(self.allowed_size) + ' MB',
                    'value': value,
                }
            )

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.allowed_size == other.allowed_size and
            self.message == other.message and
            self.code == other.code
        )
