import csv
from PotatoModel import PotatoDTO
import os
from MongoDBConnection import MongoDBConnection

# Start the database instance
dbConnection = MongoDBConnection.get_instance()

# Making a new array to store dbPotato's
dbPotatos = []
                
# Hardcoding the column names into the program as an array
columnNames = ["ID", "REF_DATE","GEO","DGUID","Area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]


# deletes the selectd Potato from the potatos list
def deleteSelected(selectedDBPotatos):
    """delete selectedPotatos from the database

    Args:
        selectedDBPotatos (Array<dbPotato>): potatos to be deleted
    """
    for potato in selectedDBPotatos:
        dbConnection.db.delete_one(potato)
    
    dbPotatos = list(dbConnection.db.find({}))
    numberOfPotatos = 0
    
    for potato in dbPotatos:
        dbConnection.db.delete_one(potato)
    
    for potato in dbPotatos:
        potato["_id"] = numberOfPotatos
        numberOfPotatos += 1
        dbConnection.db.insert_one(potato)
        
#updates the selected potatos
def updatePotatos(updatedDBPotatos):
    """replace database potatos with updatedDBPotatos

    Args:
        updatedDBPotatos (Array<dbPotatos>): dbPotatos that have been updated in the View Class
    """

    for potato in updatedDBPotatos:
        #find the id to update by the updated potatos id and update the potato with the new values
        filter = {"_id": potato["_id"]}
        newPotato = {"$set": potato}
        dbConnection.db.update_one(filter, newPotato)
    
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
        

        dbPotatos = list(dbConnection.db.find({}))
        
        # write the data, one row per potato in the list
        for potato in dbPotatos:
            row_data = [str(potato["_id"]), potato["GEO"], potato["DGUID"],\
                potato["area, production and farm value of potatoes"], potato["UOM"], str(potato["UOM_ID"]),\
                    str(potato["SCALAR_FACTOR"]), potato["SCALAR_ID"], potato["VECTOR"],\
                        str(potato["COORDINATE"]), str(potato["VALUE"]), potato["STATUS"],\
                            potato["SYMBOL"], potato["TERMINATED"], str(potato["DECIMALS"])]
            #write a row of data comma seperated
            file.write(','.join(row_data) + '\n')
    return ("New File Named " + fileName + "\n" + os.getcwd() + "\\" + fileName)
            
# Add a potato to the database
def newPotato(dbPotato):
    """Add the potato to the potato array

    Args:
        potato (dbPotato): a single database potato to be added to the database

    Returns:
        String: record stored in database
    """

    # Set the id for the new potato
    newID = dbConnection.db.estimated_document_count()
    dbPotato["_id"] = newID
    dbConnection.db.insert_one(dbPotato)
    
    return ("Your record has been stored in the database")
        
# Get the list of potatos
def getPotatos():
    """get the current array of potatos from the database

    Returns:
        Array<dbPotato>: current potatos in database
    """
    dbPotatos = list(dbConnection.db.find({}))
    return dbPotatos
    
# replace in memory data with new data read from the csv file 
def loadData():
    """Load data from the csv file using the csv API library, clears the database and adds the new data

    Returns:
        String: data loaded or data failed to load
    """
    
    dbConnection.db.delete_many({})
    dbPotatos.clear()

    # Try statement for exeption handling
    try: 

            # Reading the CSV file from the project directory.
            # irst arg is file name, second arg indicates to perform a read operation.
            # "as" indicates the name to give this file you are opening
        with open ('Project Files/32100358.csv', 'r') as csv_file:

            # Make a new variable called csv_reader that 
            # uses the csv import to use the reader function
            # passing through the file we just opened called "csv_file"
            csv_reader = csv.reader(csv_file)

            # Skipping the first row in the csv file so they do not get read when itterating through the file
            next(csv_reader)
                
            numberOfPotatos = 0
            try:
                # Itterating through the lines in the csv file called csv_reader, each line is accessed with "line"
                for line in csv_reader:
                    if numberOfPotatos < 100:
                        line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14]
                        dbPotato = {"_id": numberOfPotatos,"REF_DATE": line[0],"GEO": line[1],"DGUID": line[2], "area, production and farm value of potatoes": line[3],"UOM": line[4],"UOM_ID": line[5],"SCALAR_FACTOR": line[6],"SCALAR_ID": line[7],"VECTOR": line[8],"COORDINATE": line[9],"VALUE": line[10],"STATUS": line[11],"SYMBOL": line[12],"TERMINATED": line[13],"DECIMALS": line[14]}
                        dbPotatos.append(dbPotato)
                        numberOfPotatos += 1
                             
                dbConnection.db.insert_many(dbPotatos) 
                
            except Exception as e:
                return("An exception occurred: ", e)
        return ("Reloaded data into database")      
    # Except statment will catch any exceptions that take place
    except FileNotFoundError:
        #PotatoView.print("FILE NOT FOUND!")
        return ("FILE NOT FOUND")
        
         
    
    
        
