# Example EMV Transaction Flow

# This script demonstrates a complete EMV transaction flow with test data.

class EMVTransaction:
    def __init__(self, card_data, merchant_id):
        self.card_data = card_data  # Simulated card data
        self.merchant_id = merchant_id  # Simulated merchant ID
        self.transaction_amount = 0

    def set_transaction_amount(self, amount):
        self.transaction_amount = amount
        print(f"Transaction amount set to: {self.transaction_amount}")

    def authorize(self):
        # Simulate authorization process
        print(f"Authorizing transaction for merchant {self.merchant_id}...")
        # Use random logic to decide if authorization is successful
        from random import choice
        return choice([True, False])

    def process_transaction(self):
        # The complete transaction process
        if self.authorize():
            print("Transaction approved!")
            # Further processing like capturing the transaction could go here
        else:
            print("Transaction declined.")

# Test data
if __name__ == '__main__':
    test_card_data = {"number": "4111111111111111", "expiry": "12/25", "cvv": "123"}
    merchant_id = "MERCHANT_001"
    transaction = EMVTransaction(test_card_data, merchant_id)
    transaction.set_transaction_amount(100.0)  # Setting transaction amount
    transaction.process_transaction()  # Processing transaction