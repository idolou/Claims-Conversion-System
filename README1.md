The system is divided to 3 partrs:

conersion_system.py:
run the console application, get the pate of input file and print the
outputs path of the output files.

constants.py:
save mapping dictionary of currency rate, data formatting and reason code
as shown in the reasoncode.csv file. at first try, I load this file and created the 
reasoncode dictionary every time the code run - lines 77-87 in utils.py, but beacause this dictionary is
constant for all files i decided to just put it in the code after minor modifications.

utils.py:
responsible for creating the dictioneries from csv file, calculate new fields
and create the new json files and directories for the Output. 
