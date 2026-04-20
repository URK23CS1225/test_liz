from flask import add, greet
def test_add():
    assert add(4,5)== 9
def test_greet():
    assert greet("world")=="Hello, world"