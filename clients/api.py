import requests 

endpoint = 'http://localhost:8000/api/'


data = {
    'name': 'update_admin',
    'description': 'Create an admin user'
}

response = requests.get(endpoint, json=data)

print(response.json())

print(response.status_code)