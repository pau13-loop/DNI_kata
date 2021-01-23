from src.main import Dni, AllocationTable
import pytest


def test_set_dni_number():
    # Correct test cases
    assert True == Dni('57955596').validate_dni_number()
    assert True == Dni('41967162').validate_dni_number()
    assert True == Dni('50170821').validate_dni_number()
    assert True == Dni('01781309').validate_dni_number()
    assert True == Dni('87015111').validate_dni_number()
    #! Not correct test cases
    # Less or more than an allowed length
    assert False == Dni('1234567').validate_dni_number()
    assert False == Dni('123456789').validate_dni_number()
    # Mix of letters and numbers
    assert False == Dni('12as56gr').validate_dni_number()
    assert False == Dni('1g3j5d7n').validate_dni_number()
    # Correct length but not of numbers
    assert False == Dni('abcdefgh').validate_dni_number()


def test_get_dni_letter():
    # Correct test cases
    assert 'N' == AllocationTable('57955596').get_nif_letter()
    assert 'M' == AllocationTable('41967162').get_nif_letter()
    assert 'R' == AllocationTable('50170821').get_nif_letter()
    assert 'M' == AllocationTable('01781309').get_nif_letter()
    assert 'Q' == AllocationTable('87015111').get_nif_letter()


def test_set_dni():
    # Correct test cases
    assert '57955596N' == Dni('57955596').set_dni()
    assert '41967162M' == Dni('41967162').set_dni()
    assert '50170821R' == Dni('50170821').set_dni()
    assert '01781309M' == Dni('01781309').set_dni()
    assert '87015111Q' == Dni('87015111').set_dni()
    #! Not correct test cases
    # Less or more than an allowed length
    assert 'Try again please !' == Dni('1234567').set_dni()
    assert 'Try again please !' == Dni('123456789').set_dni()
    # Mix of letters and numbers
    assert 'Try again please !' == Dni('12as56gr').set_dni()
    assert 'Try again please !' == Dni('1g3j5d7n').set_dni()
