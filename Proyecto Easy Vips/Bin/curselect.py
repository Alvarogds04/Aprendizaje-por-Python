import AVEC2
from view import *


def CurSelet(evt):
    
    value=str((AVEC2.list1.get(AVEC2.list1.curselection())))
    #print(value)
    View(value)
    AVEC2.tree.yview_moveto(0)