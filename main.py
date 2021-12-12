import requests
import json
import jsonpath


# Test case register successful
def test_register_success():
    url = "https://reqres.in/api/register"
    file = open("data/user.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    status = response.status_code
    print("Status code: ", status)
    assert status == 200
    print(response.content)

#Test case: register fail (email not defined)
def test_register_fail_email():
    url = "https://reqres.in/api/register"
    file = open("data/userWrongEmail.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    error = jsonpath.jsonpath(response_json, 'error')
    status = response.status_code
    print("Status code: ", status)
    assert status == 400
    
    print("Error: ", error[0])
    assert error[0] == "Note: Only defined users succeed registration"

#Test case: register fail (password empty)
def test_register_empty_email():
    url = "https://reqres.in/api/register"
    file = open("data/userEmptyPass.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    error = jsonpath.jsonpath(response_json, 'error')
    status = response.status_code
    print("Status code: ", status)
    assert status == 400

    print("Error: ", error[0])
    assert error[0] == "Missing password"


#Test case: login successful
def test_login_success():
    url = "https://reqres.in/api/login"
    file = open("data/user.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    status = response.status_code
    print("Status code: ", status)
    assert status == 200
    print(response.content)

#Test case: login fail (email empty)
def test_login_empty_email():
    url = "https://reqres.in/api/login"
    file = open("data/userEmptyEmail.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    error = jsonpath.jsonpath(response_json, 'error')
    status = response.status_code
    print("Status code: ", status)
    assert status == 400

    print("Error: ", error[0])
    assert error[0] == "Missing email or username"

#Test case: login fail (password empty)
def test_login_empty_password():
    url = "https://reqres.in/api/login"
    file = open("data/userEmptyPass.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    error = jsonpath.jsonpath(response_json, 'error')
    status = response.status_code
    print("Status code: ", status)
    assert status == 400

    print("Error: ", error[0])
    assert error[0] == "Missing password"

#Test case: login fail (user not found)
def test_login_wrong_email():
    url = "https://reqres.in/api/login"
    file = open("data/userWrongEmail.json")
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    response_json = json.loads(response.text)
    error = jsonpath.jsonpath(response_json, 'error')
    status = response.status_code
    print("Status code: ", status)
    assert status == 400

    print("Error: ", error[0])
    assert error[0] == "user not found"

#Test case: Get single user success
def test_get_user_success():
    url = "https://reqres.in/api/users/2"
    response = requests.get(url)
    status = response.status_code
    print("Status code: ", status)
    assert status == 200

    response_json = json.loads(response.text)
    data = jsonpath.jsonpath(response_json, 'data')
    print(data[0])
    id = data[0]["id"]
    assert id == 2
   

#Test case: Get single user fail
def test_get_user_fail():
    url = "https://reqres.in/api/users/23"
    response = requests.get(url)
    status = response.status_code
    print("Status code: ", status)
    assert status == 404

    data = response.text
    assert data == '{}'
