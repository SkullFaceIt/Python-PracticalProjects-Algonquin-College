import csv
from PotatoModel import PotatoDTO
import os



# Making a new array to store DTO's
potatos = []
                
# Hardcoding the column names into the program as an array
columnNames = ["ID", "REF_DATE","GEO","DGUID","Area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]


# deletes the selectd Potato from the potatos list
def deleteSelected(selectedPotatos):
    """delete selectedPotatos from potatos array

    Args:
        selectedPotatos (Array<potatoDTO>): potatos to be deleted
    """
    for potato in selectedPotatos:
        potatos.remove(potato)
        
#updates the selected potato by
def updatePotatos(updatedPotatos):
    """replace in memory potatos with updatedPotatos

    Args:
        updatedPotatos (Array<potatoDTO>): potatos that have been updated in the View Class
    """
    for potato in updatedPotatos:
        #remove the old potato
        potatos.pop(potato.ID)
        #add the new one
        potatos.append(potato)
    
# Write a new file
def writePotatosToFile(fileName):
    """Write a list of potatoes to a TXT file.
    
    Arguments:
        fileName (str): The name of the file to be created.
    
    Returns:
        str: A message indicating the name of the file and its location.
    """
    # Open a new file called file
    with open(fileName, 'w') as file:
        # write the header row with the column names
        file.write(','.join(columnNames) + '\n')
        
        # write the data, one row per potato in the list
        for potato in potatos:
            row_data = [potato.REF_DATE, potato.GEO, potato.DGUID,\
                potato.description, potato.UOM, str(potato.UOM_ID),\
                    str(potato.SCALAR_FACTOR), potato.SCALAR_ID, potato.VECTOR,\
                        str(potato.COORDINATE), str(potato.VALUE), potato.STATUS,\
                            potato.SYMBOL, potato.TERMINATED, str(potato.DECIMALS)]
            #write a row of data comma seperated
            file.write(','.join(row_data) + '\n')
    return ("New File Named " + fileName + "\n" + os.getcwd() + "\\" + fileName)
            
# Add a potato to the list
def newPotato(potato):
    """Add the potato to the potato array

    Args:
        potato (potatoDTO): a single potatoDTO to be added to memory

    Returns:
        String: record stored in memory
    """
    potatos.append(potato)
    
    return ("Your record has been stored in memory")
        
# Get the list of potatos
def getPotatos():
    """get the current array of potatos

    Returns:
        Array<potatoDTO>: current potatos in memory
    """
    return potatos
    
# replace in memory data with new data read from the csv file 
def loadData():
    """Load data from the csv file using the csv API library

    Returns:
        String: data loaded or data failed to load
    """
    #clear in memory data
    potatos.clear()

    # Try statement for exeption handling
    try: 

            # Reading the CSV file from the project directory.
            # irst arg is file name, second arg indicates to perform a read operation.
            # "as" indicates the name to give this file you are opening
        with open ('32100358.csv', 'r') as csv_file:

            # Make a new variable called csv_reader that 
            # uses the csv import to use the reader function
            # passing through the file we just opened called "csv_file"
            csv_reader = csv.reader(csv_file)

            # Skipping the first row in the csv file so they do not get read when itterating through the file
            next(csv_reader)
                
            numberOfPotatos = 0

            # Itterating through the lines in the csv file called csv_reader, each line is accessed with "line"
            for line in csv_reader:
                if numberOfPotatos < 100:
                    # Make a new variable called "potato" 
                    # and set it to our DTO "PotatoDTO" 
                    # and populate the DTO with the information gathered from our current row "Line"
                    potato = PotatoDTO(numberOfPotatos, line[0], line[1], line[2], line[3], line[4],\
                        line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
                    
                    # Adding the current potato object(DTO) to the potatos array(Array of DTOS's)
                    potatos.append(potato)
                             
                    numberOfPotatos += 1       
        return ("Reloaded data into memory")        
    # Except statment will catch any exceptions that take place
    except FileNotFoundError:
        #PotatoView.print("FILE NOT FOUND!")
        return ("FILE NOT FOUND")
        
         
    
    
        
