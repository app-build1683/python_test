import argparse

#class LookBack():
#	def compare_value():

#class DataExtraction():
#"will extract data for all stock code or stock details"
#	def extract_symbols():
#	def extract_stock_data():

def arg_parser():
	ap=argparse.ArgumentParser()
	ap.add_argument("-s", "--start_date", require=True, help="start date format yyyy-mm-dd")
	ap.add_argument("-e", "--end_date", required=True, help="end date format yyyy-mm-dd")
	ap.add_argument("-y", "--symbol", required=True, help="stock Symbol")

	args=vars(ap.parse_args())

	print("symbol is {}".format(str(args['symbol'])))

def main():
	arg_parser()

#if __name__ = main()
	main()
