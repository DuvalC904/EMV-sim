import unittest

class TestEMVSimulator(unittest.TestCase):
    
    def test_emv_simulator_initialization(self):
        simulator = EMVSimulator()
        self.assertIsNotNone(simulator)
        self.assertEqual(simulator.state, 'initialized')  # Assuming state attribute

    def test_transaction_processing(self):
        simulator = EMVSimulator()
        transaction = EMVTransaction(amount=100, currency='USD')
        result = simulator.process_transaction(transaction)
        self.assertTrue(result['success'])  # Assuming process transaction returns a dict with success key

    def test_emv_transaction_initialization(self):
        transaction = EMVTransaction(amount=100, currency='USD')
        self.assertEqual(transaction.amount, 100)
        self.assertEqual(transaction.currency, 'USD')

    def test_apdu_commands(self):
        command = '00A4040000'  # Sample APDU command
        response = simulator.send_apdu(command)
        self.assertIsNotNone(response)  # Validate response not None
        self.assertIn('status', response)  # Assuming response has a status field

    def test_tlv_parser(self):
        tlv_data = '9F0206000000000100'  # Sample TLV data
        parsed_data = simulator.parse_tlv(tlv_data)
        self.assertIsInstance(parsed_data, dict)  # Validate parsed data is a dictionary
        self.assertIn('9F02', parsed_data)  # Validate specific tag is parsed

if __name__ == '__main__':
    unittest.main()