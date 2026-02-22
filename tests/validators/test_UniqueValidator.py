from examples.validator import UniqueValidator


def test_success():
    validator = UniqueValidator(['Alice', 'Bob'])

    result = validator.validate('Charlie')

    assert result.is_valid


def test_failure():
    validator = UniqueValidator(['Alice', 'Bob'])

    result = validator.validate('Bob')

    assert not result.is_valid