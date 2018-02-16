import random                                                                               # Import modules random, datetime and time.
import datetime
import time

try:                                                                                        # Ask user for directory of file.
    Path = (input("Enter file directory, use '' around text E.g. 'C:\Desktop'   :  "))
    
except SyntaxError:                                                                         # Exception if user did no include apostrophes '' around typed text.
    print("You did not include the ' ' around the text")

try:
    Save_File = str(input("Save As(E.g. 'NewFile'): "))                                     # Ask user for what name would they like to use the save the file as.

except SyntaxError:
     print("You did not include the ' ' around the text")                                   # Exception if user did no include apostrophes '' around typed text.

try:
    Dummy_File = open(Path+'\\'+str(Save_File)+'.txt','a')                                  # Opening file to be written as Dummy_File.

except NameError:
    
    print("Path not properly typed as above")                                               # Exception if user defined path is incorrectly typed.                                            

except IOError:
    print("Please ensure the file is not open")                                             # File is still open and being used by other program. Ask user to close file.                           


Time_Stamp = time.localtime(time.time())                                                    # The local timestamp with date and hours.

Dummy_File.write("Date(Y-M-D)"+'\t'+"Time(h:m:s)")                                          # Write header of Date and Time on specified file

Dummy_File.write('\n'+str(Time_Stamp[0])+"-"+str(Time_Stamp[1])+"-"+str(Time_Stamp[2]))     # Write Date on a new line split by the delimiter "-" on a new line

Dummy_File.write('\t'+str(Time_Stamp[3])+":"+str(Time_Stamp[4])+":"+str(Time_Stamp[5]))     # Write Time on same line as Date separated by a tab 

Dummy_File.write('\n')                                                                      # Write new line


Dummy_File.write('\n')                                                                      # Write new line

n=1                                                                                         # New variable n
Key_List = []                                                                               # Create new list
Dictionary = {}                                                                             # Create new dictionary

while n != 33:                                                                              # While loop that iterates 32 times(i.e. 32 clusters)
    
    for i in range(1,17):                                                                   # For loop for each cluster iterating 16 times(i.e.16 sensors)
        Key_List.append(i)                                                                  # Appending each sensor id to a list

    for j in range(0,16):                                                                   # For loop for each cluster iterating 16 times(i.e.16 sensors)                                                              
        
        Dictionary[str(Key_List[j])] = round(random.random(),1)                             # Appending a key with corresponding value of random number rounded to a decimal of 1

    Dummy_File.write(str(Dictionary))                                                       # Write Dictionary on Dummy_File for each cluster
    Dummy_File.write('\n')                                                                  # Write a new line

    n += 1                                                                                  # Move to new cluster to repeat the while loop

Dummy_File.write('\n')                                                                      # Write a new line
Dummy_File.close()                                                                          # Close Dummy_File

time.sleep(2)                                                                               # Tell python to wait for 2 second
        
Input_File = open(Path+'\\'+str(Save_File)+'.txt','r')                                      # Open the file generated above this time for reading
FileString = Input_File.readlines()                                                         # Read all lines of the file as one long list

Clusters =[]                                                                                # Crate a new list called Clusters

for j in range(0,32):                                                                       # Iterate for each cluster

    FileString[j+3].strip("{")                                                              # Strip the "{" from Filestring[j+3]from
    FileString[j+3].split()                                                                 # Get rid of whitespace
    Clusters.append(FileString[j+3].strip("}"))                                             # Append stipped item to empty list Clusters

ErrorLog = open(Path+"\\"+"Error_Log.txt",'a')                                              # Create error log to record defective sensors 
ErrorLog.write("Date(Y-M-D)"+'\t'+"Time(h:m:s)")                                            # Write header of Date and Time on specified file
ErrorLog.write("\n")                                                                        # Write a new line  

ErrorLog.write(FileString[1])                                                               # Write Date and Time on ErrorLog file

ErrorLog.write('\n')                                                                        # Write a new line


def Error_Check(DataSet):                                                                   # New Function for checking error which takes one arg DataSet

    '''Function that determines which sensor from which cluster is defective'''

    k=0                                                                                     # Initialise iterator k

    while k<32:                                                                             # While loop for each cluster

        if "err" in DataSet[k]:                                                             # Check for keyword 'err' in string DataSet[k]
            
            print("Defective Sensor is in cluster: "+str(k+1))                              # Return which cluster has a defective sensor

            DefClust = DataSet[k]                                                           # Define DefClust as a cluster with defective sensor 

            ErrPos = DefClust.rfind(": 'err',")                                             # Search index of ": 'err'," in string and assign it to variable ErrPos

            DefSensor = int((DefClust[ErrPos-3:ErrPos]).strip("'"))                         # Slice the string from three indices back to ErrPos, This is the sensor ID

            print('Defective Sensor in cluster:'+str(k+1)+' is sensor:' +str(DefSensor))    # Return the defective sensor and from which cluster it belongs

            ErrorLog.write("Pipe section: "+str(k+1)+"     Defective Sensor: "+str(DefSensor)+"\n")   # Write the defective sensor and cluster on ErrorLog file
            

        k+=1                                                                                # Move to new cluster to repeat while loop 

    try:                                                                
        return DefClust                                                                     # Return DefClust from function Error_Check
    
    except UnboundLocalError:                                                               # If there is no 'err' found data file provided, this will make exception 

        print("No defective sensor deteced yet")
        print("Please modify sensor readings in saved file "+Path+'\\'+str(Save_File)+'.txt'+"\nwith 'err' for testing")    # Ask user to edit the generated file
    
Error_Check(Clusters)                                                                       # Call the function Error_Check and pass it the list Clusters created above

ErrorLog.write('\n')                                                                        # Move to next line on ErrorLog file


Input_File.close()                                                                          # Close Input_File
ErrorLog.close()                                                                            # Close ErrorLog file










 


