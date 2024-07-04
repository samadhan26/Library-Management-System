from tkinter import *
from tkinter.messagebox import*
import tkinter as tk
from tkinter import ttk
import datetime
from tkinter.scrolledtext import*
from tkinter import messagebox
from datetime import datetime, date, timedelta
import customtkinter as ctk
import mysql.connector
import pymysql
from PIL import Image,ImageTk 


# ======================================================================================================
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="abc123",
port="3306",
auth_plugin='mysql_native_password'
)




from datetime import date

datetime = date.today()
print("Today's date:", datetime)




try:
	con = pymysql.connect(host='localhost', port=3306, user='root', password='abc123')

	with con.cursor() as cursor:
		cursor.execute("CREATE DATABASE IF NOT EXISTS pythongui")
		cursor.execute("use pythongui")
		with con.cursor() as cursor:cursor.execute("""CREATE TABLE IF NOT EXISTS register (
            	id INT AUTO_INCREMENT PRIMARY KEY,
		username VARCHAR(50) NOT NULL,
		password VARCHAR(50) NOT NULL)""")
except Exception as es:
	messagebox.showerror('Error',f'Error Due to : {str(es)}')



#===========================================================================================================================================

print(mydb)


mycursor=mydb.cursor()
mycursor.execute("use lib")

mycursor.execute(" CREATE TABLE IF NOT EXISTS Addbook(Book_ID int primary key auto_increment,Title varchar(20),Author varchar(20) not null,Edition varchar(20),Publication varchar(20),Price float unsigned )")

if(mydb):
	print('connected')

else:
	print('not connected')

#==============================================================================================================================================================


# ======================================================================================================================
def f1():
	if user_txt.get()=="" or password.get()=="":
		messagebox.showerror("Error","All fields are required")
     
	else:

         try:

            con=pymysql.connect(host='localhost',port=3308,user='root',password='abc123', database='pythongui')

            mycursor=con.cursor()

            mycursor.execute('select * from register where username=%s and password=%s',(user_txt.get(),password.get()))

            row=mycursor.fetchone()
            if row==None:

               messagebox.showerror('Error','Invalid Username And Password')
		   
               user_txt.focus()
               
            else:

               root.withdraw()
               mw.deiconify()
               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}')
	
#====================================================================================================================
def f2():
	user_txt.delete(0,END)
	password.delete(0,END)
	user_txt.focus()	
	root.deiconify()
	mw.withdraw()


#===================================================================================================================
def f3():
	RW.deiconify()
	root.withdraw()
#=============================================================================================
def f4():
	root.deiconify()
	RW.withdraw()
# ===============================================================================================
def f5():
	if entry.get()==""or entry2.get()==""or entry3.get()==""or entry4.get()=="":
    
         messagebox.showerror("Error","All Fields Are Required")
	elif entry2.get()!=entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same" )

	else:

         try:

            con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="pythongui")

            mycursor=con.cursor()

            mycursor.execute("select * from register where emailid=%s",entry3.get())

            row=mycursor.fetchone()

            if row!=None:

               messagebox.showerror("Error","User already Exist,Please try with another Email")

               

               entry.focus()

            else:

               mycursor.execute("insert into register values(%s,%s,%s,%s)",(entry.get(),entry3.get(),entry2.get(),entry4.get()))

               con.commit()

               con.close()
               messagebox.sh
               owinfo("Success","Register Succesfull")
               RW.withdraw()
               root.deiconify()
               

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}")
            
# ==========================================================================================================
def f6():
	addw.deiconify()
	mw.withdraw()
#===================================================================================================
def f7():
	mw.deiconify()
	addw.withdraw()
#===================================================================================================
def f8():
	IW.deiconify()
	


	mw.withdraw()
#===================================================================================================	
def f9():
	mw.deiconify()
	IW.withdraw()
#===================================================================================================
def f10():
	rw.deiconify()
	mw.withdraw()
#===================================================================================================
def search():


	if Entry_BID.get()=="" or Entry_SID.get()=="":
		messagebox.showerror=("Error","Enter Book ID and student ID")

	else:
		try:
			con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
			mycursor=con.cursor()

			mycursor.execute("select * from Issue_Book where Book_ID ='"+Entry_BID.get()+"' and student_ID='"+Entry_SID.get()+"'")

			

			if mycursor==None:
				messagebox.showerroe("Error","Entry is not found" )

			else:

				data=mycursor.fetchall()
				for d in data:
					


					if Entry_BID=="" or Entry_SID=="":
						messagebox.showerror("Error","")


					rw2.deiconify()
     
					BID.delete(0,END)
					BID.insert(END,d[1])

					SID.delete(0,END)
					SID.insert(END,d[2])

					ISD.delete(0,END)
					ISD.insert(END,d[3])

					DD.delete(0,END)
					DD.insert(END,d[4])

					RD.delete(0,END)
					RD.insert(END,today)
		
		except Exception as e:
			
			BID.delete(0,END)
			SID.delete(0,END)
			ISD.delete(0,END)
			messagebox.showerror('Error',"Entry Not found")


def ReturnBook():

	
	try:

		table3.delete(*table3.get_children())
		
		con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
		mycursor=con.cursor()

		mycursor.execute("use lib")
		mycursor.execute("delete from Issue_book where Book_ID ='"+Entry_BID.get()+"' and student_ID='"+Entry_SID.get()+"'")


		insert_query=("Insert into `IRdetail`(`Book_ID`, `Student_ID`, `Issue_Date`,`Due_date`, `Return_Date`)values(%s,%s,%s,%s,%s)")
		vals=(BID.get(),SID.get(),ISD.get(),DD.get(),RD.get())

		mycursor.execute(insert_query,vals)
		messagebox.showinfo("Sucsees","Book return successfully")


		mycursor.execute("use lib")
		mycursor.execute("select * from IRdetail ")
		for d in mycursor:
			table3.insert('',"end",text="d[0]",values=(d[0],d[1],d[2],d[3],d[4]))



		str_d1 = DD.get()
		str_d2 = RD.get()

	
