import requests
from bs4 import BeautifulSoup
import csv



page_counter = 0
item_counter = 0
mailing_list = []
usrl_list = ["http://www.yellowpages.co.za/Search/SEARCH OPTION/", 
			"http://www.yellowpages.co.za/Search/SEARCH OPTION2/",
			"http://www.yellowpages.co.za/Search/SEARCH OPTION3/",  
			"http://www.yellowpages.co.za/Search/SEARCH OPTION4/",
			"http://www.yellowpages.co.za/Search/SEARCH OPTION5/"]

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
	msg['Subject'] = "YOUR COMAPNY SERVICE"
	msg['From'] = me
	msg['To'] = recipient['email']

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



	    <img src="LINK TO YOU BANNER IMAGE">


		  <p>Dear Sirs, <br></p>
		  <p>Please may I have a moment of your time to explain our service.<br></p>
		
		  <p>Please do not hesitate to <a href="mailto:your.emai@provider.com">contact us</a> should you have any queries</p>

		  <p>Sincerely Yours,<br><br></p>

	    <h5>SALES CONSULTANT NAME</h5>
	    <p>Sales Manager<br>
	    YOUR COMAPNY<br>
	    Phone: 555 319 1088<br>
	    Mobile:555 738 4038<br>
	    Email: <a href="mailto:your.emai@provider.com">your.emai@provider.com</a></p>


	  </body>

	</html>

	""" 

	content = MIMEText(html, 'html')

	msg.attach(content)



	gmail_user = 'your.emai@provider.com'
	gmail_password = 'yourpassword'

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
