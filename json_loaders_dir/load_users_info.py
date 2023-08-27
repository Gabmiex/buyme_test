import json


class UserInfo:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()
        self.users = self.data["users"]

    def _load_data(self):
        with open(self.file_path, 'r') as json_file:
            return json.load(json_file)

    def get_user(self, index):
        if index < len(self.users):
            return self.users[index]
        raise ValueError("User index out of range.")

    def user_name(self, index):
        return self.get_user(index)['name']

    def user_email(self, index):
        return self.get_user(index)['email']

    def password(self, index):
        return self.get_user(index)['password']


users = UserInfo('C:/Users/Gabrielle/PycharmProjects/bymesite_test/json_dir/users_info.json')

