# DTO used to store a single row in the csv file
class PotatoDTO:
    '''
    DTO for potato data from the csv (old dto for saving to memory)
    '''
    def __init__(self, ID, REF_DATE, GEO, DGUID, description, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATED, DECIMALS):
        self.ID = ID
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