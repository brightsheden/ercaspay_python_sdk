# Ercaspay SDK for Python

Ercaspay SDK provides an easy way to interact with the Ercaspay payment gateway. This SDK simplifies the process of making payments, verifying transactions, and handling various payment methods.

## Installation

To install the Ercaspay SDK, you can use pip:

```bash
pip install ercaspy
```

## Usage

To use the Ercaspay SDK, you need to import the `Ercaspy` class and initialize it with your API key. Below is an example of how to initiate a payment:

```python
import sys
sys.path.append("..")
from ercaspy.client import Ercaspy
from ercaspy.exceptions import APIError

client = Ercaspy(api_key="YOUR_API_KEY")

payment_data = {
    "amount": "1500",
    "paymentReference": "unique_reference",
    "customerName": "John Doe",
    "customerEmail": "john.doe@example.com",
    "currency": "NGN",
    "redirectUrl": "https://your_redirect_url.com",
    "paymentMethods": "card"
}

def initiate_payment():
    try:
        response = client.initiate_checkout(payment_data=payment_data)
        print(response)
    except APIError as e:
        print(f"An error occurred while initiating payment: {e}")

initiate_payment()
```

## API Reference

### Ercaspy Class

#### `__init__(api_key: str)`

Initializes the Ercaspy client with the provided API key.

#### `initiate_checkout(payment_data: CheckOutRequest, **args) -> TransactionResponse`

Initiates a checkout process with the provided payment data.

#### `verify_transaction(payment_ref: str) -> TransactionResponse`

Verifies a transaction using the provided payment reference.

#### `initiate_bank_transfer_request(transaction_ref: str) -> TransactionResponse`

Requests bank account details for a bank transfer using the transaction reference.

#### `initiate_bank_transfer(data: TransferRequest) -> TransactionResponse`

Initiates a bank transfer using the provided data.

#### `check_direct_payment_status(transaction_ref: str, payment_method: str) -> TransactionResponse`

Checks the status of a direct payment using the transaction reference and payment method.

#### `initiate_ussd_transaction(data: TransferRequest, bank_name: str) -> TransactionResponse`

Initiates a USSD transaction with the specified bank name.

#### `initiate_card_transaction(payload: CardRequest) -> TransactionResponse`

Initiates a card transaction with the provided payload.

#### `submit_otp(otp: str, transaction_ref: str, gateaway_ref: str) -> TransactionResponse`

Submits an OTP for a transaction.

#### `resend_otp(transaction_ref: str, gateaway_ref: str) -> TransactionResponse`

Resends an OTP for a transaction.

#### `get_card_details(transaction_reference: str) -> TransactionResponse`

Retrieves card details using the transaction reference.

#### `verify_card_transaction(reference: str)`

Verifies a card transaction using the provided reference.

#### `cancle_transaction(transaction_ref: str) -> TransactionResponse`

Cancels a transaction using the transaction reference.

## Error Handling

The SDK raises `APIError` exceptions for various error scenarios, including:

- Invalid API key
- Network issues
- Invalid response from the server

You can catch these exceptions in your code to handle errors gracefully.

```python
try:
    # Your API call
except APIError as e:
    print(f"An error occurred: {e}")
```

## Examples

Here are some examples of how to use the SDK for different payment methods:

### Initiating a Card Transaction

```python
data = {
    "card_number": "5123450000000008",
    "cvv": "100",
    "pin": "1234",
    "expiry_date": "0139",
    "transaction_reference": "unique_transaction_reference"
}

def initiate_card_transaction(data):
    try:
        response = client.initiate_card_transaction(data)
        print(response)
    except APIError as e:
        print(f"An error occurred while initiating card transaction: {e}")

initiate_card_transaction(data)
```

### Verifying a Transaction

```python
def verify_transaction(transaction_ref):
    try:
        response = client.verify_transaction(transaction_ref)
        print(response)
    except APIError as e:
        print(f"An error occurred while verifying transaction: {e}")

verify_transaction("unique_transaction_reference")
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
