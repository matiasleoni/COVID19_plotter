'''
This script allows you to INPUT countries of interest, data of interest, starting date and
an integer smoothing parameter in order to plot the time series for the given type of data
and country set using matplotlib module and parsing the information provided in the dataset
collected by "Our World in Data" organization. Credits for the dataset goes to:
Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing.
Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8
'''

import csv
import requests
import datetime
import os
import pandas as pd
import warnings
warnings.filterwarnings("ignore", "(?s).*MATPLOTLIBDATA.*", category=UserWarning)
import matplotlib.pyplot as plt
import PIL.Image as pili
import data as dt






##################################################
##### GENERIC FUNCTION rolling: dataset -> dataset
##################################################


def rolling_n_deep_avg(alist,n_deep):
    '''
    INPUT: a list, integer n_deep
    OUTPUT: rolling "n_deep" data average list ("n_deep"-1 elements shorter).
            Integer rounded result
    '''
    new_list = []
    for elem in range(len(alist)-n_deep+1):
        subsidiary_list = [alist[elem+num] for num in range(n_deep)]
        new_list.append( sum(subsidiary_list)/n_deep)
    return new_list

#########################
#### PARSE DATA FUNCTIONS
#########################


def transdate(string):
    """
    INPUT: string of the form "YYYY-MM-DD"
    OUTPUT: datetime.date object with the corresponding date
    """
    day = int(string[8:])
    month = int(string[5:7])
    year = int(string[:4])
    #print(day, month, year)
    return datetime.date(year, month, day)

def parse_title(a_string):
    '''
    Take a string such as 'new_deaths_per_million' and return 'New deaths per million'
    '''
    a_list = a_string.split('_')
    b_string = (' '.join(a_list)).capitalize()
    return b_string

#####################################################
#####################################################


