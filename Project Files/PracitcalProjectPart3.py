from PotatoView import View
import PotatoController


def exit():
    """exit the program
    """
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_1():
    """Reload data from csv file into the database after clearing the database
    """
    View.print(PotatoController.loadData())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')

def case_2():
    """Write data from the database to a txt file
    """
    fileName = 'PotatoInfo.txt'
    View.print(PotatoController.writePotatosToFile(fileName=fileName))
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_3():
    """Make a new dbPotato
    """
    View.print(View.newPotato())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
       
def case_4():
    """Select Potatos and print them to console
    """
    View.printModel(View.selectPotatos())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_5():
    """Select Potatos and update them in the database
    """
    PotatoController.updatePotatos(View.updateSelected(View.selectPotatos()))
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_6():
    """Select Potatos and delete them from the database
    """
    PotatoController.deleteSelected(View.selectPotatos())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')

def case_default():
    """The users input is invalid
    """
    View.print("Invalid choice")
    View.print('PROGRAM BY SEBASTIEN RAMSAY')

switch = {
    0: exit,
    1: case_1,
    2: case_2,
    3: case_3,
    4: case_4,
    5: case_5,
    6: case_6
}

case = 10
while case != 0:
    try:
        case = int(View.printMenu())
        switch.get(case, case_default)()
    except ValueError:
        case_default()
    except Exception as e:
        print(e)
        
        