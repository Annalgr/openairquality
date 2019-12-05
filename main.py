import argparse
from mypackage.openairquality import get_quality


parser = argparse.ArgumentParser()
parser.add_argument("city", help="Name of the city to be sought")
args = parser.parse_args()

p_value = get_quality(args.city, parameter='pm10')
print("{} has a pm10 value of {}".format(args.city, p_value))
