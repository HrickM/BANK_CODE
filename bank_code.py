import streamlit as st

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
        st.write(f"Name of customer: {self.name}")
        st.write(f"Age of customer: {self.age}")
        st.write(f"Customer account: {self.account}")
        st.write(f"Customer balance: {self.balance}")

    @classmethod
    def bank_details(cls):
        st.write(f"Bank name is: {cls.bank_name}")
        st.write(f"Bank branch is: {cls.bank_branch}")


class Bank_v2:
    bank_manager = "Eswar"
    bank_number = 1234567

    def __init__(self, n, a, ac, b, pin):
        super().__init__(n, a, ac, b)
        self.pin = pin

    @classmethod
    def bank_details(cls):
        super().bank_details()
        st.write(f"Bank manager is: {cls.bank_manager}")
        st.write(f"Bank number is: {cls.bank_number}")


class Bank_v3(Bank_v2, Bank_v1):
    bank_branch = "Vizag"
    bank_ifsc = 12345

    def __init__(self, n, a, ac, b, pin):
        super().__init__(n, a, ac, b, pin)

    @classmethod
    def bank_details(cls):
        super().bank_details()
        st.write(f"Bank IFSC is: {cls.bank_ifsc}")

    def customer_details(self):
        super().customer_details()
        st.write(f"Customer PIN is: {self.pin}")


# Streamlit UI
st.title("Bank Management System")

name = st.text_input("Enter Customer Name")
age = st.number_input("Enter Age", min_value=1, step=1)
account = st.number_input("Enter Account Number", min_value=1, step=1)
balance = st.number_input("Enter Balance", min_value=0, step=1)
pin = st.number_input("Enter PIN", min_value=1000, step=1)

if st.button("Show Details"):
    Ram = Bank_v3(name, age, account, balance, pin)

    st.subheader("Customer Details")
    Ram.customer_details()

    st.subheader("Bank Details")
    Ram.bank_details()
