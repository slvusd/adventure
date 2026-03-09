def run():
	print("=== sky ===")
	print("you are not allowed to fly in the sky, did you? y/n")

	while True:
		choice = input("you are not allowed to fly in the sky, did you? y/n ")
		if  choice != "y":
			print("you go to juvie")
			return  "juvie"
		else:
			return "dungeon"y
