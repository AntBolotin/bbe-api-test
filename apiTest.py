import pytest
import requests
import jsonschema
from jsonschema import validate

@pytest.mark.regression
def test_user_operations(base_url, user_id):

    #Update User
    update_data = {
        "id": user_id,
        "username": "test_api",
        "firstName": "test",
        "lastName": "api",
        "email": "test_api@email.com",
        "password": "QWE!@#",
        "phone": "+111222333444",
        "userStatus": 0
    }
    update_user = requests.put(f'{base_url}/user/{user_id}', json=update_data)
    print("Update user response" + update_user.text)
    assert update_user.status_code == 200
    print(update_user.headers)
    assert update_user.headers['Content-Type'] == 'application/json'


    #Get User Info
    get_user = requests.get(f'{base_url}/user/test_api')
    print("Get user response" + get_user.text)
    assert get_user.status_code == 200
    print(get_user.headers)
    assert get_user.headers['Content-Type'] == 'application/json'
    user_info = get_user.json()
    assert user_info['username'] == update_data['username']
    assert user_info['email'] == update_data['email']
    assert user_info['phone'] == update_data['phone']

    schema = {
    "type": "object",
    "properties":{
        "id":{"type":"integer"},
        "username":{"type":"string"},
        "firstName":{"type":"string"},
        "lastName":{"type":"string"},
        "email":{"type":"string", "format":"email"},
        "password":{"type":"string"},
        "phone":{"type":"string"},
        "userStatus":{"type":"integer"}
    },
    "required":["id","username","firstName", "lastName", "email", "password", "phone", "userStatus"]
}

    try:
        validate(instance=user_info, schema=schema)
        print("JSON Schema validation success.")
    except jsonschema.exceptions.ValidationError as e:
        print("Error validation JSON Schema: ")
        print(e)
        raise e

@pytest.mark.skip
def test_2():
    print("Second Test")

a = 321

@pytest.mark.skipif(a != 234, reason="is not equal 234, skip test")
def test_a():
    assert a == 234

@pytest.mark.xfail(reason="Expected fail test")
def test_a2():
    assert a == 234

# @pytest.mark.parametrize("test_data", [123, 234, 345])
# def test_a3(test_data):
#     assert test_data == 234



