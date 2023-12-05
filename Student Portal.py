############################################################################
##                                                                        ##
##                           IMPORT LIBARARIES                            ##
##                                                                        ##
############################################################################

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import mysql.connector as mysqlC

############################################################################
##                                                                        ##
##                           MY SQL CONNECTION                            ##
##                                                                        ##
############################################################################

def Database_Connection():
    global conn
    global cursor
    conn = mysqlC.connect(host = "localhost", user = "root", password = "", db = "project")
    cursor = conn.cursor()

############################################################################
##                                                                        ##
##                            WINDOW GEOMETRY                             ##
##                                                                        ##
############################################################################

w = tk.Tk()
w.title("Student Portal Project")
w.geometry("%dx%d" % (w.winfo_screenwidth(), w.winfo_screenheight()))
w.state("zoomed")
w.iconbitmap('1.ico')

############################################################################
##                                                                        ##
##                                 FRAMES                                 ##
##                                                                        ##
############################################################################

global Header_Frame
Header_Frame = tk.Frame(w)

global Body_Frame
Body_Frame = tk.Frame(w)

############################################################################
##                                                                        ##
##                            GLOBAL VARIABLES                            ##
##                                                                        ##
############################################################################

global header_image
header_img = ImageTk.PhotoImage(Image.open("portalheader.png"))
header_image = tk.Label(Header_Frame, image = header_img)

global ID

############################################################################
##                                                                        ##
##                                 STYLES                                 ##
##                                                                        ##
############################################################################

menu_styles = {'height' : 2, 'width' : 30}

bar_styles = {'height' : 2, 'width' : 40, 'font' : "bold"}

style = ttk.Style()

style.theme_use("clam")

style.configure("Treeview", rowheight = 50, background = "#f0f0f0", foreground = "#000000", fieldbackground = "#f0f0f0")

style.map("Treeview", background = [("selected" , "#e0e0e0")], foreground = [("selected" , "#000000")])

############################################################################
##                                                                        ##
##                             LOGOUT FUNCTION                            ##
##                                                                        ##
############################################################################

def Admin_LogOut():
    
    logout = messagebox.askyesno("Logout", "Do You Want to Logout")
    
    if logout == 1:
        
        for widgets in Body_Frame.winfo_children():
            widgets.destroy()
        
        #RETURNS TO MAIN FUNCTION
        Admin_Main()
    
    elif logout == 0:
        pass

############################################################################
##                                                                        ##
##                        UPDATE PASSWORD FUNCTION                        ##
##                                                                        ##
############################################################################

def Admin_UpdatePassword(ID):
        
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "y", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Admin_Profile(ID))).grid(row = 0, column = 0)

    tk.Button(Menu_Frame, text = "ADD NEW STUDENTS", **menu_styles, command = (lambda : Add_Student(ID))).grid(row = 1, column = 0)

    tk.Button(Menu_Frame, text = "ADD STUDENT DETAILS", **menu_styles, command = (lambda : Add_Student_Data(ID))).grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "VIEW STUDENTS", **menu_styles, command = (lambda : View_Students(ID))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, background = "#999", state = "disabled").grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Admin_LogOut).grid(row = 5, column = 0)
    
    ############################################################################
    ##                           UPDATED FUNCTION                             ##
    ############################################################################
    
    def Updated():
        current_password = current_password_e.get()
        new_password = new_password_e.get()
        new_password_again = new_password_again_e.get()
        
        selectQ = "Select Password from admin_login WHERE ID = %s"
        
        ID_tuple = (ID, )
        cursor.execute(selectQ, ID_tuple)
        orignal_password = cursor.fetchone()

        if current_password == orignal_password[0]:
            if new_password == new_password_again:
                if new_password != current_password:
                    tk.messagebox.showinfo("Password Updated", "Password Updated Successfully")
                    updateQ = "UPDATE Login SET Password = %s WHERE ID = %s"
                    Data = (new_password, ID)
                    cursor.execute(updateQ, Data)
                    conn.commit()
                else:
                    tk.messagebox.showerror("Password Error", "Same as Your Current Password")
                    current_password_e.delete(0, tk.END)
                    new_password_e.delete(0, tk.END)
                    new_password_again_e.delete(0, tk.END)
            else:
                tk.messagebox.showerror("Password Error", "New Password is Not Matched")
                current_password_e.delete(0, tk.END)
                new_password_e.delete(0, tk.END)
                new_password_again_e.delete(0, tk.END)
        else:
            tk.messagebox.showerror("Password Error", "Wrong Current Password")
            current_password_e.delete(0, tk.END)
            new_password_e.delete(0, tk.END)
            new_password_again_e.delete(0, tk.END)
    
                    ###########################
                    ## Update_Password_FRAME ##
                    ###########################
    
    UpdatePassword_Frame = tk.LabelFrame(Body_Frame)
    UpdatePassword_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Label(UpdatePassword_Frame, text = "UPDATE PASSWORD", height = 2, font = 'Helvetica 18 bold', relief = 'ridge').grid(row = 0, column = 0, ipadx = 442)
    
    tk.Label(UpdatePassword_Frame, text = "Enter Current Password ", font = '12').grid(row = 1, column = 0, pady = 10)
    
    current_password_e = ttk.Entry(UpdatePassword_Frame, font = '12')
    current_password_e.grid(row = 2, column = 0)
    
    tk.Label(UpdatePassword_Frame, text = "New Password ", font = '12').grid(row = 3, column = 0, pady = 10)
    
    new_password_e = ttk.Entry(UpdatePassword_Frame, font = '12')
    new_password_e.grid(row = 4, column = 0)
    
    tk.Label(UpdatePassword_Frame, text = "Confirm New Password ", font = '12').grid(row = 5, column = 0, pady = 10)
    
    new_password_again_e = ttk.Entry(UpdatePassword_Frame, font = '12')
    new_password_again_e.grid(row = 6, column = 0)
    
    ttk.Button(UpdatePassword_Frame, text = "UPDATE", command = Updated).grid(row = 7, column = 0, pady = 10)

############################################################################
##                                                                        ##
##                          ATTENDANCE FUNCTION                           ##
##                                                                        ##
############################################################################

