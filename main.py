from pypackage.openairquality import get_quality

pm10=get_quality()
print("Rome has a pm10 value of {}".format(pm10))
no2=get_quality(city="Bologna", parameter='no2')
if no2==-1:
    print("Could not find a value of no2 for Bologna")


