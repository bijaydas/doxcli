from faker import Faker
from doxcli.exceptions.general import MethodNotFoundException


class Fakes:
    faker = None

    def __init__(self):
        self.faker = Faker()

    def call_user_func(self, name: str):
        """
        Checking if the runtime argument available in Faker
        """
        if not hasattr(self.faker, name):
            raise MethodNotFoundException(f'{name} not found')

        func = getattr(self.faker, name)()

        print(func)

        return 0
