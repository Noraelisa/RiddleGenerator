import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

RIDDLES_FILENAME = os.getenv("RIDDLES_FILENAME") or "riddles.csv"
RIDDLES_FILE_PATH = os.path.join(dirname, '..', 'data', RIDDLES_FILENAME)
