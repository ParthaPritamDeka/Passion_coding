import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads_list.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []

    for n in range(1,9):
        station = sheet.cell_value(0, n)

        list = sheet.col_values(n, start_rowx=1, end_rowx=None)
        max_value = max(list)
        max_pos = list.index( max_value) + 1
        Year, Month, Day, Hour, Min, Sec = xlrd.xldate_as_tuple(sheet.cell_value(max_pos, 0), 0)

        data.append([station, Year, Month, Day, Hour, max_value])


    return data


    #header = [Station, Year, Month, Day, Hour, Max Load]

    
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    

def save_file(data, filename):
    # YOUR CODE HERE

    with open(filename, 'wb') as csvfile:
         spamwriter = csv.writer(csvfile, delimiter='|')
    
         spamwriter.writerow(["Station", "Year", "Month", "Day", "Hour", "MaxLoad"])

         for i in range(len(data)):
        
             spamwriter.writerow(data[i])

def test():

    data = parse_file(datafile)
    print data
    save_file(data, outfile)
                            
                            
if __name__ =='__main__':
    test()
    
                            
