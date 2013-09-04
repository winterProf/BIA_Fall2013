import re

def parseemail(str):
    """ returns a dictionary with 'user','domain','tld' """
    """ ex: {'user':'wmason','domain':'stevens','tld':'edu'} """
    """ or empty dictionary if not valid """
