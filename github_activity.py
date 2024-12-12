import sys, urllib.request, urllib.error, json

def get_activities(username):
	url = f"https://api.github.com/users/{username}/events"

	try:
		with urllib.request.urlopen(url) as response:
			data = json.loads(response.read().decode('utf-8'))
	except urllib.error.HTTPError as e:
		print(e)
		if e.getcode() == 404:
			print("No such username exist!")
		sys.exit(1)
	except urllib.error.URLError as e:
		print(e.reason)
		print("Are you connected to the internet?")
		sys.exit(2)

	result = f"Activites of {username}:\n"
	if data:
		for event in data:
			result += f"[{event["created_at"]}] {event["repo"]["name"]}: "
			match event["type"]:
				case "CreateEvent":
					result += f"Created {event["payload"]["ref_type"]} {event["payload"]["ref"] or ""}\n"
				case "ForkEvent":
					result += f"Forked on {event["payload"]["forkee"]["full_name"]}\n"
				case "PushEvent":
					result += f"Pushed {event["payload"]["size"]} commit{"s" if event["payload"]["size"] > 1 else ""} on "
					if event["payload"]["ref"].split("/")[1] == "tags":
						result += f"tag {event["payload"]["ref"].split("/")[-1]}\n"
					else:
						result += f"{event["payload"]["ref"].split("/")[-1]} branch\n"
				case "WatchEvent":
					result += "Starred repository\n"
				case _:
					result += f"{event["type"]}\n"
	
	return result.strip()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("USAGE: github-activity [USERNAME]")
		sys.exit(1)

	print(get_activities(sys.argv[1]))