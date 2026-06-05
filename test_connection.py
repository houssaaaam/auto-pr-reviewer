import os
from dotenv import load_dotenv
from githubkit import GitHub

# Load keys from .env
load_dotenv()

# Initialize GitHub client
github = GitHub(os.getenv("GITHUB_TOKEN"))

# Try to get your own user info
try:
    user = github.rest.users.get_authenticated().parsed_data
    print(f"Successfully connected! Hello, {user.login}")
except Exception as e:
    print(f"Connection failed: {e}")