def Add_Student_Data(ID):
        
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()        
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Admin_Profile(ID))).grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD NEW STUDENTS", **menu_styles, command = (lambda : Add_Student(ID))).grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD STUDENT DETAILS", **menu_styles, background = "#999", state = "disabled").grid(row = 2, column = 0)

    tk.Button(Menu_Frame, text = "VIEW STUDENTS", **menu_styles, command = (lambda : View_Students(ID))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Admin_UpdatePassword(ID))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Admin_LogOut).grid(row = 5, column = 0)
    
    def Add_Data():

        Image = selected_image_path

        Roll_No = int(Roll_No_e.get())
        F_Name = F_Name_e.get()
        L_Name = L_Name_e.get()
        Department = Department_e.get()
        Program = Program_e.get()
        Semester = Semester_e.get()
        Section = Section_e.get()
        Session = Session_e.get()

        CNIC = CNIC_e.get()
        DOB = DOB_e.get()
        Gender = Gender_e.get()
        M_Status = M_Status_e.get()
        Nationality = Nationality_e.get()
        Province = Province_e.get()
        District = District_e.get()
        Tehsile = Tehsile_e.get()
        Zip_Code = Zip_Code_e.get()
        M_Tongue = M_Tongue_e.get()
        E_mail = E_mail_e.get()
        Ph_no = Ph_no_e.get()
        Blood = Blood_e.get()
        Religion = Religion_e.get()
        Is_Hafiz = Is_Hafiz_e.get()
        Is_Disable = Is_Disable_e.get()
        G_Name = G_Name_e.get()
        G_CNIC = G_CNIC_e.get()
        G_Ph_no = G_Ph_no_e.get()
        G_E_mail = G_E_mail_e.get()

        has_validation_errors = False
        
        if not (Roll_No and F_Name and L_Name and Department and Program and Semester and Section and Session and CNIC and DOB and Gender and M_Status and Nationality and Province and District and Tehsile and Zip_Code and M_Tongue and E_mail and Ph_no and Blood and Religion and Is_Hafiz and Is_Disable and G_Name and G_CNIC and G_Ph_no and G_E_mail):
            has_validation_errors = True

        if has_validation_errors == True:
            tk.messagebox.showerror("Insertion Error", "One or more fields are empty. Please fill in all the required fields.")
            
        else:
            selectQ = "Select Roll_No from login"
        
            cursor.execute(selectQ)
            all_students = cursor.fetchall()
            a_check = True
            for student in all_students:

                if student[0] == Roll_No:
                    a_check = False
                    student_check = True
                    selectQ = "Select Roll_No from basic"
        
                    cursor.execute(selectQ)
                    student_Data = cursor.fetchall()

                    for rollno in student_Data:
                        if rollno[0] == Roll_No:
                            student_check = False

                    if student_check == True:
                        with open(selected_image_path, "rb") as image_file:
                            image_data = image_file.read()
                        
                        InsertQ = "INSERT INTO Basic (Pic, Roll_No, F_Name, L_Name, Department, Program, Semester, Section, Session) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        tuple = (image_data, Roll_No, F_Name, L_Name, Department, Program, Semester, Section, Session)
                        cursor.execute(InsertQ, tuple)
                        conn.commit()

                        InsertQ = "INSERT INTO Other (Roll_No, CNIC, DOB, Gender, M_Status, Nationality, Province, District, Tehsile, Zip_Code, Mother_Tongue, E_mail, Phone_no, Blood, Religion, Hafiz, Disable, G_Name, G_CNIC, G_Phone_no, G_E_mail) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                        tuple = (Roll_No, CNIC, DOB, Gender, M_Status, Nationality, Province, District, Tehsile, Zip_Code, M_Tongue, E_mail, Ph_no, Blood, Religion, Is_Hafiz, Is_Disable, G_Name, G_CNIC, G_Ph_no, G_E_mail)
                        cursor.execute(InsertQ, tuple)
                        conn.commit()
                    else:
                        tk.messagebox.showerror("Insertion Error", "Data for this Roll No is already Present.")
            
            if a_check == True:
                tk.messagebox.showerror("Insertion Error", "There is No Account with this Roll No")

                    #################
                    ## BASIC_FRAME ##
                    #################
    
    Basic_Frame = tk.LabelFrame(Body_Frame)
    
    Basic_Frame.pack(expand = 1, fill = "y", side = "left")

    def open_image():
        file_path = filedialog.askopenfilename()
        if file_path:
            image_label.config(text=file_path)

            # Store the image path for later use
            global selected_image_path
            selected_image_path = file_path
    
    
    image_label = tk.Label(Basic_Frame, text=" ", fg="green")
    image_label.grid(row = 0, column = 0)
    img_button = ttk.Button(Basic_Frame, text="Upload Image", command=open_image)
    img_button.grid(row = 1, column = 0)
    # profile_img = ImageTk.PhotoImage(data = personal[1])
    
    tk.Label(Basic_Frame, text = "Roll No", font=12).grid(pady = 5, row = 2, column = 0)
    Roll_No_e = ttk.Entry(Basic_Frame, width= 47)
    Roll_No_e.grid(row = 3, column = 0)
    
    tk.Label(Basic_Frame, text = "First Name", font=12).grid(pady = 5, row = 4, column = 0)
    F_Name_e = ttk.Entry(Basic_Frame, width= 47)
    F_Name_e.grid(row = 5, column = 0)

    tk.Label(Basic_Frame, text = "Last Name", font=12).grid(pady = 5, row = 6, column = 0)
    L_Name_e = ttk.Entry(Basic_Frame, width= 47)
    L_Name_e.grid(row = 7, column = 0)

    tk.Label(Basic_Frame, text = "Department", font=12).grid(pady = 5, row = 8, column = 0)
    Department_e = ttk.Entry(Basic_Frame, width= 47)
    Department_e.grid(row = 9, column = 0)
    
    tk.Label(Basic_Frame, text = "Program", font=12).grid(pady = 5, row = 10, column = 0)
    Program_e = ttk.Entry(Basic_Frame, width= 47)
    Program_e.grid(row = 11, column = 0)

    tk.Label(Basic_Frame, text = "Semester", font=12).grid(pady = 5, row = 12, column = 0)
    Semester_e = ttk.Entry(Basic_Frame, width= 47)
    Semester_e.grid(row = 13, column = 0)
    
    tk.Label(Basic_Frame, text = "Section", font=12).grid(pady = 5, row = 14, column = 0)
    Section_e = ttk.Entry(Basic_Frame, width= 47)
    Section_e.grid(row = 15, column = 0)

    tk.Label(Basic_Frame, text = "Session", font=12).grid(pady = 5, row = 16, column = 0)
    Session_e = ttk.Entry(Basic_Frame, width= 47)
    Session_e.grid(row = 17, column = 0)
    
                    #################
                    ## OTHER_FRAME ##
                    #################
    
    Other_Frame = tk.LabelFrame(Body_Frame)
    
    Other_Frame.pack(expand = 1, fill = "both", side = "right")
    
    tk.Label(Other_Frame, text = "OTHER DETAILS", height = 2, width = 56, font = "Helvetica 18 bold").grid(row = 0, column = 0, columnspan = 4)
    
    other_styles = {'height':2, 'width':23, 'font':"bold", 'bg':"#eee", 'relief':"ridge"}
    
    tk.Label(Other_Frame, text = "CNIC", font=12).grid(pady = 5,  row = 1, column = 0)
    CNIC_e = ttk.Entry(Other_Frame, width= 30)
    CNIC_e.grid(row = 2, column = 0)

    tk.Label(Other_Frame, text = "Date of Birth", font=12).grid(pady = 5,  row = 1, column = 1)
    DOB_e = ttk.Entry(Other_Frame, width= 30)
    DOB_e.grid(row = 2, column = 1)

    tk.Label(Other_Frame, text = "Gender", font=12).grid(pady = 5,  row = 1, column = 2)
    Gender_e = ttk.Entry(Other_Frame, width= 30)
    Gender_e.grid(row = 2, column = 2)

    tk.Label(Other_Frame, text = "Martial Status", font=12).grid(pady = 5,  row = 1, column = 3)
    M_Status_e = ttk.Entry(Other_Frame, width= 30)
    M_Status_e.grid(row = 2, column = 3)

    tk.Label(Other_Frame, text = "Nationality", font=12).grid(pady = 5,  row = 3, column = 0)
    Nationality_e = ttk.Entry(Other_Frame, width= 30)
    Nationality_e.grid(row = 4, column = 0)

    tk.Label(Other_Frame, text = "Province", font=12).grid(pady = 5,  row = 3, column = 1)
    Province_e = ttk.Entry(Other_Frame, width= 30)
    Province_e.grid(row = 4, column = 1)

    tk.Label(Other_Frame, text = "District", font=12).grid(pady = 5,  row = 3, column = 2)
    District_e = ttk.Entry(Other_Frame, width= 30)
    District_e.grid(row = 4, column = 2)

    tk.Label(Other_Frame, text = "Tehsile", font=12).grid(pady = 5,  row = 3, column = 3)
    Tehsile_e = ttk.Entry(Other_Frame, width= 30)
    Tehsile_e.grid(row = 4, column = 3)

    tk.Label(Other_Frame, text = "Zip Code", font=12).grid(pady = 5,  row = 5, column = 0)
    Zip_Code_e = ttk.Entry(Other_Frame, width= 30)
    Zip_Code_e.grid(row = 6, column = 0)

    tk.Label(Other_Frame, text = "Mother Tongue", font=12).grid(pady = 5,  row = 5, column = 1)
    M_Tongue_e = ttk.Entry(Other_Frame, width= 30)
    M_Tongue_e.grid(row = 6, column = 1)

    tk.Label(Other_Frame, text = "E-mail", font=12).grid(pady = 5,  row = 5, column = 2)
    E_mail_e = ttk.Entry(Other_Frame, width= 30)
    E_mail_e.grid(row = 6, column = 2)

    tk.Label(Other_Frame, text = "Phone No", font=12).grid(pady = 5,  row = 5, column = 3)
    Ph_no_e = ttk.Entry(Other_Frame, width= 30)
    Ph_no_e.grid(row = 6, column = 3)

    tk.Label(Other_Frame, text = "Blood", font=12).grid(pady = 5,  row = 7, column = 0)
    Blood_e = ttk.Entry(Other_Frame, width= 30)
    Blood_e.grid(row = 8, column = 0)

    tk.Label(Other_Frame, text = "Religion", font=12).grid(pady = 5,  row = 7, column = 1)
    Religion_e = ttk.Entry(Other_Frame, width= 30)
    Religion_e.grid(row = 8, column = 1)

    tk.Label(Other_Frame, text = "Is Hafiz", font=12).grid(pady = 5,  row = 7, column = 2)
    Is_Hafiz_e = ttk.Entry(Other_Frame, width= 30)
    Is_Hafiz_e.grid(row = 8, column = 2)

    tk.Label(Other_Frame, text = "Is Disable", font=12).grid(pady = 5,  row = 7, column = 3)
    Is_Disable_e = ttk.Entry(Other_Frame, width= 30)
    Is_Disable_e.grid(row = 8, column = 3)

    tk.Label(Other_Frame, text = "Guardian Name", font=12).grid(pady = 5,  row = 9, column = 0)
    G_Name_e = ttk.Entry(Other_Frame, width= 30)
    G_Name_e.grid(row = 10, column = 0)

    tk.Label(Other_Frame, text = "Guardian CNIC", font=12).grid(pady = 5,  row = 9, column = 1)
    G_CNIC_e = ttk.Entry(Other_Frame, width= 30)
    G_CNIC_e.grid(row = 10, column = 1)

    tk.Label(Other_Frame, text = "Guardian Phone No", font=12).grid(pady = 5,  row = 9, column = 2)
    G_Ph_no_e = ttk.Entry(Other_Frame, width= 30)
    G_Ph_no_e.grid(row = 10, column = 2)

    tk.Label(Other_Frame, text = "Guardian E-mail", font=12).grid(pady = 5,  row = 9, column = 3)
    G_E_mail_e = ttk.Entry(Other_Frame, width= 30)
    G_E_mail_e.grid(row = 10, column = 3)

    ttk.Button(Other_Frame, text="SUBMIT", command=Add_Data).grid(pady = 10,  row = 11, column = 1, columnspan = 2)

