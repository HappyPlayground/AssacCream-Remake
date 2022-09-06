import os
import sys

if os.path.exists("config.json"):
    import json

    try:
        with open("config.json", "r+", encoding="utf-8") as f:
            config = json.load(f)
    except Exception as E:
        print(f"Error: {E}")

else:
    print("Error: No config file found")
    sys.exit(-1)

config = config
