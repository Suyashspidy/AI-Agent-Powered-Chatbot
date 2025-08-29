def get_sales_assistant_prompt(customer_query):
    return f"You are a sales assistant. A customer has asked: '{customer_query}'. Please provide a helpful and relevant response based on the context provided."

def get_objection_handling_prompt(customer_query, objections):
    return f"As a sales assistant, you need to address the following objections: {objections}. The customer has asked: '{customer_query}'. Provide a response that effectively handles these objections."