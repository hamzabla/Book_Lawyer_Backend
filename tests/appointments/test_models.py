import pytest
from django.core.exceptions import ValidationError
from mixer.backend.django import mixer
from appointments.validators import validate_text


def test_appointment_title_of_length_31_raise_exception(db):
    customer = mixer.blend('appointments.Appointment', title='A' * 31)
    with pytest.raises(ValidationError):
        customer.full_clean()


def test_title_not_capitalized_raised_exception(db):
    customer = mixer.blend('appointments.Appointment', title='appuntamento divorzio')
    with pytest.raises(ValidationError) as err:
        customer.full_clean()
    assert 'capitalized' in '\n'.join(err.value.messages)


def test_appointment_subject_of_length_201_raise_exception(db):
    customer = mixer.blend('appointments.Appointment', title='A' * 201)
    with pytest.raises(ValidationError):
        customer.full_clean()


def test_subject_not_capitalized_raised_exception(db):
    customer = mixer.blend('appointments.Appointment', title='salve, vorrei appuntamento divorzio ...')
    with pytest.raises(ValidationError) as err:
        customer.full_clean()
    assert 'capitalized' in '\n'.join(err.value.messages)
