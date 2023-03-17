import pytest
import PotatoController
from PotatoModel import PotatoDTO
from MongoDBConnection import MongoDBConnection

dbConnection = MongoDBConnection.get_instance()

nextID = dbConnection.db.estimated_document_count()

columnNames = [nextID, "REF_DATE","GEO","DGUID","area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR",\
    "SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]

def test_newUserAdded():
    """Test adding a user to the database. This test makes a new potato and checks if the potato has the requested atributes.
        The test data is removed from the database after the test is complete.
    """
    
    testDBPotato = {"_id": nextID, "REF_DATE": "REF_DATE","GEO": "GEO","DGUID": "DGUID",\
            "area, production and farm value of potatoes": "area, production and farm value of potatoes","UOM": "UOM",\
                "UOM_ID": "UOM_ID","SCALAR_FACTOR": "SCALAR_FACTOR","SCALAR_ID": "SCALAR_ID",\
                    "VECTOR": "VECTOR","COORDINATE": "COORDINATE","VALUE": "VALUE","STATUS": "STATUS",\
                        "SYMBOL": "SYMBOL","TERMINATED": "TERMINATED","DECIMALS": "DECIMALS"}
    
    PotatoController.newPotato(testDBPotato)
    potato = dbConnection.db.find_one({"_id": nextID})
    
    assert int(potato["_id"]) == int(columnNames[0]) \
       and potato["REF_DATE"] == columnNames[1] \
       and potato["GEO"] == columnNames[2] \
       and potato["DGUID"] == columnNames[3] \
       and potato["area, production and farm value of potatoes"] == columnNames[4] \
       and potato["UOM"] == columnNames[5] \
       and potato["UOM_ID"] == columnNames[6] \
       and potato["SCALAR_FACTOR"] == columnNames[7] \
       and potato["SCALAR_ID"] == columnNames[8] \
       and potato["VECTOR"] == columnNames[9] \
       and potato["COORDINATE"] == columnNames[10] \
       and potato["VALUE"] == columnNames[11] \
       and potato["STATUS"] == columnNames[12] \
       and potato["SYMBOL"] == columnNames[13] \
       and potato["TERMINATED"] == columnNames[14] \
       and potato["DECIMALS"] == columnNames[15], \
       f"Expected: {columnNames}, but got: {potato.values()}"
       
    dbConnection.db.delete_one(testDBPotato)

