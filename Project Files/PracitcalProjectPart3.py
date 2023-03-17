from PotatoView import View
import PotatoController


def exit():
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_1():
    View.print(PotatoController.loadData())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')

def case_2():
    fileName = 'PotatoInfo.txt'
    View.print(PotatoController.writePotatosToFile(fileName=fileName))
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_3():
    View.print(View.newPotato())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
       
def case_4():
    View.printModel(View.selectPotatos())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_5():
    PotatoController.updatePotatos(View.updateSelected(View.selectPotatos()))
    View.print('PROGRAM BY SEBASTIEN RAMSAY')
        
def case_6():
    PotatoController.deleteSelected(View.selectPotatos())
    View.print('PROGRAM BY SEBASTIEN RAMSAY')

def case_default():
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
        
        