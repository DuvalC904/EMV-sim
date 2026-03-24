# EMV Simulator

class EMVSimulator:
    def __init__(self):
        self.transaction_flow = []

    def initiate_transaction(self, amount):
        print(f"Initiating transaction for amount: {amount}")
        self.transaction_flow.append(f"Transaction initiated for amount: {amount}")

    def process_transaction(self):
        if not self.transaction_flow:
            print("No transaction to process.")
            return
        
        print("Processing transaction...")
        self.transaction_flow.append("Transaction processed.")

    def complete_transaction(self):
        if not self.transaction_flow:
            print("No transaction to complete.")
            return
        
        print("Completing transaction...")
        self.transaction_flow.append("Transaction completed.")

    def get_transaction_flow(self):
        return self.transaction_flow

# Example usage:
if __name__ == '__main__':
    simulator = EMVSimulator()
    simulator.initiate_transaction(100.00)
    simulator.process_transaction()
    simulator.complete_transaction()
    print(simulator.get_transaction_flow())