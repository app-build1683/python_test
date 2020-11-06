import argparse
import requests
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
        r=requests.get(new_url)
        print(r.json)
        return r.json
#   mureturn ni xa sa list na naa ang tanan symbol
#   def extract_stock_data():

def arg_parser():
    ap=argparse.ArgumentParser()
    ap.add_argument("-s", "--start_date", help="start date format yyyy-mm-dd")
    ap.add_argument("-e", "--end_date", help="end date format yyyy-mm-dd")
    ap.add_argument("-y", "--symbol", help="stock Symbol")
        
    args=vars(ap.parse_args())
    print("symbol is {}".format(str(args['symbol'])))
#   print(args)
    
    stock_code=DataExtraction(args)
    stock_list=stock_code.extract_symbols()
    print(stock_list)
    

def main():
    arg_parser()
    
if __name__==main():
    main()