############################################################################
##                                                                        ##
##                          ENROLLMENTS FUNCTION                          ##
##                                                                        ##
############################################################################

def Add_Student(ID):
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Admin_Profile(ID))).grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD NEW STUDENTS", **menu_styles, background = "#999", state = "disabled").grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD STUDENT DETAILS", **menu_styles, command = (lambda : Add_Student_Data(ID))).grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "VIEW STUDENTS", **menu_styles, command = (lambda : View_Students(ID))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Admin_UpdatePassword(ID))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Admin_LogOut).grid(row = 5, column = 0)
    
    
    ############################################################################
    ##                           UPDATED FUNCTION                             ##
    ############################################################################
    
    def Add():
        new_username = new_username_e.get()
        new_rollno = int(new_rollno_e.get())
        new_password = new_password_e.get()
        
        selectQ = "Select * from login"
        
        cursor.execute(selectQ)
        all_students = cursor.fetchall()

        roll_no_check = username_check = True
        
        for student in all_students:

            if new_rollno in student:
                roll_no_check = False
            
            if new_username in student:
                username_check = False


        if roll_no_check == True:
                
            if username_check == True:
                
                    tk.messagebox.showinfo("Success", "New Student Added")
                    insertQ = "INSERT INTO login (username, roll_no, password) VALUES (%s, %s, %s)"
                    Data = (new_username, new_rollno, new_password)
                    cursor.execute(insertQ, Data)
                    conn.commit()
    
            else:
                    tk.messagebox.showerror("Username Error", "Same Username Exists")
                    new_username_e.delete(0, tk.END)
                    new_rollno_e.delete(0, tk.END)
                    new_password_e.delete(0, tk.END)
            
        else:
                
                tk.messagebox.showerror("Roll No Error", "Same Roll No Exists")
                new_username_e.delete(0, tk.END)
                new_rollno_e.delete(0, tk.END)
                new_password_e.delete(0, tk.END)
    
                    ###########################
                    ## Update_Password_FRAME ##
                    ###########################
    
    Add_Student_Frame = tk.LabelFrame(Body_Frame)
    Add_Student_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Label(Add_Student_Frame, text = "ADD NEW STUDENT", height = 2, font = 'Helvetica 18 bold', relief = 'ridge').grid(row = 0, column = 0, ipadx = 442)
    
    tk.Label(Add_Student_Frame, text = "Enter Username", font = '12').grid(row = 1, column = 0, pady = 10)
    
    new_username_e = ttk.Entry(Add_Student_Frame, font = '12')
    new_username_e.grid(row = 2, column = 0)
    
    tk.Label(Add_Student_Frame, text = "Enter Roll No", font = '12').grid(row = 3, column = 0, pady = 10)
    
    new_rollno_e = ttk.Entry(Add_Student_Frame, font = '12')
    new_rollno_e.grid(row = 4, column = 0)
    
    tk.Label(Add_Student_Frame, text = "Enter Password ", font = '12').grid(row = 5, column = 0, pady = 10)
    
    new_password_e = ttk.Entry(Add_Student_Frame, font = '12')
    new_password_e.grid(row = 6, column = 0)
    
    ttk.Button(Add_Student_Frame, text = "ADD", command = Add).grid(row = 7, column = 0, pady = 10)

 
############################################################################
##                                                                        ##
##                            PROFILE FUNCTION                            ##
##                                                                        ##
############################################################################

def View_Students(ID):
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Admin_Profile(ID))).grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD NEW STUDENT", **menu_styles, command = (lambda : Add_Student(ID))).grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD STUDENT DETAILS", **menu_styles, command = (lambda : Add_Student_Data(ID))).grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "VIEW STUDENTS", **menu_styles, background = "#999", state = "disabled").grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Admin_UpdatePassword(ID))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Admin_LogOut).grid(row = 5, column = 0)
    
                    #################
                    ## BASIC_FRAME ##
                    #################
    
    Users_Frame = tk.LabelFrame(Body_Frame)
    
    Users_Frame.pack(expand = 1, fill = "y", side = "left")
    
    selectQ = "Select * from login"
    cursor.execute(selectQ)
    users = cursor.fetchall()
    
    users_scrollbar = tk.Scrollbar(Users_Frame)
    
    users_tree = ttk.Treeview(Users_Frame, column = ("c1", "c2", "c3"), show = "headings", yscrollcommand = users_scrollbar.set)
    
    users_scrollbar.pack(side = "right", fill = "y")
    
    users_tree = ttk.Treeview(Users_Frame, column = ("c1", "c2", "c3"), show = "headings", yscrollcommand = users_scrollbar.set)

    users_tree.column("#1", anchor = tk.CENTER, width = 400)

    users_tree.heading("#1", text = "Username")

    users_tree.column("#2", anchor = tk.CENTER, width = 350)

    users_tree.heading("#2", text = "Roll No")

    users_tree.column("#3", anchor = tk.CENTER, width = 350)

    users_tree.heading("#3", text = "Password")

    users_tree.pack()

    users_scrollbar.config(command = users_tree.yview)
    
    for user in users:
        enter = (user[0], user[1], user[2])
        users_tree.insert("", tk.END, values = enter)

############################################################################
##                                                                        ##
##                            PROFILE FUNCTION                            ##
##                                                                        ##
############################################################################

