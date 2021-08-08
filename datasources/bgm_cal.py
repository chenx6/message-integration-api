from requests import get

def bgm_cal():
    resp = get("https://api.bgm.tv/calendar")