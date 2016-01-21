"""
Converts a Toggl CSV to ICS.
"""


import sys
# Yeah this is a hack
sys.path.append('.')

from convert import Convert
from datetime import datetime

convert = Convert()
convert.CSV_FILE_LOCATION = 'toggl.csv'
convert.SAVE_LOCATION = 'toggl.ics'
convert.HEADER_COLUMNS_TO_SKIP = 2
convert.NAME = 2
togglPROJECT = 3
togglDESCRIPTION = 5
togglUSERNAME = 0
convert.START_DATE = 7
togglSTART_TIME = 8
convert.END_DATE = 9
togglEND_TIME = 10
convert.DESCRIPTION = 12
convert.LOCATION = 13

convert.read_csv()
for row in convert.csv_data:
    row[convert.NAME] = row[convert.NAME]+' - '+row[togglPROJECT]+': '+row[togglDESCRIPTION]+' - '+row[togglUSERNAME]
    row[convert.START_DATE] = datetime.strptime(row[convert.START_DATE]+' '+row[togglSTART_TIME], '%Y-%m-%d %H:%M:%S')
    row[convert.END_DATE] = datetime.strptime(row[convert.END_DATE]+' '+row[togglEND_TIME], '%Y-%m-%d %H:%M:%S')
    row[convert.DESCRIPTION] = 'tags: '+row[convert.DESCRIPTION]
    row[convert.LOCATION] = "Work"

convert.make_ical()
convert.save_ical()