# convert string to date object
		d1 = datetime.strptime(str_d1, "%Y-%m-%d")
		d2 = datetime.strptime(str_d2, "%Y-%m-%d")

# difference between dates in timedelta
		delta = d2 - d1
		print(f'Difference is {delta.days} days')
		print(delta.days)

		if delta.days<=0:
			entLate_days.insert(END,0)
			Entry_Fine.insert(END,0)

		elif (delta.days>0 and delta.days<= 5):
			amt = 0.50 * days
			entLate_days.insert(END,delta.days)
			Entry_Fine.insert(END,amt)
			print("Fine Amount Pay to Rs :", amt)
 
		elif(delta.days >= 6 and delta.days <= 10):
			amt = 1 * delta.days
			entLate_days.insert(END,delta.days)
			Entry_Fine.insert(END,amt)
			print("Fine Amount Pay to Rs :", amt)
 
		elif (delta.days > 10 and delta.days<=30):
			amt = 5 * delta.days
			entLate_days.insert(END,delta.days)
			Entry_Fine.insert(END,amt)
			print("Fine Amount Pay to Rs :", amt)
		elif (delta.days >30):
			amt = 5 * delta.days
			entLate_days.insert(END,delta.days)
			Entry_Fine.insert(END,amt)
			messagebox.showinfo("Warning","Your Membership would be Cancelled..")
			print("Your Membership would be Cancelled..")
		else:
			print("Invalid")


		FW.deiconify()


		con.commit()
		con.close()
  
	except Exception as es:
		 messagebox.showerror("Error",f"Error due to:{str(es)}")


	BID.delete(0,END)
	SID.delete(0,END)
	ISD.delete(0,END)
	RD.delete(0,END)
	BID.focus()
	rw2.withdraw()


def IRdetails():
	IRW.deiconify()
	mw.withdraw()

#===================================================================================================

def f12():
	RD.delete(0,END)
	mw.deiconify()
	rw.withdraw()
	rw2.withdraw()

def f13():

	con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
	mycursor=con.cursor()
	
	
	Entry_Title.get()
	Entry_Author.get()
	Entry_Edition.get()
	Entry_Publication.get()
	Entry_Price.get()

	if  Entry_Title.get()=="" or Entry_Author.get()=="" or Entry_Edition.get()=="" or Entry_Publication.get()=="" or Entry_Price.get()=="":
		 messagebox.showerror("Error","All Fields Are Required")

	elif (len(Entry_Title.get())==1):
		showerror("Error","Enter Correct Title")
		Entry_Title.delete(0,END)
		Entry_Title.focus()


	elif (Entry_Title.get().isdigit()):
		showerror("Error","Enter Correct Title:Enter only alphabets")
		Entry_Title.delete(0,END)
		Entry_Title.focus()

	elif(not Entry_Title.get().isalpha()):
		showerror("Error","Enter Correct Title:Enter only alphabets")
		Entry_Title.delete(0,END)
		Entry_Title.focus()


	elif(len(Entry_Author.get())==1):
		showerror("Error","Enter Correct Author_name")
		Entry_Author.delete(0,END)
		Entry_Author.focus()


	elif(Entry_Author.get().isdigit()):
		showerror("Error","Enter Correct Author_name:Enter only alphabets")
		Entry_Author.delete(0,END)
		Entry_Author.focus()
	elif(not Entry_Author.get().isalpha()):
		showerror("Error","Enter Correct Author:Enter only alphabets")
		Entry_Author.delete(0,END)
		Entry_Author.focus()

	elif(len(Entry_Publication.get())==1):
		showerror("Error","Enter Correct Publication_name")
		Entry_Publication.delete(0,END)
		Entry_Publication.focus()	


	elif( Entry_Publication.get().isdigit()):
		showerror("Error","Enter Correct Publication_name:Enter only alphabets")
		Entry_Publication.delete(0,END)
		Entry_Publication.focus()

	elif(not Entry_Publication.get().isalpha()):
		showerror("Error","Enter Correct Publication_Name:Enter only alphabets")
		Entry_Publication.delete(0,END)
		Entry_Publication.focus()



	elif(len(Entry_Edition.get())==1):
		showerror("Error","Enter Correct Edition:")
		Entry_Edition.delete(0,END)
		Entry_Edition.focus()




	elif(Entry_Edition.get().isdigit()):
		showerror("Error","Enter Correct Edition")
		Entry_Edition.delete(0,END)
		Entry_Edition.focus()
	elif(not Entry_Edition.get().isalnum()):
		showerror("Error","Enter Correct Edition")
		Entry_Edition.delete(0,END)
		Entry_Edition.focus()

	elif(len(Entry_Edition.get())==1):
		showerror("Error","Enter correct Price")
		Entry_Price.delete(0,END)
		Entry_Price.focus()
		


	elif(not Entry_Price.get().isdigit()):
		showerror("Error","Enter correct Price:Enter only Digits")
		Entry_Price.delete(0,END)
		Entry_Price.focus()


	elif(Entry_Price.get().isalpha()):
		showerror("Error","Enter Correct Price:Enter only Digits")
		Entry_Price.delete(0,END)
		Entry_Price.focus()



	else:
	

		try:
			table2.delete(*table2.get_children())

			mycursor.execute("use lib")
			
			insert_query="Insert into `Addbook`(`Title`,`Author`,`Edition`,`Publication`,`Price`)values(%s,%s,%s,%s,%s)"
			vals=(Entry_Title.get(),Entry_Author.get(),Entry_Edition.get(),Entry_Publication.get(),Entry_Price.get())


			mycursor.execute(insert_query,vals)
	
			messagebox.showinfo("Success","Book Add Succesfull")
   
			Entry_Title.delete(0,END)
			Entry_Author.delete(0,END)
			Entry_Edition.delete(0,END)
			Entry_Publication.delete(0,END)
			Entry_Price.delete(0,END)
			Entry_Title.focus()
		
			mycursor.execute("select * from addbook")
			for d in mycursor:
				table2.insert('',"end",text="d[0]",values=(d[0],d[1],d[2],d[3],d[4],d[5]))
			
			con.commit()
			con.close()

		except Exception as e:
			messagebox.showerror('Error',f"Error dur to:{str(e)}")

