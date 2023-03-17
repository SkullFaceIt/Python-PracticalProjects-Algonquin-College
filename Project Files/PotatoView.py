
import PotatoController
from PotatoModel import PotatoDTO


 

class View:
    
    def updateSelected(selectedPotatos):
        newPotatos = []
        for potato in selectedPotatos:
            REF_DATE = input("Old REF_DATE = '" + potato.REF_DATE + "' Enter REF_DATE: ")
            GEO = input("Old GEO = '" + potato.GEO + "' Enter GEO: ")
            DGUID = input("Old DGUID = '" + potato.DGUID + "' Enter DGUID: ")
            description = input("Old description = '" + potato.description + "' Enter description: ")
            UOM = input("Old UOM = '" + potato.UOM + "' Enter UOM: ")
            UOM_ID = input("Old UOM_ID = '" + potato.UOM_ID + "' Enter UOM_ID: ")
            SCALAR_FACTOR = input("Old SCALAR_FACTOR = '" + potato.SCALAR_FACTOR + "' Enter SCALAR_FACTOR: ")
            SCALAR_ID = input("Old SCALAR_ID = '" + potato.SCALAR_ID + "' Enter SCALAR_ID: ")
            VECTOR = input("Old VECTOR = '" + potato.VECTOR + "' Enter VECTOR: ")
            COORDINATE = input("Old COORDINATE = '" + potato.COORDINATE + "' Enter COORDINATE: ")
            VALUE = input("Old VALUE = '" + potato.VALUE + "' Enter VALUE: ")
            STATUS = input("Old STATUS = '" + potato.STATUS + "' Enter STATUS: ")
            SYMBOL = input("Old SYMBOL = '" + potato.SYMBOL + "' Enter SYMBOL: ")
            TERMINATED = input("Old TERMINATED = '" + potato.TERMINATED + "' Enter TERMINATED: ")
            DECIMALS = input("Old DECIMALS = '" + potato.DECIMALS + "' Enter DECIMALS: ")
            newPotatos.append(PotatoDTO(potato.ID, REF_DATE, GEO, DGUID, description, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS))
        return newPotatos
    
    def print(string):
        print(string)
    
    def printMenu():
        print('\nSelect an option below by entering it\'s number:')
        print('0: Exit')
        print('1: Reload the data from the dataset, replacing the in-memory data.')
        print('2: Persist the data from memory to the disk as a comma-separated file, writing to a new file.')
        print('3: Create a new record and store it in the simple data structure in memory.')
        print('4: Select and display either one record, or display multiple records from the in-memory data.')
        print('5: Select and edit a record held in the simple data structure in memory.')
        print('6: Select and delete a record from the simple data structure in memory.')
        print('\nPROGRAM BY SEBASTIEN RAMSAY')
        
        selection = input()
        
        return selection
    
    
    
    def printModel(potatos):

        # Hardcoding the column names into the program as an array
        columnNames = ["ID", "REF_DATE","GEO","DGUID","Area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]

        
        # Itterating through the columnNames array each column name is accessed with "columnName"
        for columnName in columnNames:    
            # Printing the columnName to console and setting end=' ' to prevent the function from printing a new line
            print(columnName, end=' ')


        # Printing a new line
        print()


        # Itterating through the potatos array(Array of DTOS's) each DTO is accessed with "potato"(DTO)
        for potato in potatos:    
            #Printing a row of data from the potato DTO and setting end=' ' to prevent the function from printing a new line
            print(potato.ID, potato.REF_DATE, potato.GEO, potato.DGUID, potato.description, potato.UOM, potato.UOM_ID, potato.SCALAR_FACTOR, potato.SCALAR_ID, potato.VECTOR, potato.COORDINATE, potato.VALUE, potato.STATUS, potato.SYMBOL, potato.TERMINATED, potato.DECIMALS, end=' ')
            # Printing a new line
            print()
    
     
    def selectPotatos():
            selectedPotatos = []
            potatos = PotatoController.getPotatos()
            selection = 0
            
            View.printModel(potatos=potatos)
            print("please select one or many potatos by entering their ID and pressing enter: \nuse space seperated numbers to select a range of \nwhen you are done enter a letter")
            
            
            while selection != -1:
                
                selection = input()
                
                if selection.isalpha():
                    return selectedPotatos
                
                selection = [int(num) for num in selection.split()]
                
                if len(selection) <=1: 
                    for potato in potatos:
                        if potato.ID == int(selection[0]):
                            selectedPotatos.append(potato)
                else:
                    for potato in potatos:
                            if potato.ID >= int(selection[0])and potato.ID <= int(selection[1]):
                                selectedPotatos.append(potato)            
                
                
            return selectedPotatos
        
    def newPotato():
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
        potato = PotatoDTO(PotatoController.getPotatos().__len__(), REF_DATE, GEO, DGUID, description, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS)
        
        return PotatoController.newPotato(potato)
        
        
    
        
