from myproject import info


def test_myfunction():
    assert info().startswith("Using myproject")
