from tkinter import*
from tkinter import ttk
import sqlite3
root=Tk()  #create a tkinter window
root.geometry("860x500")   #set dimension of window
root.title('Student Management System')

regf=Frame(root,background="white")

add=Frame(root,background="white")
loginf=Frame(root,background="white")
home=Frame(root,background="white")
div=Frame(root,background="white")
intro=Frame(root,background="white")

add.place(x=0,y=0,width=860,height=500)
regf.place(x=0,y=0,width=860,height=500)
loginf.place(x=0,y=0,width=860,height=500)
home.place(x=0,y=0,width=860,height=500)
div.place(x=0,y=0,width=860,height=500)
intro.place(x=0,y=0,width=860,height=500)

root.wm_iconbitmap('icon.ico')

def show(frame):
    frame.tkraise()
for frame in (regf,loginf,home,add,div,intro):
    frame.place(x=0,y=0)
style = ttk.Style()
style.map("C.TButton",
    foreground=[('pressed', 'red'), ('active', 'blue')],
    background=[('pressed', '!disabled', 'black'), ('active', 'white')]
    )
Estyle = ttk.Style()
Estyle.configure('TEntry', foreground = 'green')

#-----------------------------------------------------------------------
db = sqlite3.connect('projectSMS.db')
my=db.cursor()
#-----------------------------------------------------------------------

#####_______Form____#########################################################
mylist=''
def register():
    try:
        num=0
        my=db.cursor()
        pop=my.execute("select*from hifi")
        for i in my:
            num=num+1
        num=num+1
        namer="'"+str(e1r.get())+"'"
        passwordr=str(e2r.get())
        my.execute(f"""Insert into hifi Values({num},{namer},{passwordr})""")
        db.commit()
        num=num+1
        m=Label(root, text="successfully registered",fg='green',
                font=('Kristen ITC', 15, 'bold'))
        root.after(100, lambda:m.pack())
        root.after(1000, lambda:m.pack_forget())
    except:
        namesr.delete(0,END)
        pwr.delete(0,END)
        m=Label(root, text="invalid username or password"
                ,font=('Kristen ITC', 15, 'bold'),fg='red')
        root.after(100, lambda:m.pack())
        root.after(1000, lambda:m.pack_forget())
        root.after(100, lambda:pwr.delete(0,END))
        root.after(1000, lambda:namesr.delete(0,END))
cls_1,cls_2,cls_3=(Label(home),Label(home),Label(home))
teacher,m,m4=(Label(home),Label(home),Label(home))

def login():
    global cls_1,cls_2,cls_3,teacher,m
    m=Label(root, text="incorrect username or password",font=('Kristen ITC', 15, 'bold'),fg='red')
    name=e1l.get()
    password=e2l.get()
    my=db.cursor()
    my.execute("select*from hifi")
    for i in my:
       if str(i[1])==name and str(i[2])==password:
          show(home)
          cls_1=Label(home,text='class teacher : ',
                      font=('Kristen ITC', 15, 'bold'),fg='#145862',bg='white')
          cls_1.place(x=20,y=10)
          cls_2=Label(home,text='class : ',font=('Kristen ITC', 15, 'bold')
                      ,fg='#145862',bg='white')
          cls_2.place(x=650,y=10)
          teacher=Label(home,text=name,font=('Comic Sans MS', 15, 'bold'),fg='green',bg='white')
          teacher.place(x=200,y=10)
          cls_3=Label(home,text='Xll',font=('Kristen ITC', 15, 'bold'),fg='green',bg='white')
          cls_3.place(x=730,y=10)
          namesl.delete(0,END)
          pwl.delete(0,END)
          break

        
    else:
        root.after(100, lambda:m.pack())
        root.after(1000, lambda:m.pack_forget())
        namesr.delete(0,END)
        pwr.delete(0,END)        
#-----------------------registration-----------------------------------------
canvas=Canvas(regf,width=60,height=60)
canvas.place(x=240,y=55)
profile=PhotoImage(file='user.png')
canvas.create_image(0,0,anchor=NW,image=profile)
adr=Label(regf,text="student management system",bg='white'
          ,font=('Kristen ITC', 25, 'bold'),fg='#d76737')
