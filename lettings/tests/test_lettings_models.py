import pytest
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting

"""
    Tests of models.py of the 'lettings' application.
"""


@pytest.mark.django_db
def test_address_creation():
    """
        Test that an Adress instance is correctly created
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )

    assert address.number == 1
    assert address.street == "Avenue des Champs-Élysées"
    assert address.city == "Paris"
    assert address.state == "FR"
    assert address.zip_code == 75008
    assert address.country_iso_code == "FRA"


@pytest.mark.django_db
def test_address_str_method():
    """
        Test the __str__ method of the Address model.
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )

    assert str(address) == "1 Avenue des Champs-Élysées"


@pytest.mark.django_db
def test_address_meta_verbose_name_plural():
    """
        Test the verbose_name_plural attribute of the Address model.
    """
    assert Address._meta.verbose_name_plural == "Addresses"


@pytest.mark.django_db
def test_address_max_length():
    """
        Test that max_length constraints are enforced for Address fields.
    """
    address = Address(
        number=1,
        street="A" * 65,  # More than max_length=64
        city="B" * 65,  # More than max_length=64
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )

    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()

    errors = excinfo.value.message_dict

    assert "street" in errors
    assert "city" in errors

    assert len(errors) == 2


@pytest.mark.django_db
def test_address_min_length():
    """
        Test that MinLengthValidator constraints are enforced for Address fields.
    """
    address = Address(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="F",  # Less than 2 characters
        zip_code=75008,
        country_iso_code="FR"  # Less than 3 character
    )

    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()

    errors = excinfo.value.message_dict

    assert "state" in errors
    assert "country_iso_code" in errors

    assert len(errors) == 2


@pytest.mark.django_db
def test_address_max_value():
    """
        Test that MaxValueValidator constraints are enforced for Address fields.
    """
    address = Address(
        number=10000,  # More than max=9999
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=100000,  # More than max=99999
        country_iso_code="FRA"
    )

    with pytest.raises(ValidationError) as excinfo:
        address.full_clean()

    errors = excinfo.value.message_dict

    assert "number" in errors
    assert "zip_code" in errors

    assert len(errors) == 2


@pytest.mark.django_db
def test_letting_creation():
    """
        Test that a Letting instance is correctly created
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Great Apartment", address=address)

    assert letting.title == "Great Apartment"
    assert letting.address == address


@pytest.mark.django_db
def test_letting_str_method():
    """
        Test the __str__ method of the Letting model.
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )
    letting = Letting.objects.create(title="Great Apartment", address=address)

    assert str(letting) == "Great Apartment"


@pytest.mark.django_db
def test_letting_on_delete_cascade():
    """
        Test that deleting an Address deletes the associated Letting
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )
    Letting.objects.create(title="Great Apartment", address=address)

    address.delete()

    assert Letting.objects.count() == 0


@pytest.mark.django_db
def test_letting_max_length():
    """
        Test that max_length constraints are enforced for Letting fields.
    """
    address = Address.objects.create(
        number=1,
        street="Avenue des Champs-Élysées",
        city="Paris",
        state="FR",
        zip_code=75008,
        country_iso_code="FRA"
    )

    letting = Letting.objects.create(title="A"*257, address=address)  # More than max_length=256

    with pytest.raises(ValidationError) as excinfo:
        letting.full_clean()

    errors = excinfo.value.message_dict

    assert "title" in errors
    assert len(errors) == 1
