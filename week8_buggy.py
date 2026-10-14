# week8_buggy.py -- three bugs -- do not fix yet

records = [
    {"id": 1, "name": "Alice", "amount": 1200},
    {"id": 2, "name": "Jordan", "amount": 450},
    {"id": 3, "name": "Morgan", "amount": 3500},
]


def get_total(records):
    total = 0
    for rec in records:
        total += rec["amount"]
    return total


def is_over_limit(amount):
    return amount > int("1000")


def format_summary(total, count):
    return f"Total amount: ${total:.2f} across {count} records"


total_amount = get_total(records)
print(format_summary(total_amount, len(records)))
print(is_over_limit(total_amount))
