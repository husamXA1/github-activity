import sys, urllib.request, json

if len(sys.argv) != 2:
	print("USAGE: github-activity [USERNAME]")
	sys.exit(1)

url = f"https://api.github.com/users/{sys.argv[1]}/events"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

if data:
	for event in data:
		print(f"- {event["type"]} on repository {event["repo"]["name"]} at {event["created_at"]}")