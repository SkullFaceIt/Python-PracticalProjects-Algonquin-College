import pytest
import PotatoController
from PotatoModel import PotatoDTO

columnNames = ["ID", "REF_DATE","GEO","DGUID","Area, production and farm value of potatoes","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]


def test_newUserAdded():
    """Test adding a user to memory. This test makes a new potato and checks if the potato has the requested atributes.
    """
    testPotato = PotatoDTO("ID", "REF_DATE", "GEO", "DGUID", "Area, production and farm value of potatoes", "UOM", "UOM_ID", "SCALAR_FACTOR", "SCALAR_ID", "VECTOR", "COORDINATE", "VALUE", "STATUS", "SYMBOL", "TERMINATED", "DECIMALS")
    PotatoController.newPotato(testPotato)
    
    potatos = PotatoController.getPotatos()
    potato = potatos[0]
    
    assert potato.ID == columnNames[0]\
        and potato.REF_DATE == columnNames[1]\
            and potato.GEO == columnNames[2]\
                and potato.DGUID == columnNames[3]\
                    and potato.description == columnNames[4]\
                        and potato.UOM == columnNames[5]\
                            and potato.UOM_ID == columnNames[6]\
                                and potato.SCALAR_FACTOR == columnNames[7]\
                                    and potato.SCALAR_ID == columnNames[8]\
                                        and potato.VECTOR == columnNames[9]\
                                            and potato.COORDINATE == columnNames[10]\
                                                and potato.VALUE == columnNames[11]\
                                                    and potato.STATUS == columnNames[12]\
                                                        and potato.SYMBOL == columnNames[13]\
                                                            and potato.TERMINATED == columnNames[14]\
                                                                and potato.DECIMALS == columnNames[15],\
        f"Expected {columnNames[1]}, {columnNames[2]}, {columnNames[3]}, {columnNames[4]}, {columnNames[5]}, {columnNames[6]}, {columnNames[7]}, {columnNames[8]}, {columnNames[9]}, {columnNames[10]}, {columnNames[11]}, {columnNames[12]}, {columnNames[13]}, {columnNames[14]}, {columnNames[15]}, {columnNames[16]},\
            but got {potato.ID}, {potato.REF_DATE}, {potato.GEO}, {potato.DGUID}, {potato.description}, {potato.UOM}, {potato.UOM_ID}, {potato.SCALAR_FACTOR}, {potato.SCALAR_ID}, {potato.VECTOR}, {potato.COORDINATE}, {potato.VALUE}, {potato.STATUS}, {potato.SYMBOL}, {potato.TERMINATED}, {potato.DECIMALS}."

                                            