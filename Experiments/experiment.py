import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY:
    print("api key is successfully retrived")
    print(f"api key is : {GOOGLE_API_KEY}")
else:
    print("api key is not found")
