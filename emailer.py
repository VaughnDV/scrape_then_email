import smtplib
import csv


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "your.email@provider.com"

with open('saidsacontacts.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['EMAIL']
		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "YOUR COMPANY SERVICE"
		msg['From'] = me
		msg['To'] = row['EMAIL']

		html = """\
		<!DOCTYPE html>
		<html>

		  <head>
		    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		    <meta name="viewport" content="width=device-width">
		    <title>YOUR COMPANY</title>
		    <style>
		    body {
				  width: 100% !important;
				  min-width: 100%;
				  -webkit-text-size-adjust: 100%;
				  -ms-text-size-adjust: 100%;
				  margin: 0;
				  Margin: 0;
				  padding: 0;
				  -moz-box-sizing: border-box;
				  -webkit-box-sizing: border-box;
				  box-sizing: border-box; }
			</style>
			</head>
		  	<body>



		    <img src="LINK TO SOME IMAGE">


			  <p>Dear Sirs, <br></p>
			  <p>Please may I have a moment of your time to explain our service.<br></p>
			  
			  <p>Please do not hesitate to <a href="mailto:your.email@provider.com">contact us</a> should you have any queries</p>

			  <p>Sincerely Yours,<br><br></p>

		    <h5>SALES CONSULTANT</h5>
		    <p>Sales Manager<br>
		    company name<br>
		    Phone: 555 319 1088<br>
		    Mobile: 555 738 4038<br>
		    Email: <a href="mailto:your.email@provider.com">your.email@provider.com</a></p>


		  </body>

		</html>

		""" 

		# Record the MIME types of both parts - text/plain and text/html.

		content = MIMEText(html, 'html')

		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		#msg.attach(part1)
		msg.attach(content)



		gmail_user = 'your.email@provider.com'
		gmail_password = 'yourpassword'

		try:
			#server = smtplib.SMTP('smtp.gmail.com:587')
			server = smtplib.SMTP(host ='smtp.gmail.com', port='587')
			#server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', '465')
			print 'host =smtp.gmail.com, port=587'
			server.ehlo()
			print 'ehlo'
			server.starttls()
			print 'starttls'
			server.login(gmail_user, gmail_password)
			print 'Logged in'
			server.sendmail(me, row['EMAIL'], msg.as_string())
			print 'sent'
			server.quit()
			print 'successfully sent the mail'
			line = []
			line.append(row['COMPANY'])
			line.append(row['EMAIL'])
			line.append('Successful')
			with open("emailerreport.csv", "a") as fp:
				wr = csv.writer(fp, dialect='excel')
				wr.writerow(line)

		except:
			print "failed to send mail"
			line = []
			line.append(row['EMAIL'])
			line.append('Failed')

			with open("emailerreport.csv", "a") as fp:
				wr = csv.writer(fp, dialect='excel')
				wr.writerow(line)	
