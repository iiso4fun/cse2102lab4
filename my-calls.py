import httpx

url = "https://super-winner-r45g4v66rj53wxvj-5000.app.github.dev/" 


auth_data = {
    "id": "phillip.bradford@uconn.edu",
    "token": "f99aa8b8573062e9802f4fc0807ae1cb"
}


response = httpx.post(url + "login", data=auth_data)
print("Login status:", response.status_code)
print("Login response:", response.json())

if response.status_code == 200:
    
    mydata = {
        "text": "Hello Phil!",
        "param2": "Making a POST request",
        "body": "my own value"
    }

    response = httpx.post(url + "echo", data=mydata)
    print("Authorized request status:", response.status_code)
    print("Authorized request response:", response.text)

else:
    print("Login failed.")