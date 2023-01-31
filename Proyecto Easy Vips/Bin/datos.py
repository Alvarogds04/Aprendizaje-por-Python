import AVEC2

def datos(evt):
    global linea
    curItem = AVEC2.tree.focus()
    print(curItem)
    linea = AVEC2.tree.item(curItem)['values']
    #print(linea)
    #child_id = tree.get_children()
    #print(child_id)
    print("----linea")
    #global list2
    #list2 = linea