import sys, urllib.request, json

if len(sys.argv) != 2:
	print("USAGE: github-activity [USERNAME]")
	sys.exit(1)

url = f"https://api.github.com/users/{sys.argv[1]}/events"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode('utf-8'))

if data:
	for event in data:
		print(f"[{event["created_at"]}] {event["repo"]["name"]}", end=": ")
		match event["type"]:
			case "CreateEvent":
				print(f"Created {event["payload"]["ref_type"]} {event["payload"]["ref"] or ""}")
			case "ForkEvent":
				print(f"Forked on {event["payload"]["forkee"]["full_name"]}")
			case _:
				print(f"{event["type"]}")