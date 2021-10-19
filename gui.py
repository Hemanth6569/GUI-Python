from tkinter import *
from tkinter import messagebox
root=Tk()

def total():
    t5.delete(0,20)
    c=int(t3.get())+int(t4.get())
    t5.insert(0,c)
def avg():
    t6.delete(0,20)
    c=(int(t3.get())+int(t4.get()))/2
    t6.insert(0,c)
def res():
    t7.delete(0,20)
    if ((int(t3.get())>35 and int(t4.get())>35)):
        c="pass"
    else :
        c="fail"
    t7.insert(0,c)
def div():
    t8.delete(0,20)
    if ((int(t3.get())>35 and int(t4.get())>35)):
        if ((int(t3.get())+int(t4.get()))/2)>60:
            c="first class"
        elif ((int(t3.get())+int(t4.get()))/2)>50:
            c="second class"
        elif ((int(t3.get())+int(t4.get()))/2)>35:
            c="third class"
    else:
        c="no division"
    t8.insert(0,c)
def new():
    t1.delete(0,20)
    t2.delete(0,20)
    t3.delete(0,20)
    t4.delete(0,20)
    t5.delete(0,20)
    t6.delete(0,20)
    t7.delete(0,20)
    t8.delete(0,20)
    t1.focus()
def insert():
    import pymysql
    conn=pymysql.connect(host="localhost",user="root",db="test",password="Hemanth@143")
    cur=conn.cursor()
    cur.execute("insert into table1 values ('"+t1.get()+"',"+t2.get()+","+t3.get()+","+t4.get()+","+t5.get()+","+t6.get()+",'"+t7.get()+"','"+t8.get()+"')")
    conn.commit()
    cur.close()
    conn.close()
    t1.delete(0,20)
    t2.delete(0,20)
    t3.delete(0,20)
    t4.delete(0,20)
    t5.delete(0,20)
    t6.delete(0,20)
    t7.delete(0,20)
    t8.delete(0,20)
    t1.focus()
    messagebox.showinfo("insert status","inserted succesfully")
def update():
    import pymysql
    conn=pymysql.connect(host="localhost",user="root",db="test",password="Hemanth@143")
    cur=conn.cursor()
    cur.execute("update table1 set p1="+t3.get()+",p2="+t4.get()+",total="+t5.get()+",avg="+t6.get()+",res='"+t7.get()+"',divi='"+t8.get()+"' where num="+t2.get()+"")
    conn.commit()
    cur.close()
    conn.close()
    t1.delete(0,20)
    t2.delete(0,20)
    t3.delete(0,20)
    t4.delete(0,20)
    t5.delete(0,20)
    t6.delete(0,20)
    t7.delete(0,20)
    t8.delete(0,20)
    t1.focus()
    messagebox.showinfo("update status","Updated succesfully")
def delete():
    import pymysql
    conn=pymysql.connect(host="localhost",user="root",db="test",password="Hemanth@143")
    cur=conn.cursor()
    cur.execute("delete from table1 where num="+t2.get()+"")
    conn.commit()
    cur.close()
    conn.close()
    t2.delete(0,20)
    t1.focus()
    messagebox.showinfo("delete status","Deleted succesfully")
def search():
    import pymysql
    conn=pymysql.connect(host="localhost",user="root",db="test",password="Hemanth@143")
    cur=conn.cursor()
    cur.execute("select * from table1 where num="+t2.get()+"")
    conn.commit()
    for i in cur:
        l=i
    t1.insert(0,l[0])
    t3.insert(0,l[2])
    t4.insert(0,l[3])
    t5.insert(0,l[4])
    t7.insert(0,l[6])
    t6.insert(0,l[5])
    t8.insert(0,l[7])
    cur.close()
    conn.close()
    

root.geometry("800x800+50+50")
root.config(bg="light blue")
root.title("STUDENT FORM")

#creation of the lable
l1=Label(root,text="Student form ",font=("times new roman bold",20),bg="light blue")
l1.place(x=270,y=20)
l2=Label(root,text="Student name ",font=("times new roman",15),bg="light blue")
l2.place(x=50,y=100)
l3=Label(root,text="Student number ",font=("times new roman",15),bg="light blue")
l3.place(x=400,y=100)
l4=Label(root,text="Paper1 Marks ",font=("times new roman",15),bg="light blue")
l4.place(x=50,y=200)
l5=Label(root,text="Paper2 Marks ",font=("times new roman",15),bg="light blue")
l5.place(x=400,y=200)
l6=Label(root,text="Total ",font=("times new roman",15),bg="light blue")
l6.place(x=50,y=300)
l7=Label(root,text="Average ",font=("times new roman",15),bg="light blue")
l7.place(x=400,y=300)
l8=Label(root,text="Result ",font=("times new roman",15),bg="light blue")
l8.place(x=50,y=400)
l9=Label(root,text="Divison ",font=("times new roman",15),bg="light blue")
l9.place(x=400,y=400)

#creation of text box
t1=Entry(root,width=20)
t1.place(x=200,y=100)
t2=Entry(root,width=20)
t2.place(x=600,y=100)
t3=Entry(root,width=20)
t3.place(x=200,y=200)
t4=Entry(root,width=20)
t4.place(x=600,y=200)
t5=Entry(root,width=20)
t5.place(x=200,y=300)
t6=Entry(root,width=20)
t6.place(x=600,y=300)
t7=Entry(root,width=20)
t7.place(x=200,y=400)
t8=Entry(root,width=20)
t8.place(x=600,y=400)

#creation of button
b1=Button(root,text="Total",width=10,command=total)
b1.place(x=250,y=500)
b2=Button(root,text="Avarage",width=10,command=avg)
b2.place(x=500,y=500)
b3=Button(root,text="Result",width=10,command=res)
b3.place(x=250,y=550)
b4=Button(root,text="Division",width=10,command=div)
b4.place(x=500,y=550)
b5=Button(root,text="New",width=10,command=new)
b5.place(x=250,y=600)
b6=Button(root,text="Cancel",width=10,command=root.destroy)
b6.place(x=500,y=600)
b7=Button(root,text="insert",width=10,command=insert)
b7.place(x=250,y=650)
b8=Button(root,text="Update",width=10,command=update)
b8.place(x=375,y=650)
b9=Button(root,text="Delete",width=10,command=delete)
b9.place(x=500,y=650)
b10=Button(root,text="Search",width=10,command=search)
b10.place(x=375,y=700)


t1.focus()
root.mainloop()

