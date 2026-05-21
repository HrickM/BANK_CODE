# Multiple Inheritance

class Bank_v1:
    bank_name = "SBI"
    bank_branch = "Hyderabad"
    bank_ifsc = 1234

    def __init__(self, n, a, ac, b):
        self.name = n
        self.age = a
        self.account = ac
        self.balance = b

    def customer_details(self):
        print(f"name of customer {self.name}")
        print(f"age of customer {self.age}")
        print(f"customer account {self.account}")
        print(f"customer balance {self.balance}")

    @classmethod
    def bank_details(cls):
        print(f"bank name is {cls.bank_name}")
        print(f"bank branch is {cls.bank_branch}")


class Bank_v2:
    bank_manager = "Eswar"
    bank_number = 1234567

    def __init__(self, n, a, ac, b, pin):
        super().__init__(n, a, ac, b)
        self.pin = pin

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f"bank manager is {cls.bank_manager}")
        print(f"bank number is {cls.bank_number}")


class Bank_v3(Bank_v2, Bank_v1):
    bank_branch = "Vizag"
    bank_ifsc = 12345

    def __init__(self, n, a, ac, b, pin):
        super().__init__(n, a, ac, b, pin)

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f"bank ifsc is {cls.bank_ifsc}")

    def customer_details(self):
        super().customer_details()
        print(f"customer password is {self.pin}")


# Object Creation
Ram = Bank_v3("Ramul", 23, 2345, 1234, 23456)

# Method Calling
Ram.customer_details()
Ram.bank_details()
```
```python
# Multiple Inheritance

class Bank_v1:
    bank_name = "SBI"
    bank_branch = "Hyderabad"
    bank_ifsc = 1234

    def __init__(self, n, a, ac, b):
        self.name = n
        self.age = a
        self.account = ac
        self.balance = b

    def customer_details(self):
        print(f"name of customer {self.name}")
        print(f"age of customer {self.age}")
        print(f"customer account {self.account}")
        print(f"customer balance {self.balance}")

    @classmethod
    def bank_details(cls):
        print(f"bank name is {cls.bank_name}")
        print(f"bank branch is {cls.bank_branch}")


class Bank_v2:
    bank_manager = "Eswar"
    bank_number = 1234567

    def __init__(self, n, a, ac, b, pin):
        super().__init__(n, a, ac, b)
        self.pin = pin

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f"bank manager is {cls.bank_manager}")
        print(f"bank number is {cls.bank_number}")


class Bank_v3(Bank_v2, Bank_v1):
    bank_branch = "Vizag"
    bank_ifsc = 12345

    def __init__(self, n, a, ac, b, pin):
        super().__init__(n, a, ac, b, pin)

    @classmethod
    def bank_details(cls):
        super().bank_details()
        print(f"bank ifsc is {cls.bank_ifsc}")

    def customer_details(self):
        super().customer_details()
        print(f"customer password is {self.pin}")


# Object Creation
Ram = Bank_v3("Ramul", 23, 2345, 1234, 23456)

# Method Calling
Ram.customer_details()
Ram.bank_details()
