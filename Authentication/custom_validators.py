import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class UppercaseValidator:
    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least one uppercase letter."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _("The password must contain at least one uppercase letter.")


class LowercaseValidator:
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least one lowercase letter."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _("The password must contain at least one lowercase letter.")


class SymbolValidator:
    def validate(self, password, user=None):
        if not re.findall('[ !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]', password):
            raise ValidationError(
                _("The password must contain at least one special character."),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _("The password must contain at least one special character.")
