import schedule
import time
import requests
import json
import smtplib, ssl
from twilio.rest import Client


CRYSTAL_CITY_CODE = "C09"
FRANCONIA_CODE = "J03"


def connection_object(stationcode, origin):
    url = "https://api.wmata.com/StationPrediction.svc/json/GetPrediction/{}".format(
        stationcode
    )

    headers = {"api_key": "00000000000000"}

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        hello = r.json()
        # connection_object.hello2 = r.content
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    try:
        for station in hello["Trains"]:
            connection_object.train_list = (
                "These trains are on the way to " + origin + "!    "
                "Destination Name: " + station["DestinationName"],
                "  " "Arrival Min: " + station["Min"],
                "   " "Line Color: " + station["Line"],
                "  " "--------",
            )
            return connection_object.train_list
    except requests.exceptions.InvalidURL as err2:
        raise SystemExit(err2)


def send_text():

    account_sid = "000000000000000000000000000"
    auth_token = "000000000000000000000000000"
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid="MGb7941e6389915d027f73898201fadb62",
        body="{}".format(connection_object(FRANCONIA_CODE, "Work")),
        to="+17038324707",
    )

    print(message.sid)


# send_text()


# # send text via email

# # Establish a secure session with gmail's outgoing SMTP server using your gmail account
# server = smtplib.SMTP("smtp.gmail.com", 587)

# server.starttls()

# server.login("@gmail", "password")

# body = "Im alive!"
# message = (
#     "From: %s\n" % "stefano.amanuel@gmail.com"
#     + "To: %s\r\n" % "111111111@tmomail.net"
#     + "Subject: %s\r\n" % "Metro Arrival Times"
#     + "\r\n"
#     + body
# )

# # Send text message through SMS gateway of destination number
# server.sendmail("FROM", "@tmomail.net", message)


for i in ["08:00", "08:15", "08:30", "08:45", "09:00"]:
    schedule.every().monday.at(i).do(send_text)
    schedule.every().tuesday.at(i).do(send_text)
    schedule.every().wednesday.at(i).do(send_text)
    schedule.every().thursday.at(i).do(send_text)
    schedule.every().friday.at(i).do(send_text)
while True:
    schedule.run_pending()
    time.sleep(15)