def Admin_Profile(ID):
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, background = "#999", state = "disabled").grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD NEW STUDENT", **menu_styles, command = (lambda : Add_Student(ID))).grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ADD STUDENT DETAILS", **menu_styles, command = (lambda : Add_Student_Data(ID))).grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "VIEW STUDENTS", **menu_styles, command = (lambda : View_Students(ID))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Admin_UpdatePassword(ID))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Admin_LogOut).grid(row = 5, column = 0)
    
                    #################
                    ## BASIC_FRAME ##
                    #################
    
    Basic_Frame = tk.LabelFrame(Body_Frame)
    
    Basic_Frame.pack(expand = 1, fill = "y", side = "left")
    
    #Getting Data for Basic Informations from Database_Connection
    selectQ = "Select * from admin_basic where ID = %s"
    ID_tuple = (ID, )
    cursor.execute(selectQ, ID_tuple)
    personal = cursor.fetchone()
    
    global profile_img
    profile_img = ImageTk.PhotoImage(data = personal[1])
    
    tk.Label(Basic_Frame, image = profile_img).grid(row = 0, column = 0, columnspan = 2)
    tk.Label(Basic_Frame, text = personal[2] + " " + personal[3], font = "Helvetica 14 bold").grid(row = 1, column = 0, columnspan = 2)
    
    basic_styles = {'height':2, 'width':15, 'font':"bold", 'relief':"ridge"}
    
    tk.Label(Basic_Frame, text = "ID", **basic_styles).grid(row = 2, column = 0)
    tk.Label(Basic_Frame, text = personal[0], **basic_styles).grid(row = 2, column = 1)

    tk.Label(Basic_Frame, text = "Department", **basic_styles).grid(row = 3, column = 0)
    tk.Label(Basic_Frame, text = personal[4], **basic_styles).grid(row = 3, column = 1)

    tk.Label(Basic_Frame, text = "Program", **basic_styles).grid(row = 4, column = 0)
    tk.Label(Basic_Frame, text = personal[5], **basic_styles).grid(row = 4, column = 1)

    tk.Label(Basic_Frame, text = "Designation", **basic_styles).grid(row = 5, column = 0)
    tk.Label(Basic_Frame, text = personal[6], **basic_styles).grid(row = 5, column = 1)

    tk.Label(Basic_Frame, text = "Account Type", **basic_styles).grid(row = 6, column = 0)
    tk.Label(Basic_Frame, text = personal[7], **basic_styles).grid(row = 6, column = 1)

    tk.Label(Basic_Frame, text = "Joining Date", **basic_styles).grid(row = 7, column = 0)
    tk.Label(Basic_Frame, text = personal[8], **basic_styles).grid(row = 7, column = 1)
    
                    #################
                    ## OTHER_FRAME ##
                    #################
    
    Other_Frame = tk.LabelFrame(Body_Frame)
    
    Other_Frame.pack(expand = 1, fill = "both", side = "right")
    
    #Getting Data for Other Informations from Database_Connection
    selectQ = "Select * from admin_other where ID = %s"
    ID_tuple = (ID, )
    cursor.execute(selectQ, ID_tuple)
    other = cursor.fetchone()
    
    tk.Label(Other_Frame, text = "OTHER DETAILS", height = 2, width = 56, font = "Helvetica 18 bold").grid(row = 0, column = 0, columnspan = 4)
    
    other_styles = {'height':2, 'width':23, 'font':"bold", 'bg':"#eee", 'relief':"ridge"}
    
    tk.Label(Other_Frame, text = "CNIC", **other_styles).grid(row = 1, column = 0)
    tk.Label(Other_Frame, text = other[1], **other_styles).grid(row = 1, column = 1)

    tk.Label(Other_Frame, text = "Date of Birth", **other_styles).grid(row = 1, column = 2)
    tk.Label(Other_Frame, text = other[2], **other_styles).grid(row = 1, column = 3)

    tk.Label(Other_Frame, text = "Gender", **other_styles).grid(row = 2, column = 0)
    tk.Label(Other_Frame, text = other[3], **other_styles).grid(row = 2, column = 1)

    tk.Label(Other_Frame, text = "Martial Status", **other_styles).grid(row = 2, column = 2)
    tk.Label(Other_Frame, text = other[4], **other_styles).grid(row = 2, column = 3)

    tk.Label(Other_Frame, text = "Nationality", **other_styles).grid(row = 3, column = 0)
    tk.Label(Other_Frame, text = other[5], **other_styles).grid(row = 3, column = 1)

    tk.Label(Other_Frame, text = "Province", **other_styles).grid(row = 3, column = 2)
    tk.Label(Other_Frame, text = other[6], **other_styles).grid(row = 3, column = 3)

    tk.Label(Other_Frame, text = "District", **other_styles).grid(row = 4, column = 0)
    tk.Label(Other_Frame, text = other[7], **other_styles).grid(row = 4, column = 1)

    tk.Label(Other_Frame, text = "Tehsile", **other_styles).grid(row = 4, column = 2)
    tk.Label(Other_Frame, text = other[8], **other_styles).grid(row = 4, column = 3)

    tk.Label(Other_Frame, text = "Zip Code", **other_styles).grid(row = 5, column = 0)
    tk.Label(Other_Frame, text = other[9], **other_styles).grid(row = 5, column = 1)

    tk.Label(Other_Frame, text = "Mother Tongue", **other_styles).grid(row = 5, column = 2)
    tk.Label(Other_Frame, text = other[10], **other_styles).grid(row = 5, column = 3)

    tk.Label(Other_Frame, text = "E-mail", **other_styles).grid(row = 6, column = 0)
    tk.Label(Other_Frame, text = other[11], **other_styles).grid(row = 6, column = 1)

    tk.Label(Other_Frame, text = "Phone No", **other_styles).grid(row = 6, column = 2)
    tk.Label(Other_Frame, text = other[12], **other_styles).grid(row = 6, column = 3)

    tk.Label(Other_Frame, text = "Blood", **other_styles).grid(row = 7, column = 0)
    tk.Label(Other_Frame, text = other[13], **other_styles).grid(row = 7, column = 1)

    tk.Label(Other_Frame, text = "Religion", **other_styles).grid(row = 7, column = 2)
    tk.Label(Other_Frame, text = other[14], **other_styles).grid(row = 7, column = 3)

    tk.Label(Other_Frame, text = "Is Hafiz", **other_styles).grid(row = 8, column = 0)
    tk.Label(Other_Frame, text = other[15], **other_styles).grid(row = 8, column = 1)

    tk.Label(Other_Frame, text = "Is Disable", **other_styles).grid(row = 8, column = 2)
    tk.Label(Other_Frame, text = other[16], **other_styles).grid(row = 8, column = 3)

    tk.Label(Other_Frame, text = "Guardian Name", **other_styles).grid(row = 9, column = 0)
    tk.Label(Other_Frame, text = other[17], **other_styles).grid(row = 9, column = 1)

    tk.Label(Other_Frame, text = "Guardian CNIC", **other_styles).grid(row = 9, column = 2)
    tk.Label(Other_Frame, text = other[18], **other_styles).grid(row = 9, column = 3)

    tk.Label(Other_Frame, text = "Guardian Phone No", **other_styles).grid(row = 10, column = 0)
    tk.Label(Other_Frame, text = other[19], **other_styles).grid(row = 10, column = 1)

    tk.Label(Other_Frame, text = "Guardian E-mail", **other_styles).grid(row = 10, column = 2)
    tk.Label(Other_Frame, text = other[20], **other_styles).grid(row = 10, column = 3)

############################################################################
##                                                                        ##
##                          STUDENT LOGIN FUNCTION                        ##
##                                                                        ##
############################################################################

def Admin_Login():
    
    Database_Connection()
    
    Username = str(username_e.get())
    ID = str(id_e.get())
    Password = str(password_e.get())
    
    selectQ = "Select * from admin_login"

    cursor.execute(selectQ)
    rows = cursor.fetchall()
    
    check = False
    for row in rows:
        if Username == str(row[0]) and ID == str(row[1]) and Password == str(row[2]):
               check = True
    
    if check == True:
        Admin_Profile(ID)
    else:
        wrong_login = messagebox.askretrycancel("Login Error", "Wrong Details")
        if wrong_login == 1:
            for widgets in Body_Frame.winfo_children():
                widgets.destroy()
            Admin_Main()
        elif wrong_login == 0:
            w.destroy()

############################################################################
##                                                                        ##
##                           MAIN CODE FUNCTION                           ##
##                                                                        ##
############################################################################

