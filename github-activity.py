import sys, urllib.request, json

if len(sys.argv) != 2:
	print("USAGE: github-activity [USERNAME]")
	sys.exit(1)

url = f"https://api.github.com/users/{sys.argv[1]}/events"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

if data:
	print(data)
