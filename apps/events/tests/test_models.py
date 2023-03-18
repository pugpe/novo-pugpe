import pytest

from apps.events.models import Event, Venue


@pytest.mark.django_db
def test_can_create_event():
    e = Event.objects.create(
        name="Test Event",
        description="This is a test event",
        start_date="2023-04-01 10:00:00 -03:00",
    )

    assert str(e) == "Test Event"


@pytest.mark.django_db
def test_event_should_have_a_venue():
    v = Venue.objects.create(
        name="Test Venue",
        address_line_1="Universidade Federal de Pernambuco, Centro de Informática",
        address_line_2="Anfiteatro",
        neighborhood="Cidade Universitária",
        city="Recife",
        state="PE",
        instructions="Entrar pela porta principal",
    )

    e = Event.objects.create(
        name="Test Event",
        description="This is a test event",
        start_date="2023-04-01 10:00:00 -03:00",
        venue=v,
    )

    assert str(e) == "Test Event"
    assert e.venue == v