# ============================================================================================================================

def f14():
	vsw.deiconify()
	mw.withdraw()

#===================================================================================================

def f15():
	vbw.deiconify()
	mw.withdraw()
#===================================================================================================

def f16():
	mw.withdraw()
	asw.deiconify()
#===================================================================================================

def f17():
	mw.deiconify()
	asw.withdraw()
#===================================================================================================

def f18():


	if entBook_ID.get()=="" or entStudent_ID.get()=="" or entIssue_Date.get()=="" or entDue_Date.get()=="":


		messagebox.showerror("Error","All Fields Are Required")


	else:
	

		try:

			con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
			mycursor=con.cursor()

		
			insert_query="Insert into `Issue_Book`(`Book_ID`,`Student_ID`,`Issue_Date`,`Due_date`)values(%s,%s,%s,%s)"
			vals=(entBook_ID.get(),entStudent_ID.get(),entIssue_Date.get(),entDue_Date.get())


			mycursor.execute(insert_query,vals)
			messagebox.showinfo("Success","Issue book Succesfully")

			
			con.commit()
			con.close()
			
		except Exception as e:
			messagebox.showerror('Error',"Data not found")

	entBook_ID.delete(0,END)
	entStudent_ID.delete(0,END)
	
	entBook_ID.focus()

		
#===================================================================================================

def f19():
	mw.deiconify()
	vsw.withdraw()
#===================================================================================================

def f20():
	con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
	mycursor=con.cursor()
	

	if ent1.get()=="" or ent2.get()=="" or ent3.get()==""  or ent4.get()=="":
			messagebox.showerror("Error","All Fields Are Required")


	elif (len(ent1.get())==1):
			showerror("Error","Enter Correct name")
			ent1.delete(0,END)
			ent1.focus()		

	elif (ent1.get().isdigit()):
			showerror("Error","Enter Correct name:Enter only alphabets")
			ent1.get().delete(0,END)
			ent1.focus()


	elif(not ent1.get().isalpha() and not ent1.get().isspace()):
			showerror("Error","Enter Correct name:Enter only alphabets")
			ent1.delete(0,END)
			ent1.focus()


	elif (len(ent2.get())==1):
			showerror("Error","Enter Correct Department_Name")
			ent2.delete(0,END)
			ent2.focus()	

	elif( ent2.get().isdigit()):
			showerror("Error","Enter Correct Department Name:Use only alphabets")
			ent2.get().delete(0,END)
			ent2.focus()
	elif(not ent2.get().isalpha()):
			showerror("Error","Enter Correct Department Name:Use only alphabets")
			ent2.delete(0,END)
			ent2.focus()


	elif(not ent3.get().isdigit):
			showerror("Erroe","Enter 10 Digit Mobile number")
			ent3.delete(0,END)
			ent3.focus()


	elif(len(ent3.get())!=10):
			showerror("Erroe","Enter 10 Digit Mobile number")
			ent3.delete(0,END)
			ent3.focus()
	

	elif(not ent4.get().isalnum):
			showerror("Erroe","Enter correct GR number")
			ent4.focus()
	elif(len(ent4.get())!=8):
			showerror("Erroe","Enter correct GR number")
			ent4.focus()


	else:
		try:
			table.delete(*table.get_children())
			mycursor.execute("use lib")
			insert_query=("Insert into `Student`( `Student_Name`,`Department`, `Mobile_number`,  `G_R_number`)values(%s,%s,%s,%s)")
			vals=(ent1.get(),ent2.get(),ent3.get(),ent4.get())

			mycursor.execute(insert_query,vals)
			messagebox.showinfo("Success","Student Add Succesfull")

			ent1.delete(0,END)
			ent2.delete(0,END)
			ent3.delete(0,END)
			ent4.delete(0,END)
			ent1.focus()

			mycursor.execute("use lib")
			mycursor.execute("select * from student ")
			for d in mycursor:
				table.insert('',"end",text="d[0]",values=(d[0],d[1],d[2],d[3],d[4]))
			
					

			con.commit()
			con.close()

		except Exception as e:
			messagebox.showerror('Error',f"Error dur to:{str(e)}")

	

#===================================================================================================

def f21():

	vbw.withdraw()
	mw.deiconify()

#===================================================================================================

def f22():
	vsw.withdraw()

	mw.deiconify()
#===================================================================================================
def f23():
	scroll_box.delete(1.0,END)
	IRW.withdraw()
	mw.deiconify()

def searchbook():
	if EBID.get()=="":

		messagebox.showerror("Error","Enter Book ID")

	elif ESID.get()=="":
		messagebox.showerror("Error","Enter Student ID")

	else:
		try:
			con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
			mycursor=con.cursor()

			mycursor.execute("use lib")
			mycursor.execute("select * from addbook where Book_ID=%s",(EBID.get()))
			data=mycursor.fetchall()
			msg=""

			scroll_box.delete(1.0,END)
			for d in data:
				msg=msg+"Book_Name    :"+str(d[1])+"\n"+"Author_Name  :  "+str(d[2])+"\n"+"Book_Price     :"+str(d[5])+"\n"+"*********************************************"+"\n"
				
				


			mycursor.execute("use lib")
			mycursor.execute("select * from student where student_ID=%s",(ESID.get()))
			data=mycursor.fetchall()
			
			
			for s in data:
				msg2=msg+"Student_Name    :"+str(s[1])+"\n"+"Department  :  "+str(s[2])+"\n"+"Mobile No.     :"+str(s[3])+"\n"+"*********************************************"+"\n"
				
				scroll_box.insert(INSERT,msg2)
				EBID.delete(0,END)
				ESID.delete(0,END)


		except Exception as e:
			showerror("Issue",e)
		finally:
			if con is not None:
				con.close()


