import requests
from datetime import datetime, timezone
import smtplib
import time


MY_LAT = 37.9838
MY_LONG = 23.7275

MY_EMAIL = ""
MY_PASSWORD = ""




def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", timeout=10)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="http://api.sunrise-sunset.org/json", timeout=10, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(timezone.utc).hour
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False
    
email_sent = False

while True:
    time.sleep(60)
    iss_overhead = is_iss_overhead()
    night = is_night()
    if iss_overhead and night and not email_sent:
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, 
                                    to_addrs=MY_EMAIL,
                                    msg="Subject:Look Up!\n\nThe ISS is above you in the sky")
            
        email_sent = True

    if not iss_overhead:
         email_sent = False
