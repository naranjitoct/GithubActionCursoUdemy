from src.math_operations import add,sub

def test_add ():
    assert add (2,3)==5
    assert add (4,3)==7

def test_sub():
    assert sub(5,3)==2
    assert sub(8,3)==5
    assert sub(5,1)==4
    assert sub(5,8)==-3