def Admin_Main():
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()

                    #################
                    ## LOGIN_FRAME ##
                    #################
    
    Login_Frame = tk.Frame(Body_Frame)
    Login_Frame.pack()
    
    global username_e
    global id_e
    global password_e
    
    tk.Label(Login_Frame, text = "LOGIN AS ADMIN", height = 2, font = 'Helvetica 18 bold').grid(row = 0, column = 0)
    
    tk.Label(Login_Frame, text = "Username", font = 'Helvetica 12').grid(row = 1, column = 0, pady = 10)
    
    username_e = ttk.Entry(Login_Frame, font = 'Helvetica 12')
    username_e.grid(row = 2, column = 0)
    
    tk.Label(Login_Frame, text = "ID", font = 'Helvetica 12').grid(row = 3, column = 0, pady = 10)
    
    id_e = ttk.Entry(Login_Frame, font = 'Helvetica 12')
    id_e.grid(row = 4, column = 0)
    
    tk.Label(Login_Frame, text = "Password", font = 'Helvetica 12').grid(row = 5, column = 0, pady = 10)
    
    global bullet
    bullet = "\u2022"
    
    password_e = ttk.Entry(Login_Frame, font = 'Helvetica 12', show = bullet)
    password_e.grid(row = 6, column = 0)
    c_pass = tk.IntVar(value = 0)
    
    ############################################################################
    ##                        SHOW PASSWORD FUNCTION                          ##
    ############################################################################
    
    def Show_Password():
        if(c_pass.get() == 1):
            password_e.config(show = '')
        else:
            password_e.config(show = bullet)
    
    showpassword = tk.Checkbutton(Login_Frame, font = 'Helvetica 12', text = 'Show Password', variable = c_pass, onvalue = 1, offvalue = 0, command = Show_Password)
    showpassword.grid(row = 7, column = 0, pady = 10)
    
    ttk.Button(Login_Frame, text = "LOGIN ", width = 10, command = Admin_Login).grid(row = 8, pady = 5)

    ttk.Button(Login_Frame, text = "BACK", width = 10, command = Main).grid(row = 9, pady = 5)
    
############################################################################
##                                                                        ##
##                             LOGOUT FUNCTION                            ##
##                                                                        ##
############################################################################

def Student_LogOut():
    
    logout = messagebox.askyesno("Logout", "Do You Want to Logout")
    
    if logout == 1:
        
        for widgets in Body_Frame.winfo_children():
            widgets.destroy()
        
        #RETURNS TO MAIN FUNCTION
        Student_Main()
    
    elif logout == 0:
        pass

############################################################################
##                                                                        ##
##                        UPDATE PASSWORD FUNCTION                        ##
##                                                                        ##
############################################################################

def Student_UpdatePassword(Roll_No):
        
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "y", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Student_Profile(Roll_No))).grid(row = 0, column = 0)

    tk.Button(Menu_Frame, text = "ENROLLMENTS", **menu_styles, command = (lambda : Enrollments(Roll_No))).grid(row = 1, column = 0)

    tk.Button(Menu_Frame, text = "ATTENDANCE", **menu_styles, command = (lambda : Attendance(Roll_No))).grid(row = 2, column = 0)

    tk.Button(Menu_Frame, text = "RESULT", **menu_styles, command = (lambda : Result(Roll_No))).grid(row = 3, column = 0)

    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, background = "#999", state = "disabled").grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Student_LogOut).grid(row = 5, column = 0)
    
    ############################################################################
    ##                           UPDATED FUNCTION                             ##
    ############################################################################
    
    def Updated():
        current_password = current_password_e.get()
        new_password = new_password_e.get()
        new_password_again = new_password_again_e.get()
        
        selectQ = "Select Password from login WHERE Roll_No = %s"
        
        Roll_No_tuple = (Roll_No, )
        cursor.execute(selectQ, Roll_No_tuple)
        orignal_password = cursor.fetchone()

        if current_password == orignal_password[0]:
            if new_password == new_password_again:
                if new_password != current_password:
                    tk.messagebox.showinfo("Password Updated", "Password Updated Successfully")
                    updateQ = "UPDATE Login SET Password = %s WHERE Roll_No = %s"
                    Data = (new_password, Roll_No)
                    cursor.execute(updateQ, Data)
                    conn.commit()
                else:
                    tk.messagebox.showerror("Password Error", "Same as Your Current Password")
                    current_password_e.delete(0, tk.END)
                    new_password_e.delete(0, tk.END)
                    new_password_again_e.delete(0, tk.END)
            else:
                tk.messagebox.showerror("Password Error", "New Password is Not Matched")
                current_password_e.delete(0, tk.END)
                new_password_e.delete(0, tk.END)
                new_password_again_e.delete(0, tk.END)
        else:
            tk.messagebox.showerror("Password Error", "Wrong Current Password")
            current_password_e.delete(0, tk.END)
            new_password_e.delete(0, tk.END)
            new_password_again_e.delete(0, tk.END)
    
                    ###########################
                    ## Update_Password_FRAME ##
                    ###########################
    
    UpdatePassword_Frame = tk.LabelFrame(Body_Frame)
    UpdatePassword_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Label(UpdatePassword_Frame, text = "UPDATE PASSWORD", height = 2, font = 'Helvetica 18 bold', relief = 'ridge').grid(row = 0, column = 0, ipadx = 442)
    
    tk.Label(UpdatePassword_Frame, text = "Enter Current Password ", font = '12').grid(row = 1, column = 0, pady = 10)
    
    current_password_e = ttk.Entry(UpdatePassword_Frame, font = '12')
    current_password_e.grid(row = 2, column = 0)
    
    tk.Label(UpdatePassword_Frame, text = "New Password ", font = '12').grid(row = 3, column = 0, pady = 10)
    
    new_password_e = ttk.Entry(UpdatePassword_Frame, font = '12')
    new_password_e.grid(row = 4, column = 0)
    
    tk.Label(UpdatePassword_Frame, text = "Confirm New Password ", font = '12').grid(row = 5, column = 0, pady = 10)
    
    new_password_again_e = ttk.Entry(UpdatePassword_Frame, font = '12')
    new_password_again_e.grid(row = 6, column = 0)
    
    ttk.Button(UpdatePassword_Frame, text = "UPDATE", command = Updated).grid(row = 7, column = 0, pady = 10)

############################################################################
##                                                                        ##
##                            RESULT FUNCTION                             ##
##                                                                        ##
############################################################################

