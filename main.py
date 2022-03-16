import configparser
import os
from sys import platform, exit
from time import sleep

import timetable as tt
import config_editor as ce


app_path = ""
if "win" in platform:
	app_path = os.getenv("appdata").replace("\\", "/") + "/ttasbackground"
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
	hash, auth_key, id = ce.get_config()

	with open(path, "w") as f:
		f.write(f"""[Creds]
hash={hash}
auth_key={auth_key}
id={id}""")


def main():
    init_ttasbackground()
    config = get_config(app_path + "/config.ini")

    while True:
        try:
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
    
    		# set as background
            tt.set_as_background(app_path + "/tt.png")
    
            sleep(1200)

        except:
            pass


if __name__ == "__main__":
	main()
