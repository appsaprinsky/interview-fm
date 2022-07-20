# interview-fm

## PREPARING AND RUNNING
Before running the project, please create virtual environment:
```
python3.9 -m venv venv
```
activate virtual environment:
```
source venv/bin/activate
```
and install all dependencies:
```
pip install -r requirements.txt
```

In order to check all results at once, please run: 
```
python main.py 
```
You could check each result individually:


## TASK 1
In order to check Task 1 results, please uncomment ```task1_run() ``` at the end of the file and run in terminal
```
python task1.py 
```
First print will show results from sql command, second print will show same result, 
but with pandas work.

## TASK 2
In order to check Task 2 results, please uncomment ```task2_run() ``` at the end of the file and run in terminal
```
python task2.py 
```
First print will show results from sql command, second print will show same result, 
but with pandas work.


## TASK 3
In order to check Task 3 results, please uncomment ```task3_run() ``` at the end of the file and run in terminal
```
python task3.py 
```
First csv file (output/pd_combined.sql) will show results from sql command, second csv file (output/pd_combined.csv) will show same result, 
but with pandas work.


## TASK 4
In order to check Task 4 results, please uncomment ```task4_run() ``` at the end of the file and run in terminal
```
python task4.py 
```
This time I have duplicated Database (transactions_4.db), as we are going to updated all values 
in row there. So all original values will be taken from database transactions.db and updated in transactions_4.db.
You can also see changes to be made in file output/task4_result.csv.
I have added an opportunity to change Currency. If currency is not present there, the output will be: Cannot find Currency.


## TASK 5
To check connection with PostgreSQL, I have create cloud database with mailru and elephantsql:
For Mailru credentials are:
login: trial.interview.ns@mail.ru
password: EasyPassword111

For Elephantsql credentials are:
https://www.elephantsql.com/plans.html
login: trial.interview.ns@mail.ru
password: EasyPassword111
Name: database1

The issue is solved by creating another class (DatabasePostgreSQL), that will focus
on the execution commands for PostgreSQL.



## HOW COULD IT BE IMPROVED?
Add code to Classes to check all inputs and outputs. Catching all possible errors in a code.
Adding pytest to ensure everything is working properly and as expected.
Write class(es) for pandas part. 

## HOW DID I APPROACH THE ISSUE?
Firstly, I have created simple class(es), where the simple results could be get. The idea is to create reusable 
methods, so that I could apply them in similar situations. 
Secondly, I approached issues with different angles and I have tried to check the results using different ways.
This help me to be more confident in my final answers.

