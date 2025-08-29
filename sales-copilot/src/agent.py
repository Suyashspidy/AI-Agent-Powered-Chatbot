from langchain import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA
from langchain.vectorstores import DeepLake
from langchain.embeddings import GoogleGeminiEmbeddings
from config import get_api_key

class SalesAgent:
    def __init__(self):
        self.memory = ConversationBufferMemory()
        self.embeddings = GoogleGeminiEmbeddings(api_key=get_api_key())
        self.vector_store = DeepLake(embedding_function=self.embeddings)

        self.prompt_template = PromptTemplate(
            input_variables=["context", "customer_query"],
            template="You are a sales assistant. Given the context: {context}, respond to the customer query: {customer_query}"
        )

        self.chain = LLMChain(
            llm=self.embeddings,
            prompt=self.prompt_template,
            memory=self.memory
        )

    def analyze_query(self, customer_query):
        # Logic to analyze the query for potential objections can be added here
        return customer_query

    def retrieve_context(self, customer_query):
        # Retrieve relevant context from the Deep Lake knowledge base
        return self.vector_store.similarity_search(customer_query)

    def generate_response(self, customer_query):
        analyzed_query = self.analyze_query(customer_query)
        context = self.retrieve_context(analyzed_query)
        response = self.chain.run(context=context, customer_query=analyzed_query)
        return response

# Example usage
# agent = SalesAgent()
# response = agent.generate_response("What are the benefits of your product?")
# print(response)