adr.pack()
l1r=Label(regf,text="username",font=('Kristen ITC', 25, 'bold'),fg='orange',bg='white')
l1r.place(x=240,y=120)
l2r=Label(regf,text="password",font=('Kristen ITC', 25, 'bold'),fg='orange',bg='white')
l2r.place(x=240,y=210)
e1r=StringVar()
namesr=ttk.Entry(regf,textvariable=e1r,font = ('Kristen ITC', 22, 'bold'))
namesr.focus_force()
namesr.place(x=240,y=175)
e2r=StringVar()
pwr=ttk.Entry(regf,textvariable=e2r,show='*',font = ('Kristen ITC', 22, 'bold'))
pwr.focus_force()
pwr.place(x=240,y=260)
submitr=ttk.Button(regf,text="sign up",width=20,command=register,style='C.TButton')
submitr.place(x=250,y=320)
logr=ttk.Button(regf,text="log in",width=20,command=lambda:show(loginf),style='C.TButton')
logr.place(x=450,y=320)
#-------------------------------------------------------------------------------------




#-----------------------login---------------------------------------------------------
canvas=Canvas(loginf,width=60,height=60)
canvas.place(x=240,y=55)
profile1=PhotoImage(file='user.png')
canvas.create_image(0,0,anchor=NW,image=profile1)

adl=Label(loginf,text="student management system",bg='white'
          ,font=('Kristen ITC', 25, 'bold'),fg='#d76737')
adl.pack()
l1l=Label(loginf,text="username",font=('Kristen ITC', 25, 'bold'),fg='orange',bg='white')
l1l.place(x=240,y=120)
l2l=Label(loginf,text="password",font=('Kristen ITC', 25, 'bold'),fg='orange',bg='white')
l2l.place(x=240,y=210)
e1l=StringVar()
namesl=ttk.Entry(loginf,textvariable=e1l,font = ('Kristen ITC', 22, 'bold'))
namesl.place(x=240,y=175)
e2l=StringVar()
pwl=ttk.Entry(loginf,textvariable=e2l,show='*',font = ('Kristen ITC', 22, 'bold'))
pwl.place(x=240,y=260)
submitl=ttk.Button(loginf,text="sign up",width=20,command=lambda:show(regf),style='C.TButton')
submitl.place(x=250,y=320)
logl=ttk.Button(loginf,text="log in",width=20,command=login ,style='C.TButton')
logl.place(x=450,y=320)
#-------------------------------------------------------------------------------------
st=ttk.Button(regf,text="start",width=30,command=lambda:show(home) ,style='C.TButton')
st.place(x=332,y=360)


#####_____function_______________###################################################
def backi():
    global style
    div_nma.delete(0,END)
    div_poia.delete(0,END)
    div_pera.delete(0,END)
    div_doba.delete(0,END)
    div_gena.delete(0,END)
    show(home)
#################___Home____###############################################################
####____tree view______####
def log_out():
    show(loginf)
tree=ttk.Treeview(home,height=15)
my.execute('select* from hifi')
tree['columns']=('sno','name','admission no.','percent','DOB','gender')
tree.column('#0',width=50)
tree.column('#1',width=220)
tree.column('#2',width=130)
tree.column('#3',width=100)
tree.column('#4',width=160)
tree.column('#5',width=140)
tree.column('#6',width=0)

tree.heading('#0',text='sno',)
tree.heading('#1',text='name')
tree.heading('#2',text='Admission no.')
tree.heading('#3',text='percent')
tree.heading('#4',text='DOB')
tree.heading('#5',text='Gender')
tree.heading('#6',text='')
sno=0

def veiw():
    global sno
#    sn=my.execute("select* from student")

    my.execute("select* from student")
#    sn=list(range(1,len(sn)+1))
    for i in my:
        sno=sno+1
        tree.insert('',str(sno),'item '+str(sno),text=sno
                    ,values=(i[0],i[1],i[2],i[3],i[4]))
    sno=0
tree.place(x=20,y=50)
veiw()
item='False'
def show_div():
    global item
    if 'item' in item: # item = 'item {any number}'
        show(div)
    else:
        pass        #print('not called')
sth=ttk.Button(home,text="veiw data",style='C.TButton',command=show_div)
sth.place(x=80,y=400)
logout=ttk.Button(home,text="log out",style='C.TButton',command=lambda:show(loginf))
logout.place(x=650,y=400)
adh=ttk.Button(home,text="add",width=10,command=lambda:show(add),style='C.TButton')
#show frame 'div' whene clicked
adh.place(x=240,y=400)
about=ttk.Button(home,text="about us",width=10,command=lambda:show(intro)
                 ,style='C.TButton')  #show frame 'div' whene clicked
