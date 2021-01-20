from src.main import DNI
import pytest


def test_dni_validation():
    # Correct test cases
    assert True == DNI('57955596').dni_validation()
    assert True == DNI('41967162').dni_validation()
    assert True == DNI('50170821').dni_validation()
    assert True == DNI('01781309').dni_validation()
    assert True == DNI('87015111').dni_validation()
    #! Not correct test cases
    # Less or more than an allowed length
    assert False == DNI('1234567').dni_validation()
    assert False == DNI('123456789').dni_validation()
    # Mix of letters and numbers
    assert False == DNI('12as56gr').dni_validation()
    assert False == DNI('1g3j5d7n').dni_validation()


def test_get_letter():
    # Correct test cases
    assert 'N' == DNI('57955596').get_letter()
    assert 'M' == DNI('41967162').get_letter()
    assert 'R' == DNI('50170821').get_letter()
    assert 'M' == DNI('01781309').get_letter()
    assert 'Q' == DNI('87015111').get_letter()
    #! Not correct test cases
    # Less or more than an allowed length
    assert False == DNI('1234567').get_letter()
    assert False == DNI('123456789').get_letter()
    # Mix of letters and numbers
    assert False == DNI('12as56gr').get_letter()
    assert False == DNI('1g3j5d7n').get_letter()


def test_get_dni():
    # Correct test cases
    assert '57955596N' == DNI('57955596').get_dni()
    assert '41967162M' == DNI('41967162').get_dni()
    assert '50170821R' == DNI('50170821').get_dni()
    assert '01781309M' == DNI('01781309').get_dni()
    assert '87015111Q' == DNI('87015111').get_dni()
    #! Not correct test cases
    # Less or more than an allowed length
    assert 'Try again please !' == DNI('1234567').get_dni()
    assert 'Try again please !' == DNI('123456789').get_dni()
    # Mix of letters and numbers
    assert 'Try again please !' == DNI('12as56gr').get_dni()
    assert 'Try again please !' == DNI('1g3j5d7n').get_dni()
