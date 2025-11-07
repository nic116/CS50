from plates import is_valid


def test_valid():
    assert is_valid("HELLO") == True
    assert is_valid("TROOP") == True
    assert is_valid("CS50") == True

def test_invalid():
    assert is_valid("HELLOWORLD") == False
    assert is_valid("CS05") == False
    assert is_valid("50") == False
    assert is_valid("CS50A") == False
    assert is_valid("PI3.14") == False 

