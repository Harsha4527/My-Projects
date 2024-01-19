from tkinter import *
from tkinter import messagebox
import random
billnumber=random.randint(1000,9999)
# Declare product variables as global
thumsup = 0
Maza = 0
fanta = 0
limca = 0
cocacola = 0
sprite = 0

Cycle = 0
football = 0
cricketbat = 0
badmintion = 0
waterbottel = 0
waveboard = 0

rice = 0
milk = 0
meat = 0
eggs = 0
oil = 0
biscuits = 0

#funtion part
def Billarea():
   # if nameentry.get()==''or phoneentry.get()=='':
       # messagebox.showerror('Error','Customer Details Are Required')
   # elif cooldrinkpriceentry.get()==''and sportspriceentry.get()=='' and groceryspriceentry.get()=='':
        
        #  messagebox.showerror('Error','No products are selected')
    #elif cooldrinkpriceentry.get()=='0Rs'and sportspriceentry.get()=='0Rs' and groceryspriceentry.get()=='0Rs':
        
        #  messagebox.showerror('Error','No products are selected')
    #else:
        textarea.delete(0.1,END)
        textarea.insert(END,'\t\t***Welcome Customer***')
        textarea.insert(END,'\nBill Number :'+ str(billnumber))
        textarea.insert(END,'\nCustomer Name :'+ str(nameentry.get()))
        textarea.insert(END,'\nPhone Number :'+ str(phoneentry.get()))
        textarea.insert(END,'\n==================================================')
        textarea.insert(END,'\nProduct\t\t   Quantity     \t\t\tPrice')
        textarea.insert(END,'\n==================================================')
        if thumsupentry.get()!='0':
            textarea.insert(END,f'\nThumsup\t\t   {thumsupentry.get()}\t\t\t{thumsup}')
        if Mazaentry.get()!='0':
            textarea.insert(END,f'\nMaza   \t\t   {Mazaentry.get()}    \t\t\t{Maza}')
        if Fantaentry.get()!='0':
            textarea.insert(END,f'\nFanta\t\t     {Fantaentry.get()}   \t\t\t{fanta}')
        if limcaentry.get()!='0':
            textarea.insert(END,f'\nLimca\t\t   {limcaentry.get()} \t\t\t{limca}')
        if cocacolaentry.get()!='0':
            textarea.insert(END,f'\nCocacola\t\t   {cocacolaentry.get()} \t\t\t{cocacola}')
        if spriteentry.get()!='0':
            textarea.insert(END,f'\nSprite\t\t   {spriteentry.get()} \t\t\t{sprite}')
        if Cycleentry.get()!='0':
            textarea.insert(END,f'\nCycle\t\t   {Cycleentry.get()}\t\t\t{Cycle}')
        if footballentry.get()!='0':
            textarea.insert(END,f'\nFootball   \t\t   {footballentry.get()}    \t\t\t{football}')
        if cricketbatentry.get()!='0':
            textarea.insert(END,f'\nCricket Bat\t\t     {cricketbatentry.get()}   \t\t\t{cricketbat}')
        if badmintionentry.get()!='0':
            textarea.insert(END,f'\nBadmintion\t\t   {badmintionentry.get()} \t\t\t{badmintion}')
        if waterbottelentry.get()!='0':
            textarea.insert(END,f'\Waterbotte\t\t   {waterbottelentry.get()} \t\t\t{waterbotte}')
        if waveboardentry.get()!='0':
            textarea.insert(END,f'\nWaveboard\t\t   {waveboardentry.get()} \t\t\t{waveboard}')
        if riceentry.get()!='0':
            textarea.insert(END,f'\nRice\t\t   {riceentry.get()}\t\t\t{rice}')
        if milkentry.get()!='0':
            textarea.insert(END,f'\nMilk  \t\t   {milkentry.get()}    \t\t\t{milk}')
        if Meatentry.get()!='0':
            textarea.insert(END,f'\nMeat Bat\t\t     {Meatentry.get()}   \t\t\t{meat}')
        if Eggsentry.get()!='0':
            textarea.insert(END,f'\nEgg\t\t   {Eggsentry.get()} \t\t\t{eggs}')
        if oilentry.get()!='0':
            textarea.insert(END,f'\nOil\t\t   {oil.get()} \t\t\t{oil}')
        if Biscuitsentry.get()!='0':
            textarea.insert(END,f'\nBiscuits\t\t   {Biscuitsentry.get()} \t\t\t{biscuits}')
        textarea.insert(END,'\n--------------------------------------------------')
        if cooldrinktaxentry.get()!='0.0Rs':
            textarea.insert(END,f'\nCoolDrink Tax:\t\t   {cooldrinktaxentry.get()}  ')
        if sportstaxentry.get()!='0.0Rs':
            textarea.insert(END,f'\nSports Tax:\t\t   {sportstaxentry.get()}  ')
        if grocerystaxentry.get()!='0.0Rs':
            textarea.insert(END,f'\nGrocery Tax:\t\t   {grocerystaxentry.get()}  ')
        textarea.insert(END,'\n--------------------------------------------------')   
        if totalbillentry.get()!=0:
                textarea.insert(END,f'\nTotal Bill:\t\t   {totalbillentry.get()}  ')
           
        
        
        
    
