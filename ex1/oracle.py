import os
from dotenv import load_dotenv

load_dotenv()
print("ORACLE STATUS: Consulting the configuration...")

print("\nConfiguration loaded:")
MATRIX_MODE = os.getenv("MATRIX_MODE", "production")
DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL")
ZION_ENDPOINT = os.getenv("ZION_ENDPOINT")

print(f"Mode: {MATRIX_MODE}")

if MATRIX_MODE == "development":
    print("Development mode: Debugging enabled")
elif MATRIX_MODE == "production":
    print("Production mode: Debugging disabled")
else:
    print("[WARNING] Unknown configuration mode")

if DATABASE_URL:
    print("Database: Connected to local instance")
else:
    print("Database: [WARNING] No database URL found")

if API_KEY:
    print("API Access: Authenticated")
else:
    print("API Access: [WARNING] No API key found")

if LOG_LEVEL:
    print(f"Log Level: {LOG_LEVEL}")
else:
    print("Log Level: [WARNING] No log level found")

if ZION_ENDPOINT:
    print("Remote Network: Online")
else:
    print("Remote Network: [WARNING] No remote endpoint found")
