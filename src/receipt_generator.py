from escpos.printer import Usb

#48 chars per line size 1

from escpos.connections import *

def generate_recipt_old(orderjson):
    p = getUSBPrinter()(idVendor=0x0483,
                          idProduct=0x5720,
                          inputEndPoint=0x82,
                          outputEndPoint=0x01)
    
    #p.image("chainhack.png", high_density_vertical=True, high_density_horizontal=True)

    p.doubleHeight()
    p.invert()
    p.align('center')
    p.text("Chainhack 4")
    p.invert(False)
    p.text("The Block")
    p.text("Lisbon")

    p.doubleHeight(False)
    p.align('right')
    p.text('abc')

    '''
    p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
    p.text("===========================\n")
    p.text("=============== Sales Recipt ===========\n")
    p.text("===========================\n")
    '''
    items = orderjson.get('items')

    print(items)
    p.cutPaper()


    '''
    p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
    p.text('Coffee')
    p.set(align='right', smooth=True, invert=False, density=2, width=1, height=1)
    p.text('\t2eur\n')
    p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
    p.text(str(2) + " x " + "1eur\n")
    '''

    '''
    for i in range(len(items)):
        p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
        p.text(items[i].get("name"))
        p.set(align='right', smooth=True, invert=False, density=2, width=1, height=1)
        p.text(str(items[i].get("total_price")))
        p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
        p.text(str(items[i].get("qty")) + "x" + str(items[i].get("unit_price")) + " ")
    '''


    
    #p.cut()
    



def generate_recipt(orderjson):
    p = Usb(0x0483, 0x5720, 0)

    #p.image("chainhack.png", high_density_vertical=True, high_density_horizontal=True)

    p.set(align='center', smooth=True, invert=True, density=8, width=4, height=4, font='1')
    p.text("Chainhack 4\n")
    p.set(align='center', smooth=True, invert=False, density=4, width=4, height=4)
    p.text("The Block\n")
    p.set(align='center', smooth=True, invert=False, density=4, width=4, height=4)
    p.text("Lisbon\n")

    '''
    p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
    p.text("===========================\n")
    p.text("=============== Sales Recipt ===========\n")
    p.text("===========================\n")
    '''
    items = orderjson.get('items')

    print(items)

    '''
    p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
    p.text('Coffee\n')
    p.set(align='right', smooth=True, invert=False, density=2, width=1, height=1)
    p.text(str(2) + " x " + "1eur\n")
    p.set(align='right', smooth=True, invert=False, density=2, width=1, height=1)
    p.text('2eur\n')
    
    
    for i in range(len(items)):
        p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
        p.text(items[i].get("name"))
        p.set(align='right', smooth=True, invert=False, density=2, width=1, height=1)
        p.text(str(items[i].get("total_price")))
        p.set(align='left', smooth=True, invert=False, density=2, width=1, height=1)
        p.text(str(items[i].get("qty")) + "x" + str(items[i].get("unit_price")) + " ")
    '''


    
    #p.cut()
    
