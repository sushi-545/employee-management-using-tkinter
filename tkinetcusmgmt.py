import pymysql
import tkinter
from tkinter import *
import tkinter.messagebox


class Customer:
    con=pymysql.connect(host='localhost',user='root',password='sushant',database='myspace')
   # mycursor=con.cursor()


    def __init__(self):
        self.id=0
        self.name=""
        self.mobile=0
        self.age=0
    def addcust(self):
        mycursor = Customer.con.cursor()
        strquery="insert into customer values(%s,%s,%s,%s)"
        mycursor.execute(strquery,(self.id,self.name,self.age,self.mobile))
        Customer.con.commit()




    def searchcust(self):
        mycursor=Customer.con.cursor()
        strquery="select * from customer where id=%s"
        rowaffected=mycursor.execute(strquery,(self.id))
        data=mycursor.fetchone()
        self.name=data[1]
        self.age=data[2]
        self.mobile=data[3]
        if(rowaffected==0):
            raise Exception("id doesnt exist")





    def deletecust(self):
        mycursor=Customer.con.cursor()
        strquery="delete from customer where id=%s"
        rowaffected=mycursor.execute(strquery,(self.id))
        Customer.con.commit()

    def modify(self):
        mycursor=Customer.con.cursor()
        strquery="update customer set name=%s,age=%s,mobile=%s where id=%s"
        rowaffected=mycursor.execute(strquery,(self.name,self.age,self.mobile,self.id))
        Customer.con.commit()
        if(rowaffected==0):
            raise Exception("ID DOESNT EXIST")

    def display(self):
        mycursor=Customer.con.cursor()
        strquery="select * from customer"
        mycursor.execute(strquery)
        for row in mycursor.fetchall():
            for cell in row:
                print(cell,end='\t')
            print()



root=tkinter.Tk()
Tk.configure(root,background="light green")
def donothing():
    print("okok i wont")
#root=Tk()
menu=Menu(root)
root.config(menu=menu)
subMenu=Menu(menu)
menu.add_cascade(label="file",menu=subMenu)

subMenu.add_command(label="new project",command=donothing)
subMenu.add_command(label="new",command=donothing)
subMenu.add_separator()
subMenu.add_command(label="exit",command=donothing)
editMenu=Menu(menu)
menu.add_cascade(label="new",menu=editMenu)
editMenu.add_command(label="redo",command=donothing)
labelfont=(root,50)
def btnadd_click():
    cus=Customer()
    cus.id=varid.get()
    cus.name=varname.get()
    cus.age=varage.get()
    cus.mobile=varmobile.get()
    Customer.addcust(cus)
    tkinter.messagebox.showinfo("success!","customer added successfully")
def btndelete_click():
    cus=Customer()
    cus.id=varid.get()
    Customer.deletecust(cus)
    tkinter.messagebox.showinfo("success","deleted! succesfully")
def btnupdate_click():
    try:
        cus=Customer()
        cus.id=varid.get()
        cus.name=varname.get()
        cus.age=varage.get()
        cus.mobile=varmobile.get()
        cus.modify()
        tkinter.messagebox.showinfo("success","customer updated successfully")
    except Exception as ex:
        tkinter.messagebox.showinfo("failure",ex)
def btnsearch_click():
    try:
        cus=Customer()
        cus.id=varid.get()
        cus.searchcust()
        varname.set(cus.name)
        varage.set(cus.age)
        varmobile.set(cus.mobile)
    except Exception as ex:
        tkinter.messagebox.showinfo("FAILURE",ex)






root.title("customer form")
labelfont = ('times', 20, 'bold')
root.minsize(height=699,width=699)


lblid=tkinter.Label(root,text="customer id:    ",fg='black',bg='yellow',font="Times 32",height=2)
lblid.grid(row=0,column=0)
lblname=tkinter.Label(root,text="customer name:",fg='blue',bg='pink',font="Times 32",height=2)
lblname.grid(row=2,column=0)
lblage=tkinter.Label(root,text="age:           ",fg='green',bg='red',font="Times 32",height=2)
lblage.grid(row=4,column=0)
lblmob=tkinter.Label(root,text="customer mobile:",fg='black',bg='skyblue',font="Times 32",height=2)
lblmob.grid(row=6,column=0)
varid=tkinter.IntVar()
textid=tkinter.Entry(root,text="  ",textvariable=varid)
textid.grid(row=0,column=2)
varname=tkinter.StringVar()
textname=tkinter.Entry(root,textvariable=varname)
textname.grid(row=2,column=2,pady=5,padx=50)
varage=tkinter.IntVar()
txtage=tkinter.Entry(root,text="  ",textvariable=varage)
txtage.grid(row=4,column=2)
varmobile=tkinter.StringVar()
txtmobile=tkinter.Entry(root,textvariable=varmobile)
txtmobile.grid(row=6,column=2)
btnadd=tkinter.Button(root,text="add",command=btnadd_click,fg='red',height=6,width=6)
btnadd.place(x=0,y=425,width=100)
btndelete=tkinter.Button(root,text="delete",command=btndelete_click,fg='green',height=6,width=6)
btndelete.place(x=100,y=425,width=100)
btnmodify=tkinter.Button(root,text="update",command=btnupdate_click,fg='blue',height=6,width=6)
btnmodify.place(x=200,y=425,width=100)
btnsearch=tkinter.Button(root,text="search",command=btnsearch_click,fg='black',height=6,width=6)
btnsearch.place(x=300,y=425,width=100)
Label.config(root,width=2000)
root.mainloop()























