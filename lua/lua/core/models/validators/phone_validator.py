from django.core.validators import RegexValidator

"""
Source: Igor Kravtsov, http://regexlib.com/REDetails.aspx?regexp_id=58

Matches US phone number format. 1 in the beginning is optional,
    area code is required, spaces or dashes can be used as optional divider between number groups.
Also alphanumeric format is allowed after area code.

Matches: 1-(123)-123-1234 | 123 123 1234 | 1-800-ALPHNUM
Non-matches: 1.123.123.1234 | (123)-1234-123 | 123-1234
"""
phone_validator = RegexValidator(regex=r'^([0-9]( |-)?)?(\(?[0-9]{3}\)?|'
                                   r'[0-9]{3})( |-)?([0-9]{3}( |-)?[0-9]{4}|'
                                   r'[a-zA-Z0-9]{7})$',
                             message="Allowed formats: 1-(123)-123-1234 | 123 123 1234 | 1-800-ALPHNUM")
