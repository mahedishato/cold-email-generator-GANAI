import chromadb

client = chromadb.Client()
collection = client.create_collection(name="my_collection")

collection.add(
    documents=[
        "This is a document about Bangladesh",
        "This is a document about india"
    ],
    ids=["id1", "id2"]
)

results = collection.query(
    query_texts=["Dhaka is the capitale"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)
