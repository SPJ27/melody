import os
import dotenv

dotenv.load_dotenv()

def env(name):
    return os.getenv(name)