import requests
import json

file_url = 'https://cats.com/wp-content/uploads/2023/09/fluffy-cat-lies-on-the-windowsill- and-looks-into-the-camera.jpg'

response = requests.get(file_url)
with open('cat2.jpg', 'wb') as file:
    file.write(response.content)
print(response.status_code)
print(response.text)






# pet_id = 20593238
# base_url = "https://petstore.swagger.io/v2"
# endpoint = f'/pet/{pet_id}/uploadImage'
#
# with open('cat.jpg', 'rb') as image_file:
#     response = requests.post(base_url + endpoint, files={'file': image_file})
#
# print(response.status_code)
# print(response.text)



# form_data = {
#     "username": "test_api",
#     "password": "QWE!@#"
# }
#
# response = requests.get("https://petstore.swagger.io/v2/user/login", data=form_data)
# print(response.status_code)
# print(response.text)





# session = requests.Session()
#
# response = session.get('https://httpbin.org/cookies/set?session_id=123456')
# print(response.status_code)
# print(response.text)
#
# response = session.get('https://httpbin.org/cookies')
# print(response.status_code)
# print(response.text)


# base_url = 'https://httpbin.org/'
#
# endpoint = '/cookies'
# cookies = {
#     'location': 'Barcelona'
# }
#
# response = requests.get(base_url + endpoint, cookies=cookies)
# print(response.status_code)
# print(response.text)




# base_url = "https://petstore.swagger.io/v2"
#
# endpoint = "/pet"
#
# headers = {
#     'api_key': 'special-key'
# }
#
# response = requests.delete(base_url+endpoint + '/13')
#
# print(response.status_code)
# print(response.text)




# url = "https://petstore.swagger.io/v2/pet/findByStatus?status=sold"
#
# payload = {}
# files={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload, files=files)
#
# print(response.text)
