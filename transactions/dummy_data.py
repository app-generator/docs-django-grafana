import random
from decimal import Decimal
from .models import Transaction  # Adjust the import based on your app name


def create_dummy_transactions(num_records=20000):
    transaction_types = ["credit", "debit"]

    for _ in range(num_records):
        user_id = random.randint(1, 100)
        amount = Decimal(random.uniform(1.00, 1000.00)).quantize(Decimal("0.01"))
        transaction_type = random.choice(transaction_types)

        Transaction.objects.create(
            user_id=user_id, amount=amount, transaction_type=transaction_type
        )

    print(f"{num_records} dummy transactions added to the database.")


create_dummy_transactions()
