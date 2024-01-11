import requests
from requests.auth import HTTPBasicAUTH

def authenticate_client(client_id,client_secret, token_url, scope=""):
  auth = HTTPBacisAuth(client_id, client_secret)
  data = {
    'grant_type': 'client_credentials', 'scope': scope
  }
  response = requests.post(token_url, auth=auth, data = data)
  if response.status_code == 200:
    access_token = response.json().get('access_token')
    return access_token
  else:
    raise Excception(f"Authentication error: {response.status_code} - {response.text}")
def get_posts(api_url, access_token, user_id=None):
  base_url = f"{api_url}/posts"

  if user_id is not None:
    url = f"{base_url}?userId={user_id}"
  else:
    url = base_url

  headers = {'Authorization' : f'Bearer {access_token}'}

  try:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
      posts = response.json()
      for post in posts:
        print(f"Post {post['id']}: {post['title']}")
    else:
      print(f"Error: {response.status_code} - {response.text}")
  except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
if __name__ == "__main__":
  client_id = 'your_client_id'
  client_secret = 'your_client_secret'
  token_url = 'partner_token_url'
  api_url = 'partner_api_url'

  access_token = authenticate_client(client_id, client_secret, token_url, scop= "partner_scope")
  get_posts(api_url, access_token)
  
      
