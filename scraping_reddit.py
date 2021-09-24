

import os

# I have saved my reddit username and password as environment variables
# Retrieving the username and password from environment variables:
from dotenv import load_dotenv
load_dotenv()
reddit_username = os.environ["reddit_username"]
reddit_password = os.environ["reddit_password"]
print(reddit_username, reddit_password)
