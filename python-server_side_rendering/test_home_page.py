import requests

response = requests.get("http://127.0.0.1:5000")
assert response.status_code == 200, "Home page did not load successfully"
assert "Welcome to My Flask App" in response.text, "Home page test failed"
print("Home page test passed!")
