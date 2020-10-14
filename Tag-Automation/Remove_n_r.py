import requests

content = requests.get("https://test-abhay.s3.amazonaws.com/App_tag.json").json()
print(content)