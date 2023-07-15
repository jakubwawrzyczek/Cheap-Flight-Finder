import requests

SHEETY_ENDPOINT = 'https://api.sheety.co/ab269c66e0f540cca900afbfe11fd000/kopiaFlightDeals/users'

HEADERS = {
  'Authorization': 'Bearer siematotoken'
}

class DataManager:
  
  def get_data(self):
    response = requests.get(url=SHEETY_ENDPOINT, headers=HEADERS)
    return response.json()

  def post_new_user_data(self, user_data):
    params = {
        'user': {
          'firstName': user_data['firstName'],
          'lastName': user_data['lastName'],
          'email': user_data['email'],
      }
    }
    
    if self.check_if_not_enrolled(user_data['email']):
      response = requests.post(url=SHEETY_ENDPOINT, headers=HEADERS, json=params)
      print('You are enrolled! Now you can wait for the e-mail!')
    else:
      print('Given email is already enrolled!')
      
  def check_if_not_enrolled(self, email):
    data = self.get_data()['users']
    for row in data:
      if row['email'] == email:
        return False
        break
      return True