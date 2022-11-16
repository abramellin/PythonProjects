#!/usr/bin/python3

'''
csvdupe by Christian Lawrence
This is to find duplicate hostnames from the AMP computer list csv file.
'''

import csv
import pprint
fname = "csv1.csv"
with open(fname, "r") as fin:
    reader = csv.reader(fin)
    # create a dictionary of column:frequency pairs
    freq = {}
    for row in reader:
        #Organize columns in csv "headers"
        Connector_GUID,Hostname,Operating_System,Connector_Version,Group,Install_Date,Last_Seen,Internal_IP,External_IP,MAC_Addresses,iOS_Serial_Number,Connector_Antivirus,Last_Definitions_Update,Last_Definitions_Update_Failure,Processor_Hardware_Identifier = row
        #get frequency of selected column "Hostname"
        freq[Hostname] = freq.get(Hostname, 0) + 1
#Using list comprehension with dict() function to identify key values and then print key and value pairs based on if statement.
d = dict((k,v) for k, v in freq.items() if v >= 2)
print('-' * 70)
# show results
pprint.pprint(d)
print('-' * 70)

