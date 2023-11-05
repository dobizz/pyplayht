import pytest

from pyplayht.types import GenerateStatus, OutputFormat, OutputQuality


@pytest.mark.parametrize(
    "type_class, fields",
    [
        (OutputFormat, {"FLAC", "MP3", "MULAW", "OGG", "WAV"}),
        (GenerateStatus, {"GENERATING", "COMPLETED", "ERROR"}),
        (OutputQuality, {"DRAFT", "LOW", "MEDIUM", "HIGH", "PREMIUM"}),
    ],
)
def test_static_types(type_class, fields):
    test_fields = set()
    for attr in dir(type_class):
        test_condition_1 = not callable(getattr(type_class, attr))
        test_condition_2 = not attr.startswith("__")
        if test_condition_1 and test_condition_2:
            test_fields.add(attr)
    assert test_fields == fields
