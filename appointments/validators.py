from django.core.exceptions import ValidationError
import datetime


def validate_text(value: str) -> None:
    if len(value) == 0:
        raise ValidationError('Title and Subject must not be blank')
    if not value[0].isupper():
        raise ValidationError('Title and Subject must be capitalized')


def validate_date(value: datetime) -> None:
    if value <= datetime.datetime.now():
        raise ValidationError('The appointment must not be in the past or right now')
