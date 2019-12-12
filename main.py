import argparse
from pypackage.openairquality import list_csv
from pypackage.openairquality import check_city
from pypackage.openairquality import get_quality
from pypackage.db_connection import check_db

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Username to log-in (password required)")
parser.add_argument("-p", "--password", help="Password to log-in required", required=True)
parser.add_argument("-c", "--city", help="Name of the European city to be sought", required=True)
parser.add_argument("-m", "--molecule", help="Polluting molecule required (default=pm10)", choices = list_csv('pypackage/parameters.csv'), default="pm10")
parser.add_argument("-v", "--verbosity", help="Increase output verbosity", action="count")
args = parser.parse_args()


# Check if the username is registered
if check_db(args):

    # Get air quality value   
    p_value = get_quality(args.city, args.molecule)

    # Print the result based on verbosity level
    if args.verbosity == 2:
        print("Second level of verbosity turned on")

        if p_value == -1:
            print("Could not find a value of {} for {}".format(args.molecule, args.city))
        else:
            print("The city of {} has a {} value of {}".format(args.city, args.molecule, p_value))

    elif args.verbosity == 1:
        print("First level of verbosity turned on")

        if p_value == -1:
            print("{} for {} not found".format(args.molecule, args.city))
        else:
            print("{} in {} = {}".format(args.molecule, args.city, p_value))

    else:
        if p_value == -1:
            print("None")
        else:
            print(p_value)