about.place(x=540,y=400)
###############__add__################################################################
def insert():
  global style,sno
  no=0
  name="'"+str(nm1.get())+"'"
  admission="'"+str(p1.get())+"'"
  pc="'"+str(per1.get())+"'"
  dob="'"+str(dob1.get())+"'"
  gender="'"+str(gen1.get())+"'"
  if name=="''" or admission=="''":
      pass
  else:
      my.execute("insert into student values({},{},{},{},{})".format(name,admission,pc,dob,gender))
      db.commit()
      my.execute('select* from student')
      nma.delete(0,END)
      poia.delete(0,END)
      pera.delete(0,END)
      doba.delete(0,END)
      gena.delete(0,END)
      sno=0
      for i in my:
          sno=sno+1
          lst=i
      tree.insert('',str(sno),'item '+str(sno),text=sno,values=(lst[0],lst[1],lst[2],lst[3],lst[4]))   #insert into tree ,last row of table
      m4=Label(root, text="successfully added to database",font=('Kristen ITC', 15, 'bold'),fg='green')
      root.after(100, lambda:m4.pack())
      root.after(1500, lambda:m4.pack_forget())

add_name1=Label(add,text='name',bg='white',fg='#145862',font=('Kristen ITC', 15, 'bold'))
add_name1.place(x=50,y=100)
nm1=StringVar()
nma=ttk.Entry(add,textvariable=nm1 ,font = ('Kristen ITC', 10, 'bold'))
nma.place(x=50,y=130)
admis1=Label(add,text='admission no.',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
admis1.place(x=50,y=200)

p1=StringVar()
poia=ttk.Entry(add,textvariable=p1 ,font = ('Kristen ITC', 10, 'bold'))
poia.place(x=50,y=230)

percent1=Label(add,text='percent',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
percent1.place(x=350,y=220)
per1=StringVar()
pera=ttk.Entry(add,textvariable=per1 ,font = ('Kristen ITC', 10, 'bold'))
pera.place(x=350,y=250)

dob_1=Label(add,text='DOB',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
dob_1.place(x=350,y=100)
dob1=StringVar()
doba=ttk.Entry(add,textvariable=dob1 ,font = ('Kristen ITC', 10, 'bold'))
doba.place(x=350,y=130)

gender1=Label(add,text='Gender',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
gender1.place(x=350,y=160)
gen1=StringVar()
gena=ttk.Entry(add,textvariable=gen1 ,font = ('Kristen ITC', 10, 'bold'))
gena.place(x=350,y=190)

sub=ttk.Button(add,text="submit",command=insert,width=10,style='C.TButton')
sub.place(x=50,y=340)

back=ttk.Button(add,text="back",width=10,command=backi,style='C.TButton')
back.place(x=200,y=340)
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
        pass
    else:
        tree.delete('item '+str(dictc['text']))
        my.execute("delete from student where name={}".format(named))
        db.commit()
        div_nma.delete(0,END)
        div_poia.delete(0,END)
        div_pera.delete(0,END)
        div_doba.delete(0,END)
        div_gena.delete(0,END)
        m=Label(root, text="successfully removed from database",font=('Kristen ITC', 15, 'bold'),fg='green')
        root.after(10, lambda:m.pack())
        root.after(4500, lambda:m.pack_forget())
def update():
  global old_paw
  nm=str(div_nm1.get())
  pw=str(div_p1.get())
  pct=str(div_per1.get())
  dobt=str(div_dob1.get())
  gendert=str(div_gen1.get())

  name1="'"+str(div_nm1.get())+"'"
  paw1="'"+str(div_p1.get())+"'"
  pc="'"+str(div_per1.get())+"'"
  dob="'"+str(div_dob1.get())+"'"
  gender="'"+str(div_gen1.get())+"'"
  my.execute("update student set name={},admisson={},percent={},dob={},gender={} where admisson={}".format(name1,paw1,pc,dob,gender,old_paw))
  db.commit()
  m3=Label(root, text="successfully updated",font=('Kristen ITC', 15, 'bold'),fg='green')
  root.after(100, lambda:m3.pack())
  root.after(1500, lambda:m3.pack_forget())
  if nm=='' or pw.isspace():
      pass
  else:
      item=tree.focus()
      tree.item(item,values=(nm,pw,pct,dobt,gendert))  # it is use to update tree
div_sub=ttk.Button(div,text="update",command=update,width=10,style='C.TButton')
div_sub.place(x=60,y=340)

div_del=ttk.Button(div,text="delete",command=delete,width=10,style='C.TButton')
div_del.place(x=160,y=340)

back=ttk.Button(div,text="back",width=10,command=backi,style='C.TButton')
back.place(x=260,y=340)
######
up_name=Label(div,text='name',bg='white',fg='#145862',font=('Kristen ITC', 15, 'bold'))
up_name.place(x=50,y=100)
div_nm1=StringVar()
div_nma=ttk.Entry(div,textvariable=div_nm1 ,font = ('Kristen ITC', 10, 'bold'))
div_nma.place(x=50,y=130)

admis2=Label(div,text='admission no.',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
admis2.place(x=50,y=200)

div_p1=StringVar()
div_poia=ttk.Entry(div,textvariable=div_p1 ,font = ('Kristen ITC', 10, 'bold'))
div_poia.place(x=50,y=230)

percent2=Label(div,text='percent',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
percent2.place(x=350,y=220)
div_per1=StringVar()
div_pera=ttk.Entry(div,textvariable=div_per1 ,font = ('Kristen ITC', 10, 'bold'))
div_pera.place(x=350,y=250)

dob_2=Label(div,text='DOB',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
dob_2.place(x=350,y=100)
div_dob1=StringVar()
div_doba=ttk.Entry(div,textvariable=div_dob1 ,font = ('Kristen ITC', 10, 'bold'))
div_doba.place(x=350,y=130)

gender2=Label(div,text='Gender',fg='#145862',bg='white',font = ('Kristen ITC', 15, 'bold'))
gender2.place(x=350,y=160)
div_gen1=StringVar()
div_gena=ttk.Entry(div,textvariable=div_gen1 ,font = ('Kristen ITC', 10, 'bold'))
div_gena.place(x=350,y=190)
######################################################################################################
#########_intro___________________________############################################################
bg_color='white'

team=Label(intro,text='Team member',font = ('Kristen ITC', 25, 'bold'),bg='white',fg='#ff0303')
team.pack()

n1=Label(intro,text='i)   Rohit kumar',font = ('Kristen ITC', 15, 'bold'),bg='white',fg='#0061b0')
n1.place(x=10,y=100)
n2=Label(intro,text='ii)  om prakash',font = ('Kristen ITC', 15, 'bold'),bg='white',fg='#0061b0')
n2.place(x=10,y=150)
n3=Label(intro,text='iii) sanya santosh',font = ('Kristen ITC', 15, 'bold'),bg='white',fg='#0061b0')
n3.place(x=10,y=200)
n4=Label(intro,text='Computer teacher',font = ('Kristen ITC', 15, 'bold'),bg='white',fg='red')
n4.place(x=10,y=250)

n5=Label(intro,text='#Kumar Gaurav',font = ('Kristen ITC', 15, 'bold'),bg='white',fg='#0061b0')
n5.place(x=10,y=300)

ttk.Button(intro,text="back",width=30,command=lambda:show(home),style='C.TButton').place(x=330,y=340)

canvas=Canvas(intro,width=225,height=225)
canvas.place(x=550,y=70)

profile2=PhotoImage(file='python2.png')
canvas.create_image(0,0,anchor=NW,image=profile2)
tuples1=('intro','team','regf','add','div','home','loginf','n1','n2','n3','adr','l1r','l2r','adl','l1l','l2l','add_name1','admis1','percent1','dob_1','gender1')
tuples2=('up_name','admis2','percent2','dob_2','gender2','cls_1','cls_2','cls_3','teacher','m','m4','n4','n5')
tuples=tuples1+tuples2
style=ttk.Style(root)

def normal():
    global tuples
    dark.config(text='dark mode',command=dark_mode)
    for i in tuples:
        eval(i).config(bg='white')
    style.configure('Treeview',background='white',foreground='black',fieldbackground='black')
    profile.config(file='user.png')
    profile1.config(file='user.png')
    profile2.config(file='python2.png')
    canvas.config(bg='white')
   

'''
    n1.config(bg='white')
    n2.config(bg='white')
    n3.config(bg='white')
    team_meamber.config(bg='white')
'''

def dark_mode():
    global tuples
    dark.config(text='normal',command=normal)
    style.configure('Treeview',background='black',foreground='white',fieldbackground='black')#To change the color of the Treeveiw
    for i in tuples:
        eval(i).config(bg='black')
    profile.config(file='man.png')
    profile1.config(file='man.png')
    profile2.config(file='python.png')
    profile2.config(file='python.png')
    canvas.config(bg='black')

'''
    n1.config(bg='black')
    n2.config(bg='black')
    n3.config(bg='black')
    team_meamber.config(bg='black')
'''
dark=ttk.Button(intro,text="dark mode",width=10,command=dark_mode,style='C.TButton')
dark.place(x=630,y=340)
######################################################################################################
show(regf)











































root.mainloop()
