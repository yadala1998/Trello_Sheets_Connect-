import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

#Define the scope of this application - Currently we access sheets and drive
#More about scope: https://developers.google.com/identity/protocols/googlescopes 
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#Create credentials using the scope and the JSON that we got from GCP
creds = ServiceAccountCredentials.from_json_keyfile_name('TrelloSheetsConnect-92516d3a10f3.json', scope)

def main():
	#Create a GSPread Client and authorize it use the credentials created
	client = gspread.authorize(creds)
	#Access the google sheet
	sheet = client.open('Trello_Test').sheet1
	#Testing the access
	pp = pprint.PrettyPrinter()
	#pp.pprint(sheet.row_values(2))
	pp.pprint(sheet.acell('A1').value)






if __name__ == '__main__':
    main()