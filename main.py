import json
import time
print("Hello World")
print("Hello GITHUBd")
curr = "Hello"
with open("sample.json", "w") as outfile:
    json.dump(curr, outfile)

while True:
    time.sleep(1)