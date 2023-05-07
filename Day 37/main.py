import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
username = "ongmo"
graph_id = "s1lj8l12ufjdk9"
token = "23urnsdljfs93lskd"
user_params = {
    "token": token,
    "username": "ongmo",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# # Create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_params = {
    "id": graph_id,
    "name": "test-graph",
    "unit": "calory",
    "type": "int",
    "color": "ajisai",
    "timezone": "America/New_York",
}
headers = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph_endpoint, headers=headers, json=graph_params)
# print(response.text)

add_pixel_endpoint = f"{graph_endpoint}/{graph_id}"

pixel_params = {
    "date": dt.datetime.now().strftime("%Y%m%d"),
    "quantity": "20",
}

# response = requests.post(url=add_pixel_endpoint, headers=headers, json=pixel_params)
# print(response.text)

date = "20230506"
update_pixel_endpoint = f"{add_pixel_endpoint}/{date}"
update_pixel_params = {
    "quantity": "50",
}

# response = requests.put(url=update_pixel_endpoint, headers=headers, json=update_pixel_params)
# print(response.text)

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)
