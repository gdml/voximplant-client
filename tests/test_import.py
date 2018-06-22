def test_import(client):
    from voximplant_client import VoximplantClient
    assert VoximplantClient is not None