def f24():
	rw2.withdraw()
	rw.withdraw()
	mw.deiconify()

	

def select_data():
	curItem=table.focus()
	values=table.item(curItem,"values")
	print(values)
	update_frame=Frame(vsw,bg='white')
	update_frame.place(x=320,y=340,height=450,width=500)


	label=Label(update_frame,text="Enter Student Name ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=80)
	ent1=Entry(update_frame,font=("times new roman",18,"bold"),bg="lightgray")
	ent1.place(x=280,y=85)


	label=Label(update_frame,text="Enter Department",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=130)
	ent2=Entry(update_frame,font=("times new roman",18,"bold"),bg="lightgray")
	ent2.place(x=280,y=135)



	label=Label(update_frame,text="Enter Mobile NO.",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=180)
	ent3=Entry(update_frame,font=("times new roman",18,"bold"),bg="lightgray")
	ent3.place(x=280,y=185)


	label=Label(update_frame,text="Enter GR No.",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=230)
	ent4=Entry(update_frame,font=("times new roman",18,"bold"),bg="lightgray")
	ent4.place(x=280,y=235)


	ent1.insert(0,values[1])
	ent2.insert(0,values[2])
	ent3.insert(0,values[3])
	ent4.insert(0,values[4])


	def update_data():


	
		if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="":
		
			messagebox.showerror("Error","All fields are required")



		elif (len(ent1.get())==1):
				showerror("Error","Enter Correct name")
				ent1.delete(0,END)
				ent1.focus()

		elif (ent1.get().isdigit()):
				showerror("Error","Enter Correct name:Enter only alphabets")
				ent1.delete(0,END)
				ent1.focus()
		elif(not ent1.get().isalpha()):
			showerror("Error","Enter Correct name:Enter only alphabets")
			ent1.delete(0,END)
			ent1.focus()

		elif (len(ent2.get())==1):
			showerror("Error","Enter Correct name")
			ent2.delete(0,END)
			ent2.focus()


		elif( ent2.get().isdigit()):
			showerror("Error","Enter Correct Department Name:Use only alphabets")
			ent1.delete(0,END)
			ent2.focus()
		elif(not ent2.get().isalpha()):
			showerror("Error","Enter Correct Department Name:Use only alphabets")
			ent1.delete(0,END)
			ent2.focus()


		elif(len(ent3.get())!=10):
			showerror("Erroe","Enter 10 Digit Mobile number")
			ent3.delete(0,END)
			ent3.focus()
		elif (not ent3.get().isdigit()):
			showerror("Error","Enter Correct name:Enter only Digit")
			ent1.delete(0,END)
			ent1.focus()



		elif(not ent4.get().isalnum):
			showerror("Erroe","Enter correct GR number")
			ent4.delete(0,END)

			ent4.focus()
		elif(len(ent4.get())!=8):
			showerror("Erroe","Enter correct GR number")
			ent4.delete(0,END)
			ent4.focus()



		else:
			con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
			mycursor=con.cursor()
	
			st_name=ent1.get()

			dpt=ent2.get()
			mb=ent3.get()
			GR=ent4.get()
			table.item(curItem,values=(values[0],st_name,dpt,mb,GR))
			mycursor.execute("update student set student_name=%s,Department=%s,Mobile_Number=%s,G_R_number=%s where student_ID=%s",(st_name,dpt,mb,GR,values[0]))
			messagebox.showinfo("Success","Student data Updated")
			ent1.delete(0,END)
			ent2.delete(0,END)
			ent3.delete(0,END)
			ent4.delete(0,END)
			ent1.focus()
		

			table.item(curItem,values=(values[0],st_name,dpt,mb,GR))
		
			con.commit()
			con.close()
	update = ctk.CTkButton(update_frame,height=20,width=60, text = 'Update', command=update_data,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
	update.place(x=30,y=300)

	back= ctk.CTkButton(update_frame,height=20,width=60,text = 'Back',command=update_frame.destroy,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
	back.place(x=280,y=300)


def delete_data():
	try:

	
		con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
		mycursor=con.cursor()
		selected_item=table.selection()[0]
		st_id=table.item(selected_item)['values'][0]
		mycursor.execute("delete from student where student_ID=%s",st_id)
		con.commit()
		con.close()
		table.delete(selected_item)
		messagebox.showinfo("success","Data deleted")
	except Exception as e:
		mb.showerror("Error",{str(e)})


def select_bdata():
	curItem=table2.focus()
	values=table2.item(curItem,"values")
	print(values)
	update_bframe=Frame(vbw,bg='white')
	update_bframe.place(x=320,y=340,height=500,width=545)




	label=Label(update_bframe,text="Enter Title ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=80)
	ent1=Entry(update_bframe,font=("times new roman",18,"bold"),bg="lightgray")
	ent1.place(x=280,y=85)


	label=Label(update_bframe,text="Enter Author",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=130)
	ent2=Entry(update_bframe,font=("times new roman",18,"bold"),bg="lightgray")
	ent2.place(x=280,y=135)



	label=Label(update_bframe,text="Enter Edition.",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=180)
	ent3=Entry(update_bframe,font=("times new roman",18,"bold"),bg="lightgray")
	ent3.place(x=280,y=185)


	label=Label(update_bframe,text="Enter Publication",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=230)
	ent4=Entry(update_bframe,font=("times new roman",18,"bold"),bg="lightgray")
	ent4.place(x=280,y=235)

	label=Label(update_bframe,text="Enter Price",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
	label.place(x=30,y=280)
	ent5=Entry(update_bframe,font=("times new roman",18,"bold"),bg="lightgray")
	ent5.place(x=280,y=285)





	ent1.insert(0,values[1])
	ent2.insert(0,values[2])
	ent3.insert(0,values[3])
	ent4.insert(0,values[4])
	ent5.insert(0,values[5])


	def update_bdata():


	
		if ent1.get()=="" or ent2.get()=="" or ent3.get()=="" or ent4.get()=="" or ent5.get()=="":
		
			messagebox.showerror("Error","All fields are required")


		elif(ent1.get().isdigit()):
			showerror("Error","Enter Correct Title:Enter only alphabets")
			ent1.delete(0,END)
			ent1.focus()

		elif(len(ent1.get())==1):
			showerror("Error","Enter Correct Title")
			ent1.delete(0,END)
			ent1.focus()



		elif(not ent1.get().isalpha()):
			showerror("Error","Enter Correct Title:Enter only alphabets")
			ent1.delete(0,END)
			ent1.focus()



		elif(len(ent2.get())==1):
			showerror("Error","Enter Correct Author_Name")
			ent2.delete(0,END)
			ent2.focus()


		elif(ent2.get().isdigit()):
			showerror("Error","Enter Correct Author_name:Enter only alphabets")
			ent2.delete(0,END)
			ent2.focus()
		elif(not ent2.get().isalpha()):
			showerror("Error","Enter Correct Author:Enter only alphabets")
			ent2.delete(0,END)
			ent2.focus()



		elif(len(ent3.get())==1):
			showerror("Error","Enter Correct Edition")
			ent3.delete(0,END)
			ent3.focus()


		elif(ent3.get().isalpha()):
			showerror("Error","Enter Correct Edition")
			ent3.delete(0,END)
			ent3.focus()

		elif( not ent3.get().isalnum()):
			showerror("Error","Enter Correct Edition")
			ent3.delete(0,END)
			ent3.focus()


		elif( ent3.get().isdigit()):
			showerror("Error","Enter Correct Edition")
			ent3.delete(0,END)
			ent3.focus()


		elif(len(ent4.get())==1):
			showerror("Error","Enter Correct Publication")
			ent4.delete(0,END)
			ent4.focus()



		elif(ent4.get().isdigit()):
			showerror("Error","Enter Correct Publication:Enter only alphabets")
			ent4.delete(0,END)
			ent4.focus()
		elif(not ent4.get().isalpha()):
			showerror("Error","Enter Correct Publication:Enter only alphabets")
			ent4.delete(0,END)
			ent4.focus()
		




		elif(ent5.get()==0):
			showerror("Error","Enter correct Price")
			ent5.delete(0,END)
			ent5.focus()




		elif(not ent5.get().isdigit()):
			showerror("Error","Enter correct Price:Enter only Digits")
			ent5.delete(0,END)
			ent5.focus()


		elif(ent5.get().isalpha()):
			showerror("Error","Enter Correct Price:Enter only Digits")
			ent5.delete(0,END)
			ent5.focus()

  	else:
			try:
				con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
				mycursor=con.cursor()
	
				Title=ent1.get()

				Author=ent2.get()
				Edition=ent3.get()
				Publication=ent4.get()
				Price=ent5.get()
				table2.item(curItem,values=(values[0],Title,Author,Edition,Publication,Price))
				mycursor.execute("update addbook set Title=%s,Author=%s,Edition=%s,Publication=%s,Price=%s where Book_ID=%s",(Title,Author,Edition,Publication,Price,values[0]))
				messagebox.showinfo("Success","Book data Updated")
				ent1.delete(0,END)
				ent2.delete(0,END)
				ent3.delete(0,END)
				ent4.delete(0,END)
				ent4.delete(0,END)
				ent5.delete(0,END)
				ent1.focus()
		

				table2.item(curItem,values=(values[0],Title,Author,Edition,Publication,Price))
		
				con.commit()
				con.close()

			except :
				messagebox.showerror("Error","Select the data first")


	update = ctk.CTkButton(update_bframe,height=20,width=60, text = 'Update', command=update_bdata,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
	update.place(x=30,y=330)

	back= ctk.CTkButton(update_bframe,height=20,width=60,text = 'Back',command=update_bframe.destroy,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
	back.place(x=280,y=330)



def delete_bdata():
	try:

	
		con=pymysql.connect(host="localhost",port=3308,user="root",password="abc123",database="lib")
		mycursor=con.cursor()
		selected_item=table2.selection()[0]
		st_id=table2.item(selected_item)['values'][0]
		mycursor.execute("delete from addbook where Book_ID=%s",st_id)
		con.commit()
		con.close()
		table2.delete(selected_item)
		messagebox.showinfo("success","Data deleted")
	except :
		messagebox.showerror("Error","Select the data first")




def save():
	FW.withdraw()

#=======================================================================================================================

root=Tk()
root.title("LOgin page")
root.geometry("1000x5000+300+50")


Frame_login=Frame(root,bg="White")
Frame_login.place(x=0,y=0,height=700,width=1366)

      
img1 = ImageTk.PhotoImage(Image.open("Lib.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(root, image = img1,height=0000,width=000)
label.pack(padx=0,pady=0)

      
frame_input=Frame(root,bg='white')
frame_input.place(x=320,y=130,height=450,width=350)


label=Label(root,text="Welcome To Library",font=('impact',32,'bold'),fg="Orange",bg='white')
label.place(x=310,y=0)



label1=Label(frame_input,text="Admin Login Here",font=('impact',25,'bold'), fg="black",bg='white')
label1.place(x=75,y=20)



label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label2.place(x=30,y=95)

      
user_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
user_txt.place(x=30,y=145,width=270,height=35)

      
label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label3.place(x=30,y=195)

password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',show="*")
password.place(x=30,y=245,width=270,height=35)


btn2=Button(frame_input,text="Login",cursor="hand2",command=f1, font=("times new roman",15),fg="white",bg="orangered", bd=0,width=15,height=1)
btn2.place(x=90,y=340)

        

btn3=Button(frame_input,text="Not Registered?register here",command=f3,cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
btn3.place(x=110,y=390)


#============================================================================================================================


mw=Toplevel(root)
mw.title("Admin_Dashboard")
mw.geometry("1000x5000+300+50")


img2=ImageTk.PhotoImage(file="LIB.jpeg")
img=Label(mw,image=img2).place(x=2,y=0,width=1000,height=700)

button = ctk.CTkButton(mw, text = 'Add student',command=f16,height=50,width=500, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=10)


button = ctk.CTkButton(mw, text = 'View student',command=f14,height=50,width=500, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=9)

button = ctk.CTkButton(mw, text = 'Add Book',command=f6,height=50,width=500, fg_color = '#030303',text_color ='#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=9)
     

button = ctk.CTkButton(mw, text = 'View Book List',command=f15,height=50,width=500, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=9)

button = ctk.CTkButton(mw, text = 'Issue Book To Student',command=f8,height=50,width=500, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=9)

button = ctk.CTkButton(mw, text = 'Return Book',command=f10,height=50,width=500, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=10)


button = ctk.CTkButton(mw, text = 'Issue And Return Details',command=IRdetails,height=50,width=500, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=9)


button = ctk.CTkButton(mw, text = 'Exit',height=50,width=500,command=f2, fg_color = '#030303',text_color = '#F0F8FF',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.pack(pady=20,padx=9)
mw.withdraw()


#=====================================================================================================================================
RW=Toplevel(root)
RW.title("Admin_Dashboard")
RW.geometry("1000x5000+300+50")


Frame_login1=Frame(RW,bg="white")
Frame_login1.place(x=0,y=0,height=700,width=1200)


img3 = ImageTk.PhotoImage(Image.open("Lib.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(RW, image = img3,height=0,width=0)
label.pack(padx=0,pady=0)   


      
frame_input2=Frame(RW,bg='white')
frame_input2.place(x=200,y=0,height=450,width=630)


label1=Label(frame_input2,text="Register Here",font=('impact',32,'bold'),fg="black",bg='white')
label1.place(x=45,y=20)



label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label2.place(x=30,y=95)

entry=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
entry.place(x=30,y=145,width=270,height=35)

label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label3.place(x=30,y=195)

entry2=Entry(frame_input2,font=("times new roman",15,"bold"),
bg='lightgray')
entry2.place(x=30,y=245,width=270,height=35)


label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label4.place(x=330,y=95)

      
entry3=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
entry3.place(x=330,y=145,width=270,height=35)



label5=Label(frame_input2,text="Confirm Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label5.place(x=330,y=195)

entry4=Entry(frame_input2,font=("times new roman",15,"bold"),bg='lightgray')
entry4.place(x=330,y=245,width=270,height=35)



btn2=Button(frame_input2,text="Register",command=f5,cursor="hand2",font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
btn2.place(x=90,y=340)

        

btn3=Button(frame_input2,text="Already Registered?Login",command=f4,cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
btn3.place(x=110,y=390)

RW.withdraw()

#======================================================================================================================================
addw=Toplevel(root)
addw.title("Add_Book")
addw.geometry("900x600+300+50")


img4 = ImageTk.PhotoImage(Image.open("Lib.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(addw, image = img4,height=0,width=0)
label.pack(padx=0,pady=0)



Add_frame=Frame(addw,bg="White")
Add_frame.place(height=500,width=500,x=200,y=120)

label=Label(Add_frame,text="Add Book Details",font=('impact',32,'bold'),fg="Black",bg='white')
label.place(x=120,y=50)


label=Label(Add_frame,text="Enter Title          ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=130)
Entry_Title=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
Entry_Title.place(x=240,y=135)

label=Label(Add_frame,text="Enter Author      ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=180)
Entry_Author=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
Entry_Author.place(x=240,y=185)


label=Label(Add_frame,text="Enter Edition      ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=230)
Entry_Edition=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
Entry_Edition.place(x=240,y=235)

label=Label(Add_frame,text="Enter Publication",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=280)
Entry_Publication=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
Entry_Publication.place(x=240,y=285)

label=Label(Add_frame,text="Enter Price",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=330)
Entry_Price=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
Entry_Price.place(x=240,y=335)

submit = ctk.CTkButton(Add_frame, text = 'Submit',command=f13, fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
submit.place(x=30,y=385)



back = ctk.CTkButton(Add_frame, text = 'Back',command=f7,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
back.place(x=240,y=385)

addw.withdraw()

# =======================================================================

IW=Toplevel(root)
IW.title("Issue_Book")
IW.geometry("900x600+300+50")

img = ImageTk.PhotoImage(Image.open("Lib.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(IW, image = img,height=0,width=0)
label.pack(padx=0,pady=0)


label=Label(IW,text="Issue Books",font=('impact',32,'bold'),fg="Black",bg='white')
label.place(x=340,y=50)

Issue_frame=Frame(IW,bg="White")
Issue_frame.place(height=400,width=500,x=200,y=120)

label=Label(Issue_frame,text="Enter Book ID         ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=30)
entBook_ID=Entry(Issue_frame,font=("times new roman",18,"bold"),bg="lightgray")
entBook_ID.place(x=240,y=35)

label=Label(Issue_frame,text="Enter Student ID          ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=80)
entStudent_ID=Entry(Issue_frame,font=("times new roman",18,"bold"),bg="lightgray")
entStudent_ID.place(x=240,y=85)

label=Label(Issue_frame,text="Enter Issue Date      ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=130)
entIssue_Date=Entry(Issue_frame,font=("times new roman",18,"bold"),bg="lightgray")
entIssue_Date.place(x=240,y=135)
entIssue_Date.insert(END,datetime)

from datetime import datetime, date, timedelta
today  = date.today()
print(today + timedelta(days=7))

label=Label(Issue_frame,text="Due Date      ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=180)
entDue_Date=Entry(Issue_frame,font=("times new roman",18,"bold"),bg="lightgray")
entDue_Date.place(x=240,y=185)
entDue_Date.insert(END,(today + timedelta(days=7)))

submit = ctk.CTkButton(Issue_frame, text = 'Issue Book', command=f18,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
submit.place(x=30,y=290)



back = ctk.CTkButton(Issue_frame, text = 'Back',command=f9, fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
back.place(x=240,y=290)

IW.withdraw()

# ============================================================================================================================================================================

rw=Toplevel(root)
rw.title("Return  window")
rw.geometry("1000x5000+300+50")



img6 = ImageTk.PhotoImage(Image.open("Lib.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(rw, image = img6,height=0000,width=000)
label.pack(padx=0,pady=0)




label=Label(rw,text="Return Books",font=('impact',32,'bold'),fg="Black",bg='white')
label.place(x=390,y=50)


return_frame=Frame(rw,bg='#BF3EFF')
return_frame.place(x=200,y=100,height=450,width=630)


img7 = ImageTk.PhotoImage(Image.open("return.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(return_frame, image = img7,height=0000,width=000)
label.pack(padx=0,pady=0)

label=Label(return_frame,text="Enter Book_ID and Student_ID",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=10)


Entry_BID=Entry(return_frame,font=("times new roman",14,"bold"),bg="lightgray")
Entry_BID.place(x=3,y=60)


Entry_SID=Entry(return_frame,font=("times new roman",14,"bold"),bg="lightgray")
Entry_SID.place(x=300,y=60)



button = ctk.CTkButton(return_frame, text = 'Search',command=search,height=30,width=40, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.place(x=520,y=10)


button = ctk.CTkButton(return_frame, text = 'Back',command=f24,height=30,width=40, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='#BF3EFF')
button.place(x=520,y=155)

rw.withdraw()


# =====================================================================================================



rw2=Toplevel(root)
rw2.title("Return_Book")
rw2.geometry("400x350+620+250")


label=Label(rw2,text="Book ID",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
label.place(x=10,y=50)

BID=Entry(rw2,font=("times new roman",15,"bold"),bg="lightgray")
BID.place(x=140,y=55)


label=Label(rw2,text="Student ID",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
label.place(x=10,y=95)

SID=Entry(rw2,font=("times new roman",15,"bold"),bg="lightgray")
SID.place(x=140,y=100)


label=Label(rw2,text="Issue Date",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
label.place(x=10,y=140)

ISD=Entry(rw2,font=("times new roman",15,"bold"),bg="lightgray")
ISD.place(x=140,y=145)

label=Label(rw2,text="Due Date",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
label.place(x=10,y=185)
DD=Entry(rw2,font=("times new roman",15,"bold"),bg="lightgray")
DD.place(x=140,y=190)


label=Label(rw2,text="Return Date",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
label.place(x=10,y=230)
RD=Entry(rw2,font=("times new roman",15,"bold"),bg="lightgray")
RD.place(x=140,y=235)

submit = ctk.CTkButton(rw2, text = 'Return Book', command=ReturnBook,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
submit.place(x=30,y=280)


back = ctk.CTkButton(rw2, text = 'Back',command=f12, fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
back.place(x=200,y=280)


rw2.withdraw()

#=====================================================================================================================================================================





#=========================================================================================================================================

asw=Toplevel(root)
asw.title("Add_Student")
asw.geometry("900x600+300+50")


img9 = ImageTk.PhotoImage(Image.open("Lib.jpeg"))
# Create a Label Widget to display the text or Image
label = Label(asw, image = img9,height=0,width=0)
label.pack(padx=0,pady=0)

label=Label(asw,text="Add Student Details",font=('impact',32,'bold'),fg="Black",bg='white')
label.place(x=300,y=50)

Add_frame=Frame(asw,bg="White")
Add_frame.place(height=400,width=550,x=200,y=120)

label=Label(Add_frame,text="Enter Student Name ",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=80)

ent1=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
ent1.place(x=280,y=85)

label=Label(Add_frame,text="Enter Department",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=130)
ent2=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
ent2.place(x=280,y=135)

label=Label(Add_frame,text="Enter Mobile NO.",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=180)
ent3=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
ent3.place(x=280,y=185)

label=Label(Add_frame,text="Enter GR No.",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
label.place(x=30,y=230)
ent4=Entry(Add_frame,font=("times new roman",18,"bold"),bg="lightgray")
ent4.place(x=280,y=235)

submit = ctk.CTkButton(Add_frame, text = 'Submit', command=f20,fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
submit.place(x=30,y=300)

back = ctk.CTkButton(Add_frame, command=f17,text = 'Back',fg_color = 'orangered',text_color = 'White',font=("Goudy old style",25,"bold"),hover_color ='purple')
back.place(x=240,y=300)

asw.withdraw()

#==================================================================================================================================================================
vsw=tk.Toplevel(root)
vsw.geometry("900x700+200+50")
vsw.title("Student_Details")


button = ctk.CTkButton(vsw, text = 'Back',command=f22,height=60,width=200, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=350,y=250)


table=ttk.Treeview(vsw,columns=("Student_ID","Name","Department","Mobile_No","GR_No"),show="headings")
table.heading("Student_ID",text="Student ID")
table.heading("Name",text="Student Name")
table.heading("Department",text="Student Department")
table.heading("Mobile_No",text="Mobile No")
table.heading("GR_No",text="GR_No")
	
table.column("Student_ID",width=175,anchor=CENTER)
table.column("Name",width=175,anchor=CENTER)
table.column("Department",width=175,anchor=CENTER)
table.column("Mobile_No",width=175,anchor=CENTER)
table.column("GR_No",width=175,anchor=CENTER)
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview.Heading", font=("12"),background="black", foreground="white")

button = ctk.CTkButton(vsw, text = 'Update',command=select_data,height=60,width=200, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=100,y=250)

button = ctk.CTkButton(vsw, text = 'delete',command=delete_data,height=60,width=200, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=630,y=250)
	
def std():
	mycursor.execute("use lib")
	mycursor.execute("select * from student ")
	for d in mycursor:
		table.insert('',"end",text="d[0]",values=(d[0],d[1],d[2],d[3],d[4]))

std()


table.pack()
vsw.withdraw()
# ======================================================================================================================================================================
vbw=tk.Toplevel(root)
vbw.geometry("1420x700+50+50")
vbw.title("Book_Details")


table2=ttk.Treeview(vbw,columns=("Book_ID","Title","Author","Edition","Publication","Price"),show="headings")

table2.heading("Book_ID",text="Book ID",anchor=CENTER)

table2.heading("Title",text="Title ",anchor=CENTER)
table2.heading("Author",text="Author",anchor=CENTER)
table2.heading("Edition",text="Edition",anchor=CENTER)
table2.heading("Publication",text="Publication",anchor=CENTER)
table2.heading("Price",text="Price(RS)",anchor=CENTER)

table2.column("Book_ID",width=200,anchor=CENTER)

table2.column("Title",width=200,anchor=CENTER)
table2.column("Author",width=200,anchor=CENTER)
table2.column("Edition",width=200,anchor=CENTER)
table2.column("Publication",width=200,anchor=CENTER)
table2.column("Price",width=200,anchor=CENTER)

style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview.Heading",font=("Goudy old style",16,"bold"), background="black", foreground="white")
style.configure("Treeview.columns",font=("Goudy old style",40,"bold"), foreground="white")


def bookd():
	mycursor.execute("use lib")
	mycursor.execute("select * from addbook ")
	for d in mycursor:
		table2.insert('',"end",text="d[0]",values=(d[0],d[1],d[2],d[3],d[4],d[5]))


bookd()

table2.pack()

button = ctk.CTkButton(vbw, text = 'Update',command=select_bdata,height=60,width=200, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=100,y=250)



button = ctk.CTkButton(vbw, text = 'Back',height=60,width=200,command=f21, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=350,y=250)



button = ctk.CTkButton(vbw, text = 'delete',command=delete_bdata,height=60,width=200, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=630,y=250)



vbw.withdraw()
table2.pack()


#==============================================================================================

IRW=Toplevel(root)
IRW.title("Issue_Return_details")
IRW.geometry("950x600+300+50")


table3=ttk.Treeview(IRW,columns=("Book_ID","Student_ID","Issue_Date","Due_Date","Return_Date"),show="headings")
table3.heading("Book_ID",text="Book_ID")
table3.heading("Student_ID",text="Student_ID")
table3.heading("Issue_Date",text="Issue_Date")
table3.heading("Due_Date",text="Due_Date")
table3.heading("Return_Date",text="Return_Date")
	
table3.column("Book_ID",width=200,anchor=CENTER)
table3.column("Student_ID",width=200,anchor=CENTER)
table3.column("Issue_Date",width=200,anchor=CENTER)
table3.column("Due_Date",width=200,anchor=CENTER)
table3.column("Return_Date",width=200,anchor=CENTER)
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview.Heading", font=("12"),background="black", foreground="white")



def IRd():
	mycursor.execute("use lib")
	mycursor.execute("select * from IRdetail")
	for d in mycursor:
		table3.insert('',"end",text="d[0]",values=(d[0],d[1],d[2],d[3],d[4]))

IRd()


table3.pack()

button = ctk.CTkButton(IRW ,text = 'Back',height=60,width=200,command=f23, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=350,y=250)
button = ctk.CTkButton(IRW ,text = 'Search',command=searchbook,height=60,width=200, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=350,y=520)

scroll_box=ScrolledText(IRW,width=30,height=8,font=('arial',16,'bold'),bg="lightgray")

scroll_box.place(x=270,y=320)

Entry_search_BookID=Label(IRW,text="Enter Book  ID",font=("Goudy old style",14,"bold"),fg='orangered',bg='white')
Entry_search_BookID.place(x=10,y=320)

Entry_search_studentID=Label(IRW,text="Enter Student ID",font=("Goudy old style",14,"bold"),fg='orangered',bg='white')
Entry_search_studentID.place(x=720,y=320)


EBID=Entry(IRW,font=("times new roman",12,"bold"),bg="lightgray")
EBID.place(x=10,y=350)

ESID=Entry(IRW,font=("times new roman",12,"bold"),bg="lightgray")
ESID.place(x=720,y=350)
EBID.focus()


IRW.withdraw()



FW=Toplevel(root)
FW.title("Fine_Details")
FW.geometry("200x200+700+500")

Late_days=Label(FW,text="Late days",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
Late_days.place(x=0,y=0)


entLate_days=Entry(FW,text="Late days",font=("times new roman",15,"bold"),bg='lightgray')
entLate_days.place(x=100,y=0)


Fine=Label(FW,text="Fine",font=("Goudy old style",16,"bold"),fg='orangered',bg='white')
Fine.place(x=0,y=50)


Entry_Fine=Entry(FW,font=("times new roman",15,"bold"),bg='lightgray')
Entry_Fine.place(x=100,y=50)


button = ctk.CTkButton(FW, text = 'Save',command=save,height=30,width=100, fg_color = 'Orangered',text_color = 'White',font=("Goudy old style",30,"bold"),hover_color ='#BF3EFF')
button.place(x=70,y=150)



root.mainloop()
