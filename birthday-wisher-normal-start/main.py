import smtplib
import datetime as dt
import smtplib
import pandas
import random

now = dt.datetime.now()
today_tuple = (now.month, now.day)

MY_EMAIL = "mogaka1mogaka2@gmail.com"
PASSWORD = "uqgswzqubzzyisoa"


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_boy_girl = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_chosen:
        contents = letter_chosen.read()
        contents = contents.replace("[NAME]", birthday_boy_girl["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=RECEIVER,
                            msg=f"Subject: Happy Birthday!\n\n {contents}"
                            )




