#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Common classes library module.
(sorta like everyday swissarmy knife for the console user)

Evgeni.Antonov@gmail.com 2022"""


import sys
import math
import time
import signal
import logging
import datetime
from iso3166 import countries
from pprint import pprint, pformat




class GenericClass(object):
    """Generic class infrastructure"""
    
    # Default logger settings
    logging_format              = "[%(asctime)s][%(levelname)-8s][%(funcName)s] %(message)s"
    logging_level               = logging.INFO # NOTSET > DEBUG > INFO > WARNING > ERROR > CRITICAL
    
    
    def __init__(self, **kwargs):
        """Provides basic class setup"""
        
        self.logging_level      = GenericClass.logging_level
        self.logging_format     = GenericClass.logging_format
        logging.basicConfig(format=self.logging_format)
        
        for key in kwargs:
            setattr(self, key, kwargs[key])
        
        self.logger             = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        
        
        
    @staticmethod
    def get_timestamp():
        return int(time.time())
        



class BasicCountryInfo(object):
    """Basic country info, based on ISO3166"""
    
    """The folowing is an array holding hotfix data, in case because
    of war or else a new country emerges or an old changes any data
    item. The parent module won't reflect that, so we can quickly
    handle it ourselves using pull requests.
    
    Format: [name, alpha2, alpha3, numeric, apolitical_name]
    where alpha2 and alpha3 must be UPPERCASE."""
    hotfix_country_data         = [
        ["Test Country Name", "@@", "###", 999, "Test Country Name no political"],
        ["Moldova", "MD", "MDA", 498, "Moldova (the Republic of)"]
    ]
    
    
    @staticmethod
    def country_in_hotfixes(country):
        for c in BasicCountryInfo.hotfix_country_data:
            (name, alpha2, alpha3, numeric, apolitical_name) = c
            
            if country.upper() == name.upper() or \
                country.upper() == alpha2.upper() or \
                country.upper() == alpha3.upper() or \
                country == numeric or \
                country.upper() == apolitical_name.upper():
                    return c
        
        return None
    
    
    @staticmethod
    def get(country):
        c                       = BasicCountryInfo.country_in_hotfixes(country)
        
        if c:
            return c
        
        try:
            c                   = countries.get(country)
            l                   = [c.name, c.alpha2, c.alpha3, c.numeric, c.apolitical_name]
            return l
        
        except KeyError as ex:
            raise Exception(f"BasicCountryInfo.get('{country}'): Country not found.")




class SignalHandlers:
    """Generic signal handling methods"""
    
    # Private method
    @staticmethod
    def __sigint_signal_handler(signal, frame):
        """SIGINT signal handler (CTRL-C)
        
        Will intercept and handle CTRL-C press, but will not exit.
        Instead will raise KeyboardInterrupt exception, so the local
        script could deal with the clean-up properly, according to the
        local need."""
        
        print("\n---")
        user_input              = " "
        while user_input is None or len(user_input) < 1 or user_input[0] != "n":
            user_input          = str.lower(input("CTRL-C detected. Quit? (y/n): "))
            user_input          = user_input.strip()
            
            if user_input is not None and len(user_input) > 0 and user_input[0] == "y":
                raise KeyboardInterrupt
    
    
    @staticmethod
    def set_ctrl_c_handler():
        """Set the CTRL-C (SIGINT) handler"""
        signal.signal(signal.SIGINT, SignalHandlers.__sigint_signal_handler)




class UserInterfaceBasics:
    """User interface basic methods"""
    
    @staticmethod
    def make_shell_pause():
        input("Press ENTER to continue...")




class MathTools:
    """Convenient math functions"""
    
    @staticmethod
    def calculate_percentage(args):
        """Calculate percentage
        
        Args:
            'total': int # The total
            'value': int # Value to convert to percentage
        
        Return:
            'percentage': int # Current progress
        """
        
        if args['total'] < 1:
            args['base']        = 0
        
        if 'base' not in args:
            args['base']        = 100/args['total']
        
        args['percentage']      = int(math.ceil(args['value']*args['base']))
        
        if (args['percentage'] > 100):
            args['percentage']  = 100
        
        return args
    
    
    @staticmethod
    def calculate_eta(args):
        """Calculate ETA
        
        Args: {'percentage':int}
        
        Return: {'eta':time} ##, 'eta_formatted':string}
        """
        
        # If this is first invocation, just do the setup and return
        if 'start' not in args:
            args['start']       = GenericClass.get_timestamp() # Seconds
            args['eta']         = 'N/A'
            return args
        
        now                     = GenericClass.get_timestamp()
        time_elapsed            = now - args['start']
        
        if (args['percentage'] < 1):
            return args
        
        eta_seconds             = (time_elapsed / args['percentage']) * (100 - args['percentage'])
        args['eta']             = str(datetime.timedelta(seconds=eta_seconds))
        
        return args




class SimpleCSVReader(GenericClass):
    """Simple CSV reader class"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content            = self.read()
        
        if not hasattr(self, "read_headers"):
            self.read_headers   = True
        
        if not hasattr(self, "filename"):
            raise Exception("No filename given to the SimpleCSVReader.")
    
    
    def read(self):
        self.logger.info(f"Reading CSV: {self.filename} ...")
        content                 = {"header":[], "data":[]}
        
        with open(self.filename, "r", encoding="utf-8") as f:
            csvreader           = csv.reader(f)
            
            if self.read_headers:
                content["header"] = next(csvreader)
        
            for row in csvreader:
                content["data"].append(row)
        
        return content




# For later implementation. Maybe run unit tests.
if __name__ == '__main__':
    pass