def Result(Roll_No):
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Student_Profile(Roll_No))).grid(row = 0, column = 0)

    tk.Button(Menu_Frame, text = "ENROLLMENTS", **menu_styles, command = (lambda : Enrollments(Roll_No))).grid(row = 1, column = 0)

    tk.Button(Menu_Frame, text = "ATTENDANCE", **menu_styles, command = (lambda : Attendance(Roll_No))).grid(row = 2, column = 0)

    tk.Button(Menu_Frame, text = "RESULT", **menu_styles, background = "#999", state = "disabled").grid(row = 3, column = 0)

    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Student_UpdatePassword(Roll_No))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Student_LogOut).grid(row = 5, column = 0)
    
    ############################################################################
    ##                       SEMESTER RESULT FUNCTION                         ##
    ############################################################################
    
    def Semester_Result():
        try:    
            for record in result_tree.get_children():
                result_tree.delete(record)
            
            r_table = "result_s_" + str(Roll_No)
            selectQ = "Select * from " + r_table + " where Semester = %s"
        
            s = (semester.get(), )
            cursor.execute(selectQ, s)
            rows = cursor.fetchall()
            points = []
            credit = []
        
            for row in rows:
            
                total = int(row[4] + row[5] + row[6])
            
                if total >= 90:
                    grade = "A+"
                    point = 4.0
            
                elif total >= 80 and total < 90:
                    grade = "A"
                    point = 4.0
            
                elif total >= 70 and total < 80:
                    grade = "B"
                    if total == 79:
                        point = 3.9
                
                    elif total == 78:
                        point = 3.8
                
                    elif total == 77:
                        point = 3.7
                
                    elif total == 76:
                        point = 3.6
                
                    elif total == 75:
                        point = 3.5

                    elif total == 74:
                        point = 3.4
                
                    elif total == 73:
                        point = 3.3

                    elif total == 72:
                        point = 3.2
                
                    elif total == 71:
                        point = 3.1
                
                    elif total == 70:
                        point = 3.0
            
                elif total >= 60 and total < 70:
                    grade = "C"
                    if total == 69:
                        point = 2.9
                
                    elif total == 68:
                        point = 2.8
                
                    elif total == 67:
                        point = 2.7
                
                    elif total == 66:
                        point = 2.6
                
                    elif total == 65:
                        point = 2.5
                
                    elif total == 64:
                        point = 2.4
                
                    elif total == 63:
                        point = 2.3
                
                    elif total == 62:
                        point = 2.2
                
                    elif total == 61:
                        point = 2.1

                    elif total == 60:
                        point = 2.0
            
                elif total >= 50 and total < 60:
                    grade = "D"
                    if total == 59:
                        point = 1.9
                
                    elif total == 58:
                        point = 1.8
                
                    elif total == 57:
                        point = 1.7
                
                    elif total == 56:
                        point = 1.6
                
                    elif total == 55:
                        point = 1.5
                
                    elif total == 54:
                        point = 1.4
                
                    elif total == 53:
                        point = 1.3
                
                    elif total == 52:
                        point = 1.2

                    elif total == 51:
                        point = 1.1

                    elif total == 50:
                        point = 1.0
            
                elif total < 50:
                    grade = "F"
                    point = 0.0
            
                cr_hr = row[2]
                credit.append(float(cr_hr[0]))
                points.append(float(point))
            
                result = (row[0], row[1], row[2], row[4], row[5], row[6], total, grade, point)
            
                result_tree.insert("", tk.END, values = result)

            gpa_points = 0.0
            total_credit = 0.0
            for i in range(len(points)):
                gpa_points += float(points[i]*credit[i])
                total_credit += credit[i]

            gpa = gpa_points/total_credit
            gpa = str(gpa)
            gpa = gpa[0] + gpa[1] + gpa[2] + gpa[3]
            gpa_l.config(text = "GPA: "+ str(gpa))
        except:
            result = ("-", "-", "-", "-", "-", "-", "-", "-", "-")
            result_tree.insert("", tk.END, values = result)
                    ##################
                    ## RESULT_FRAME ##
                    ##################
    
    Result_Frame = tk.LabelFrame(Body_Frame)
    
    Result_Frame.pack(expand = 1, fill = "both", side = "left")
    
    
    selectQ = "Select F_Name, L_Name, Semester from basic where Roll_No = %s"
    Roll_No_tuple = (Roll_No, )
    cursor.execute(selectQ, Roll_No_tuple)
    basic = cursor.fetchone()
    
                    ##################
                    ## SELECT_FRAME ##
                    ##################
    
    Select_Frame = tk.Frame(Result_Frame)
    
    Select_Frame.pack(expand = 1, fill = "x")

    semesters = []

    for i in range(1, int(basic[2])):
        semesters.append(i)

    semester = tk.StringVar()
    semester.set("1")

    select_l = tk.Label(Select_Frame, text = "Semester:", anchor = "w", font = "bold")
    select_l.grid(row = 0, column = 0)

    select = ttk.Combobox(Select_Frame, textvariable = semester, value = semesters, state = "readonly")
    select.grid(row = 0, column = 1, padx = 10, pady = 10)

    view_r_b = ttk.Button(Select_Frame, text = "VIEW", command = Semester_Result)
    view_r_b.grid(row = 0, column = 2)
    
                    ###############
                    ## GPA_FRAME ##
                    ###############
    
    GPA_Frame = tk.LabelFrame(Result_Frame)
    
    GPA_Frame.pack(expand = 1, fill = "x")
    
    Result_Roll_No = "Roll No: " + str(Roll_No)
    roll_l = tk.Label(GPA_Frame, text = Result_Roll_No, **bar_styles, anchor = "w")
    roll_l.grid(row = 0, column = 0)
    
    Result_Name = "Name: " + basic[0] + " " + basic[1]
    Name_l = tk.Label(GPA_Frame, text = Result_Name, **bar_styles, anchor = "w")
    Name_l.grid(row = 0, column = 1)
    
    gpa_l = tk.Label(GPA_Frame, text = "GPA: ", **bar_styles, anchor = "e")
    gpa_l.grid(row = 0, column = 2)
    
                    #######################
                    ## RESULT_TREE_FRAME ##
                    #######################
    
    Result_tree_Frame = tk.Frame(Result_Frame)
    
    Result_tree_Frame.pack(expand = 1, fill = "both", side = "left")
    
    result_scrollbar = tk.Scrollbar(Result_tree_Frame)
    
    result_tree = ttk.Treeview(Result_tree_Frame, column = ("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show = "headings", yscrollcommand = result_scrollbar.set)

    result_scrollbar.pack(side = "right", fill = "y")
    
    result_tree.column("#1", anchor = tk.CENTER, width = 335)
    
    result_tree.heading("#1", text = "Course Name")
    
    result_tree.column("#2", anchor = tk.CENTER, width = 200)
    
    result_tree.heading("#2", text = "Teacher Name")
    
    result_tree.column("#3", anchor = tk.CENTER, width = 100)
    
    result_tree.heading("#3", text = "Cr. Hr")
    
    result_tree.column("#4", anchor = tk.CENTER, width = 80)
    
    result_tree.heading("#4", text = "Mid")
    
    result_tree.column("#5", anchor = tk.CENTER, width = 80)
    
    result_tree.heading("#5", text = "Sessional")
    
    result_tree.column("#6", anchor = tk.CENTER, width = 80)
    
    result_tree.heading("#6", text = "Final")
    
    result_tree.column("#7", anchor = tk.CENTER, width = 80)
    
    result_tree.heading("#7", text = "Total")
    
    result_tree.column("#8", anchor = tk.CENTER, width = 80)
    
    result_tree.heading("#8", text = "Grade")
    
    result_tree.column("#9", anchor = tk.CENTER, width = 80)
    
    result_tree.heading("#9", text = "Points")
    
    result_tree.pack()
    
    result_scrollbar.config(command = result_tree.yview)

############################################################################
##                                                                        ##
##                          ATTENDANCE FUNCTION                           ##
##                                                                        ##
############################################################################

def Attendance(Roll_No):
        
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Student_Profile(Roll_No))).grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ENROLLMENTS", **menu_styles, command = (lambda : Enrollments(Roll_No))).grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ATTENDANCE", **menu_styles, background = "#999", state = "disabled").grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "RESULT", **menu_styles, command = (lambda : Result(Roll_No))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Student_UpdatePassword(Roll_No))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Student_LogOut).grid(row = 5, column = 0)
    
                    ##########################
                    ## ATTENDANCE_BAR_FRAME ##
                    ##########################
    
    Attendance_Bar_Frame = tk.LabelFrame(Body_Frame)
    
    Attendance_Bar_Frame.pack(expand = 1, fill = "x")
    
    selectQ = "Select F_Name, L_Name, Semester from basic where Roll_No = %s"
    Roll_No_tuple = (Roll_No, )
    cursor.execute(selectQ, Roll_No_tuple)
    basic = cursor.fetchone()
    
    tk.Label(Attendance_Bar_Frame, text = "Roll No: " + str(Roll_No), **bar_styles, anchor = "w").grid(row = 0, column = 0)

    tk.Label(Attendance_Bar_Frame, text = "Name: " + basic[0] + " " + basic[1], **bar_styles, anchor = "w").grid(row = 0, column = 1)

    tk.Label(Attendance_Bar_Frame, text = "Current Semester: " + basic[2], **bar_styles, anchor = "e").grid(row = 0, column = 2)
    
                    ######################
                    ## ATTENDANCE_FRAME ##
                    ######################
    
    Attendance_Frame = tk.Frame(Body_Frame)
    
    Attendance_Frame.pack(expand = 1, fill = "both", side = "left")
    
    attendance_scrollbar = tk.Scrollbar(Attendance_Frame)
    
    attendance_scrollbar.pack(side = "right", fill = "y")
    
    attendance_tree = ttk.Treeview(Attendance_Frame, column = ("c1", "c2", "c3", "c4", "c5", "c6", "c5", "c6"), show = "headings", yscrollcommand = attendance_scrollbar.set)
    
    attendance_tree.column("#1", anchor = tk.CENTER, width = 319)
    
    attendance_tree.heading("#1", text = "Course Name")
    
    attendance_tree.column("#2", anchor = tk.CENTER, width = 200)
    
    attendance_tree.heading("#2", text = "Teacher Name")
    
    attendance_tree.column("#3", anchor = tk.CENTER, width = 100)
    
    attendance_tree.heading("#3", text = "Cr. Hr")
    
    attendance_tree.column("#4", anchor = tk.CENTER, width = 100)
    
    attendance_tree.heading("#4", text = "Lectures")
    
    attendance_tree.column("#5", anchor = tk.CENTER, width = 100)
    
    attendance_tree.heading("#5", text = "Presents")
    
    attendance_tree.column("#6", anchor = tk.CENTER, width = 100)
    
    attendance_tree.heading("#6", text = "Absents")
    
    attendance_tree.column("#7", anchor = tk.CENTER, width = 100)
    
    attendance_tree.heading("#7", text = "Percent")
    
    attendance_tree.column("#8", anchor = tk.CENTER, width = 100)
    
    attendance_tree.heading("#8", text = "Status")
    
    attendance_tree.pack()
    
    attendance_scrollbar.config(command = attendance_tree.yview)
    
    try:
        a_table = "attendance_s_" + str(Roll_No)
        selectQ = "Select * from " + a_table
    
        cursor.execute(selectQ)
        rows = cursor.fetchall()
    
        for row in rows:
    
            percent = int((int(row[5])/int(row[4]))*100)
            if percent >= 75:
                status = "Eligible"
            else:
                status = "Not Eligible"
        
            attendance = (row[0], row[1], row[2], row[4], row[5], row[6], percent, status)
    
            attendance_tree.insert("", tk.END, values = attendance)
    
    except:
           
        attendance = ("-", "-", "-", "-", "-", "-", "-", "-")
        attendance_tree.insert("", tk.END, values = attendance)

