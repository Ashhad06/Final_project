from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector as mysql
from tkinter.ttk import Combobox

root = Tk()
root.title("Main Window")
root.minsize(width=660,height=250)
root.maxsize(width=660,height=250)
root.configure(bg="Black")
Total=0


def Customer():

    customer_login_window = Toplevel(root)
    customer_login_window.title("Customer login")
    customer_login_window.minsize(width=300,height=200)
    customer_login_window.maxsize(width=700,height=200)
    customer_login_window.configure(bg="cornsilk")
    root.withdraw()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "" or password == "":
            Messagebox.showinfo(".", "Please Fill all fields")
        else:
            con = mysql.connect(host="localhost", user="root", database="online_order")
            cursor = con.cursor()
            cursor.execute(" select * from customer_login")
            check = cursor.fetchall()
            for i in check:
                if i[0] == username and i[1] == password:
                    con.close()
                    customer_window = Toplevel(root)
                    customer_window.title("New Window")
                    customer_window.minsize(width=300,height=180)
                    dropdown = Combobox(customer_window, values=["kfc", "bovichic",  "broadway"],font="verdana 15",width=15)
                    dropdown.place(x=35, y=37)
                    dropdown.set("Select a restaurant")
                    customer_login_window.destroy()
                    

                    def kfc():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        Label(order_window, text="Items in cart :", font=("A", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)
                        kfc_window = Toplevel(customer_window,bg="white")
                        kfc_window.minsize(width=500, height=300)
                        kfc_window.maxsize(width=500, height=300)
                        
                        Label(kfc_window, text="Welcome to KFC", font=("FrizQuadrataBold", 40, "normal", "italic"),fg="red",bg="White").place(x=20, y=1)
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()

                            
                            cursor.execute('SELECT Name FROM kfc')
                            data = cursor.fetchall()

                            
                            conn.close()

                           
                            dropdown['values'] = ()

                            
                            dropdown['values'] = [row[0] for row in data]

                        
                        label = Label(kfc_window, text="Select an option:",font="Verdana 15")
                        label.place(x=157,y=75)

                        
                        dropdown = Combobox(kfc_window)
                        populate_dropdown()  
                        dropdown.place(x=130,y=100)

                       
                        def Add():
                            global Total
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from kfc where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0])+" : "+str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total
                        def Checkout():
                            global Total
                            Total = str(Total)
                            Restaurant = "Kfc"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            Messagebox.showinfo("Status","Your order has been placed")
                            order_window.withdraw()
                            con.close()
                            kfc_window.withdraw()
                        add_button = Button(kfc_window, text="Add", command=Add).place(x=90, y=130)
                        checkout_window = Button(order_window, bg="white", font=("CeraCondensedPro-Bold", 15), text="Checkout", command=Checkout).pack()
                        con.close()

                    def bovichic():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        Label(order_window, text="Items in cart :", font=("A", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)
                        bovichic_window = Toplevel(customer_window,bg="darkgoldenrod1")
                        bovichic_window.minsize(width=500, height=300)
                        bovichic_window.maxsize(width=500, height=300)
                        Label(bovichic_window, text="Welcome to Bovichic",font=("Verdana 15", 30),fg="Red",bg="darkgoldenrod1").place(x=65, y=1)
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()
                            cursor.execute('SELECT Name FROM bovichic')
                            data = cursor.fetchall()
                            conn.close()
                            dropdown['values'] = ()
                            dropdown['values'] = [row[0] for row in data]
                        label = Label(bovichic_window, text="Select an option:")
                        label.place(x=180,y=58)
                        dropdown = Combobox(bovichic_window)
                        populate_dropdown()
                        dropdown.place(x=157,y=75)

                        def Add():
                            global Total
                            
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from bovichic where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0])+" : "+str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total
                        def Checkout():
                            global Total
                            Total = str(Total)
                            Restaurant = "bovichic"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            Messagebox.showinfo("Status","Your order has been placed")
                            order_window.withdraw()
                            con.close()
                            bovichic_window.withdraw()
                        add_button = Button(bovichic_window, text="Add", command=Add).place(x=90, y=130)
                        checkout_window = Button(order_window, bg="white", font=("CeraCondensedPro-Bold", 15), text="Checkout", command=Checkout).pack()
                        con.close()

                    def broadway():
                        order_window = Toplevel(customer_window)
                        order_window.title("Cart")
                        order_window.minsize(width=500, height=300)
                        order_window.maxsize(width=500, height=300)
                        Label(order_window, text="Items in cart :", font=("A", 15)).pack()
                        Label(order_window, text="Your Total is: ", font=("Product Sans Bold", 15)).place(x=10, y=5)
                        broadway_window = Toplevel(customer_window)
                        broadway_window.minsize(width=500, height=300)
                        broadway_window.maxsize(width=500, height=300)
                        Label(broadway_window, text="Welcome to Broadway", font=("Verdana 15", 30)).place(x=1, y=1)
                        con = mysql.connect(host="localhost", user="root", database="online_order")
                        cursor = con.cursor()

                        def populate_dropdown():
                            conn = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = conn.cursor()
                            cursor.execute('SELECT Name FROM broadway')
                            data = cursor.fetchall()
                            conn.close()
                            dropdown['values'] = ()
                            dropdown['values'] = [row[0] for row in data]

                        label = Label(broadway_window, text="Select an option:")
                        label.place(x=157,y=75)
                        dropdown = Combobox(broadway_window)
                        populate_dropdown()
                        dropdown.place(x=130,y=100)

                        def Add():
                            global Total
                            
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("select * from broadway where Name='" + dropdown.get() + "'")
                            price = cursor.fetchall()
                            for i in price:
                                abc = str(i[0])+" : "+str(i[1])
                                Label(order_window, text=abc, font=("Product Sans Bold", 15)).pack()
                                Total += int(i[1])
                            Label(order_window, text=Total, width=5, font=("Neutral Face", 30, "bold")).place(x=1, y=30)
                            return Total
                        def Checkout():
                            global Total
                            Total = str(Total)
                            Restaurant = "broadway"
                            con = mysql.connect(host="localhost", user="root", database="online_order")
                            cursor = con.cursor()
                            cursor.execute("insert into orders values('" + username + "','" + Restaurant + "', '" + Total + "')")
                            cursor.execute("commit")
                            Messagebox.showinfo("Status","Your order has been placed")
                            order_window.withdraw()
                            con.close()
                            broadway_window.withdraw()

                        add_button = Button(broadway_window, text="Add", command=Add).place(x=50, y=50)
                        checkout_window = Button(order_window, bg="white", font=("CeraCondensedPro-Bold", 15), text="Checkout", command=Checkout).pack()
                        con.close()


                    def select():
                        if dropdown.get() == "kfc":
                            kfc()
                        elif dropdown.get() == "bovichic":
                            bovichic()
                        elif dropdown.get() == "broadway":
                            broadway()




                    Button(customer_window, text="Select", command=select,font="verdana 15",bd=3).place(x=100, y=100)

    def Register():

        register_window = Toplevel(root)
        register_window.title("Registration")
        register_window.geometry("400x300")
        lbl12 = Label(register_window, text="Username:")
        lbl12.grid(row=0, column=0)
        username_entry2 = Entry(register_window, width=50)
        username_entry2.grid(row=0, column=1)
        lbl22 = Label(register_window, text="Password:")
        lbl22.grid(row=1, column=0)
        password_entry2 = Entry(register_window, width=50)
        password_entry2.grid(row=1, column=1)

        def Click():
            username2 = username_entry2.get()
            password2 = password_entry2.get()
            if username_entry2 == "" or password_entry2 == "":
                Messagebox.showinfo(".", "Please Fill all fields")
            else:
                con = mysql.connect(host="localhost", user="root", database="online_order")
                cursor = con.cursor()

                cursor.execute("insert into customer_login values('" + username2 + "', '" + password2 + "')")
                cursor.execute("commit")
                Messagebox.showinfo(".", "User registered")
                con.close()
                register_window.destroy()

        Button(register_window, text="submit", command=Click).grid(row=2, column=1)

    lbl1 = Label(customer_login_window, text="Username:",font="verdana 15")
    lbl1.grid(row=0, column=0)
    username_entry = Entry(customer_login_window, width=50,bd=4)
    username_entry.grid(row=0, column=1)
    lbl2 = Label(customer_login_window, text="Password:",font="verdana 15")
    lbl2.grid(row=1, column=0)
    password_entry = Entry(customer_login_window, width=50,bd=4)
    password_entry.grid(row=1, column=1)
    Button(customer_login_window, text="Login", command=login,font="verdana 15",bd=4).place(x=80, y=70)
    Label(customer_login_window, text="Don't have an account?",font="verdana 15").place(x=165, y=73)
    Button(customer_login_window, text="Register", command=Register,font="verdana 15",bd=4).place(x=280, y=117)

