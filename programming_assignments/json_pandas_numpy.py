# Census Bureau
# Quarterly Workforce Indicators
# 1990 - Present
# Will Wagner

import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pprint
# import matplotlib.pyplot as plt


req = ''
parsed_json = {}
json_string = ""
json_dict = {}

def assemble_CENB_URL (CENB_MidURL):
    CENB_CompleteURL = CENB_BaseURL + CENB_MidURL + CENB_APIKEY
    return CENB_CompleteURL


def URL_Test(url):
    r = requests.get(url)
    print ('r.status_code: ' + str(r.status_code))
    print('')
    print ("r.headers['content-type']" + r.headers['content-type'])
    print('')
    print ("r.encoding: " + r.encoding)
    print('')
    print ("r.text: " + r.text)
    print('')
    print ("r.json(): " + str(r.json()))
    print('')
    print('')

def make_json_dict_req(url):
    req = requests.get(url)
    json_dict = req.json()
    if error_verbose == True:
        print ('req status: ' + str(req.status_code))
        print ('json_string: ' )
        print (json_dict)
        print()
        print ('=============  END REQUEST FUNCTION  ==============')
        print ()
    return json_dict

def pandas_Test(url):
    dataframe = pd.DataFrame(json_dict)
    print (dataframe)
    return dataframe


# Use Pandas
def print_BDS_pd(url):
    
    json_dict = make_json_dict_req ( url )
    # ['metro']['sic1']['fage4']['fsize']['ifsize']['year2']['us']
    # print (json_dict)

    # Use Pandas
    dataframe = pd.DataFrame(json_dict)
    print()
    print('================')
    print ("Pandas dataframe: ")
    print (dataframe)
    print ()
    print ("End Pandas dataframe: ")
    print('================')


# Use pprint
def print_BDS_pp(url):
    
    json_dict = make_json_dict_req ( url )

    # Use pprint
   
    print()
    print('================')
    print ("pprint dataframe: ")
    pprint.pprint (json_dict)
    print ()
    print ("End pprint dataframe: ")
    print('================')
