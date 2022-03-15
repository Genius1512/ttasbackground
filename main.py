import configparser
import os


def init_ttasbackground():
	os.mkdir(".ttasbackground/")


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

	with open(path, "w") as f:
		f.write(f"""[Creds]
hash={hash}
auth_key={auth_key}""")


def main():
	config = get_config("config.ini")
	print(config)


main()