from testcicd import count_even_odd,add

def test_count_even_odd():

    assert count_even_odd(100) == (50,50)

def test_add():
    assert add(2,3) == 5