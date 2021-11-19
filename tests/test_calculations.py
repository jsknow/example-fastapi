from app.calculations import add, subtract, multipy, divide


def test_add():
    print("testing add fuction")
    assert add(5, 3) == 9

def test_subtract():
    assert subtract(9, 4) == 5