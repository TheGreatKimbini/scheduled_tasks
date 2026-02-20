import smtplib
import random
import datetime as dt
import pandas

#emails
my_email = "fake_email@gmail.com"
fake_password = "password123"

#date strips time
current_date = dt.date.today()

#reads csv & turns into dataframe
birthdays = pandas.read_csv("birthdays.csv")


b_days = {(row["month"], row["day"]): row for index, row in birthdays.iterrows()}
if (current_date.month, current_date.day) in b_days:
    match = b_days[(current_date.month, current_date.day)]
    letter = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open (letter) as file:
        contents = file.read()
    contents = contents.replace("[NAME]", match["name"])

    print(contents)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = my_email, password = fake_password)
        connection.sendmail(
            from_addr = my_email,
            to_addrs = match["email"],
            msg = f"Subject: this is fake\n\n{contents}"
        )

