import pytest
import requests

@pytest.fixture(scope="module")
def base_url():
    base_url = 'https://petstore.swagger.io/v2'
    return base_url

@pytest.fixture(scope="module")
def user_id():
    user_id = 123
    return user_id


#Setup
@pytest.fixture(scope="module", autouse=True)
def setup(base_url, user_id):

    # Create User
    data = {
        "id": user_id,
        "username": "test_api",
        "firstName": "test",
        "lastName": "api",
        "email": "test_api@email.com",
        "password": "QWE!@#",
        "phone": "+123321",
        "userStatus": 0
    }

    create_user = requests.post(f'{base_url}/user', json=data)
    print("Create user response" + create_user.text)
    assert create_user.status_code == 200
    print(create_user.headers)
    assert create_user.headers['Content-Type'] == 'application/json'

    yield

    #Delete user
    delete_user = requests.delete(f'{base_url}/user/test_api')
    print("Delete user response" + delete_user.text)
    assert delete_user.status_code == 200
    print(delete_user.headers)
    assert delete_user.headers['Content-Type'] == 'application/json'

