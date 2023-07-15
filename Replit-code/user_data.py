class UserData:
  
  def get_data_from_user(self):
    self.first_name = input('What\'s your first name? ')
    self.last_name = input('What\'s your second name? ')
    self.email = input('What\'s your email? ')
    self.email_repeated = input('Please repeat your email: ')

    is_empty = self.first_name == '' or self.last_name == '' or self.email == ''
    are_emails_the_same = self.email == self.email_repeated
  
    if not are_emails_the_same:
      print('\nThe emails provided do not match, please try again.')
      user_data = self.get_data_from_user()

    elif is_empty:
      print('\nSome fields are empty! Try again.')
      user_data = self.get_data_from_user()
      
    else:
      user_data = {
        'firstName': self.first_name.capitalize(),
        'lastName': self.last_name.capitalize(),
        'email': self.email
      }
    return user_data
