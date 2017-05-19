import requests
from bs4 import BeautifulSoup
import csv



page_counter = 0
item_counter = 0
mailing_list = []
usrl_list = ["http://www.yellowpages.co.za/Search/security/", 
			"http://www.yellowpages.co.za/Search/neighbourhood+watch/",
			"http://www.yellowpages.co.za/Search/sa+police/",  
			"http://www.yellowpages.co.za/Search/municipalities/",
			"http://www.yellowpages.co.za/Search/community/"]

for page in range(1, 100):

	for url in usrl_list:
		try:
			url = url  + str(page)

			r = requests.get(url)

			soup = BeautifulSoup(r.content, "html.parser")

			ul = soup.find_all('ul', {"class": "resultContact"})

			for li in ul:
				data = li.find_all('a', {"class": "Book resultWebLink"})
				tel = li.find_all('a', {"class": "resultMainNumber contracted"})[0].text
				row = []
				for item in data:
					#if item['data-businesskeywoords'].find('GUARDS') or keywords.find('GUARD') or keywords.find('ARMED'):
					#if item['data-businesskeywoords'].find(''):
					if item['data-name'] != '':
						print('#################################')
						print(item_counter)
						print(item['data-name'])
						print(item['data-address'])
						print(item['data-email'])
						print(tel)
						item_counter += 1
						row.append(item['data-name'])
						row.append(item['data-email'])
						row.append(tel)
						if item['data-email'] != '':
							try:
								#yourlist.append(yourdict.copy())
								contact = {'name':item['data-name'], 'email':item['data-email']}
								mailing_list.append(contact.copy())
								print('WORKING')
							except:
									pass
						#row.append(item['data-address'])
						with open("output.csv", "a") as fp:
							wr = csv.writer(fp, dialect='excel')
							wr.writerow(row)	
				else:
					pass
		except:
			pass

		page_counter += 1



for item in mailing_list:
	print("*********************")
	print(item['name'])
	print(item['email']) 
	print("*********************")


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "reportprowlers@gmail.com"

name = "Subscriber"

for recipient in mailing_list:
	# Create message container - the correct MIME type is multipart/alternative.
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "Report Prowlers Service"
	msg['From'] = me
	msg['To'] = recipient['email']

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
		    <li>Helpful in your marketing stratergy with regards to promoting your product or services</li>
		    <li>Promoted on social media platforms such as facebook and twitter ** Campaigns already under way</li>
		    <li>Easy to setup: No installation, no additional hardware, no proprietary software</li>
		    <li>A proactive approach in preventing incedents in your areas</li>
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

	content = MIMEText(html, 'html')

	msg.attach(content)



	gmail_user = 'reportprowlers@gmail.com'
	gmail_password = '123password123'

	try:
		server = smtplib.SMTP(host ='smtp.gmail.com', port='587')
		print('host =smtp.gmail.com, port=587')
		server.ehlo()
		print('ehlo')
		server.starttls()
		print('starttls')
		server.login(gmail_user, gmail_password)
		print('Logged in')
		server.sendmail(me, recipient['email'], msg.as_string())
		#server.sendmail(me, "vaughndevilliers@gmail.com", msg.as_string())
		print('sent')
		server.quit()
		print('successfully sent the mail to ' + recipient['email'])
		row = []
		row.append(recipient['name'])
		row.append(recipient['email'])
		row.append('Successful')

		with open("report.csv", "a") as fp:
			wr = csv.writer(fp, dialect='excel')
			wr.writerow(row)
	except:
		print("failed to send mail to " + recipient['email'] )
		row = []
		row.append(recipient['name'])
		row.append(recipient['email'])
		row.append('Failed')

		with open("report.csv", "a") as fp:
			wr = csv.writer(fp, dialect='excel')
			wr.writerow(row)	

print('Total pages = ' + str(page_counter))
print('Total items = ' + str(item_counter))
print(len(mailing_list))