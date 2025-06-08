from src.utils import get_phones

phones = get_phones()
# phones = ["5627116282", "5561319352", "5627116282", "5561319352"]


class Index:
    def __init__(self):
        self.value = 0
        self.phone = phones[0]

    def __update_phone(self):
        self.phone = phones[self.value]

    def change_value(self, to):
        new_v = self.value + to
        if new_v < 0:
            raise self.value
        if new_v > len(phones) - 1:
            raise self.value
        self.value = new_v
        self.__update_phone()
        return self.value


current_index = Index()
isEditing = False
