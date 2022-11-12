from albums.serializers import *
from albums.models import *
import zoneinfo, pytest


@pytest.mark.django_db
def test_contains_expected_fields():
    input_data = {
        "name": "album",
        "release_date": datetime(2023, 11, 10, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost": 120
    }
    print(input_data)
    serializer = AlbumSerializer(data=input_data)
    serializer.is_valid(raise_exception=False)
    output_data = serializer.validated_data
    assert input_data['name'] == output_data['name']
    assert input_data['cost'] == output_data['cost']
    assert input_data['release_date'] == output_data['release_date']