def parser_local(countries):
    """
    INPUT: List of Country Names in English
    OUTPUT: A dictionary of dictionaries. The key value of the outer dictionary is a tuple (date, 'country').
    The inner dictionary has keys from dt.COLUMNS and their respective values.
    """
    num_of_countries = len(countries)
    tot_entries = ((datetime.date.today()-datetime.date(2019, 12, 31)).days+1)*num_of_countries
    print('')
    print('At most a total of',tot_entries,'entries expected.')
    
    with open(dt.FILE, 'rt', newline = "", encoding='utf-8-sig') as myfile:
        csvreader = csv.reader(myfile,skipinitialspace = True,
                           delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        ntable = []
        num = 0
        print('')
        for line in csvreader:
            if line[2] in countries:
                ntable.append(line)
                num += 1
                #print(num,'\b', sep=' ', end='', flush=True)
        #print('')
        print(num,'entries found for selected countries ... OK')
        print('')
        ncolumn = dt.COLUMNS
        mydic = {}
        for element in ntable:
            mydic[(element[2],element[3])] = {ncolumn[index]: element[index] for index in range(len(ncolumn))}
    return mydic




def order_for_plot(mydic, country, init_date, type_graph, deep):
    '''
    INPUT: - Parsed dictionary with all the data corresponding to selected countries. Assumed the form
             returned by parser_local function
           - a single country (string)
           - initial date to consider in format 'YYYY-MM-DD'
           - type_graph data we are interested in
           - integer deep level or rolling average
    RETURNS: List of [date, data] elements with the moving average applied on data for single country
    '''
    data_table = []
    date_table = []
    for key, val in mydic.items():
        if len(val[type_graph]) > 0 and key[0] == country and transdate(val['date']) >= transdate(init_date):
            data_table.append(float(val[type_graph]))
            date_table.append(transdate(val['date']))
        elif len(val[type_graph]) == 0 and key[0] == country and transdate(val['date']) >= transdate(init_date):
            data_table.append(0)
            date_table.append(transdate(val['date']))
    if len(data_table) == 0:
        return []
    else:
        new_data = rolling_n_deep_avg(data_table,deep)
        new_date = list(date_table)
        for iter in range(deep-1):
            new_date.pop(0)
        return pd.Series(data=new_data, index=new_date)


#####################################################
#####################################################


def draw_many_lines(countries, data_type, deep=7, init_date='2019-12-31', outputfile=0):
    """
    INPUT: - List of countries written as strings in English
           - String with the data type
           - depth of the moving average. Default being 7
           - Initial date to consider in format 'YYYY-MM-DD'. Default being the whole COVID series.
           - name of output file. If parameter omitted plot is rendered in the browser
    OUTPUT: Produces a png plot rendered in a temporary file (unless outputfile chosen)
            for the specified countries and data type with a deep-day rolling mean.
    RETURN: None
    """
    plt.style.use('seaborn-notebook')
    if os.path.exists(dt.FILE):
        statbuf = datetime.datetime.fromtimestamp((os.stat(dt.FILE)).st_mtime)
        print('')
        print('=============================================================')
        print('')
        print("LAST DOWNLOAD OF DATA: {}".format(statbuf))
        print('')
        fresh_or_not = input("Want to download fresh data? Press y/n (default is 'n'): ")
        if fresh_or_not == 'y':
            print('')
            print('Downloading fresh data from "Our World in Data" ...', end='')
            my_web = requests.get(dt.WEB, allow_redirects=True)
            with open('owid-covid-data.csv', 'wb') as newdatafile:
                newdatafile.write(my_web.content)
    elif not os.path.exists(dt.FILE):
        print('')
        print('Downloading fresh data from "Our World in Data" ...', end='')
        my_web = requests.get(dt.WEB, allow_redirects=True)
        with open('owid-covid-data.csv', 'wb') as newdatafile:
            newdatafile.write(my_web.content)        
    print('OK')
    mydic = parser_local(countries)
    for pais in countries:
        print('Processing data for',pais,'... ', end='')
        if data_type in dt.COLUMNS:
            mytable = order_for_plot(mydic, pais, init_date, data_type, deep)
        else:
            print('')
            print('')
            print('WARNING!!!!')
            print('No such data type as '+data_type+'. Please check your spelling and run again.')
            print('')
            return      
        if len(mytable) > 0:
            print('OK')
            if deep == 1:
                plot_title = parse_title(data_type)+". dataset OWID"
            elif deep > 1:
                plot_title = parse_title(data_type)+". "+str(deep)+" days moving average. dataset OWID"
            mytable.plot(legend=True, label=pais, grid=True, logy=False, figsize=(12,6),
                         title=plot_title, xlabel='date')
        else:
            print('')
            print('')
            print('WARNING!!!!')
            print('No such country as '+pais+'. Please check your spelling and run again.')
            print('')
            return       
    if outputfile == 0:
        print('Preparing plot... ', end='')
        plt.savefig('temporalMLO2511.png')
        fooooo = pili.open('temporalMLO2511.png').show()
        os.remove('temporalMLO2511.png')
        print('OK')
    else:
        print('Saving plot... ', end='')
        plt.savefig(outputfile)
        print('OK')
        print('File saved to',outputfile)


def input_output_execution():
    '''
    INPUT: -
    RETURN: -
    OUTPUT: after executing input questions to the user ir executes draw_many_lines function with the proper arguments
    '''
    ### GENERAL INFORMATION
    print('======================================================================================================')
    print('')
    print('                                  PLOT COVID-19 DATA                                                  ')
    print('This program is designed to plot time series lines for different COVID-19 data of different countries.')
    print('Author: Matias Leoni')
    print('')
    print('Credit for the dataset:')
    print('Hasell, J., Mathieu, E., Beltekian, D. et al. A cross-country database of COVID-19 testing.')
    print('Sci Data 7, 345 (2020). https://doi.org/10.1038/s41597-020-00688-8')
    print('======================================================================================================')
    
    ### INPUT Country names in English
    country_list = []
    while True:
        print()
        print('Input country name in english (e.g. Argentina).')
        country = input('If no more countries are needed just press ENTER: ')
        if country == '' and len(country_list) > 0:
            break
        elif country == '' and len(country_list) == 0:
            print()
            print('At least one country name is needed')
        elif country.title() not in dt.COUNTRIES:
            print()
            print(country, 'is non-existent. Check your spelling')
        elif country.title() in dt.COUNTRIES:
            country_list.append(country.title())
    print('')
    print('Your set of country choices is:     ', country_list)
    
    ### Present data types
    print()
    print('=====================================================================')
    print()
    print()
    print('LIST OF DATA TYPES')
    print('----------------------------------------------------------------------')
    print("total_cases, new_cases, total_deaths, new_deaths, total_cases_per_million")
    print("new_cases_per_million, total_deaths_per_million, new_deaths_per_million")
    print("total_tests, new_tests, total_tests_per_thousand, new_tests_per_thousand")
    print("tests_per_case, positive_rate, tests_units, stringency_index")
    print('----------------------------------------------------------------------')
    print()
    
    ### INPUT Data types
    more = True
    while more:
        print('Please choose a data type from the previous list.')
        data_type = input('Write it literally as in the list (e.g. new_cases): ')
        if data_type in dt.COLUMNS:
            more = False
        else:
            print('')
            print('Check your spelling. Try again')
            print('')        
    print()
    print()
    
    ### INPUT integer number corresponding to the number of days for the moving average
    while True:
        try:
            print('Input an integer number (days) for smoothing data with moving average.')
            deep_avg = input('1 is the default. 7 is the recommended for daily data: ')
            if deep_avg == '':
                deep_avg = 1
            else:
                deep_avg = int(deep_avg)
            break
        except ValueError:
            print('')
            print('That was not an integer number. Please try again')
            print('')            
    print()
    print()
    
    ### INPUT the desired starting date
    while True:
        try:
            print('Input starting date in format YYYY-MM-DD.')
            init_date = input('For example 2020-06-30. Press ENTER for default (beginning of the pandemic):')
            if init_date == '':
                init_date = '2019-12-31'
            else:
                transdate(init_date)
            break
        except ValueError:
            print('')
            print('Non-existent date or incorrect format. Please try again')
            print('')
    print()
    print()
    
    ### INPUT the name of the file to render the plot
    print('Input the file name for the output (e.g: grafico.png).')
    outputfile = input('Press ENTER to show the plot without saving it: ')
    if outputfile == '':
        outputfile = 0
    ### EXECUTE
    draw_many_lines(country_list, data_type, deep_avg, init_date, outputfile)

# while True:
#     execute = input('Do you want to execute the program interactively? (y/n): ')
#     if execute == 'y':
#         input_output_execution()
#         del(execute)
#         break
#     elif execute == 'n':
#         del(execute)
#         break

input_output_execution()


