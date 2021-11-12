import os
from src.app import create_app  

try:
    print("INITIALIZING APP")
    app = create_app(os.getenv('ENV') or 'DEV') 
except Exception as exc:
    print(f"ERROR INITIALIZING APP: {exc}")
    raise exc
