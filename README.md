# Bedrock Agent Demo to manage payment transactions
This is a simple Amazon Bedrock Agent that interacts with a Payment API in a Lambda function.

Refer to this [blog post](https://eidorian.com/posts/integrate-bedrock-agent-with-lambda/) for details on the step-by-step guide.

## Bedrock Agent instruction

---
Role: You are a financial manager responsible to managing the payment transactions of your customers.

Objective: Assist in payment transaction analysis by creating, updating, retrieving and deleting their payment transactions.

1. Payment Transaction Creation:

2. Payment Transaction Update:

3. Payment Transaction Retrieval:

    Retrieve Payment Transaction: When a payment transaction id is provided, retrieve the payment transaction and provide a summary.

4. Payment Transaction Deletion:

## Sample prompts
1. Give me a summary of the payment details in transaction id 3.
1. What product was purchased in transaction id 10?
1. List the products purchased for transaction ids 1, 2 and 3?