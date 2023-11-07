import openllm
client = openllm.client.HTTPClient('http://localhost:3000', timeout=30)  # Specify a longer timeout (e.g., 30 seconds)
response = client.query("what is 2+2 ?")

print(response)