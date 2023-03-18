import pytest

from apps.events.models import Event


@pytest.mark.django_db
def test_can_create_event():
    e = Event.objects.create(
        name="Test Event",
        description="This is a test event",
        start_date="2023-04-01",
    )

    assert e.name == "Test Event"