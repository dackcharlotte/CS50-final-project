import pytest
import sys
from unittest.mock import patch, mock_open, MagicMock

from project import check_extention, check_if_souce_eng, check_lang_in_dict, merging_txt

def test_check_extention_valid_extension(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['project.py', 'testfile.txt'])
    assert check_extention() == True

def test_check_extention_invalid_extension(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['project.py', 'testfile.pdf'])
    with pytest.raises(SystemExit) as e:
        check_extention()
    assert str(e.value) == "The file type is invalid. The File must be a .txt file"

def test_check_if_souce_eng_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'English')
    assert check_if_souce_eng() == "EN"

def test_check_if_souce_eng_invalid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'French')
    with pytest.raises(SystemExit) as e:
        check_if_souce_eng()
    assert str(e.value) == "This source language is currently not supported."

def test_check_lang_in_dict_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'Spanish')
    monkeypatch.setattr(sys, 'argv', ['project.py', 'testfile.txt'])
    assert check_lang_in_dict() == "ES"

def test_check_lang_in_dict_invalid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'InvalidLanguage')
    with pytest.raises(SystemExit) as e:
        check_lang_in_dict()
    assert str(e.value) == "Language not valid"

def test_merging_txt(monkeypatch):
    m = mock_open(read_data='line1\nline2\nline3\n')
    with patch('builtins.open', m):
        name_of_file = 'testfile'
        monkeypatch.setattr(sys, 'argv', ['project.py', f'{name_of_file}.txt'])
        assert merging_txt(name_of_file) == True
