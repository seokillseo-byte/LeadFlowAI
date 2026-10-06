from datetime import datetime, timezone

def test_timestamp_is_timezone_aware():
    value = datetime.now(timezone.utc)
    assert value.tzinfo is not None
