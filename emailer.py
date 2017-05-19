import smtplib
import csv


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
me = "reportprowlers@gmail.com"

with open('saidsacontacts.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print row['EMAIL']
		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Report Prowlers Service"
		msg['From'] = me
		msg['To'] = row['EMAIL']

		html = """\
		<!DOCTYPE html>
		<html>

		  <head>
		    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		    <meta name="viewport" content="width=device-width">
		    <title>Report Prowlers</title>
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



		    <img src="http://www.reportprowlers.co.za/static/images/reportprowlersbanner.png">


			  <p>Dear Sirs, <br></p>
			  <p>Please may I have a moment of your time to explain our service.<br></p>
			  <p>Report Prowlers is an internet based service designed to advance security in neighborhoods through simplified online communication between the neighborhood's residents, and the local security services.<br><br></p>
			  <h3 class="text-center" style="color: #28475C;"><strong>How it works:</strong></h3>
			  <p><br><strong>USERS = Area's Residents and Security Personal on patrol</strong><br><br>
			  Users login, and send reports of suspicious activity in their area. Its free, and easy to use. From the USERS perspective, the process is as follows:<br><br>
			  </p>
			  <p class="text-center" style="color: #28475C;">Login > Send Report > Safer Neighborhood</p>
			  <br><br>
			  </p>
			  <p><strong>SUBSCRIBERS = Area's Security Services: </strong><br><br>
			  Receive these reports, with additional intelligence on comparisons with other recent reports, recommended response level. Subscribers pay a monthly subscription fee for each area they wish to monitor:<br><br></p>
			  <p class="text-center" style="color: #28475C;">Monitor Emails > Receive Reports > Allocate Appropriate Response</p>
			  <br><br>
			  <p><strong>BUILT TO BE:</strong><br><br>
			  <ul>
			    <li>Fast and reliable, using Google's Emailing Servers</li>
			    <li>Easy to use, and mobile phone friendly</li>
			    <li>Stable using well established technologies</li>
			    <li>Free for Users to send reports</li>
			    <li>Cost effective subscription fees at R150/Month per subscribed area</li>
			    <li>Helpful in your marketing stratergy to grow your client base, or promote your services</li>
			    <li>Promoted on social media platforms such as facebook and twitter ** Campaigns already under way</li>
			    <li>Easy to setup: No installation, no additional hardware, no proprietary software</li>
			    <li>A proactive approach to being at the right place at the right time</li>
			    <li>Helpful in deciding where to allocate resources</li>
			    <li>Structured and easy to understand reports</li>
			    <li>Helpful in building intelligence</li>
			    <li>Available everywhere in South Africa</li>
			  </ul>
			  <br><br></p>
			  <p class="text-center" style="color: #28475C;">Click on the image below to visit the website</p>

			  <a href="http://www.reportprowlers.co.za"> <img src="http://www.reportprowlers.co.za/static/images/fbreportprowlers.png"></a>
			  
			  <h3>Click <a href="www.reportprowlers.co.za/register"> here </a>to subscribe or to recieve additional information</h3>

			  <p>Please do not hesitate to <a href="mailto:reportprowlers@gmail.com">contact us</a> should you have any queries</p>

			  <p>Sincerely Yours,<br><br></p>

		    <h5>Hannah Swan</h5>
		    <p>Sales Manager<br>
		    Report Prowlers<br>
		    Phone: 039 319 1088<br>
		    Mobile: 078 738 4038<br>
		    Email: <a href="mailto:reportprowlers@gmail.com">reportprowlers@gmail.com</a></p>


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



		gmail_user = 'reportprowlers@gmail.com'
		gmail_password = '123password123'

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
