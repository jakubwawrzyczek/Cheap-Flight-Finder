from user_data import UserData
from data_manager import DataManager
user_data = UserData()
data_manager = DataManager()

print('Welcome to Cheap-Flight-Finder project, if you want to be informed about the best offers please fill the form below \/')

new_user_data = user_data.get_data_from_user()
data_manager.post_new_user_data(new_user_data)