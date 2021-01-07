from src.main import dniProgram
import pytest


def test_dni_validation():
    # Correct test cases
    assert True == dniProgram('57955596').dni_validation()
    assert True == dniProgram('41967162').dni_validation()
    assert True == dniProgram('50170821').dni_validation()
    assert True == dniProgram('01781309').dni_validation()
    assert True == dniProgram('87015111').dni_validation()
    #! Not correct test cases
    # Less or more than an allowed length
    assert False == dniProgram('1234567').dni_validation()
    assert False == dniProgram('123456789').dni_validation()
    # Mix of letters and numbers
    assert False == dniProgram('12as56gr').dni_validation()
    assert False == dniProgram('1g3j5d7n').dni_validation()


def test_get_letter():
    # Correct test cases
    assert 'N' == dniProgram('57955596').get_letter()
    assert 'M' == dniProgram('41967162').get_letter()
    assert 'R' == dniProgram('50170821').get_letter()
    assert 'M' == dniProgram('01781309').get_letter()
    assert 'Q' == dniProgram('87015111').get_letter()
    #! Not correct test cases
    # Less or more than an allowed length
    assert False == dniProgram('1234567').get_letter()
    assert False == dniProgram('123456789').get_letter()
    # Mix of letters and numbers
    assert False == dniProgram('12as56gr').get_letter()
    assert False == dniProgram('1g3j5d7n').get_letter()


def test_get_dni():
    # Correct test cases
    assert '57955596N' == dniProgram('57955596').get_dni()
    assert '41967162M' == dniProgram('41967162').get_dni()
    assert '50170821R' == dniProgram('50170821').get_dni()
    assert '01781309M' == dniProgram('01781309').get_dni()
    assert '87015111Q' == dniProgram('87015111').get_dni()
    #! Not correct test cases
    # Less or more than an allowed length
    assert 'Try again please !' == dniProgram('1234567').get_dni()
    assert 'Try again please !' == dniProgram('123456789').get_dni()
    # Mix of letters and numbers
    assert 'Try again please !' == dniProgram('12as56gr').get_dni()
    assert 'Try again please !' == dniProgram('1g3j5d7n').get_dni()
