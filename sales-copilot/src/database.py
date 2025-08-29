from deeplake import DeepLake

class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.dataset = DeepLake.load(db_path)

    def store_embedding(self, text_chunk, embedding):
        self.dataset.add({"text": text_chunk, "embedding": embedding})

    def retrieve_embedding(self, query_embedding):
        results = self.dataset.query({"embedding": query_embedding})
        return results

    def close(self):
        self.dataset.close()