# from testcicd import count_even_odd,add,sub,multi

# def test_count_even_odd():
#     assert count_even_odd(100) == (50,50)

# def test_add():
#     assert add(2,3) == 5
# def test_sub():
#     assert sub(4,3) == 1

# def test_multi():

#     assert multi(2,3) == 6
import json
from testcicd import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)

    assert response['statusCode'] == 200
    assert json.loads(response['body']) == 'Hello from Lambda!'
