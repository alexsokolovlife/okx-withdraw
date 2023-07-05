import requests
import time
import hashlib
import hmac

# OKEx API information
api_key = 'YOUR_API_KEY'
secret_key = 'YOUR_SECRET_KEY'
passphrase = 'YOUR_API_PASSPHRASE'

# Withdrawal details
withdrawal_currency = 'ETH'
withdrawal_amount = 1.0
wallet_address = 'YOUR_WALLET_ADDRESS'

# Generate timestamp
timestamp = str(int(time.time() * 1000))

# Create payload for withdrawal request
payload = {
    'currency': withdrawal_currency,
    'amount': withdrawal_amount,
    'destination': '3',  # 3 for external address withdrawal
    'to_address': wallet_address,
}

# Create request URL
base_url = 'https://www.okex.com'
request_path = '/api/v5/account/withdrawal'
url = f'{base_url}{request_path}'

# Generate signature
message = timestamp + 'POST' + request_path + str(payload)
signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()

# Create headers
headers = {
    'OK-ACCESS-KEY': api_key,
    'OK-ACCESS-SIGN': signature,
    'OK-ACCESS-TIMESTAMP': timestamp,
    'OK-ACCESS-PASSPHRASE': passphrase,
    'Content-Type': 'application/json'
}

# Send withdrawal request
response = requests.post(url, json=payload, headers=headers)

# Check response status
if response.status_code == 200:
    print('Withdrawal request successful.')
    print('Withdrawal details:')
    print(response.json())
else:
    print('Withdrawal request failed.')
    print('Error message:', response.json())
