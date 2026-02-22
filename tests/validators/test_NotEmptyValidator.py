from inquirer_textual.validators.NotEmptyValidator import NotEmptyValidator


def test_success():
    validator = NotEmptyValidator()

    result = validator.validate('Charlie')

    assert result.is_valid


def test_failure():
    validator = NotEmptyValidator()

    result = validator.validate('')

    assert not result.is_valid

    result = validator.validate('   ')

    assert not result.is_valid
