Log Analysis Project

Description
A reporting tool that prints out reportsbased on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

Installation
Python 2.7 needs to be installed to run the program
Vagrant and VirtualBox needs to be installed

How to run the code
We need to change directory to vagrant directory .
Follow following steps:
1)vagrant up command to run the vagrant on vm
2)vagrant ssh to login into vm
3)change directory to vagrant
4)use command psql -d news -f newsdata.sql to load database
5)Run python log.py to run the program

Screenshot of working of code is present as Capture.jpg
