
import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import tempfile


# Load environment variables from a .env file if present
load_dotenv()

client = OpenAI()

VECTOR_STORE_NAME = "MEMORIESTORE"

mcp = FastMCP('Memories')

# Create or get the vector store for memories (this will be used to store and retrieve memories) 
# [Reference OPENAI boilerplate code for  vector stores](https://platform.openai.com/docs/guides/vector-stores/quickstart)
def get_or_create_vector_store():
    # Try to find existing vector store, else create
    stores = client.vector_stores.list()
    for store in stores:
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_stores.create(name=VECTOR_STORE_NAME)
