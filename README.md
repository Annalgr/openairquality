# Open Air Quality
### Monitor pollution levels of major European cities :deciduous_tree: :partly_sunny:

There are little particles in the atmosphere, so small and light that they can float. Some of these particles determine air pollution and can be harmful to your health. In this repository you can find a file named ```main.py``` that can help you monitoring European city's air pollution levels. Indeed, it queries the [OpenAQ](https://openaq.org) website for air quality measurements within specific European cities. Data of the following polluting molecules are gathered from multiple sources and made web-accessible through the [Open AQ Platform API](https://docs.openaq.org/): bc, co, no2, o3, pm10, pm25, so2.


### Get started!
The following modules are required:```argparse```, ```sqlite3```, ```hashlib```, ```random```, ```requests```, ```json```, ```csv```, ```unittest```, ```os```, and ```sys```.
Firstly, **registration is required** to access information about the atmosphere!
In order to register you need to: 

**1. Go to the ```scripts``` folder;** <br/>
**2. Register with username and password:**
```
$ python dbmanager.py -a username -p password 
```
The output will confirm the registration:
```
The registration had been successful
```
> **Note:** you can add as many users as you want repeating these steps. Remember, you can't add more than one user with the same username.


If you run the program for the first time, this will create a username and password database (read more about database creation and population below). Now you can run the main program as follows:

**3. Execute the main file by running the program with:**
```
$ python main.py username -p password -c city -m molecule
```

You will get this kind of result:	
```
Successful log-in. Welcome username!
16.043478260869566
```
> **Note:** in case the user forgets to specify the molecule, the program uses by default “pm10”. Indeed, pm10 is the most common polluting particle from 2.5 to 10 micrometers in diameter.


You may want to turn on output verbosity. The following example shows a user looking for pm10 value in Roma: 
```
$ python main.py user -p password -c Roma -m pm10 -v 
``` 
Verbosity will generate this kind of result:
```
Successful log-in. Welcome user!
First level of verbosity turned on
pm10 in Roma = 20.91304347826087 
```

### Parameters Guide
To join the program, after inserting your username and password, you are allowed to choose:
- a **city**, among the European cities listed in the [OpenAQ API](https://api.openaq.org/v1/cities) documentation. 
  > Try with some of the most important European cities like Roma, Paris, London, Berlin, Luxembourg, Bristol, Cambridge, Edinburgh, Oxford, Amsterdam, Budapest, Brussels, Oslo, Granada, Stockholm.
- a **molecule**, from the set of molecules: bc, co, no2, o3, pm10, pm25, so2.<br/>

Cities and polluting molecule's parameters have been gathered and stored in ```pypackage``` as csv files; respectively in ```cities.csv``` and ```parameters.csv```

*Positional arguments*:

• **username**: name of the user to log-in.

*Optional arguments*:

•	**-p**, **--password**: user password to log-in (required).

•	**-c**, **--city**: name of the European city (required).

•	**-m**, **--molecule**: name of the polluting molecule (pm10 by default).

•	**-v**, **--verbosity**: output verbosity (three levels of verbosity admitted).



### Create and Populate openaq_user.db
Before running ```main.py``` you need to register with a username and a password. First time sign-in is necessary for the database to record all the users' information. You can find all the processes needed to create the database inside the ```dbmanager.py```file inside ```scripts``` folder. 
By importing and using the ```sqlite3``` library, the program checks if the database is already existing, otherwise creates a new one called ```user_database``` by using: 
```
cursor.execute('''CREATE TABLE user_database
                     (username CHAR(30) NOT NULL,
                     password_digest CHAR(64) NOT NULL,
                     salt CHAR(30), PRIMARY KEY (username))'''))
```
 
This creates a table with 3 columns (username, password_digest, and salt). NOT NULL and CHAR() conditions ensure that users does not register with Nan value or more characters than allowed.

*Optional arguments*:

•	**-a**: add a username (password required).

•	**-p**: password to be associated with the username (required).

•	**-c**: check for a username (password required).



### Testing 
You can test the code running the module ```test_openairquality``` inside ```tests``` folder. The function tested is the **list_csv** of the module ```openairquality.py``` inside ```pypackage``` folder.
To run the unittest go to the ```tests``` folder and do:
```
$ python -m unittest -v -b test_openairquality.py
```
You will obtain this kind of result: 
```
 test_empty_file (tests.test_main.TestCsvCreation) ... ok
 test_invalid_file (tests.test_main.TestCsvCreation) ... ok
 test_no_file (tests.test_main.TestCsvCreation) ... ok
 test_valid_file (tests.test_main.TestCsvCreation) ... ok
```
> **Note:** inside the folder the two files ```eu.csv``` and ```ibelieveinmyself.jpg``` are used in the module ```test_main``` to test that the function accepts a csv file and does not accept a file with a different format (i.e. jpg).



#### This repository has been created by the Group Unicorns :unicorn: :
868543 - Anna Lagrasta <br/>
866764 - Francesca Griggio <br/>
869442 - Martina Gualandi

