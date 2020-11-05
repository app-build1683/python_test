import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-s", "--start_date", help="start date format yyyy-mm-dd")
ap.add_argument("-e", "--end_date", help="end date format yyyy-mm-dd")
ap.add_argument("-y", "--symbol", required=True, help="stock Symbol")

args=vars(ap.parse_args())

print("symbol is {}".format(str(args['symbol'])))
