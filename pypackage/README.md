## Implementation of an Air Quality data fetching library


In this repository you can find a file named ```openairquality.py``` that implements the ```get_quality(city, parameter)``` function. It queries the [OpenAQ](https://openaq.org) website to fetch the value of some air quality parameter in a world city. This function is used in the ```main.py``` file to obtain the value of pm10 in Rome and the value of no2 in Bologna. The second attempt will fail, as the database does not contain such value. If you run the program, executing the main file with: ```python main.py``` it will  give you results similar to the following: 

```
$ python main.py
Rome has a pm10 value of 18.391304347826086
Could not find a value of no2 for Bologna
```

Note that the project requires the ```json``` and ```requests``` module to run. [OpenAQ](https://openaq.org/) is a project that receives air quality data from people and serves them on-line. The APIs are documented in a [API documentation page](https://docs.openaq.org/). 