def total():
    #cool drinks
    global thumsup
    thumsup= int(thumsupentry.get())*100
    Maza= int(Mazaentry.get())*89
    fanta= int(Fantaentry.get())*20
    limca= int(limcaentry.get())*20
    cocacola= int(cocacolaentry.get())*119
    sprite= int(spriteentry.get())*88
    totalcooldrinksprice=thumsup+Maza+fanta+limca+cocacola+sprite
    cooldrinkpriceentry.delete(0,END)
    cooldrinkpriceentry.insert(0, str(totalcooldrinksprice)+'Rs')
    cooldrinktax= totalcooldrinksprice*0.08
    cooldrinktaxentry.delete(0,END)
    cooldrinktaxentry.insert(0,str(cooldrinktax)+'Rs')
    #sports
    cycle= int(Cycleentry.get())*14999
    football= int(footballentry.get())*499
    cricketbat= int(cricketbatentry.get())*299
    badmintion= int(badmintionentry.get())*249
    waterbottel= int(waterbottelentry.get())*99
    waveboard= int(waveboardentry.get())*4999
    totalsports= cycle+football+cricketbat+badmintion+waterbottel+waveboard
    sportspriceentry.delete(0,END)
    sportspriceentry.insert(0, str(totalsports)+'Rs')
    sportstax = totalsports * 0.012
    sportstaxentry.delete(0,END)
    sportstaxentry.insert(0,str(sportstax)+'Rs')
    #grocery
    rice= int(riceentry.get())*1499
    milk= int(milkentry.get())*49
    meat= int(Meatentry.get())*299
    eggs= int(Eggsentry.get())*7
    oil= int(oilentry.get())*249
    biscuits= int(Biscuitsentry.get())*10
    totalgrocery=rice+milk+meat+eggs+oil+biscuits
    groceryspriceentry.delete(0,END)
    groceryspriceentry.insert(0, str(totalgrocery)+'Rs')
    grocerystax = totalgrocery *0.04
    grocerystaxentry.delete(0,END)
    grocerystaxentry.insert(0,str(grocerystax)+'Rs')
    
    #totalbill
    totalbill=totalcooldrinksprice+cooldrinktax+totalsports+sportstax+totalgrocery+grocerystax
    totalbillentry.delete(0,END)
    totalbillentry.insert(0,str(totalbill)+'Rs')
    

  
  


 





































#GUI Part
root = Tk()
root.title("Retail Billing System")
root.geometry("1240x640")
root.iconbitmap("icon.ico")

