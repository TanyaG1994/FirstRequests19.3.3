import requests

#Запрос Get на получение данных всех доступных питомцев

status='available'

res_get = requests.get( f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers = {'accept': 'application/json'})

print(res_get.status_code)
print(res_get.json())
all_pets = res_get.json()


#Запрос Post на добавление питомца

data = {
  "id": 1122334455,
  "name": "Vally",
  "photoUrls": ["string"],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

res_post = requests.post(f"https://petstore.swagger.io/v2/pet", headers= {'accept': 'application/json'}, json =data)

print(res_post.status_code)
print(res_post.json())


#Запрос Put на зменения данных питомца

data_change = {
  "id": 1122334455,
  "name": "Maggy",
  "photoUrls": ["str"],
  "tags": [
    {
      "id": 1,
      "name": "str"
    }
  ],
  "status": "available"
}

res_put = requests.put(f"https://petstore.swagger.io/v2/pet", headers= {'accept': 'application/json'}, json =data_change)

print(res_put.status_code)
print(res_put.json())


#Запрос Delete на удаление питомца по Id

petId = all_pets[0]['id']

res_del = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId}")

print(res_del.status_code)
print(res_del.json())