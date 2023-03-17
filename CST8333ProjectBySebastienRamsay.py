import csv

# DTO used to store a single row in the csv file
class PotatoDTO:
    '''
    DTO for potato data from the csv
    '''
    def __init__(self, REF_DATE, GEO, DGUID, description, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS):
        self.REF_DATE = REF_DATE
        self.GEO = GEO
        self.DGUID = DGUID
        self.description = description
        self.UOM = UOM
        self.UOM_ID = UOM_ID
        self.SCALAR_FACTOR = SCALAR_FACTOR
        self.SCALAR_ID = SCALAR_ID
        self.VECTOR = VECTOR
        self.COORDINATE = COORDINATE
        self.VALUE = VALUE
        self.STATUS = STATUS
        self.SYMBOL = SYMBOL
        self.TERMINATED = TERMINATED
        self.DECIMALS = DECIMALS

# Try statement for exeption handling
try: 

    # Reading the CSV file from the project directory. First arg is file name, second arg indicates to perform a read operation. "as" indicates the name to give this file you are opening
    with open ('32100358.csv', 'r') as csv_file:

        # Make a new variable called csv_reader that uses the csv import to use the reader function passing through the file we just opened called "csv_file"
        csv_reader = csv.reader(csv_file)

        # Skipping the first row in the csv file so they do not get read when itterating through the file
        next(csv_reader)

        # Hardcoding the column names into the program as an array
        columnNames = ["REF_DATE","GEO","DGUID","Area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]
        
        # Making a new array to store DTO's
        potatos = []

        # Itterating through the lines in the csv file called csv_reader, each line is accessed with "line"
        for line in csv_reader:
            # Make a new variable called "potato" and set it to our DTO "PotatoDTO" and populate the DTO with the information gathered from our current row "Line"
            potato = PotatoDTO(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12], line[13], line[14])
            # Adding the current potato object(DTO) to the potatos array(Array of DTOS's)
            potatos.append(potato)

    

    # Itterating through the columnNames array each column name is accessed with "columnName"
    for columnName in columnNames:    
        # Printing the columnName to console and setting end=' ' to prevent the function from printing a new line
        print(columnName, end=' ')


    # Printing a new line
    print()


    # Itterating through the potatos array(Array of DTOS's) each DTO is accessed with "potato"(DTO)
    for potato in potatos:    
        #Printing a row of data from the potato DTO and setting end=' ' to prevent the function from printing a new line
        print(potato.REF_DATE, potato.GEO, potato.DGUID, potato.description, potato.UOM, potato.UOM_ID, potato.SCALAR_FACTOR, potato.SCALAR_ID, potato.VECTOR, potato.COORDINATE, potato.VALUE, potato.STATUS, potato.SYMBOL, potato.TERMINATED, potato.DECIMALS, end=' ')
        # Printing a new line
        print()

# Except statment will catch any exceptions that take place
except:
    print("FILE NOT FOUND!")

print("PROGRAM BY: Sebastien Ramsay")
