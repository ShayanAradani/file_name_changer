import datetime
import os

# Also can input other path into it
name_list=os.listdir()

# Also can input other formats into it
formats =[".png"]

for file_name in name_list:
    if file_name[-4:].lower() in formats :
        date=os.path.getmtime(file_name) # Not human readable date
        hdate=list(str(datetime.datetime.fromtimestamp( date ) ) ) # Human readable date
        for i in range(len(hdate)) :
            if hdate[i] in ['-' , ':' , ' ']:
                hdate[i] ="_"
        final_file_name=""

        for i in hdate:
            final_file_name+=i

        # The new name now can set
        # Next line is vary customizable
        final_file_name+="___"+file_name[0:11]+".PNG"
        os.rename(file_name, final_file_name)
        print(file_name + "'s name changed to : \n" + final_file_name +"\n")