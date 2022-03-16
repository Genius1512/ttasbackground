import requests as req
import convertapi as capi
import time as t
from sys import platform


def to_image(path, auth_key):
    """
	path without ending, ex.: "timetable."
	"""

    capi.api_secret = auth_key
    capi.convert("png", {"File": path + "pdf"}).file.save(path + "png")


def set_as_background(path):
    if platform == "linux":
        pass
    else:
        __import__("ctypes").windll.user32.SystemParametersInfoW(
            20, 0, path, 2)


def fetch_pdf(id, time, cookie, path):
    # URL to replicate: https://intranet.tam.ch/ksl/print/pdf-timetable?filter=student&id=4020344&start=2022-2-28&table=week&daysviewed=week&reservations=0
    url = f"https://intranet.tam.ch/ksl/print/pdf-timetable?filter=student&id={id}&start={time}&table=week&daysviewed=week&reservations=0"
    out = req.get(url, cookies=cookie)
    with open(path, "wb") as f:
        f.write(out.content)


def get_sturm_session(hash: str):
    # URL to replicate: https://intranet.tam.ch/ksl/rest/ics/type/timetable/date/1642582786/auth/gr001@c2lsdmFuLnNjaG1pZHQ=:OGY4NmQxYjExYTM5MDRjNWMwMWMwODZjNmE2OGUxOGQ3NmMwZWY5Mw==/calendar.ics
    url = f"https://intranet.tam.ch/ksl/rest/ics/type/1642582786/date/1642682786/auth/{hash}/calendar.ics"
    resp = req.get(url)
    return resp.cookies


def get_date():
    time = t.strftime("%Y-%m-")
    today = t.strftime("%a")

    if today == "Mon":
        time += t.strftime("%d")
    elif today == "Tue":
        time += str(int(t.strftime("%d")) - 1)
    elif today == "Wed":
        time += str(int(t.strftime("%d")) - 2)
    elif today == "Thu":
        time += str(int(t.strftime("%d") - 3))
    elif today == "Fri":
        time += str(int(t.strftime("%d")) - 4)
    elif today == "Sat":
        time += str(int(t.strftime("%d")) + 2)
    elif today == "Sun":
        time += str(int(t.strftime("%d")) + 1)
    return time
