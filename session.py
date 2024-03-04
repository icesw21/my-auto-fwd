import requests

url = "https://raw.githubusercontent.com/TeamUltroid/Ultroid/main/resources/session/ssgen.py"

# Fetch the raw content of the file
response = requests.get(url)
code = response.text

# Execute the Python code
exec(code)