############################################################################
##                                                                        ##
##                          ENROLLMENTS FUNCTION                          ##
##                                                                        ##
############################################################################

def Enrollments(Roll_No):
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, command = (lambda : Student_Profile(Roll_No))).grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ENROLLMENTS", **menu_styles, background = "#999", state = "disabled").grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ATTENDANCE", **menu_styles, command = (lambda : Attendance(Roll_No))).grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "RESULT", **menu_styles, command = (lambda : Result(Roll_No))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Student_UpdatePassword(Roll_No))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Student_LogOut).grid(row = 5, column = 0)
    
                    ###########################
                    ## ENROLLMENTS_BAR_FRAME ##
                    ###########################
    
    selectQ = "Select F_Name, L_Name, Semester from basic where Roll_No = %s"
    Roll_No_tuple = (Roll_No, )
    cursor.execute(selectQ, Roll_No_tuple)
    basic = cursor.fetchone()
    
    Enrollments_Bar_Frame = tk.LabelFrame(Body_Frame)
    
    Enrollments_Bar_Frame.pack(expand = 1, fill = "x")

    tk.Label(Enrollments_Bar_Frame, text = "Roll No: " + str(Roll_No), **bar_styles, anchor = "w").grid(row = 0, column = 0)

    tk.Label(Enrollments_Bar_Frame, text = "Name: " + basic[0] + " " + basic[1], **bar_styles, anchor = "w").grid(row = 0, column = 1)

    tk.Label(Enrollments_Bar_Frame, text = "Current Semester: " + basic[2], **bar_styles, anchor = "e").grid(row = 0, column = 2)

                    #######################
                    ## ENROLLMENTS_FRAME ##
                    #######################
    
    Enrollments_Frame = tk.Frame(Body_Frame)
    
    Enrollments_Frame.pack(expand = 1, fill = "both", side = "left")

    enrollments_scrollbar = tk.Scrollbar(Enrollments_Frame)
    
    enrollments_tree = ttk.Treeview(Enrollments_Frame, column = ("c1", "c2", "c3", "c4"), show = "headings", yscrollcommand = enrollments_scrollbar.set)
    
    enrollments_scrollbar.pack(side = "right", fill = "y")
    
    enrollments_tree = ttk.Treeview(Enrollments_Frame, column = ("c1", "c2", "c3", "c4"), show = "headings", yscrollcommand = enrollments_scrollbar.set)

    enrollments_tree.column("#1", anchor = tk.CENTER, width = 460)

    enrollments_tree.heading("#1", text = "Course Name")

    enrollments_tree.column("#2", anchor = tk.CENTER, width = 360)

    enrollments_tree.heading("#2", text = "Teacher Name")

    enrollments_tree.column("#3", anchor = tk.CENTER, width = 150)

    enrollments_tree.heading("#3", text = "Cr. Hr")

    enrollments_tree.column("#4", anchor = tk.CENTER, width = 150)

    enrollments_tree.heading("#4", text = "Semester")

    enrollments_tree.pack()

    enrollments_scrollbar.config(command = enrollments_tree.yview)
    
    try:
        e_table = "enrollments_s_" + Roll_No
        selectQ = "Select Course_Name, Teacher_Name, Credits, Semester from " + e_table + " ORDER BY Semester"

        cursor.execute(selectQ)
        rows = cursor.fetchall()

        for row in rows:    
            enrollments = (row[0], row[1], row[2], row[3])
            enrollments_tree.insert("", tk.END, values = enrollments)
    except:   
        enrollments = ("-", "-", "-", "-")
        enrollments_tree.insert("", tk.END, values = enrollments)

############################################################################
##                                                                        ##
##                            PROFILE FUNCTION                            ##
##                                                                        ##
############################################################################

