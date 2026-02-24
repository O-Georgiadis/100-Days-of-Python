import smtplib
from datetime import datetime
from pathlib import Path
import random
import pandas as pd


MY_EMAIL = ""
MY_PASSWORD = ""

today = datetime.now()
today_tuple = (today.month, today.day)

df = pd.read_csv("birthdays.csv")

birthdays_dict = {(df_row.month,df_row.day): df_row for (index, df_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = Path(__file__).parent/f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person.name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=birthday_person.email,
                            msg=f"Subject:Happy Birthday!\n\n{contents}")
      

