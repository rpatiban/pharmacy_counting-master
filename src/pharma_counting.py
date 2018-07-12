#!C:/Program Files/Python36/python.exe

# #####################################################################################
# Author : Raghu Patibandla
# Date   : July 7th 2018
# ====================================================================================
# Program to generate a list of all drugs, number of unique providers and the total cost
#       by processing the input dataset.
# input: cleaned and simplified versoin of dataset that was obtained from the CMS  
# Constraint: Output should be sorted in desc. order by total cost, drug name
# #####################################################################################

import sys

# Dictionary for List of Drugs and total cost
dict_Drug_Cost= dict()

# Dictionary for List of Drugs and unique prescribers
dict_Drug_Pres = dict()

# Tuple for final dump and output
tpl_Drugs = ();  


# ============= Main flow Starts Here ==========================
# Main flow
def main_func() :

    #Getting starting time
    current_time = datetime.datetime.now()
    print(current_time)

    #if (len(sys.argv) != 3) :
    #    print('ERROR: not enough parameters')
    #    exit()
    #else :
    #    # Assigning parameters to appropriate variables
    #    # in case of parameters sequence change - please change it here
    #    input_file = sys.argv[1]
    #    output_file = sys.argv[2]

    try :
        #inact_file = r"../input/inactivity_period.txt"
        #input_file = r"../input/log_test1.csv"

        with open(input_file,'r') as pharmaLog :
            for logLine in pharmaLog:
                rowIP = logLine['ip']


    #Getting Ending time
    current_time = datetime.datetime.now()
    print(current_time)

# ============= Main flow Ends Here ==========================

if __name__ == '__main__':
    main_func()