headinglabel = Label(root, text="Harsha Kaushik Enterprises", font=("times new roman", 30, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
headinglabel.pack(fill=X)

Customerdetailsframe = LabelFrame(root, text="Customer Details",font=("times new roman", 15, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
Customerdetailsframe.pack(fill=X)

namelabel = Label(Customerdetailsframe, text="Name ",font=("times new roman", 15), bg='gray20', fg='white' )
namelabel.grid(row=0, column=0,padx=20,pady=2)

nameentry = Entry(Customerdetailsframe,font=("arial", 15, "bold"),bd=7,width=18)
nameentry.grid(row=0, column=1,padx=8)

phonelabel = Label(Customerdetailsframe, text="Phone number ",font=("times new roman", 15), bg='gray20', fg='white' )
phonelabel.grid(row=0, column=2,padx=20,pady=2)

phoneentry = Entry(Customerdetailsframe,font=("arial", 15, "bold"),bd=7,width=18)
phoneentry.grid(row=0, column=3,padx=8)

BILLlabel = Label(Customerdetailsframe, text="Bill no",font=("times new roman", 15), bg='gray20', fg='white' )
BILLlabel.grid(row=0, column=4,padx=20,pady=2)

BILLentry = Entry(Customerdetailsframe,font=("arial", 15, "bold"),bd=7,width=18)
BILLentry.grid(row=0, column=5,padx=20)

searchbutton= Button(Customerdetailsframe,text="search",font=("times new roman", 12, "bold"),bd=7,width=10 )
searchbutton.grid(row=0, column=6,padx=14,pady=7)

productsframe= Frame(root)
productsframe.pack()

cooldrinksframe = LabelFrame(productsframe, text="Cool Drinks",font=("times new roman", 15, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
cooldrinksframe.pack()
cooldrinksframe.grid(row=0,column=0)


thumsuplabel = Label(cooldrinksframe, text="Thums Up ",font=("times new roman", 15), bg='gray20', fg='white' )
thumsuplabel.grid(row=1, column=0,padx=20,pady=2)

thumsupentry = Entry(cooldrinksframe,font=("arial", 15, "bold"),bd=7,width=18)
thumsupentry.grid(row=1, column=1,padx=8)
thumsupentry.insert(0,0)

Mazalabel = Label(cooldrinksframe, text="Maza ",font=("times new roman", 15), bg='gray20', fg='white' )
Mazalabel.grid(row=2, column=0,padx=20,pady=2)

Mazaentry = Entry(cooldrinksframe,font=("arial", 15, "bold"),bd=7,width=18)
Mazaentry.grid(row=2, column=1,padx=8)
Mazaentry.insert(0,0)

Fantalabel = Label(cooldrinksframe, text=" Fanta ",font=("times new roman", 15), bg='gray20', fg='white' )
Fantalabel.grid(row=3, column=0,padx=20,pady=2)

Fantaentry = Entry(cooldrinksframe,font=("arial", 15, "bold"),bd=7,width=18)
Fantaentry.grid(row=3, column=1,padx=8)
Fantaentry.insert(0,0)

limcalabel = Label(cooldrinksframe, text="Limca ",font=("times new roman", 15), bg='gray20', fg='white' )
limcalabel.grid(row=4, column=0,padx=20,pady=2)

limcaentry = Entry(cooldrinksframe,font=("arial", 15, "bold"),bd=7,width=18)
limcaentry.grid(row=4, column=1,padx=8)
limcaentry.insert(0,0)

cocacolalabel = Label(cooldrinksframe, text="CocaCola ",font=("times new roman", 15), bg='gray20', fg='white' )
cocacolalabel.grid(row=5, column=0,padx=20,pady=2)

cocacolaentry = Entry(cooldrinksframe,font=("arial", 15, "bold"),bd=7,width=18)
cocacolaentry.grid(row=5, column=1,padx=8)
cocacolaentry.insert(0,0)

spritelabel = Label(cooldrinksframe, text="Sprite ",font=("times new roman", 15), bg='gray20', fg='white' )
spritelabel.grid(row=6, column=0,padx=20,pady=2)

spriteentry = Entry(cooldrinksframe,font=("arial", 15, "bold"),bd=7,width=18)
spriteentry.grid(row=6, column=1,padx=8)
spriteentry.insert(0,0)

 
Sportsframe = LabelFrame(productsframe, text="Sports",font=("times new roman", 15, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
Sportsframe.grid(row=0,column=1)
 

Cyclelabel = Label(Sportsframe, text="Cycle ",font=("times new roman", 15), bg='gray20', fg='white' )
Cyclelabel.grid(row=1, column=0,padx=20,pady=2)

Cycleentry = Entry(Sportsframe,font=("arial", 15, "bold"),bd=7,width=18)
Cycleentry.grid(row=1, column=1,padx=8)
Cycleentry.insert(0,0)

footballlabel = Label(Sportsframe, text="football ",font=("times new roman", 15), bg='gray20', fg='white' )
footballlabel.grid(row=2, column=0,padx=20,pady=2)

footballentry = Entry(Sportsframe,font=("arial", 15, "bold"),bd=7,width=18)
footballentry.grid(row=2, column=1,padx=8)
footballentry.insert(0,0)

cricketbatlabel = Label(Sportsframe, text=" Cricket Bat ",font=("times new roman", 15), bg='gray20', fg='white' )
cricketbatlabel.grid(row=3, column=0,padx=20,pady=2)

cricketbatentry = Entry(Sportsframe,font=("arial", 15, "bold"),bd=7,width=18)
cricketbatentry.grid(row=3, column=1,padx=8)
cricketbatentry.insert(0,0)

badmintionlabel = Label(Sportsframe, text="Badmintion Racket ",font=("times new roman", 15), bg='gray20', fg='white' )
badmintionlabel.grid(row=4, column=0,padx=20,pady=2)

badmintionentry = Entry(Sportsframe,font=("arial", 15, "bold"),bd=7,width=18)
badmintionentry.grid(row=4, column=1,padx=8)
badmintionentry.insert(0,0)

waveboardlabel = Label(Sportsframe, text=" Waveboard ",font=("times new roman", 15), bg='gray20', fg='white' )
waveboardlabel.grid(row=5, column=0,padx=20,pady=2)

waveboardentry = Entry(Sportsframe,font=("arial", 15, "bold"),bd=7,width=18)
waveboardentry.grid(row=5, column=1,padx=8)
waveboardentry.insert(0,0)

waterbottellabel = Label(Sportsframe, text="Water Bottel ",font=("times new roman", 15), bg='gray20', fg='white' )
waterbottellabel.grid(row=6, column=0,padx=20,pady=2)

waterbottelentry = Entry(Sportsframe,font=("arial", 15, "bold"),bd=7,width=18)
waterbottelentry.grid(row=6, column=1,padx=8)
waterbottelentry.insert(0,0)
 
 
groceryframe = LabelFrame(productsframe, text="Grocery",font=("times new roman", 15, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
groceryframe.grid(row=0,column=2)
 

ricelabel = Label(groceryframe, text="Rice ",font=("times new roman", 15), bg='gray20', fg='white' )
ricelabel.grid(row=1, column=0,padx=20,pady=2)

riceentry = Entry(groceryframe,font=("arial", 15, "bold"),bd=7,width=18)
riceentry.grid(row=1, column=1,padx=8)
riceentry.insert(0,0)

milklabel = Label(groceryframe, text="Milk ",font=("times new roman", 15), bg='gray20', fg='white' )
milklabel.grid(row=2, column=0,padx=20,pady=2)

milkentry = Entry(groceryframe,font=("arial", 15, "bold"),bd=7,width=18)
milkentry.grid(row=2, column=1,padx=8)
milkentry.insert(0,0)

Meatlabel = Label(groceryframe, text="  Meat ",font=("times new roman", 15), bg='gray20', fg='white' )
Meatlabel.grid(row=3, column=0,padx=20,pady=2)

Meatentry = Entry(groceryframe,font=("arial", 15, "bold"),bd=7,width=18)
Meatentry.grid(row=3, column=1,padx=8)
Meatentry.insert(0,0)

Eggslabel = Label(groceryframe, text=" Eggs",font=("times new roman", 15), bg='gray20', fg='white' )
Eggslabel.grid(row=4, column=0,padx=20,pady=2)

Eggsentry = Entry(groceryframe,font=("arial", 15, "bold"),bd=7,width=18)
Eggsentry.grid(row=4, column=1,padx=8)
Eggsentry.insert(0,0)

oillabel = Label(groceryframe, text=" Oil ",font=("times new roman", 15), bg='gray20', fg='white' )
oillabel.grid(row=5, column=0,padx=20,pady=2)

oilentry = Entry(groceryframe,font=("arial", 15, "bold"),bd=7,width=18)
oilentry.grid(row=5, column=1,padx=8)
oilentry.insert(0,0)

Biscuitslabel = Label(groceryframe, text="Biscuits ",font=("times new roman", 15), bg='gray20', fg='white' )
Biscuitslabel.grid(row=6, column=0,padx=20,pady=2)

Biscuitsentry = Entry(groceryframe,font=("arial", 15, "bold"),bd=7,width=18)
Biscuitsentry.grid(row=6, column=1,padx=8)
Biscuitsentry.insert(0,0)

billframe = LabelFrame(productsframe, text="BIll AREA",font=("times new roman", 15, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billarealabel=Label(billframe,text="Bill Area",font=("times new roman", 13, "bold"),  bd=12, relief=GROOVE)
billarealabel.pack(fill=X)
scrollbar = Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side = RIGHT,fill = Y)

textarea=Text(billframe,height=15,width=50,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuframe = LabelFrame(root,text="Bill Menu",font=("times new roman", 15, "bold"), bg='gray20', fg='gold', bd=12, relief=GROOVE)
billmenuframe.pack() 


cooldrinkpricelabel = Label(billmenuframe, text="Cool Drink Price ",font=("times new roman", 15), bg='gray20', fg='white' )
cooldrinkpricelabel.grid(row=0, column=0)

cooldrinkpriceentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
cooldrinkpriceentry.grid(row=0, column=1,padx=8)


sportspricelabel = Label(billmenuframe, text="Sports Price ",font=("times new roman", 15), bg='gray20', fg='white' )
sportspricelabel.grid(row=1, column=0)

sportspriceentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
sportspriceentry.grid(row=1, column=1,padx=8)


groceryspricelabel = Label(billmenuframe, text=" grocerys price ",font=("times new roman", 15), bg='gray20', fg='white' )
groceryspricelabel.grid(row=2, column=0)

groceryspriceentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
groceryspriceentry.grid(row=2, column=1,padx=8)

totalbilllabel = Label(billmenuframe, text="Total Bill ",font=("times new roman", 15), bg='gray20', fg='white' )
totalbilllabel.grid(row=3, column=0)

totalbillentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
totalbillentry.grid(row=3, column=1,padx=8,columnspan = 3)
totalbillentry.insert(0,0)

cooldrinktaxlabel = Label(billmenuframe, text="Cool Drink  Tax ",font=("times new roman", 15), bg='gray20', fg='white' )
cooldrinktaxlabel.grid(row=0, column=2)

cooldrinktaxentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
cooldrinktaxentry.grid(row=0, column=3,padx=8)


sportstaxlabel = Label(billmenuframe, text="Sports  Tax ",font=("times new roman", 15), bg='gray20', fg='white' )
sportstaxlabel.grid(row=1, column=2)

sportstaxentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
sportstaxentry.grid(row=1, column=3,padx=8)


grocerystaxlabel = Label(billmenuframe, text=" grocerys  Tax ",font=("times new roman", 15), bg='gray20', fg='white' )
grocerystaxlabel.grid(row=2, column=2)

grocerystaxentry = Entry(billmenuframe,font=("arial", 15, "bold"),bd=7,width=18)
grocerystaxentry.grid(row=2, column=3,padx=8)

buttonframe=Frame(billmenuframe,bd=8,relief =GROOVE)
buttonframe.grid(row=0,column=4,rowspan=3)

Totalbutton =Button(buttonframe, text="Total ",font=("times new roman", 15,"bold"), bg='gray20', fg='black',bd=5,width=8,command = total )
Totalbutton.grid(row=0, column=0,)

Billbutton =Button(buttonframe, text=" Bill ",font=("times new roman", 15,"bold"), bg='gray20', fg='black',bd=5,width=8,command = Billarea )
Billbutton.grid(row=0, column=1)

Emailbutton =Button(buttonframe, text=" Email ",font=("times new roman", 15,"bold"), bg='gray20', fg='black',bd=5,width=8 )
Emailbutton.grid(row=0, column=2)

printbutton =Button(buttonframe, text=" Print ",font=("times new roman", 15,"bold"), bg='gray20', fg='black',bd=5,width=8 )
printbutton.grid(row=0, column=3)


root.mainloop()


