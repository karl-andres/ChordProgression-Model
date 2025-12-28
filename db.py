import pandas as pd
import chromadb

df = pd.read_csv("data/final_dataset.csv")

chroma_client = chromadb.PersistentClient()

collection = chroma_client.create_collection(name="songs")