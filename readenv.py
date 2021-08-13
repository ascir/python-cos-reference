import os
from dotenv import dotenv_values, load_dotenv
# from pathlib import Path

load_dotenv()


config = dotenv_values(".env") 

print(config['COS_API_KEY_ID'])
print(os.getenv("COS_API_KEY_ID"))


