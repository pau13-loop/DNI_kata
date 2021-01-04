from src.dni import dniProgram
import pytest


def test_get_letter():
    assert 'N' == dniProgram('57955596').get_letter()
    assert 'M' == dniProgram('41967162').get_letter()
    assert 'R' == dniProgram('50170821').get_letter()
    assert 'M' == dniProgram('01781309').get_letter()
    assert 'Q' == dniProgram('87015111').get_letter()


def test_get_dni():
    assert '57955596N' == dniProgram(number,).get_dni()
    assert '41967162M' == dniProgram().get_dni()
    assert '50170821R' == dniProgram().get_dni()
    assert '01781309M' == dniProgram().get_dni()
    assert '87015111Q' == dniProgram().get_dni()


def test_prove_dni():
    assert True ==


def test_get_letter():
    assert 'N' == dniProgram('57955596').get_letter()
    assert 'M' == dniProgram('41967162').get_letter()
    assert 'R' == dniProgram('50170821').get_letter()
    assert 'M' == dniProgram('01781309').get_letter()
    assert 'Q' == dniProgram('87015111').get_letter()


def test_get_dni():
    assert '57955596N' == dniProgram(number,).get_dni()
    assert '41967162M' == dniProgram().get_dni()
    assert '50170821R' == dniProgram().get_dni()
    assert '01781309M' == dniProgram().get_dni()
    assert '87015111Q' == dniProgram().get_dni()


def test_prove_dni():
    assert True ==
