import os # used to check if the database file, hash file exist, removing the hash file and also for displaying the machine username

import sys # used for exiting the program

import time # mainly used for selenium to wait until the site loads properly and used for some animation purposes

import random

import string

import stdiomask # used with getpass to display the password as '*'

import getpass # used to make the password typing hidden

import sqlite3 # SQL Lite database that will be used for our program

import bcrypt # a hasher for our master password

from sqlite3.dbapi2 import Cursor # cursor is used to execute SQL commands (ex. INSERT, UPDATE...)

from texttable import Texttable # used for displaying data in a proper tabular format