from requests.auth import HTTPBasicAuth

url = "https://httpbin.org/basic-auth/user/pass")
basic = HTTPBasicAuth("user", "pass")
resp = requests.get(url, auth=basic)