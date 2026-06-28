from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

from emv_simulator import EMVSimulator
from example_transaction import EMVTransaction

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# Single global simulator instance for the demo/dev server
simulator = EMVSimulator()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/status')
def status():
    return jsonify({
        'status': 'ok',
        'transaction_flow': simulator.get_transaction_flow()
    })


@app.route('/api/transaction/initiate', methods=['POST'])
def initiate_transaction():
    data = request.get_json() or {}
    amount = data.get('amount')
    if amount is None:
        return jsonify({'error': 'amount is required'}), 400

    simulator.initiate_transaction(amount)
    return jsonify({'transaction_flow': simulator.get_transaction_flow()})


@app.route('/api/transaction/process', methods=['POST'])
def process_transaction():
    simulator.process_transaction()
    return jsonify({'transaction_flow': simulator.get_transaction_flow()})


@app.route('/api/transaction/complete', methods=['POST'])
def complete_transaction():
    simulator.complete_transaction()
    return jsonify({'transaction_flow': simulator.get_transaction_flow()})


@app.route('/api/transaction/flow')
def transaction_flow():
    return jsonify({'transaction_flow': simulator.get_transaction_flow()})


@app.route('/api/example', methods=['POST'])
def run_example():
    """Run the example transaction flow (uses example_transaction.EMVTransaction).
    Optional JSON body: { "amount": <number>, "merchant_id": "..." }
    """
    data = request.get_json() or {}
    amount = data.get('amount', 100.0)
    merchant_id = data.get('merchant_id', 'MERCHANT_001')

    tx = EMVTransaction(card_data={'number': '4111111111111111', 'expiry': '12/25', 'cvv': '123'},
                        merchant_id=merchant_id)
    tx.set_transaction_amount(amount)
    approved = tx.authorize()

    if approved:
        simulator.transaction_flow.append(f"Example transaction approved for {amount}")
        result = {'approved': True}
    else:
        simulator.transaction_flow.append(f"Example transaction declined for {amount}")
        result = {'approved': False}

    return jsonify({'result': result, 'transaction_flow': simulator.get_transaction_flow()})


if __name__ == '__main__':
    # Development server only
    app.run(host='127.0.0.1', port=5000, debug=True)
