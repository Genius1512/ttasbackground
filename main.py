import configparser
import os
from sys import platform, exit

import timetable as tt


app_path = ""
if "win" in platform:
	app_path = "" # TODO: insert app_path for windows
elif "linux" in platform:
	app_path = "/home/" + os.getenv("USER") + "/.ttasbackground"
else:
	print("Your OS is not supported")
	exit(1)


def init_ttasbackground():
	try:
		os.mkdir(app_path)
	except FileExistsError:
		pass


def get_config(path):
	if not os.path.exists(path):
		make_config(path)

	config = configparser.ConfigParser(interpolation=None)

	config.read(path)
	return config


def make_config(path):
	hash = input("Enter hash: ")
	auth_key = input("Enter auth key: ")
	id = input("Enter id: ")

	with open(path, "w") as f:
		f.write(f"""[Creds]
hash={hash}
auth_key={auth_key}
id={id}""")


def main():
	config = get_config(app_path + "/config.ini")

    # fetch pdf
	tt.fetch_pdf(
		config["Creds"]["id"],
		tt.get_date(),
		tt.get_sturm_session(config["Creds"]["hash"]),
		app_path + "/tt.pdf"
	)
	# convert to png
	tt.to_image(
		app_path + "/tt.",
		config["Creds"]["auth_key"]
	)

	# TODO: set as background


init_ttasbackground()
main()
