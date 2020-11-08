import argparse
import requests
import json
#class LookBack():
#   def compare_value():

class DataExtraction:
#"will extract data for all stock code or stock details"
   def __init__(self,args):
       self.stock_code=(args['symbol'])
       self.start_date=(args['start_date'])
       self.end_date=(args['end_date'])
       self.base_url='https://pselookup.vrymel.com/api'
       print(args)
        
   def extract_symbols(self):
       new_url=self.base_url +'/stocks'
       print(new_url)
       r=requests.get(new_url).json()
       return r

#   mureturn ni xa sa list na naa ang tanan symbol
#   def extract_stock_data():

def arg_parser():
    ap=argparse.ArgumentParser()
    ap.add_argument("-s", "--start_date", help="start date format yyyy-mm-dd")
    ap.add_argument("-e", "--end_date", help="end date format yyyy-mm-dd")
    ap.add_argument("-y", "--symbol", help="stock Symbol")
        
#   print("symbol is {}".format(str(args['symbol'])))
#   print(args)
    
    stock_code=DataExtraction(vars(ap.parse_args()))
    stock_list=stock_code.extract_symbols()
#    print(stock_list)
#    for i in stock_list['stocks']:
#        if i['ticker_symbol'] == ticker:
#            print("found")
#        else:
#            print("Invalid code. Please see list")
#            print(i['ticker_symbol'])
    if [x for x in stock_list['stocks'] if x.get('ticker_symbol')==(vars(ap.parse_args())['symbol'])]:
        print("found")
    else:
        print("Symbol not found, please check below list:")
        for i in stock_list['stocks']:
           print(i['ticker_symbol'])




def main():
    arg_parser()
    
if __name__==main():
    main()
