class Handbook:
    def __init__(self):
        self._records = set()

    def add(self, record):
        self._records.add(record)

    def remove(self, name):
        for record in self._records:
            if record.name == name:
                self._records.remove(record)
                return True
        return False

    def search(self, name):
        for record in self._records:
            if record.name.strip().lower() == name.strip().lower():
                return record
        return None


class Record:
    def __init__(self, name, phone_number):
        self.name = name.strip()
        self.phone_number = phone_number


class Interface:
    def __init__(self, handbook):
        self.handbook = handbook

    def run(self):
        while True:
            selection = input("choose the option: \n1 = add\n2 = remove\n3 = display record\n")

            if selection == "1":
                name = input("Enter the name: ")
                phone_number = input("Enter the phone number: ")
                rec = Record(name, phone_number)
                self.handbook.add(rec)
                print("Record added\n")

            elif selection == "2":
                name = input("Enter the name: ")
                if self.handbook.remove(name):
                    print("Record removed")
                else:
                    print("Record not found")

            elif selection == "3":
                name = input("Enter the name to search for: ")
                record = self.handbook.search(name.strip())
                if record is not None:
                    print(f"Record found: Name: {record.name}, Phone Number: {record.phone_number}")
                else:
                    print("Record not found.")

            else:
                print("Invalid selection")


def main():
    handbook = Handbook()
    interface = Interface(handbook)
    interface.run()


if __name__ == '__main__':
    main()
