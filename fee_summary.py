name = input("Name:").strip().title()

program = input("Programe:").strip().title()

total_fees = int(input("Total fees:"))
amount_paid = int(input("Amount paid:"))
balance = total_fees - amount_paid
print(f"Name:{name}")
print(f"Program:{program}")
print(f"Balance:{balance}")

