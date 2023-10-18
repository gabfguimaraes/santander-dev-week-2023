import pandas as pd
import requests
import json


sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'
df = pd.read_csv('SDW2023.csv')
user_ids = df['UserID'].tolist()


def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

def update_user(user):
  response = requests.put(f"{sdw2023_api_url}/users/{user['id']}", json=user)
  return True if response.status_code == 200 else False


users = [user for id in user_ids if (user := get_user(id)) is not None]

for user in users:
  news = f"O usuário {user['name']} chegou com tudo!"
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })
  success = update_user(user)
  print(f"O usuário {user['name']} foi atualizado? {success}!")