from tkinter import*
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from cryptography.fernet import Fernet

root=Tk()  #create a tkinter window
root.geometry("1500x500")   #set dimension of window
root.title('library Management System')

regf=Frame(root,background="white")

add=Frame(root,background="skyblue")
loginf=Frame(root,background="palegreen")
home=Frame(root,background="magenta")
div=Frame(root,background="light blue")
intro=Frame(root,background="skyblue")
#admin=Frame(root,background="magenta")
library=Frame(root,background="skyblue")
books=Frame(root,background="skyblue")
login=Frame(root)
login2=Frame(root)
pas_reset=Frame(root)
login3=Frame(root)


add.place(x=0,y=0,width=500,height=500)
regf.place(x=0,y=0,width=1500,height=500)
loginf.place(x=0,y=0,width=1500,height=500)
home.place(x=0,y=0,width=15000,height=500)
div.place(x=0,y=0,width=1500,height=500)
intro.place(x=0,y=0,width=1500,height=500)
#admin.place(x=0,y=0,width=1500,height=500)
library.place(x=0,y=0,width=1500,height=500)
books.place(x=0,y=0,width=1500,height=500)
login.place(x=350,y=50,width=750,height=400)
login2.place(x=250,y=50,width=750,height=400)
login3.place(x=250,y=50,width=750,height=400)
pas_reset.place(x=250,y=50,width=750,height=400)


root.wm_iconbitmap()


