
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