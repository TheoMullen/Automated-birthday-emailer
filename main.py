
import smtplib
import random
import datetime as dt
import pandas

my_email = "myemail@gmail.com"
password = "my_password"


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

date = dt.datetime.now()
current_month = date.month
current_day = date.day

data = pandas.read_csv("birthdays.csv")
birthday_dict = data.to_dict(orient="records")

people_list = [person for person in birthday_dict if person['month'] == current_month and person["day"] == current_day]


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if len(people_list) != 0:
    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

    for person in people_list:
        with open(random.choice(letter_list)) as template_data:
            template = template_data.read()
            letter = template.replace("[NAME]", person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=person["email"], msg=f"Subject:Happy Birthday\n\n{letter}")


