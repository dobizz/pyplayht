from pyplayht.classes import Client


def test_client():
    client = Client()
    # check for available methods
    assert hasattr(client, "get_voices") and callable(client.get_voices)
    assert hasattr(client, "new_conversion_job") and callable(
        client.new_conversion_job,
    )
    assert hasattr(client, "get_coversion_job_status") and callable(
        client.get_coversion_job_status,
    )
    assert hasattr(client, "download_file") and callable(client.download_file)
