#python3

import pandas as pd
import numpy as np

import time

#load the csv as the dataframe with only the columns you care about
df = pd.read_csv('repoffinput.csv', usecols = ['Organization Name (English)', 'Organization Name (Chinese)', 'Professional Supervisory Unit (English)', 'Professional Supervisory Unit (Chinese)', 'Organization Origin', 'Field of Work', 'Registration Location', 'Date of Registration', 'Permitted Area(s) of Operation'])


#reorders the columns
columnsTitles = ['Organization Name (English)', 'Organization Name (Chinese)', 'Professional Supervisory Unit (English)', 'Professional Supervisory Unit (Chinese)', 'Organization Origin', 'Field of Work', 'Registration Location', 'Date of Registration', 'Permitted Area(s) of Operation']
df = df.reindex(columns=columnsTitles)

#prevents truncation of field data
pd.set_option('max_colwidth', -1)

#outputs html to a file
#index = false is to avoid printing the index column
new_table = df.to_html(index = False, classes = ['tableizer-firstrow'], border = 0)

#removes the formatting
#changes the formatting for the table headers
#I'm sure there is a more elegant way of doing this but I don't know it


fixed_table_1 = new_table.strip('<table border="0" class="dataframe tableizer-firstrow">')
fixed_table_1a = fixed_table_1.replace('<tr style="text-align: right;">', '<tr style="text-align: center;">')
fixed_table_2 = fixed_table_1a.replace('<th>Organization Name (English)</th>', '<th style="width:10%">Organization Name (English)</th>')
fixed_table_3 = fixed_table_2.replace('<th>Organization Name (Chinese)</th>', '<th style="width:10%">Organization Name (Chinese)</th>')
fixed_table_4 = fixed_table_3.replace('<th>Professional Supervisory Unit (English)</th>', '<th style="width:10%">Professional Supervisory Unit (English)</th>')
fixed_table_5 = fixed_table_4.replace('<th>Professional Supervisory Unit (Chinese)</th>', '<th style="width:5%">Professional Supervisory Unit (Chinese)</th>')
fixed_table_6 = fixed_table_5.replace('<th>Organization Origin</th>', '<th style="width:5%">Organization Origin</th>')
fixed_table_7 = fixed_table_6.replace('<th>Field of Work</th>', '<th style="width:10%">Field of Work</th>')
fixed_table_8 = fixed_table_7.replace('<th>Registration Location</th>', '<th style="width:5%">Registration Location</th>')
fixed_table_9 = fixed_table_8.replace('<th>Date of Registration</th>', '<th style="width:5%">Date of Registration</th>')
fixed_table_10 = fixed_table_9.replace('<th>Permitted Area(s) of Operation</th>', '<th style="width:40%">Permitted Area(s) of Operation</th>')

fixed_table = fixed_table_10

#This is the first part of the html page
top_half = open('site_top.html', 'r')

#this is the regular output
output_page = open('index_RO_table.html', 'w')

#this creates the archive output
timestamp = time.strftime("%Y%m%d")
output_page_archive_filename = "index_RO_table" + timestamp + ".html"
archive_page = open(output_page_archive_filename, 'w')


#writes the html to the new page
for item in top_half:
    output_page.write(item)
    archive_page.write(item)
#writes the table
for item in fixed_table:
    output_page.write(item)
    archive_page.write(item)
#closes out the page (this should be in the table but it isn't because I don't know why
output_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")
archive_page.write("table> <!–– add your tableizer data above this line––> </body> </html>")

top_half.close()
output_page.close()
archive_page.close()
