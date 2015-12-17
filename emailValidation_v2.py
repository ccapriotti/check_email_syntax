#!/usr/bin/python


# Code by Carlos Capriotti
#
# If you use this code somehow, play nice and mention the author.
#
#
# Batch validates a list of email addresses, checking them agains a regular expression.
# Correctly build addresses are saved to a "good" file, and wrongly formed addresses
# are saved to a report. 

import io
import re

def validateEmail(email):

	if len(email) > 7:
		#if re.match("^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$", email) != None:
		if re.match("^[^\.][a-z0-9._%+-]+@[^\.][a-z0-9.-]+\.[a-z]{2,4}$", email) != None:
			return 1
	return 0

list_filename = '/Users/the_correct_addresses_here.txt'
report_filename = '/Users/addresses_with_errors_here.txt'

email_list = open('/Users/original_email_file.csv', 'r')
correct_list = open(list_filename,'w')
minority_report = open(report_filename,'w')


line = 1
counter = 1
batch = 2
currentAddress = ""


for currentAddress in email_list:
   currentAddress = currentAddress.lower()
   currentAddress = currentAddress.strip()
   print(currentAddress)
   #raw_input("Any key to continue")
   if validateEmail(currentAddress):
      correct_list.write(currentAddress + "\n")
   else:
      minority_report.write(currentAddress + "\n")

#com='''
   if counter >= 450:
      correct_list.close()
      minority_report.close()
      list_filename =  '/Users/validated_list' + str(batch) + '.txt'
      report_filename = '/Users/error_report' + str(batch) + '.txt'
      correct_list = open(list_filename,'w')
      minority_report = open(report_filename,'w')
      batch=batch+1
      counter = 1
   counter=counter+1
#'''
correct_list.close()
minority_report.close()
email_list.close()

