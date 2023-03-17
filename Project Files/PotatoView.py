
import PotatoController
from PotatoModel import PotatoDTO
from MongoDBConnection import MongoDBConnection

# get instance of db connection
dbConnection = MongoDBConnection.get_instance()


 

class View:
    
    def updateSelected(selectedPotatos):
        """_summary_

        Args:
            selectedPotatos (dbPotatos): holds an array of dbPotatos selected by the user.

        Returns:
            dbPotato: the selected potatos after being updated by the user.
        """
        updatedPotatos = []
        for potato in selectedPotatos:
            REF_DATE = input("Old REF_DATE = '" + potato["REF_DATE"] + "' Enter REF_DATE: ")
            GEO = input("Old GEO = '" + potato["GEO"] + "' Enter GEO: ")
            DGUID = input("Old DGUID = '" + potato["DGUID"] + "' Enter DGUID: ")
            description = input("Old description = '" + potato["area, production and farm value of potatoes"] + "' Enter description: ")
            UOM = input("Old UOM = '" + potato["UOM"] + "' Enter UOM: ")
            UOM_ID = input("Old UOM_ID = '" + potato["UOM_ID"] + "' Enter UOM_ID: ")
            SCALAR_FACTOR = input("Old SCALAR_FACTOR = '" + potato["SCALAR_FACTOR"] + "' Enter SCALAR_FACTOR: ")
            SCALAR_ID = input("Old SCALAR_ID = '" + potato["SCALAR_ID"] + "' Enter SCALAR_ID: ")
            VECTOR = input("Old VECTOR = '" + potato["VECTOR"] + "' Enter VECTOR: ")
            COORDINATE = input("Old COORDINATE = '" + potato["COORDINATE"] + "' Enter COORDINATE: ")
            VALUE = input("Old VALUE = '" + potato["VALUE"] + "' Enter VALUE: ")
            STATUS = input("Old STATUS = '" + potato["STATUS"] + "' Enter STATUS: ")
            SYMBOL = input("Old SYMBOL = '" + potato["SYMBOL"] + "' Enter SYMBOL: ")
            TERMINATED = input("Old TERMINATED = '" + potato["TERMINATED"] + "' Enter TERMINATED: ")
            DECIMALS = input("Old DECIMALS = '" + potato["DECIMALS"] + "' Enter DECIMALS: ")
            
            dbPotato = {"_id": potato["_id"],"REF_DATE": REF_DATE,"GEO": GEO,"DGUID": DGUID,\
            "area, production and farm value of potatoes": description,"UOM": UOM,\
                "UOM_ID": UOM_ID,"SCALAR_FACTOR": SCALAR_FACTOR,"SCALAR_ID": SCALAR_ID,\
                    "VECTOR": VECTOR,"COORDINATE": COORDINATE,"VALUE": VALUE,"STATUS": STATUS,\
                        "SYMBOL": SYMBOL,"TERMINATED": TERMINATED,"DECIMALS": DECIMALS}
            
            updatedPotatos.append(dbPotato)
        
        View.printModel(updatedPotatos)
        
        return updatedPotatos
    
    def print(string):
        print(string)
    
    def printMenu():
        """prints the main menu and takes user input

        Returns:
            selection(int): user input
        """
        print('\nSelect an option below by entering it\'s number:')
        print('0: Exit')
        print('1: Reload the data from the dataset, replacing the data in the database.')
        print('2: Persist the data from the database to the disk as a comma-separated file, writing to a new file.')
        print('3: Create a new record and store it in the simple data structure in the database.')
        print('4: Select and display either one record, or display multiple records from the database.')
        print('5: Select and edit a record held in the simple data structure in the database.')
        print('6: Select and delete a record from the simple data structure in the database.')
        print('\nPROGRAM BY SEBASTIEN RAMSAY')
        
        selection = input()
        
        return selection
    
    
    
    def printModel(dbPotatos):
        """prints the array of potatos

        Args:
            dbPotatos (dbPotato): an array of dbPotatos to be printed
        """
        # Hardcoding the column names into the program as an array
        columnNames = ["ID", "REF_DATE","GEO","DGUID","Area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]

        
        # Itterating through the columnNames array each column name is accessed with "columnName"
        for columnName in columnNames:    
            # Printing the columnName to console and setting end=' ' to prevent the function from printing a new line
            print(columnName, end=' ')


        # Printing a new line
        print()


        # Itterating through the potatos array(Array of DTOS's) each DTO is accessed with "potato"(DTO)
        for potato in dbPotatos:    
            #Printing a row of data from the potato DTO and setting end=' ' to prevent the function from printing a new line
            print(str(potato["_id"]), potato["GEO"], potato["DGUID"],\
                potato["area, production and farm value of potatoes"], potato["UOM"], str(potato["UOM_ID"]),\
                    str(potato["SCALAR_FACTOR"]), potato["SCALAR_ID"], potato["VECTOR"],\
                        str(potato["COORDINATE"]), str(potato["VALUE"]), potato["STATUS"],\
                            potato["SYMBOL"], potato["TERMINATED"], str(potato["DECIMALS"]), end=' ')
            # Printing a new line
            print()
    
     
    def selectPotatos():
        """prints the potatos in the database and gives two options for selecting potatos.
        select one or many potatos by entering their ID and pressing enter, use space seperated numbers to select a range of potatos.

        Returns:
            selectedPotatos(dbPotatos): an array of dbPotatos selected by the user.
        """
        
        selectedPotatos = []
        # populate the dbPotatos list from the database
        dbPotatos = PotatoController.getPotatos()
        selection = 0
            
        View.printModel(dbPotatos)
        print("please select one or many potatos by entering their ID and pressing enter: \nuse space seperated numbers to select a range of potatos\nwhen you are done enter a letter")
            
            
        # Endless loop
        while selection != -1:
            
            # Take user input
            selection = input()
                
            # return if selection is a letter
            if selection.isalpha():
                return selectedPotatos
                
            # Split the input into an array of ids
            selection = [int(num) for num in selection.split()]
                
            # if the user is not selecting a range of ids
            if len(selection) <=1: 
                for dbPotato in dbPotatos:
                    if int(dbPotato["_id"]) == int(selection[0]):
                        selectedPotatos.append(dbPotato)
            # The user is selecting a range of ids meaning selection will have a min value and a max value in unknown order
            else:
                if int(selection[0]) < int(selection[1]):
                    for dbPotato in dbPotatos:
                        if int(dbPotato["_id"]) >= int(selection[0])and int(dbPotato["_id"]) <= int(selection[1]):
                            selectedPotatos.append(dbPotato)
                if int(selection[1]) < int(selection[0]):
                    for dbPotato in reversed(dbPotatos):
                        if int(dbPotato["_id"]) >= int(selection[1])and int(dbPotato["_id"]) <= int(selection[0]):
                            selectedPotatos.append(dbPotato)
                if int(selection[1]) == int(selection[0]):
                    for dbPotato in dbPotatos:
                        if int(dbPotato["_id"]) == int(selection[1])and int(dbPotato["_id"]) == int(selection[0]):
                            selectedPotatos.append(dbPotato)
        
    def newPotato():
        """take user input to make a new dbPotato

        Returns:
            String: the return method calls newPotato in the PotatoController which return a string "Your record has been stored in the database"
        """
        REF_DATE = input("Enter REF_DATE: ")
        GEO = input("Enter GEO: ")
        DGUID = input("Enter DGUID: ")
        description = input("Enter description: ")
        UOM = input("Enter UOM: ")
        UOM_ID = input("Enter UOM_ID: ")
        SCALAR_FACTOR = input("Enter SCALAR_FACTOR: ")
        SCALAR_ID = input("Enter SCALAR_ID: ")
        VECTOR = input("Enter VECTOR: ")
        COORDINATE = input("Enter COORDINATE: ")
        VALUE = input("Enter VALUE: ")
        STATUS = input("Enter STATUS: ")
        SYMBOL = input("Enter SYMBOL: ")
        TERMINATED = input("Enter TERMINATED: ")
        DECIMALS = input("Enter DECIMALS: ")
        dbPotato = {"_id": 0,"REF_DATE": REF_DATE,"GEO": GEO,"DGUID": DGUID,\
            "area, production and farm value of potatoes": description,"UOM": UOM,\
                "UOM_ID": UOM_ID,"SCALAR_FACTOR": SCALAR_FACTOR,"SCALAR_ID": SCALAR_ID,\
                    "VECTOR": VECTOR,"COORDINATE": COORDINATE,"VALUE": VALUE,"STATUS": STATUS,\
                        "SYMBOL": SYMBOL,"TERMINATED": TERMINATED,"DECIMALS": DECIMALS}
        return PotatoController.newPotato(dbPotato)
        
        
    
        
