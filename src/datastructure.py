class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

        self.add_member({
            "first_name": "Tommy",
            "age": 10,
            "lucky_numbers": [5, 6]
        })

        self.add_member({
            "first_name": "John",
            "age": 33,
            "lucky_numbers": [7, 13, 22]
        })

        self.add_member({
            "first_name": "Jane",
            "age": 35,
            "lucky_numbers": [10, 14, 3]
        })

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        new_member = {
            "id": self._generate_id(),
            "first_name": member.get("first_name"),
            "last_name": self.last_name,
            "age": member.get("age"),
            "lucky_numbers": member.get("lucky_numbers", [])
        }

        self._members.append(new_member)
        return new_member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return True
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members