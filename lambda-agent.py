import json

payment_transactions = [
    {"transactionId": 1, "amount": 2.00, "product": "coffee", "quantity": 1, "date": "10-03-2024"},
    {"transactionId": 2, "amount": 1.50, "product": "tea", "quantity": 3, "date": "11-03-2024"},
    {"transactionId": 3, "amount": 3.00, "product": "biscuits", "quantity": 1, "date": "11-03-2024"},
    {"transactionId": 4, "amount": 6.00, "product": "chips", "quantity": 2, "date": "03-04-2024"},
    {"transactionId": 5, "amount": 15.00, "product": "cake", "quantity": 1, "date": "12-04-2024"},
    {"transactionId": 6, "amount": 6.00, "product": "cookies", "quantity": 3, "date": "19-04-2024"},
    {"transactionId": 7, "amount": 17.00, "product": "pizza", "quantity": 1, "date": "30-04-2024"},
    {"transactionId": 8, "amount": 12.00, "product": "sandwich", "quantity": 1, "date": "01-05-2024"},
    {"transactionId": 9, "amount": 22.00, "product": "burger", "quantity": 1, "date": "03-05-2024"},
    {"transactionId": 10, "amount": 10.00, "product": "fries", "quantity": 2, "date": "04-05-2024"},
    {"transactionId": 11, "amount": 9.50, "product": "noodles", "quantity": 1, "date": "10-05-2024"},
    {"transactionId": 12, "amount": 16.80, "product": "pasta", "quantity": 4, "date": "14-05-2024"}
]

def get_parameter_value(event, name):
    return next(item for item in event["parameters"] if item["name"] == name)['value']

def get_transaction(event, id):
    for transaction in payment_transactions:
        if transaction["transactionId"] == id:
            return transaction
    return None

def lambda_handler(event, context):
    print(event)

    agent = event['agent']
    api_path = event['apiPath']
    response_code = 404 
    response_body = { 'TEXT': "API path not found"}

    if api_path == '/getTransaction/':
        transaction_id = int(get_parameter_value(event, 'transactionId'))
        transaction = get_transaction(event, transaction_id)
        if transaction is None:
            response_code = 404
            response_body = {'TEXT': "Transaction not found"}
        else:
            response_code = 200
            response_body = {
                'application/json': {
                    'body': {
                        'transaction': transaction
                    }
                }
            }

    action_response = {
        'actionGroup': event['actionGroup'],
        'apiPath': api_path,
        'httpMethod': event['httpMethod'],
        'httpStatusCode': response_code,
        'responseBody': response_body
    }

    session_attributes = event['sessionAttributes']
    prompt_session_attributes = event['promptSessionAttributes']

    api_response = {
        'messageVersion': '1.0',
        'response': action_response,
        'sessionAttributes': session_attributes,
        'promptSessionAttributes': prompt_session_attributes
    }

    print(api_response)
    return api_response
