phones = ["5627116282", "5561319352", "5627116282", "5561319352"]


class Index:
    def __init__(self):
        self.value = 0

    def change_value(self, to):
        new_v = self.value + to
        if new_v < 0:
            raise self.value
        if new_v > len(phones) - 1:
            raise self.value
        self.value = new_v
        return self.value


current_index = Index()
isEditing = False
