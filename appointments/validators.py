from django.core.exceptions import ValidationError
import datetime


def validate_text(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Title and Subject must not be blank')
    if not value[0].isupper():
        raise ValidationError('Title and Subject must be capitalized')
