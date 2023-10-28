import re

from rest_framework.exceptions import ValidationError


class URLValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_value = dict(value).get(self.field)
        if field_value:
            if not bool(re.search(r'youtube.com', field_value)):
                raise ValidationError('Личные ссылки запрещены')
