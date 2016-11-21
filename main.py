import preprocessing
import xlrd 
from openpyxl import Workbook
from openpyxl import load_workbook
from xlrd import open_workbook
import csv

fp = open('tweet3000.csv', 'r')
line = fp.read()
inpTweets = csv.reader(open('twiit.csv', 'rb'), delimiter=';', quotechar='|')
pre=preprocessing.preprocess(line)

see=preprocessing.fitur_ekstraksi(pre)

print see
