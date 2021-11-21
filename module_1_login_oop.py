# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:47:30 2021

@author: adellegia
"""

from sys import exit
import pandas as pd
import csv


class User:
    def __init__(self, cdb = pd.DataFrame(), username="", password="", userid = "", index = ""):
        self.cdb = cdb
        self.username = username
        self.__password = password
        self.userid = userid
        self.index = index
        
    def LogIn(self):
        self.cdb = pd.read_csv("credentials_database.csv")
        print("\nPlease log in using your valid username and password.\n")
    
        self.username = str(input("Enter username: \n"))
        n1 = 0
        n2 = 0
        self.index = self.cdb.index
            
        while (len((self.cdb[self.cdb.username == self.username]['username'] == self.username).index) == 0):
            n1 += 1
            if (n1 < 3):
                print("\nInvalid username. Please enter an existing username.\n")
                self.username = str(input("Enter username: \n"))
            else:
                print("Sorry, you have entered an invalid username. Try creating a new account instead.\n")
                exit()
        else:
           #print("\nUsername is valid.")
           ind = self.index[self.cdb.username == self.username].tolist()
           self.password = str(input("\nEnter password: \n"))
           while ~((self.cdb.password[ind] == self.password)[ind[0]]): 
               n2 += 1
               if (n2 < 3):
                    print("\nIncorrect password. Please enter your correct credentials.\n")
                    print("Username:\n" + self.username)
                    self.password = str(input("Enter password: \n"))
               else:
                    print("Sorry, you have entered an invalid password.\n")
                    exit()
           print("\nYou have successfully logged in!\n")
           #exit() # go to MODULE 2
        
    def NewUser(self):
        self.cdb = pd.read_csv("credentials_database.csv")
        print("\nRegister now as a new user to access GetHelp!\n")       
        n3 = 0 
        self.username = str(input("Please enter your new username: \n"))
        while(len(self.cdb[self.cdb.username == self.username])):
            n3 += 1
            if (n3 < 3):
                print("\nUsername already exists. Please create a new account using a unique username.\n")
                self.username = str(input("Please enter a unique username: \n"))
            if (n3 == 2):
                print("Try logging in instead. \n")
                User.LogIn(self)
        self.password = str(input("Please enter your password: \n"))
        print("\nThank you for registering!\n")
        
        self.userid = str(len(self.cdb) + 1) #5-digit userid
        if len(self.userid) == 1:
            self.userid = "0000" + self.userid
        elif len(self.userid) == 2:
            self.userid = "000" + self.userid
        elif len(self.userid) == 3:
            self.userid = "00" + self.userid
        elif len(self.userid) == 4:
            self.userid = "0" + self.userid
        
        with open("credentials_database.csv", 'a', encoding = 'UTF8', newline = '') as credentials:
            credentials_writer = csv.writer(credentials)
            credentials_writer.writerow([self.userid, 
                                         self.username, 
                                         self.password])
        User.LogIn(self)
        
    ## getters    
    def getuserId(self):
        self.cdb = pd.read_csv("credentials_database.csv")
        #ind = len((self.cdb.username == self.username).index.tolist())-1
        #self.userid = self.cdb.userid[ind]
        ind = self.index[self.cdb.username == self.username].tolist()
        self.userid = self.cdb.userid[ind[0]]
        return self.userid   

    def getuserName(self):
        return self.username