def admin():
    admin_login_window = Toplevel(root)
    admin_login_window.title("Admin Login")
    admin_login_window.minsize(width=500, height=300)
    admin_login_window.maxsize(width=500, height=300)
    lbl3 = Label(admin_login_window, text="Username:")
    lbl3.grid(row=0, column=0)
    username3_entry = Entry(admin_login_window, width=50)
    username3_entry.grid(row=0, column=1)
    lbl3 = Label(admin_login_window, text="Password:")
    lbl3.grid(row=1, column=0)
    password_entry3 = Entry(admin_login_window, width=50)
    password_entry3.grid(row=1, column=1)
    def admin_login():
        username3 = username3_entry.get()
        password3 = password_entry3.get()

        if username3 == "admin" and password3 == "admin":
            admin_window = Toplevel(admin_login_window)
            admin_window.title("Admin Dashboard")
            admin_window.minsize(width=500, height=300)
            admin_window.maxsize(width=500, height=300)

    Button(admin_login_window, text="Login", command=admin_login).place(x=100, y=50)






Start = Label(root, text="Who are you?", font=("Neutral Face", 30, "bold"),bg="Black",fg="gold1")
Start.place(x=180, y=15)

Customer = Button(root, text="Customer", height=2,width=12,font=("Product Sans Bold",15),bd=4, command=Customer,bg="cornsilk")
Customer.place(x=10, y=80)

Owner = Button(root, text="Restaurant Owner",height=2,width=21,font=("Product Sans Bold",15),bd=4,bg="cornsilk")
Owner.place(x=190, y=80)

Admin = Button(root, text="Admin", height=2,width=13,font=("Product Sans Bold",15),bd=4, command=admin,bg="cornsilk")
Admin.place(x=480, y=80)

root.mainloop()