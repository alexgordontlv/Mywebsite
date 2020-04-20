from flask import Flask, render_template, url_for, request, redirect
import csv
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
import chekmypassword
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        send_my_email(data)
        return redirect('/thankyou.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!'


@app.route('/submit_form2', methods=['POST', 'GET'])
def submit_form2():
    if request.method == 'POST':
  #    try:
 #       data = request.form.to_dict()
 #       password = chekmypassword.check(data["password"])
        return redirect("https://github.com/alexgordontlv/passwordcheck")

   #   except:
 #       return 'did not save to database'
  #  else:
  #    return 'something went wrong. Try again!'

def send_my_email(data):
    emaildata = data["email"]
    subject = data["subject"]
    message = data["message"]
    email = EmailMessage()
    email['from'] = emaildata
    email['to'] = "alexaybn@gmail.com"
    email['subject'] = subject
    email.set_content(message)

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('alexgordon.tlv@gmail.com', 'lopinking89')
        smtp.send_message(email)


