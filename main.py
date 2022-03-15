import configparser
import os

import timetable as tt


def init_ttasbackground():
    os.mkdir(".ttasbackground/")  # TODO: point to ~/.ttasbackground


def get_config(path):
    if not os.path.exists(path):
    	make_config(path)

    config = configparser.ConfigParser(interpolation=None)

    config.read(path)
    return config


def make_config(path):
	if not os.path.exists(os.path.split(path)[1]):
		init_ttasbackground()

	hash = input("Enter hash: ")
	auth_key = input("Enter auth key: ")
	id = input("Enter id: ")

	with open(path, "w") as f:
		f.write(f"""[Creds]
hash={hash}
auth_key={auth_key}
id={id}""")


def main():
	config = get_config("config.ini")  # TODO: correct path

    # TODO: fetch pdf
	tt.fetch_pdf(
		config["Creds"]["id"],
		tt.get_date(),
		tt.get_sturm_session(hash),
		"tt.pdf"
	)
	# TODO: convert to png
	# TODO: set as background


main()