def Student_Profile(Roll_No):
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    ################
                    ## MENU_FRAME ##
                    ################
    
    Menu_Frame = tk.LabelFrame(Body_Frame)
    
    Menu_Frame.pack(expand = 1, fill = "both", side = "left")
    
    tk.Button(Menu_Frame, text = "MY PROFILE", **menu_styles, background = "#999", state = "disabled").grid(row = 0, column = 0)
    
    tk.Button(Menu_Frame, text = "ENROLLMENTS", **menu_styles, command = (lambda : Enrollments(Roll_No))).grid(row = 1, column = 0)
    
    tk.Button(Menu_Frame, text = "ATTENDANCE", **menu_styles, command = (lambda : Attendance(Roll_No))).grid(row = 2, column = 0)
    
    tk.Button(Menu_Frame, text = "RESULT", **menu_styles, command = (lambda : Result(Roll_No))).grid(row = 3, column = 0)
    
    tk.Button(Menu_Frame, text = "UPDATE PASSWORD", **menu_styles, command = (lambda : Student_UpdatePassword(Roll_No))).grid(row = 4, column = 0)
    
    tk.Button(Menu_Frame, text = "LOGOUT", **menu_styles, command = Student_LogOut).grid(row = 5, column = 0)
    
                    #################
                    ## BASIC_FRAME ##
                    #################
    
    Basic_Frame = tk.LabelFrame(Body_Frame)
    
    Basic_Frame.pack(expand = 1, fill = "y", side = "left")
    
    #Getting Data for Basic Informations from Database_Connection
    selectQ = "Select * from basic where Roll_No = %s"
    Roll_No_tuple = (Roll_No, )
    cursor.execute(selectQ, Roll_No_tuple)
    personal = cursor.fetchone()
    
    global profile_img
    profile_img = ImageTk.PhotoImage(data = personal[1])
    
    tk.Label(Basic_Frame, image = profile_img).grid(row = 0, column = 0, columnspan = 2)
    tk.Label(Basic_Frame, text = personal[2] + " " + personal[3], font = "Helvetica 14 bold").grid(row = 1, column = 0, columnspan = 2)
    
    basic_styles = {'height':2, 'width':15, 'font':"bold", 'relief':"ridge"}
    
    tk.Label(Basic_Frame, text = "Roll No", **basic_styles).grid(row = 2, column = 0)
    tk.Label(Basic_Frame, text = personal[0], **basic_styles).grid(row = 2, column = 1)

    tk.Label(Basic_Frame, text = "Department", **basic_styles).grid(row = 3, column = 0)
    tk.Label(Basic_Frame, text = personal[4], **basic_styles).grid(row = 3, column = 1)

    tk.Label(Basic_Frame, text = "Program", **basic_styles).grid(row = 4, column = 0)
    tk.Label(Basic_Frame, text = personal[5], **basic_styles).grid(row = 4, column = 1)

    tk.Label(Basic_Frame, text = "Semester", **basic_styles).grid(row = 5, column = 0)
    tk.Label(Basic_Frame, text = personal[6], **basic_styles).grid(row = 5, column = 1)

    tk.Label(Basic_Frame, text = "Section", **basic_styles).grid(row = 6, column = 0)
    tk.Label(Basic_Frame, text = personal[7], **basic_styles).grid(row = 6, column = 1)

    tk.Label(Basic_Frame, text = "Session", **basic_styles).grid(row = 7, column = 0)
    tk.Label(Basic_Frame, text = personal[8], **basic_styles).grid(row = 7, column = 1)
    
                    #################
                    ## OTHER_FRAME ##
                    #################
    
    Other_Frame = tk.LabelFrame(Body_Frame)
    
    Other_Frame.pack(expand = 1, fill = "both", side = "right")
    
    #Getting Data for Other Informations from Database_Connection
    selectQ = "Select * from other where Roll_No = %s"
    Roll_No_tuple = (Roll_No, )
    cursor.execute(selectQ, Roll_No_tuple)
    other = cursor.fetchone()
    
    tk.Label(Other_Frame, text = "OTHER DETAILS", height = 2, width = 56, font = "Helvetica 18 bold").grid(row = 0, column = 0, columnspan = 4)
    
    other_styles = {'height':2, 'width':23, 'font':"bold", 'bg':"#eee", 'relief':"ridge"}
    
    tk.Label(Other_Frame, text = "CNIC", **other_styles).grid(row = 1, column = 0)
    tk.Label(Other_Frame, text = other[1], **other_styles).grid(row = 1, column = 1)

    tk.Label(Other_Frame, text = "Date of Birth", **other_styles).grid(row = 1, column = 2)
    tk.Label(Other_Frame, text = other[2], **other_styles).grid(row = 1, column = 3)

    tk.Label(Other_Frame, text = "Gender", **other_styles).grid(row = 2, column = 0)
    tk.Label(Other_Frame, text = other[3], **other_styles).grid(row = 2, column = 1)

    tk.Label(Other_Frame, text = "Martial Status", **other_styles).grid(row = 2, column = 2)
    tk.Label(Other_Frame, text = other[4], **other_styles).grid(row = 2, column = 3)

    tk.Label(Other_Frame, text = "Nationality", **other_styles).grid(row = 3, column = 0)
    tk.Label(Other_Frame, text = other[5], **other_styles).grid(row = 3, column = 1)

    tk.Label(Other_Frame, text = "Province", **other_styles).grid(row = 3, column = 2)
    tk.Label(Other_Frame, text = other[6], **other_styles).grid(row = 3, column = 3)

    tk.Label(Other_Frame, text = "District", **other_styles).grid(row = 4, column = 0)
    tk.Label(Other_Frame, text = other[7], **other_styles).grid(row = 4, column = 1)

    tk.Label(Other_Frame, text = "Tehsile", **other_styles).grid(row = 4, column = 2)
    tk.Label(Other_Frame, text = other[8], **other_styles).grid(row = 4, column = 3)

    tk.Label(Other_Frame, text = "Zip Code", **other_styles).grid(row = 5, column = 0)
    tk.Label(Other_Frame, text = other[9], **other_styles).grid(row = 5, column = 1)

    tk.Label(Other_Frame, text = "Mother Tongue", **other_styles).grid(row = 5, column = 2)
    tk.Label(Other_Frame, text = other[10], **other_styles).grid(row = 5, column = 3)

    tk.Label(Other_Frame, text = "E-mail", **other_styles).grid(row = 6, column = 0)
    tk.Label(Other_Frame, text = other[11], **other_styles).grid(row = 6, column = 1)

    tk.Label(Other_Frame, text = "Phone No", **other_styles).grid(row = 6, column = 2)
    tk.Label(Other_Frame, text = other[12], **other_styles).grid(row = 6, column = 3)

    tk.Label(Other_Frame, text = "Blood", **other_styles).grid(row = 7, column = 0)
    tk.Label(Other_Frame, text = other[13], **other_styles).grid(row = 7, column = 1)

    tk.Label(Other_Frame, text = "Religion", **other_styles).grid(row = 7, column = 2)
    tk.Label(Other_Frame, text = other[14], **other_styles).grid(row = 7, column = 3)

    tk.Label(Other_Frame, text = "Is Hafiz", **other_styles).grid(row = 8, column = 0)
    tk.Label(Other_Frame, text = other[15], **other_styles).grid(row = 8, column = 1)

    tk.Label(Other_Frame, text = "Is Disable", **other_styles).grid(row = 8, column = 2)
    tk.Label(Other_Frame, text = other[16], **other_styles).grid(row = 8, column = 3)

    tk.Label(Other_Frame, text = "Guardian Name", **other_styles).grid(row = 9, column = 0)
    tk.Label(Other_Frame, text = other[17], **other_styles).grid(row = 9, column = 1)

    tk.Label(Other_Frame, text = "Guardian CNIC", **other_styles).grid(row = 9, column = 2)
    tk.Label(Other_Frame, text = other[18], **other_styles).grid(row = 9, column = 3)

    tk.Label(Other_Frame, text = "Guardian Phone No", **other_styles).grid(row = 10, column = 0)
    tk.Label(Other_Frame, text = other[19], **other_styles).grid(row = 10, column = 1)

    tk.Label(Other_Frame, text = "Guardian E-mail", **other_styles).grid(row = 10, column = 2)
    tk.Label(Other_Frame, text = other[20], **other_styles).grid(row = 10, column = 3)
    
############################################################################
##                                                                        ##
##                          STUDENT LOGIN FUNCTION                        ##
##                                                                        ##
############################################################################

def Student_Login():
    
    Database_Connection()
    
    Username = str(username_e.get())
    Roll_No = str(rollno_e.get())
    Password = str(password_e.get())
    
    selectQ = "Select * from login"

    cursor.execute(selectQ)
    rows = cursor.fetchall()
    
    check = False
    for row in rows:
        if Username == str(row[0]) and Roll_No == str(row[1]) and Password == str(row[2]):
               check = True
    
    
    if check == True:
        Student_Profile(Roll_No)
    else:
        wrong_login = messagebox.askretrycancel("Login Error", "Wrong Details")
        if wrong_login == 1:
            for widgets in Body_Frame.winfo_children():
                widgets.destroy()
            Student_Main()
        elif wrong_login == 0:
            w.destroy()

############################################################################
##                                                                        ##
##                           MAIN CODE FUNCTION                           ##
##                                                                        ##
############################################################################

def Student_Main():
    
    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
                    #################
                    ## LOGIN_FRAME ##
                    #################
    
    Login_Frame = tk.Frame(Body_Frame)
    Login_Frame.pack()
    
    global username_e
    global rollno_e
    global password_e
    
    tk.Label(Login_Frame, text = "LOGIN AS STUDENT", height = 2, font = 'Helvetica 18 bold').grid(row = 0, column = 0)
    
    tk.Label(Login_Frame, text = "Username", font = 'Helvetica 12').grid(row = 1, column = 0, pady = 10)
    
    username_e = ttk.Entry(Login_Frame, font = 'Helvetica 12')
    username_e.grid(row = 2, column = 0)
    
    tk.Label(Login_Frame, text = "Roll No", font = 'Helvetica 12').grid(row = 3, column = 0, pady = 10)
    
    rollno_e = ttk.Entry(Login_Frame, font = 'Helvetica 12')
    rollno_e.grid(row = 4, column = 0)
    
    tk.Label(Login_Frame, text = "Password", font = 'Helvetica 12').grid(row = 5, column = 0, pady = 10)
    
    global bullet
    bullet = "\u2022"
    
    password_e = ttk.Entry(Login_Frame, font = 'Helvetica 12', show = bullet)
    password_e.grid(row = 6, column = 0)
    c_pass = tk.IntVar(value = 0)
    
    ############################################################################
    ##                        SHOW PASSWORD FUNCTION                          ##
    ############################################################################
    
    def Show_Password():
        if(c_pass.get() == 1):
            password_e.config(show = '')
        else:
            password_e.config(show = bullet)
    
    showpassword = tk.Checkbutton(Login_Frame, font = 'Helvetica 12', text = 'Show Password', variable = c_pass, onvalue = 1, offvalue = 0, command = Show_Password)
    showpassword.grid(row = 7, column = 0, pady = 10)
    
    ttk.Button(Login_Frame, text = "LOGIN", width = 10, command = Student_Login).grid(row = 8, pady = 5)

    ttk.Button(Login_Frame, text = "BACK", width = 10, command = Main).grid(row = 9, pady = 5)

############################################################################
##                                                                        ##
##                           MAIN CODE FUNCTION                           ##
##                                                                        ##
############################################################################

def Main():

    for widgets in Body_Frame.winfo_children():
        widgets.destroy()
    
    ttk.Button(Body_Frame, text = "LOGIN AS ADMIN", width = 20, command = Admin_Main).pack(pady = 10)

    ttk.Button(Body_Frame, text = "LOGIN AS STUDENT", width = 20, command = Student_Main).pack()


    
                    ##################
                    ## HEADER_FRAME ##
                    ##################
    
Header_Frame.pack(side = "top")
    
header_image.pack()

                    ################
                    ## BODY_FRAME ##
                    ################
    
Body_Frame.pack(expand = 1, fill = "both")

Main()

w.mainloop()