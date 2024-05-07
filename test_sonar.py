from testcicd import count_even_odd,add,sub

def test_count_even_odd():

    assert count_even_odd(100) == (50,50)

def test_add():
    assert add(2,3) == 5
def test_sub():
    assert sub(4,3) == 1