def log():
    username = userName.get()
    Pass = password.get()
        	#Establish Connection
    with sqlite3.connect('projectSMS.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
    find_passwords = ('SELECT * FROM passwords WHERE username = ? and  pasword = ?')
    c.execute(find_passwords,[(userName.get()),(password.get())])
    result = c.fetchall()
    if result:
        show(home)
        m4=Label(root, text="successfully loged in",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
            
                     
    else:
        messagebox.showerror('Username Not Found.')
        m4=Label(root, text="Enter correct  details",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
def log2():
    username = userName1.get()
    Pass = password1.get()
        	#Establish Connection
    with sqlite3.connect('projectSMS.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
    find_passwords= ('SELECT * FROM passwords WHERE username = ? and pasword = ?')
    c.execute(find_passwords,[(userName1.get()),(password1.get())])
    result = c.fetchall()
    if result:
        show(library)
                     
    else:
        messagebox.showerror('Username Not Found.')
def log3():
    username3= userName3.get()
    Pass3 = password3.get()
        	#Establish Connection
    with sqlite3.connect('projectSMS.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
    find_passwords = ('SELECT * FROM passwords WHERE username = ? and  pasword = ?')
    c.execute(find_passwords,[(userName3.get()),(password3.get())])
    result = c.fetchall()
    if result:
        show(pas_reset)
        m4=Label(root, text=" VERIFIED",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())
            
                     
    else:
        messagebox.showerror('Oops!','NOT AUTHORISED.')
        m4=Label(root, text="pleace enter correct  login",font=('Kristen ITC', 15, 'bold'),fg='red',bg="skyblue")
            
        root.after(100, lambda:m4.grid(row=3,column=5))
        root.after(1500, lambda:m4.grid_forget())

            

      
   
        
def show(frame):
    frame.tkraise()
for frame in (regf,loginf,home,add,div,intro,library):
    frame.place(x=0,y=0)
style = ttk.Style()

Estyle = ttk.Style()
Estyle.configure('TEntry', foreground = 'green')

#-----------------------------------------------------------------------
db = sqlite3.connect('projectSMS.db')
my=db.cursor()
#-----------------------------------------------------------------------

#####_______Form____#########################################################
mylist=''
      
#-----------------------registration-----------------------------------------
adr=Label(regf,text="LIBRARY MANAGEMENT SYSTEM",bg='white'
          ,font=('Kristen ITC', 30, 'bold','italic','underline'),fg='blue')
adr.pack()
#-------------------------------------------------------------------------------------




#-----------------------login---------------------------------------------------------

#-------------------------------------------------------------------------------------

Label(regf,text="",bg="white").pack()
Label(regf,text="",bg="white").pack()
st=ttk.Button(regf,text="ADMINISTRATOR",width=30,command=lambda:show(login) ,style='C.TButton')
st.pack()
Label(regf,text="",bg="white").pack()
Label(regf,text="",bg="white").pack()
st=ttk.Button(regf,text="LIBRARIAN",width=30,command=lambda:show(login2) ,style='C.TButton')
st.pack()
Label(regf,text="",bg="white").pack()
Label(regf,text="",bg="white").pack()

#####_____function_______________###################################################
def backi():
    global style
    div_nma.delete(0,END)
    div_poia.delete(0,END)
    div_pera.delete(0,END)
    div_doba.delete(0,END)
    div_gena.delete(0,END)
    show(library)
def backi1():
    global style
    div_nma.delete(0,END)
    div_poia.delete(0,END)
    div_pera.delete(0,END)
    div_doba.delete(0,END)
    div_gena.delete(0,END)
    show(home)
#################___
#################___Home____###############################################################
####____tree view______####
def log_out():
    show(loginf)
table_frame = Frame(library,bg='light blue')
table_frame.place(x=150,y=45,width=1200,height=415)

scroll_x = Scrollbar(table_frame,orient="horizontal")
scroll_y = Scrollbar(table_frame,orient="vertical")



tree=ttk.Treeview(table_frame,columns=('sno','name','admission no.','percent','DOB','fine'),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tree.xview)
scroll_y.config(command=tree.yview)
tree.column('#0',width=50)
tree.column('#1',width=150)
tree.column('#2',width=200)
tree.column('#3',width=200)
tree.column('#4',width=200)
tree.column('#5',width=200)
tree.column('#6',width=200)

tree.heading('#0',text='no',)
tree.heading('#1',text='ADM NO')
tree.heading('#2',text='NAME.')
tree.heading('#3',text='BOOK')
tree.heading('#4',text='BORROWED ON')
tree.heading('#5',text='RETURNED ON')
tree.heading('#6',text='FINE')





sno=0
tree.pack(fill=BOTH,expand=1)


tableframe = Frame(home,bg='light blue')
tableframe.place(x=150,y=45,width=1200,height=415)

scroll_x = Scrollbar(tableframe,orient="horizontal")
scroll_y = Scrollbar(tableframe,orient="vertical")



tre=ttk.Treeview(tableframe,columns=('sno','name','admission no.','percent','DOB','fine'),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tre.xview)
scroll_y.config(command=tre.yview)
tre.column('#0',width=50)
tre.column('#1',width=150)
tre.column('#2',width=200)
tre.column('#3',width=200)
tre.column('#4',width=200)
tre.column('#5',width=200)
tre.column('#6',width=200)

tre.heading('#0',text='no',)
tre.heading('#1',text='ADM NO')
tre.heading('#2',text='NAME.')
tre.heading('#3',text='BOOK  ')
tre.heading('#4',text='BORROWED ON')
tre.heading('#5',text='RETURNED ON')
tre.heading('#6',text='FINE')



sno=0
tre.pack(fill=BOTH,expand=1)
#TREE IN ADMIN
Tframe = Frame(intro,bg='light blue')
Tframe.place(x=370,y=10,width=1000,height=480)

scroll_x = Scrollbar(Tframe,orient="horizontal")
scroll_y = Scrollbar(Tframe,orient="vertical")



tr=ttk.Treeview(Tframe,columns=('go','1','2','3'),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tr.xview)
scroll_y.config(command=tr.yview)
tr.column('#0',width=10)
tr.column('#1',width=50)
tr.column('#2',width=50)
tr.column('#3',width=50)


tr.heading('#0',text='NO',)
tr.heading('#1',text='BOOK ID')
tr.heading('#2',text='BOOK TITLE')
tr.heading('#3',text='AUTHOR')
gno=0
#TREE IN ADMIN
Tframe = Frame(intro,bg='light blue')
Tframe.place(x=370,y=10,width=1000,height=480)

scroll_x = Scrollbar(Tframe,orient="horizontal")
scroll_y = Scrollbar(Tframe,orient="vertical")



tr=ttk.Treeview(Tframe,columns=('go','1','2','3'),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tr.xview)
scroll_y.config(command=tr.yview)
tr.column('#0',width=10)
tr.column('#1',width=50)
tr.column('#2',width=50)
tr.column('#3',width=50)


tr.heading('#0',text='NO',)
tr.heading('#1',text='BOOK ID')
tr.heading('#2',text='BOOK TITLE')
tr.heading('#3',text='AUTHOR')
gno=0
#LIBRARIAN BOOKS VIEW
Mframe = Frame(books,bg='light blue')
Mframe.place(x=200,y=10,width=1000,height=480)

scroll_x = Scrollbar(Mframe,orient="horizontal")
scroll_y = Scrollbar(Mframe,orient="vertical")



tb=ttk.Treeview(Mframe,columns=('go','1','2','3'),
                  xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=tb.xview)
scroll_y.config(command=tb.yview)
tb.column('#0',width=10)
tb.column('#1',width=50)
tb.column('#2',width=50)
tb.column('#3',width=50)


tb.heading('#0',text='NO',)
tb.heading('#1',text='BOOK ID')
tb.heading('#2',text='BOOK TITLE')
tb.heading('#3',text='AUTHOR')
gno=0
def vew2():
    global gno
    my.execute("select* from books")
#    sn=list(range(1,len(sn)+1))
    for k in my:
        gno=gno+1
        tr.insert('',str(gno),'item '+str(gno),text=gno,values=(k[0],k[1],k[2]))
        tb.insert('',str(gno),'item '+str(gno),text=gno,values=(k[0],k[1],k[2]))
        #gno=0

tr.pack(fill=BOTH,expand=1)
tb.pack(fill=BOTH,expand=1)
vew2()
def veiw():
    global sno
#    sn=my.execute("select* from student")

    my.execute("select* from student")
#    sn=list(range(1,len(sn)+1))
    for i in my:
        sno=sno+1
        tre.insert('',str(sno),'item '+str(sno),text=sno,values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        tree.insert('',str(sno),'item '+str(sno),text=sno,values=(i[0],i[1],i[2],i[3],i[4],i[5]))
        
        



veiw()

item='False'
def show_div():
    global item
    if 'item' in item: # item = 'item {any number}'
        show(div)
    else:
        messagebox.showerror("reminder","select  any person to view details")       #print('not called')
T1=LabelFrame(home,bg="skyblue").place(x=5,y=45,width=130,height=415)

T3=LabelFrame(home,bg="skyblue")
T3.place(x=5,y=5,width=1350,height=30)
T4=LabelFrame(home,bg="skyblue")
T4.place(x=5,y=465,width=1350,height=30)
name=Label(T3,text="LIBRARY MANAGEMENT SOFTWARE",fg="white",bg="skyblue",font=('Kristen ITC', 15, 'bold'))
footer=Label(T4,text="designed by MARILYNE CSC/023/2020",bg='skyblue')
footer.pack()
name.pack()

logout=ttk.Button(home,text="log out",style='C.TButton',command=lambda:show(regf))
logout.place(x=20,y=220)
adh=ttk.Button(home,text="add student",width=10,command=lambda:show(add),style='C.TButton')
#show frame 'div' whene clicked2
adh.place(x=20,y=70)
about=ttk.Button(home,text="add book",width=10,command=lambda:show(intro) ,style='C.TButton')  #show frame 'div' whene clicked
about.place(x=20,y=120)
pa_reset=ttk.Button(home,text="paswords",style='C.TButton',command=lambda:show(login3))
pa_reset.place(x=20,y=170)


#in library screen
sth=ttk.Button(library,text="veiw data",style='C.TButton',command=show_div)
sth.place(x=20,y=70)
logout=ttk.Button(library,text="log out",style='C.TButton',command=lambda:show(regf))
logout.place(x=20,y=170)

about=ttk.Button(library,text="BOOK",width=10,command=lambda:show(books)
                 ,style='C.TButton')  #show frame 'div' whene clicked
about.place(x=20,y=120)
''''issue=ttk.Button(library,text="issue book",width=10,command=lambda:show(books)
                 ,style='C.TButton')  #show frame 'div' whene clicked
issue.place(x=20,y=10)'''
###############__add__################################################################
def insert():
  global style
  sno=0
  book=0
  ret=0
  bor=0
  fin=0
  admission="'"+str(nm1.get())+"'"
  name="'"+str(p1.get())+"'"
  bok=book
  rtnd=ret
  brwd=bor
  fine=fin
  if name=="''" or admission=="''":
      messagebox.showerror("Error","ADM & NAME must be provided before you register")
  else:
      my.execute("insert into student values({},{},{},{},{},{})".format(admission,name,bok,brwd,rtnd,fine))
      db.commit()
      my.execute('select* from student')
      nma.delete(0,END)
      poia.delete(0,END)
      #pera.delete(0,END)
     # doba.delete(0,END)
     # gena.delete(0,END)
      #gen.delete(0,END)
      sno=0
      for i in my:
          sno=sno+1
          lst=i
      tree.insert('',str(sno),'item '+str(sno),text=sno,values=(lst[0],lst[1],lst[2],lst[3],lst[4],[5]))   #insert into tree ,last row of table
      tre.insert('',str(sno),'item '+str(sno),text=sno,values=(lst[0],lst[1],lst[2],lst[3],lst[4],[5]))
      m4=Label(root, text="successfully added to database",font=('Kristen ITC', 15, 'bold'),fg='green')
      messagebox.showerror("success","data aded to database")
      root.after(100, lambda:m4.pack())
      root.after(1500, lambda:m4.pack_forget())
def addbook():
    global style,gno
    gno=0
    bookid="'"+str(book_id.get())+"'"
    booktitle="'"+str(book_title.get())+"'"
    auth="'"+str(author.get())+"'"
    if bookid=="''" or booktitle=="''":
        messagebox.showerror("Error","BOOKID & BOOKTITLE must be provided before you register")
    else:
        my.execute("insert into books values({},{},{})".format(bookid,booktitle,auth))
        db.commit()
        my.execute('select* from books')
        p.delete(0,END)
        po.delete(0,END)
        nm.delete(0,END)
        gno=0
        
        for k in my:
            
            gno=gno+1
            l=k
           
        tr.insert('',str(gno),'item '+str(gno),text=gno,values=(l[0],l[1],l[2]))   #insert into tree ,last row of table
        m4=Label(root, text="successfully added to database",font=('Kristen ITC', 15, 'bold'),fg='green')
        m4.pack()
        messagebox.showerror("success","data aded to database")
        root.after(100, lambda:m4.pack())
        root.after(1500, lambda:m4.pack_forget())
        
def insert2():
    
  username="'"+str(userName4.get())+"'"
  pasword="'"+str(pasword4.get())+"'"
  if username=="''" or pasword=="''":
      messagebox.showerror("Error","userNAME & PASSWORD must be provided befor you update")
  else:
      my.execute("insert into passwords values({},{})".format(username,pasword,))
      db.commit()
      my.execute('select* from passwords')
      textBox1.delete(0,END)
      textBox2.delete(0,END)
      messagebox.showerror("success","pasword updated succes")
def insert3():
  username="'"+str(userName5.get())+"'"
  pasword="'"+str(pword5.get())+"'"
  if username=="''" or pasword=="''":
      messagebox.showerror("Error","userNAME & PASSWORD must be provided befor you update")
  else:
      my.execute("insert into users values({},{})".format(username,pasword,))
      db.commit()
      my.execute('select* from users')
      textBox1.delete(0,END)
      textBox2.delete(0,END)
      messagebox.showerror("success","pasword updated succes")      
     


add_name1=Label(add,text='ADM:',fg='white',font=('Kristen ITC', 15, 'bold'))
add_name1.place(x=10,y=20)
nm1=StringVar()
nma=ttk.Entry(add,textvariable=nm1 ,font = ('Kristen ITC', 10, 'bold'))
nma.place(x=90,y=20)
admis1=Label(add,text='NAME:',fg='white',font = ('Kristen ITC', 15, 'bold'))
admis1.place(x=10,y=50)

p1=StringVar()
poia=ttk.Entry(add,textvariable=p1 ,font = ('Kristen ITC', 10, 'bold'))
poia.place(x=90,y=50)
'''
percent1=Label(add,text='BOOK:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
percent1.place(x=10,y=80)
per1=StringVar()
pera=ttk.Entry(add,textvariable=per1 ,font = ('Kristen ITC', 10, 'bold'))
pera.place(x=100,y=80)

dob_1=Label(add,text='BORROWED ON:',fg='#145862',bg='sky blue',font = ('Kristen ITC', 15, 'bold'))
dob_1.place(x=10,y=110)
dob1=StringVar()
doba=ttk.Entry(add,textvariable=dob1 ,font = ('Kristen ITC', 10, 'bold'))
doba.place(x=150,y=110)

gender1=Label(add,text='RETURNED ON',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
gender1.place(x=10,y=140)
gen1=StringVar()
gena=ttk.Entry(add,textvariable=gen1 ,font = ('Kristen ITC', 10, 'bold'))
gena.place(x=140,y=140)
fine1=Label(add,text='FINE:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
fine1.place(x=10,y=170)
fin1=StringVar()
gen=ttk.Entry(add,textvariable=gen1 ,font = ('Kristen ITC', 10, 'bold'))
gen.place(x=140,y=160)
'''


sub=ttk.Button(add,text="submit",command=insert,width=10,style='C.TButton')
sub.place(x=50,y=90)

back=ttk.Button(add,text="back",width=10,command=backi1,style='C.TButton')
back.place(x=200,y=90)
###############__div__####################################################################
old_paw=''
def set_hifi(event):
    global old_paw,item
    item=tree.focus()  #return item name whene clicked
    dictc=tree.item(item)
    old_paw="'"+str(dictc['values'][1])+"'" #in dictc value[1] is password
    if div_nm1.get().isalnum():
        pass
    else:
        div_nma.insert(1,str(dictc['values'][0]))#value[0] is user name
        div_poia.insert(1,str(dictc['values'][1]))
        div_pera.insert(1,str(dictc['values'][2]))
        div_doba.insert(1,str(dictc['values'][3]))
        div_gena.insert(1,str(dictc['values'][4]))


def hifiv(event):
    global tp,old_paw,style
    my.execute("select* from student ")

tree.bind('<<TreeviewSelect>>',set_hifi)
def delete():
    global m4
    named="'"+str(div_nm1.get())+"'"
    item=tree.focus()  #return item name whene clicked
    dictc=tree.item(item)
    if dictc['text']=='':  #cheak if name deleted
        messagebox.showerror("Error","no data to be deleted")
    else:
        tree.delete('item '+str(dictc['text']))
        my.execute("delete from student where name={}".format(named))
        messagebox.showerror("Hey!!","confirm to delete",)
        db.commit()
        div_nma.delete(0,END)
        div_poia.delete(0,END)
        div_pera.delete(0,END)
        div_doba.delete(0,END)
        div_gena.delete(0,END)
        div_fina.delete(0,END)
        m=Label(root, text="successfully removed from database",font=('Kristen ITC', 15, 'bold'),fg='green')
        root.after(10, lambda:m.pack())
        root.after(4500, lambda:m.pack_forget())
        messagebox.showerror("succes","data deleated succesifully!")
def update():
  global old_paw
  adm=str(div_nm1.get())
  sname=str(div_p1.get())
  bk=str(div_per1.get())
  brd=str(div_dob1.get())
  retn=str(div_gen1.get())
  finet=str(div_fina.get())

  sname1="'"+str(div_nm1.get())+"'"
  paw1="'"+str(div_p1.get())+"'"
  book="'"+str(div_per1.get())+"'"
  bor_on="'"+str(div_dob1.get())+"'"
  ret_on="'"+str(div_gen1.get())+"'"
  fine="'"+str(div_fin1.get())+"'"
 
  my.execute("update student set adm={},sname={},book={},bor_on={},ret_on={},fine={} where adm={}".format(sname1,paw1,book,bor_on,ret_on,fine,old_paw))
  db.commit()

  m3=Label(root, text="successfully updated",font=('Kristen ITC', 15, 'bold'),bg="skyblue",fg='red')
  
  root.after(100, lambda:m3.pack())
  root.after(1500, lambda:m3.pack_forget())
  item=tree.focus()
  tree.item(item,values=(adm,sname,bk,brd,retn,finet)) 
  




######
F5= Frame(div,bg='skyblue')
F5.place(x=10,y=10,width=550,height=415)
div_sub=ttk.Button(F5,text="update",command=update,width=10,style='C.TButton')
div_sub.place(x=60,y=340)

div_del=ttk.Button(F5,text="delete",command=delete,width=10,style='C.TButton')
div_del.place(x=160,y=340)

back=ttk.Button(F5,text="back",width=10,command=backi,style='C.TButton')
back.place(x=260,y=340)

up_name=Label(F5,text='ADM:',bg='skyblue',fg='#145862',font=('Kristen ITC', 15, 'bold'))
up_name.place(x=10,y=10)
div_nm1=StringVar()
div_nma=ttk.Entry(F5,textvariable=div_nm1 ,font = ('Kristen ITC', 10, 'bold'))
div_nma.place(x=90,y=10)

admis2=Label(F5,text='NAME:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
admis2.place(x=10,y=40)

div_p1=StringVar()
div_poia=ttk.Entry(F5,textvariable=div_p1 ,font = ('Kristen ITC', 10, 'bold'))
div_poia.place(x=90,y=40)

percent2=Label(F5,text='BOOK',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
percent2.place(x=10,y=70)
div_per1=StringVar()
div_pera=ttk.Entry(F5,textvariable=div_per1 ,font = ('Kristen ITC', 10, 'bold'))
div_pera.place(x=110,y=70)

dob_2=Label(F5,text='BORROWED ON:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
dob_2.place(x=10,y=100)
div_dob1=StringVar()
div_doba=ttk.Entry(F5,textvariable=div_dob1 ,font = ('Kristen ITC', 10, 'bold'))
div_doba.place(x=150,y=100)

gender2=Label(F5,text='RETURNED ON',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
gender2.place(x=10,y=130)
div_gen1=StringVar()
div_gena=ttk.Entry(F5,textvariable=div_gen1 ,font = ('Kristen ITC', 10, 'bold'))

div_gena.place(x=140,y=130)
fine2=Label(F5,text='FINE',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
fine2.place(x=10,y=160)
div_fin1=StringVar()
div_fina=ttk.Entry(F5,textvariable=div_fin1 ,font = ('Kristen ITC', 10, 'bold'))
div_fina.place(x=90,y=160)






add_name1=Label(intro,text='BOOK ID:',bg='skyblue',fg='#145862',font=('Kristen ITC', 15, 'bold'))
add_name1.place(x=10,y=20)
book_id=StringVar()
nm=ttk.Entry(intro,textvariable=book_id,font = ('Kristen ITC', 10, 'bold'))
nm.place(x=130,y=20)
admis1=Label(intro,text='BOOK TITLE:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
admis1.place(x=10,y=50)

book_title=StringVar()
po=ttk.Entry(intro,textvariable=book_title,font = ('Kristen ITC', 10, 'bold'))
po.place(x=170,y=50)

percent1=Label(intro,text='AUTHOR:',fg='#145862',bg='skyblue',font = ('Kristen ITC', 15, 'bold'))
percent1.place(x=10,y=80)
author=StringVar()
p=ttk.Entry(intro ,textvariable=author,font = ('Kristen ITC', 10, 'bold'))
p.place(x=130,y=80)





sub=ttk.Button(intro,text="ADD",width=10,command=addbook,style='C.TButton')
sub.place(x=50,y=115)


K=ttk.Button(intro,text="back",width=10,command=lambda:show(home),style='C.TButton')
K.place(x=200,y=115)
K=ttk.Button(books,text="back",width=10,command=lambda:show(library),style='C.TButton')
K.place(x=5,y=5)

#admin login
label2 = Label(login, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(login, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(login, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password = StringVar()
textBox2 = Entry(login, textvar = password,validate='key',font = ("arial", 16, "bold"), width = 30, show="*")
textBox2.place(x = 290, y = 250)

button1 = Button(login, text = "   Login   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"), command = log)
button1.place(x = 335, y = 320)
button1 = Button(login, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(regf))
button1.place(x = 355, y = 360)


label2 = Label(login3, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName3 = StringVar()
textBox1 = Entry(login3, textvar = userName3, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(login3, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password3 = StringVar()
textBox2 = Entry(login3, textvar = password3,validate='key',font = ("arial", 16, "bold"), width = 30, show="*")
textBox2.place(x = 290, y = 250)

button1 = Button(login3, text = "   Login   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"), command = log3)
button1.place(x = 335, y = 320)
button1 = Button(login3, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(home))
button1.place(x = 355, y = 360)

### librarian login

label2 = Label(login2, text = "User Name :", font = ("arial", 16, "bold"))
label2.place(x = 110, y = 150)

userName1 = StringVar()
textBox1 = Entry(login2, textvar = userName, width = 30, font = ("arial", 16, "bold"))
textBox1.place(x = 290, y = 150)

label3 = Label(login2, text = "Password :", font = ("arial", 16, "bold"))
label3.place(x = 116, y = 250)

password1 = StringVar()
textBox2 = Entry(login2, textvar = password,validate='key',font = ("arial", 16, "bold"), width = 30, )
textBox2.place(x = 290, y = 250)

button1 = Button(login2, text = "   Login   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"), command = log2)
button1.place(x = 335, y = 320)
button1 = Button(login2, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(regf))
button1.place(x = 355, y = 360)

## pasword reset 


label1 = Label(pas_reset, text = " admin ", fg = "white", font = ("new times roman", 20, "bold"))
label1.place(x = 50, y = 60)
label1 = Label(pas_reset, text = " librarian", fg = "white", font = ("new times roman", 20, "bold"))
label1.place(x = 500, y = 60) 
label2 = Label(pas_reset, text = " Enter New UserName :",fg = "white",font = ("arial", 16, "bold"))
label2.place(x =20, y = 110)

userName4 = StringVar()
textBox1 = Entry(pas_reset, textvar = userName4, width = 20, font = ("arial", 15, "bold"))
textBox1.place(x = 20, y = 150)

label3 = Label(pas_reset, text = " Enter New Password :",fg = "white", font = ("arial", 16, "bold"))
label3.place(x = 20, y = 190)

pasword4 = StringVar()
textBox2 = Entry(pas_reset, textvar = pasword4, width = 20, font = ("arial", 15, "bold"))
textBox2.place(x = 20, y = 230)


label2 = Label(pas_reset, text = " Enter New UserName :",fg = "white",font = ("arial", 16, "bold"))
label2.place(x =400, y = 110)

userName5 = StringVar()
textBox1 = Entry(pas_reset, textvar = userName5, width = 20, font = ("arial", 15, "bold"))
textBox1.place(x = 400, y = 150)

label3 = Label(pas_reset, text = " Enter New Password :",fg = "white", font = ("arial", 16, "bold"))
label3.place(x = 400, y = 190)

userName5 = StringVar()
textBox1 = Entry(pas_reset, textvar = userName5, width = 20, font = ("arial", 15, "bold"))
textBox1.place(x = 400, y = 230)
pasword5 = StringVar()
textBox2 = Entry(pas_reset, textvar = pasword5, width = 20, font = ("arial", 15, "bold"))
textBox2.place(x = 20, y = 230)

button1 = Button(pas_reset, text = "   Reset   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"),command=insert2 )
button1.place(x = 30, y = 280)
button1 = Button(pas_reset, text = "   Reset   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 16, "bold"),command=insert3)
button1.place(x = 430, y = 280)
button1 = Button(pas_reset, text = "   Exit   ", fg = "white", bg = "black", relief = "raised", font = ("arial", 10, "bold"), command=lambda:show(home))
button1.place(x = 355, y = 360)
  


######################################################################################################
show(regf)



root.mainloop()
