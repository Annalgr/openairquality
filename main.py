import argparse
from pypackage.openairquality import get_quality


parser = argparse.ArgumentParser()
parser.add_argument("city", help="Name of the city to be sought")
parser.add_argument("-p", "--parameter", help="Polluting particles")
parser.add_argument("-v", "--verbosity", help="Increase output verbosity", action="count")
args = parser.parse_args()

p_value = get_quality(args.city, args.parameter)

if args.verbosity == 2:
    print("Second level of verbosity turned on")

    if p_value == -1:
        print("Could not find a value of {} for {}".format(args.parameter, args.city))
    else:
        print("The city of {} has a {} value of {}".format(args.city, args.parameter, p_value))

elif args.verbosity == 1:
    print("First level of verbosity turned on")

    if p_value == -1:
        print("{} for {} not found".format(args.parameter, args.city))
    else:
        print("{} in {} = {}".format(args.parameter, args.city, p_value))

else:
    if p_value == -1:
        print("None")
    else:
        print(p_value)


