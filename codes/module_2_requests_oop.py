#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 2: Input Requests and Support Details

A User is asked if they want to get Help or provide Help.    
    
"""

from datetime import datetime 
from datetime import date 
from geopy.geocoders import Nominatim

def geo(loc):  
    """
    Function defines the location of student.
    
    Paramters
    ---------
    loc: string
        The location name of a user.
    
    Returns
    -------
    Geolocated code for user.
    """
    geolocator = Nominatim(user_agent="http")
    return geolocator.geocode(loc)

class Request:
    """
    A class to input details of help requested.
    
    Attributes
    ----------
    type: category
        The category of help requested.
    """
    def __init__(self, type):
        """
        Function defines the type of help requested.
        
        Parameters
        ----------
        Category : dict
            Type of help requested.
        optionsDict : dict
            Offer options for help based on selection in Category.
        
        Returns
        -------
        None.
        """
        self.type = type
        
        self.Category = {"1": "Errands",
                         "2": "Ride",
                         "3": "Translate",
                         "4": "Tutor"}
      
        self.optionsDict = {"Errands": {"1": "Flat maintenance",
                                        "2": "Government services",
                                        "3": "Grocery shopping",
                                        "4": "Mall shopping",
                                        "5": "Move in/out",
                                        "6": "Take care of pets/plants"},
                            "Ride": {"1": "Charlottenburg",
                                     "2": "Friedrichshain",
                                     "3": "Kreuzberg",
                                     "4": "Litchtenberg",
                                     "5": "Mitte",
                                     "6": "Neukoelln",
                                     "7": "Pankow",
                                     "8": "Spandau",
                                     "9": "Steglitz",
                                     "10": "Tempelhof",
                                     "11": "Schoeneberg",
                                     "12": "Treptow-Koepenick"},
                            "Translate": {"1": "English",
                                          "2": "French",
                                          "3": "German",
                                          "4": "Hindi",
                                          "5": "Japanese",
                                          "6": "Mandarin",
                                          "7": "Polish",
                                          "8": "Russian",
                                          "9": "Spanish",
                                          "10": "Swedish"},
                            "Tutor": {"1": "Economics",
                                      "2": "Finance",
                                      "3": "History",
                                      "4": "Law",
                                      "5": "Literature",
                                      "6": "Mathematics",
                                      "7": "Programming Language: Python",
                                      "8": "Programming Language: R",
                                      "9": "Statistics",
                                      "10": "Sciences"}
                         }
    
    # general function for selecting from dictionary    
    def OptionsSelect(self, options, name):
        """
        Function allows for selecting from help options
        
        Returns
        -------
        Selected option.
        """
        index = 0
        indexValidList = []
        print('Select ' + name + ':')
    
        for optionName in options:
            """
            For multiple help requests
            """
            index = index + 1
            indexValidList.extend([options[optionName]])
            print(str(index) + '. ' + options[optionName])
        inputValid = False
        
        while not inputValid:
            """
            Defining response for invalid input
            """
            inputRaw = input(name + ': ')
            inputNo = int(inputRaw) - 1
            
            if inputNo > -1 and inputNo < len(indexValidList):
                selected = indexValidList[inputNo]
                print('Selected ' +  name + ': ' + selected)
                inputValid = True
                break
            else:
                print('Please select a valid ' + name + ' number')
        
        return selected
    
    # select category    
    def CatSelect(self):
        """
        Defines selected category
        
        Returns
        -------
        None.
        
        """
        self.selectCat = self.OptionsSelect(self.Category, self.type)
    
    # select option
    def OptSelect(self):
        """
        Defines selected options
        
        Returns
        -------
        None.
        
        """
        if self.selectCat != "Ride":
            self.catOptions = self.optionsDict[self.selectCat]
            self.selectOption= self.OptionsSelect(self.catOptions, (self.type + " Option"))            
        else:
            self.selectOption = "NA"
    
    # input location
    def LocSelect(self):
        """
        Defines location, if a ride is requested
        
        Returns
        -------
        None.
        
        """
        while True:
            try:
                if self.selectCat == "Ride":
                    self.OptOrg = str(input("Please enter the complete address of your origin: "))
                    self.OrgAdd = geo(str(self.OptOrg) + " Berlin, Deutschland").address #must always be within Berlin state
                    self.OrgCoord = (geo(self.OptOrg).latitude, geo(self.OptOrg).longitude)
                    
                    self.OptDest = str(input("Please enter the complete address of your destination: "))
                    self.DestAdd = geo(str(self.OptDest) + " Berlin, Deutschland").address
                    self.DestCoord = (geo(self.OptDest).latitude, geo(self.OptDest).longitude)            
                
                else: #also enter address for other categories
                    self.OptOrg = str(input("Please enter the complete address of your preferred location: "))
                    self.OrgAdd = geo(str(self.OptOrg) + " Berlin, Deutschland").address #must always be within Berlin state
                    self.OrgCoord = (geo(self.OptOrg).latitude, geo(self.OptOrg).longitude)
                    
                    self.OptDest = "NA"
                    self.DestAdd = "NA"
                    self.DestCoord = "NA"
                    
            except AttributeError:
                    print ("Invalid address. Please enter address within Berlin only.") 
                    continue
            break
   
    # input date    
    def validDate(self):  
        """
        Defines data of request.
        
        Returns
        -------
        None.
        
        """
        while True:
            try:
                self.requestdate = datetime.date(datetime.strptime(input("Enter date for request (YYYY-MM-DD): ") ,'%Y-%m-%d'))
                if self.requestdate < date.today():
                    print("Invalid date. Please enter a future date.")
                    continue
            except ValueError:
                print ("Invalid date. Please enter date in YYYY-MM-DD format.") 
                continue
            break
    
    # input time 
    def validTime(self):   
        """
        Defines time of request.
        
        Returns
        -------
        None.
        
        """
        while True: 
            try:
                self.requesttime = datetime.time(datetime.strptime(input("Enter time for request (HH:MM): "), "%H:%M"))
            except ValueError:
                print ("Invalid time. Please enter date in HH:MM format.") 
                continue
            else: 
                break
    
    # input additional information:
    def AddInfo(self):
        """
        Allows user to put in any additional information
        
        Returns
        -------
        None.
        
        """
        self.info = str(input("Please provide any additional information regarding your request (enter NONE if no further details are needed): "))
    
    def TimeStamp(self):
        """
        Gets the timestamp when request/support is sent
        
        Returns
        -------
        timenow: timestamp.
        
        """
        self.timenow = datetime.now()
    
    # print request details
    def printDetails(self):
        """
        Prints the details of the User's request or support

        Returns
        -------
        selectcat: str
            Category
        OrgAdd: 
            Exact location of the Origin
        DestAdd:
            Exact location of the Desitnation
        requestdate: date
            Date of request or support
        requesttime: time
            Time of request or support            
        info: str
            Additional information            
        Timestamp: time
            Timestamp when request/support is sent
        """

        
        
        if self.selectCat == "Ride":
            print("Thank you! Your", self.type, "has been recorded with the following details:" +
                  "\n Category: ", self.selectCat +
                  #"\n Option: ", self.selectOption +
                  "\n Origin: ", self.OrgAdd +
                  "\n Destination: ", self.DestAdd +
                  "\n Date: ", str(self.requestdate) +
                  "\n Time: ", str(self.requesttime) +
                  "\n Additional Information: ", self.info,
                  "\n Timestamp: ", self.timenow)
        else:
            print("Thank you! Your", self.type, "has been recorded with the following details:" +
                  "\n Category: ", self.selectCat +
                  "\n Option: ", self.selectOption +
                  "\n Location: ", self.OrgAdd +
                  #"\n Destination: ", self.DestAdd +
                  "\n Date: ", str(self.requestdate) +
                  "\n Time: ", str(self.requesttime) +
                  "\n Additional Information: ", self.info,
                  "\n Timestamp: ", self.timenow)
    
    def runAll(self):
        """
        Runs all functions necessary of Class Request

        Returns
        -------
        All objects generated from functions inside

        """
        
        self.CatSelect()
        self.OptSelect()
        self.LocSelect()
        self.validDate()
        self.validTime()
        self.AddInfo()
        self.TimeStamp()
        self.printDetails()
    
    # getters
    def getreqCat(self):
        return self.selectCat
        """
        Returns
        -------
        Selected category.
        
        """    
    def getreqOpt(self):
        return self.selectOption
        """
        Returns
        -------
        Selected option.
        
        """
    def getreqOrg(self):
        return self.OptOrg
        """
        Returns
        -------
        Identified pick-up address.
        
        """ 
    def getreqOrg_add(self):
        return self.OrgAdd
        """
        Returns
        -------
        Identified pick-up location.
        
        """ 
    def getreqOrg_coord(self):
        return self.OrgCoord
        """
        Returns
        -------
        Pick-up coordinates.
        
        """ 
    def getreqDest(self):
        return self.OptDest
        """
        Returns
        -------
        Identified destination.
        
        """ 
    def getreqDest_add(self):
        return self.DestAdd
        """
        Returns
        -------
        Identified destination location.
        
        """ 
    def getreqDest_coord(self):
        return self.DestCoord
        """
        Returns
        -------
        Destination coordinates.
        
        """ 
    def getreqDate(self):
        return self.requestdate
        """
        Returns
        -------
        Date that help is requested.
   
        """      
    def getreqTime(self):
        return self.requesttime
        """
        Returns
        -------
        Time that help is requested.
        
        """ 
    def getreqInfo(self):
        return self.info
        """
        Returns
        -------
        Additional information provided.
        
        """ 
    def getTimestamp(self):
        return self.timenow
        """
        Returns
        -------
        Current time.
        
        """ 

    
