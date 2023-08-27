import json


class ReceiverInfo:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self._load_data()
        self.receiver = self.data["receivers"]

    def _load_data(self):
        with open(self.file_path, 'r') as json_file:
            return json.load(json_file)

    def get_receiver(self, index):
        if index < len(self.receiver):
            return self.receiver[index]
        raise ValueError("Receiver index out of range.")

    def receiver_name(self, index):
        return self.get_receiver(index)['name']

    def receiver_phone(self, index):
        return self.get_receiver(index)['phone_number']

    def receiver_greeting(self, index):
        return self.get_receiver(index)['greeting']


receivers = ReceiverInfo('C:/Users/Gabrielle/PycharmProjects/bymesite_test/json_dir/receiver_info.json')
