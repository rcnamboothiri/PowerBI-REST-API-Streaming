
import time
import json
import random
import datetime
import requests
import schedule


def randomtemperature():
 random.seed()
 return str(round(random.uniform(50, 100),2))

def currenttime():
	now = datetime.datetime.now() - datetime.timedelta(hours = 5) - datetime.timedelta(minutes = 30)
	formatted_time = "{0}T{1}Z".format(now.date(),now.time())

	return formatted_time


def schedule_job():
	random_temp= randomtemperature()
	current_time = currenttime()
	payload = [{'Timestamp' : current_time,'Temp' : random_temp , 'TempL' : 98.6 , 'TempH' : 98.6}]
	print(json.dumps(payload))
	r = requests.post("https://api.powerbi.com/beta/6b5bd02b-92d2-40b2-9ffd-c9c94280c757/datasets/0eacd941-d2c4-41f7-bca3-7ccaa030fa94/rows?key=GTvQMQt8MHoNX6yycNHgtywR3%2FmjSzBgOGraYgNVJJvF6HhZgHLjrgVKrVllay3z4WMo5BLsiyv531VTsLnASA%3D%3D", data= json.dumps(payload))
	print(r.status_code)
	print(r.content)
	print(random_temp)


schedule.every(5).seconds.do(schedule_job)
while True:
    schedule.run_pending()
    time.sleep(1)