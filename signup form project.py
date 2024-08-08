# Creating a simple GUI registration form using Tkinter in Python
# import the tkinter module into our code
from tkinter import *

import tkinter.messagebox as msg

# Creating the object 'base' of the Tk()
base = Tk()

# Using the Geometry method to the form certain dimensions
base.geometry("800x800")

#using the config method to assign style to the window
base.config(bg='lightblue')

#database section

def register_data():
    if enter_1.get() == '':
        msg.showerror('Alert', "Please enter your first name")
    elif enter_2.get() == '':
        msg.showerror('Alert', "Please enter your last name")
    elif vars.get() == '':
        msg.showerror('Alert', "Please select your gender")
    elif enter_4.get() =='':
        msg.showerror('Alert', "Please enter your age")
    elif enter_5.get() =='':
        msg.showerror('Alert', "Please enter your email")
    elif cv.get() =='':
        msg.showerror('Alert', "Please select your country")
    elif enter_7.get() == '':
        msg.showerror('Alert', "Please enter your phone number")
    else:

        import mysql.connector

        mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="register_db")

        mycursor = mydb.cursor()

        First_Name = enter_1.get()
        Last_Name = enter_2.get()
        Gender = vars.get()
        Age = enter_4.get()
        Email = enter_5.get()
        Country = cv.get()
        Phone_no = enter_7.get()



        mycursor.execute("insert into formdata values(%s,%s,%s,%s,%s,%s,%s)",( First_Name,Last_Name,Gender,Age,Email,Country,Phone_no))

        mydb.commit()
        msg.showinfo("Registration", "Resigtered successfully")
           
#using base.destroy() to close the window after submission
        base.destroy()






# Using title method to give the title to the window
base.title('Registration form')

# Now, we will use 'Label' method to add widget in the Registration Form and also use place() method to set their positions.
lbl_0 = Label(base, text="Registration form", width=20, font=("bold", 20))

# the place method in tkinter module helps user to set the geometry, that is, the dimensions of a certain widget by placing them at a certain position
lbl_0.place(x=200, y=60)

# Using 'Label' widget to create Full name label and using place() method to set its position.
lbl_1 = Label(base, text="First Name", width=20, font=("bold", 10))
lbl_1.place(x=80, y=160)

lbl_2 = Label(base, text="Last Name", width=20, font=("bold", 10))
lbl_2.place(x=420, y=160)

# Using Enrty widget to make a text entry box for accepting the input string in text from user.
enter_1 = Entry(base)
enter_1.place(x=270, y=160)

enter_2 = Entry(base)
enter_2.place(x=600, y=160)




# Using 'Label' widget to create Gender label and using place() method to set its position.
lbl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
lbl_3.place(x=80, y=200)

# Using variable 'vars' to store the string value, which by deault is selected by user
vars=StringVar(value=NONE)

# Using Radio button widget to create an option choosing button and using place() method to set its position.

Radiobutton(base, text="Male", padx=20, variable=vars,value='Male').place(x=270, y=200)
Radiobutton(base, text="Female", padx=5, variable=vars,value='Female').place(x=380, y=200)


lbl_4 = Label(base, text="Age", width=20, font=("bold", 10))
lbl_4.place(x=80, y=240)

def validate_int(age):
    if age.isdigit() and len(age) < 4:
        return True
    elif age == "":
        return True
    else:
        return False

validat_cmd = base.register(validate_int)

enter_4 = Entry(base,validate="key", validatecommand=(validat_cmd, '%P'))
enter_4.place(x=270, y=240, width=40)



lbl_5 = Label(base, text="Email", width=20, font=("bold", 10))
lbl_5.place(x=80, y=290)
# Using Enrty widget to make a text entry box for accepting the input string in text from user.
enter_5 = Entry(base)
enter_5.place(x=275, y=290, width=180)



# Using 'Label' widget to create Countries label and using place() method, set its position.
lbl_6 = Label(base, text="Country", width=18, font=("bold", 11))
lbl_6.place(x=80, y=340)

# this creates list of countries available in the dropdown list.
list_of_cntry = ["Afghanistan", "Albania", "Algeria","America", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi",
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the", "Costa Rica", "Cote d'Ivoire", "Croatia",
    "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
    "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo", "Kuwait", "Kyrgyzstan",
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", "Mexico",
    "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru",
    "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
    "Portugal", "Qatar", "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia"]


# the variable 'cv' is introduced to store the String Value, which by default is (empty) ""
cv = StringVar()
drplist = OptionMenu(base, cv, *list_of_cntry)
drplist.config(width=15)
cv.set('Select your Country')
drplist.place(x=275, y=336)

# Using 'Label' widget to create phone-no. label and using place() method, set its position.
lbl_7 = Label(base, text="Phone-no.", width=20, font=('bold', 10))
lbl_7.place(x=80, y=400)

def validate_integer(text):
    if text.isdigit():
        return True
    elif text == "":
        return True
    else:
        return False

validate_cmd = base.register(validate_integer)

enter_7 = Entry(base,validate="key", validatecommand=(validate_cmd, '%P'))
enter_7.place(x=275, y=400)



# Using the Button widget, we get to create a button for submitting all the data that has been entered in the entry boxes of the form by the user.
Button(base, text='Submit', width=20, bg="green", font=('bold', 12), fg='white',command=register_data).place(x=290, y=480)


# Calling the mainloop method to execute the entire program.
base.mainloop()





















