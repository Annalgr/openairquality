import argparse
from pypackage.openairquality import get_quality


parser = argparse.ArgumentParser()
parser.add_argument("city", help="Name of the city to be sought")
parser.add_argument("-p", "--parameter", help="Polluting particles")
parser.add_argument("-v", "--verbosity", help="Increase output verbosity", action="store_true")
args = parser.parse_args()

p_value = get_quality(args.city, args.parameter)

if args.verbosity:
    print("{} has a {} value of {}".format(args.city, args.parameter, p_value))
    
else:
    print(p_value)
