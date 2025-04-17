import PIL
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import mysql.connector
from tkinter import messagebox



class Student:
    def __init__(self,root):
        self.root=root
        root.geometry("1530x790+0+0")
        self.root.title("SCHOLARSHIP MANAGEMENT SYSTEM")


        #Variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_marks=StringVar()
        self.var_income=StringVar()
        

        #1st image
        img = Image.open(r"C:\Users\khush\OneDrive\Desktop\Scholarship Management System\Images\download4.jpeg") 
        img = img.resize((540,160),PIL.Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Button(self.root,image=self.photoimg,cursor="hand2")
        self.btn_1.place(x=0,y=0,width=540,height=160)

        #2nd image
        img_2 = Image.open(r"C:\Users\khush\OneDrive\Desktop\Scholarship Management System\Images\download1.jpeg") 
        img_2 = img_2.resize((540,160),PIL.Image.Resampling.LANCZOS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Button(self.root,image=self.photoimg_2,cursor="hand2")
        self.btn_2.place(x=540,y=0,width=540,height=160)

        #3rd image
        img_3 = Image.open(r"C:\Users\khush\OneDrive\Desktop\Scholarship Management System\Images\download15.jpeg") 
        img_3 = img_3.resize((540,160),PIL.Image.Resampling.LANCZOS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Button(self.root,image=self.photoimg_3,cursor="hand2")
        self.btn_3.place(x=1000,y=0,width=540,height=160)

        # bg image
        img_4 = Image.open(r"C:\Users\khush\OneDrive\Desktop\Scholarship Management System\Images\download12.jpg") 
        img_4 = img_4.resize((1530,710),PIL.Image.Resampling.LANCZOS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=160,width=1530,height=710)

        lbl_title=Label(bg_lbl,text="SCHOLARSHIP MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="blue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)
      
        #manage frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=55,width=1500,height=560)

        #left frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=660,height=540)

        #img1
        img_5 = Image.open(r"C:\Users\khush\OneDrive\Desktop\Scholarship Management System\Images\download17.jpg") 
        img_5 = img_5.resize((650,120),PIL.Image.Resampling.LANCZOS)
        self.photoimg_5=ImageTk.PhotoImage(img_5)

        my_img=Label(DataLeftFrame,image=self.photoimg_5,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=650,height=120)

        #Current course Labelframe Information
        std_lbl_info_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Current Course Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_info_frame.place(x=0,y=120,width=650,height=115)

        #Labels and Combobox
        #department
        lbl_dep=Label(std_lbl_info_frame,text="Department",font=("arial",12,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","Computer Science" , "IT", "Civil" ,"Mechanical" ,"EEE","ECE")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_std=Label(std_lbl_info_frame,text="Courses:",font=("arial",12,"bold"),bg="white")
        course_std.grid(row=0,column=2,padx=2,sticky=W,pady=10)

        com_txtcourse_std=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_course,font=("arial",12,"bold"),width=17,state="readonly")
        com_txtcourse_std["value"]=("Select Course","BTech" ,"BCA", "MBA", "MCA" ,"BSC", "BCOM")
        com_txtcourse_std.current(0)
        com_txtcourse_std.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        current_year=Label(std_lbl_info_frame,text="Year:",font=("arial",12,"bold"),bg="white")
        current_year.grid(row=1,column=0,padx=2,sticky=W,pady=10)

        com_txt_current_year=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_year,font=("arial",12,"bold"),width=17,state="readonly")
        com_txt_current_year["value"]=("Select Year","2020-2021" ,"2021-2022", "2022-2023", "2023-2024" ,"2024-2025")
        com_txt_current_year.current(0)
        com_txt_current_year.grid(row=1,column=1,padx=2,sticky=W)

        #semester
        label_Semester=Label(std_lbl_info_frame,text="Semester",font=("arial",12,"bold"),bg="white")
        label_Semester.grid(row=1,column=2,padx=2,sticky=W,pady=10)

        comSemester=ttk.Combobox(std_lbl_info_frame,textvariable=self.var_semester,font=("arial",12,"bold"),width=17,state="readonly")
        comSemester["value"]=("Select Semester","1" ,"2", "3", "4" ,"5", "6","7", "8 ")
        comSemester.current(0)
        comSemester.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Student class Labelframe Information
        std_lbl_class_frame=LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Personal   Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        std_lbl_class_frame.place(x=0,y=235,width=650,height=235 )

        #ID
        lbl_id=Label(std_lbl_class_frame,text="StudentID:",font=("arial",12,"bold"),bg="white")
        lbl_id.grid(row=0,column=0,padx=2,sticky=W,pady=7)

        id_entry=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_id,font=("arial",12,"bold"),width=22)
        id_entry.grid(row=0,column=1,sticky=W,padx=2,pady=7)

        #Name
        lbl_Name=Label(std_lbl_class_frame,text="Student Name:",font=("arial",12,"bold"),bg="white")
        lbl_Name.grid(row=0,column=2,padx=2,sticky=W,pady=7)

        txt_name=ttk.Entry(std_lbl_class_frame,textvariable=self.var_std_name,font=("arial",12,"bold"),width=22)
        txt_name.grid(row=0,column=3,sticky=W,padx=2,pady=7)  

        #Division
        lbl_div=Label(std_lbl_class_frame,text="Class Division",font=("arial",12,"bold"),bg="white")
        lbl_div.grid(row=1,column=0,padx=2,sticky=W,pady=7)

        com_txt_div=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_div,font=("arial",12,"bold"),width=17,state="readonly")
        com_txt_div["value"]=("Select Division","A" , "B", "C")
        com_txt_div.current(0)
        com_txt_div.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Roll No
        lbl_roll=Label(std_lbl_class_frame,text="Roll No:",font=("arial",12,"bold"),bg="white")
        lbl_roll.grid(row=1,column=2,padx=2,sticky=W,pady=7)

        txt_roll=ttk.Entry(std_lbl_class_frame,textvariable=self.var_roll,font=("arial",12,"bold"),width=22)
        txt_roll.grid(row=1,column=3,padx=2,pady=7)

        #Gender
        lbl_gender=Label(std_lbl_class_frame,text="Gender:",font=("arial",12,"bold"),bg="white")
        lbl_gender.grid(row=2,column=0,padx=2,sticky=W,pady=7)

        com_txt_gender=ttk.Combobox(std_lbl_class_frame,textvariable=self.var_gender,font=("arial",12,"bold"),width=17,state="readonly")
        com_txt_gender["value"]=("Male","Female" , "Others")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=2,column=1,padx=2,pady=7,sticky=W)

        #DOB
        lbl_dob=Label(std_lbl_class_frame,text="DOB:",font=("arial",12,"bold"),bg="white")
        lbl_dob.grid(row=2,column=2,padx=2,sticky=W,pady=7)

        txt_dob=ttk.Entry(std_lbl_class_frame,textvariable=self.var_dob,font=("arial",12,"bold"),width=22)
        txt_dob.grid(row=2,column=3,padx=2,pady=7)

        #Email
        lbl_email=Label(std_lbl_class_frame,text="Email:",font=("arial",12,"bold"),bg="white")
        lbl_email.grid(row=3,column=0,padx=2,sticky=W,pady=7)

        txt_email=ttk.Entry(std_lbl_class_frame,textvariable=self.var_email,font=("arial",12,"bold"),width=22)
        txt_email.grid(row=3,column=1,padx=2,pady=7)

        #Phone
        lbl_phone=Label(std_lbl_class_frame,text="Phone No.:",font=("arial",12,"bold"),bg="white")
        lbl_phone.grid(row=3,column=2,padx=2,sticky=W,pady=7)

        txt_phone=ttk.Entry(std_lbl_class_frame,textvariable=self.var_phone,font=("arial",12,"bold"),width=22)
        txt_phone.grid(row=3,column=3,padx=2,pady=7)

        #Marks Percentage
        lbl_sa=Label(std_lbl_class_frame,text="Marks percentage :",font=("arial",12,"bold"),bg="white")
        lbl_sa.grid(row=4,column=0,padx=2,sticky=W,pady=7)

        txt_sa=ttk.Entry(std_lbl_class_frame,textvariable=self.var_marks,font=("arial",12,"bold"),width=22)
        txt_sa.grid(row=4,column=1,padx=2,pady=7, sticky=W)

        #Annual Income
        lbl_ai=Label(std_lbl_class_frame,text="Annual Income:",font=("arial",12,"bold"),bg="white")
        lbl_ai.grid(row=4,column=2,padx=2,sticky=W,pady=7)

        txt_ai=ttk.Entry(std_lbl_class_frame,textvariable=self.var_income,font=("arial",12,"bold"),width=22)
        txt_ai.grid(row=4,column=3,padx=2,pady=7)


        #Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=470,width=650,height=38)

        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",11,"bold"),width=17,bg="blue",fg="white")
        btn_reset.grid(row=0,column=3,padx=1)









        #right frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        DataRightFrame.place(x=680,y=10,width=800,height=540)


        #img1
        img_6 = Image.open(r"C:\Users\khush\OneDrive\Desktop\Scholarship Management System\Images\download2.jpeg") 
        img_6 = img_6.resize((780,200),PIL.Image.Resampling.LANCZOS)
        self.photoimg_6=ImageTk.PhotoImage(img_6)

        my_img=Label(DataRightFrame,image=self.photoimg_6,bd=2,relief=RIDGE)
        my_img.place(x=0,y=0,width=790,height=200)

        #Search Frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Student Information",font=("times new roman",12,"bold"),fg="red",bg="white")
        Search_Frame.place(x=0,y=200,width=790,height=60)

        search_by=Label(Search_Frame,text="Search By:",font=("arial",12,"bold"),fg="white",bg="red")
        search_by.grid(row=0,column=0,padx=5,sticky=W,)


        #search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,font=("arial",12,"bold"),width=15,state="readonly")
        com_txt_search["value"]=("Select Option","Roll","Phone","Student_ID","Eligibility")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)



        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search,font=("arial",12,"bold"),width=22)
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(Search_Frame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(Search_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)


        # ==============================Student Table and Scroll Bar=======================
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=260,width=790,height=250)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.scholarship_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","marks","income",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.scholarship_table.xview)
        scroll_y.config(command=self.scholarship_table.yview)

        self.scholarship_table.heading("dep",text="Department")
        self.scholarship_table.heading("course",text="Course")
        self.scholarship_table.heading("year",text="Year")
        self.scholarship_table.heading("sem",text="Semester")
        self.scholarship_table.heading("id",text="StudentID")
        self.scholarship_table.heading("name",text="Student Name")
        self.scholarship_table.heading("div",text="Class Division")
        self.scholarship_table.heading("roll",text="Roll No")
        self.scholarship_table.heading("gender",text="Gender")
        self.scholarship_table.heading("dob",text="DOB")
        self.scholarship_table.heading("email",text="Email")
        self.scholarship_table.heading("phone",text="Phone")
        self.scholarship_table.heading("marks",text="Marks")
        self.scholarship_table.heading("income",text="Income")

        self.scholarship_table["show"]="headings"

        self.scholarship_table.column("dep",width=110)
        self.scholarship_table.column("course",width=100)
        self.scholarship_table.column("year",width=100)
        self.scholarship_table.column("sem",width=100)
        self.scholarship_table.column("id",width=100)
        self.scholarship_table.column("name",width=100)
        self.scholarship_table.column("div",width=100)
        self.scholarship_table.column("roll",width=100)
        self.scholarship_table.column("gender",width=100)
        self.scholarship_table.column("dob",width=100)
        self.scholarship_table.column("email",width=100)
        self.scholarship_table.column("phone",width=100)
        self.scholarship_table.column("marks",width=110)
        self.scholarship_table.column("income",width=100)
        

        
        self.scholarship_table.pack(fill=BOTH,expand=1)
        self.scholarship_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
        if (self.var_dep.get=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="BangtanBoys7",database="scholarshipmanagement")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into scholarship values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_dep.get(),
                                                                                                           self.var_course.get(),
                                                                                                           self.var_year.get(),
                                                                                                           self.var_semester.get(),
                                                                                                           self.var_std_id.get(),
                                                                                                           self.var_std_name.get(),
                                                                                                           self.var_div.get(),
                                                                                                           self.var_roll.get(),
                                                                                                           self.var_gender.get(),
                                                                                                           self.var_dob.get(),
                                                                                                           self.var_email.get(),
                                                                                                           self.var_phone.get(),
                                                                                                           self.var_marks.get(),
                                                                                                           self.var_income.get()))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #Fetch Function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="BangtanBoys7",database="scholarshipmanagement")
        my_cursur=conn.cursor()

        my_cursur.execute("select * from scholarship")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.scholarship_table.delete(*self.scholarship_table.get_children())
            for i in data:
                self.scholarship_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.scholarship_table.focus()
        content=self.scholarship_table.item(cursor_row)
        data=content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_marks.set(data[12])
        self.var_income.set(data[13])

    def update_data(self):
        if (self.var_dep.get=="" or self.var_email.get()=="" or self.var_std_id.get()==""):
            messagebox.showerror("Error","All Fields are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this student data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="BangtanBoys7",database="scholarshipmanagement")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update scholarship set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Marks=%s,Income=%s where student_id=%s",(self.var_dep.get(),
                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                                                self.var_marks.get(),
                                                                                                                                                                                                                                self.var_income.get(),
                                                                                                                                                                                                                                self.var_std_id.get()))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Success","Student data successfully updated",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #Delete
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are Required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are you sure delete this student")
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="BangtanBoys7",database="scholarshipmanagement")
                    my_cursur=conn.cursor()
                    sql="delete from scholarship where student_id=%s"
                    value=(self.var_std_id.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Data has been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    #Reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_marks.set("")
        self.var_income.set("")

    #searchdata
    def search_data(self):
        if self.var_com_search.get()=="":
            messagebox.showerror("Error","Please select option")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="BangtanBoys7",database="scholarshipmanagement")
                my_cursur=conn.cursor()
                if (self.var_com_search.get()=="Eligibility"):
                    my_cursur.execute("select * from scholarship where Marks>80 and Income<500000")
                else:
                    my_cursur.execute("select * from scholarship where "+ str(self.var_com_search.get())+" LIKE '%" + str(self.var_search.get())+"%'")
                data=my_cursur.fetchall()
                if len(data)!=0:
                    self.scholarship_table.delete(*self.scholarship_table.get_children())
                    for i in data:
                        self.scholarship_table.insert("",END,values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

                            
                
                

                                                                                                                                            
                    
        


            
if __name__ =="__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()
                    
