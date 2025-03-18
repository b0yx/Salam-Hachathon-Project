from django.test import TestCase

# Create your tests here.
import requests

url1 = "http://127.0.0.1:8000/api/Test1/"
url2 = "http://127.0.0.1:8000/api/Test2/"

data1 = {"name": "John", "age": 25}
data2 = {"product": "Laptop", "price": 1200}

response1 = requests.post(url1, json=data1)
response2 = requests.post(url2, json=data2)

print("Response from endpoint1:", response1.json())
print("Response from endpoint2:", response2.json())
