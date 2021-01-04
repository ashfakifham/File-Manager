import os
import time
"""
Helper function to check if folder path available for the month and year
"""
def dir_gen(folder, extension, datefolder):
    if not os.path.exists(folder + '/' + extension + datefolder):
        os.makedirs(folder + '/' + extension + datefolder)
        time.sleep(3)
    return print("Created path Successfully")



