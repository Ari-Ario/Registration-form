"""A Simple form to save data by entering new registrations; functional programming"""

from tkinter import *
import sqlite3 #is not used, just in case an sql file will be added
from tkinter import messagebox, ttk
import os
import openpyxl
from datetime import date

win= Tk()
win.title("FORM")
win.geometry("350x300")

#database function
def database():
    global first, second, dob, var_con, language_vars, var4
    first = entry_firstname.get()
    second= entry_lastname.get()
    if first and second:
        dob = entry_birthday.get()
        var_con = var_coun.get()
        #these variables need verification as clicked
        var1= var_c1 if "selected" in c1.state() else ""
        var2= var_c2 if "selected" in c2.state() else ""
        var3= var_c3 if "selected" in c3.state() else ""
        var4 = radio_var_gender.get()

        #this line is a string for text data as backup
        heading = ["First Name", "Last Name", "Birthday", "country", "languages", "Gender"]
        line =f"[{first},{second},{dob},{var_con},{var1},{var2},{var3},{var4}]\n"
        #opening the backup data, or creating it, in case it does not exist
        form_text= "form.txt"
        if not os.path.exists(form_text):
            file= open(form_text, mode="w", encoding="utf-8")
            file.write(str(heading)+"\n")
        file = open(form_text, mode="a", encoding="utf-8")
        file.write(line)
        file.close()

        #opening/creating an exel file in the same directory
        form_exel = "form.xlsx"

        if not os.path.exists(form_exel):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            sheet.append(heading)
            workbook.save(form_exel)

        language_vars= f"{var1}, {var2}, {var3}"
        workbook = openpyxl.load_workbook(form_exel)
        sheet = workbook.active
        sheet.append([first, second, dob, var_con, language_vars, var4])
        workbook.save(form_exel)
        #give to the function success_entry as a new window
        success_entry_win()

    else:
        messagebox.showerror("Name Error", "First- and Second-name are required")

#popup window, if data has been added in .txt and exel. It asks for SQL-archive in case some important data.
def success_entry_win():
    success_win= Tk()
    success_win.title("Congratulation")
    success_frame= LabelFrame(success_win, text="You have registered successfully")
    success_frame.pack()
    label_success= Label(success_frame, text="Do you want data to SQL-query as second backup?", font="bold")
    label_success.pack()
    butt_success= Button(success_frame, text="Yes, sure!", command=sql_data_insertion, bg="green")
    butt_success.pack(side=LEFT)
    butt_no_quit= Button(success_frame, text="No, Quit", command=success_win.destroy , bg="red")
    butt_no_quit.pack(side=RIGHT)

#extra method to collect the date in, install sqlitebrowser from: https://sqlitebrowser.org/dl/
def sql_data_insertion():
    global first, second, dob, var_con, language_vars, var4
    today = date.today()
    day, month, year= dob.split(".")
    age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
    #it can be activatad in case the button Yes, sure is clicked
    conn_sql = sqlite3.connect('data.db')
    tabel_create_query= '''CREATE TABLE IF NOT EXISTS Form_data(firstname TEXT, lastname TEXT, 
    age INT, country TEXT, language TEXT, gender TEXT)'''
    conn_sql.execute(tabel_create_query)
    #insert data into the query
    data_insert_into_query= '''INSERT INTO Form_data(firstname, lastname, age, country, 
    language, gender) VALUES(?, ?, ? ,? ,?, ?)'''
    data_insertion_tuple= (firstname, lastname, age, var_con, language_vars, gender)
    cursor= conn_sql.cursor()
    cursor.execute(data_insert_into_query, data_insertion_tuple)
    conn_sql.commit()
    conn_sql.close()

#variables
firstname= StringVar()
lastname= StringVar()
birthday= StringVar()
var_coun= StringVar(win)
var_c1 = "C"
var_c2= "SQL"
var_c3= "Other"
radio_var_gender= StringVar()

label_heading = Label(win, text="REGISTRATION FORM", font="Currier", relief=SOLID).place(x=75, y=15)

#all labels, entries and etc.
label_firstname = Label(win, text="First Name:").place(x=50, y =50)
entry_firstname = Entry(win, width=16, textvariable=firstname)
entry_firstname.place(x=150, y=50)

label_lastname = Label(win, text="Last Name:").place(x=50, y =80)
entry_lastname = Entry(win, width=16, textvariable=lastname)
entry_lastname.place(x=150, y=80)

label_birthday = Label(win, text="Birthday:").place(x=50, y =110)
entry_birthday = Entry(win, width=16, textvariable=birthday)
entry_birthday.place(x=150, y=110)
entry_birthday.focus()
entry_birthday.insert(0, "dd.mm.yy")

#list of countries
countries = ('Abkhazia', 'Afghanistan', 'Akrotiri and Dhekelia', 'Albania', 'Algeria', 
             'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua and Barbuda', 'Argentina', 
             'Armenia', 'Aruba', 'Ascension Island', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 
             'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 
             'Bhutan', 'Bolivia', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 
             'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 
             'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 
             'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Cook Islands', 'Costa Rica', 'Croatia', 
             'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', "Côte d'Ivoire", 'Democratic Republic of the Congo', 
             'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor-Leste)', 'Easter Island', 
             'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 
             'Falkland Islands', 'Faroe Islands', 'Federated States of Micronesia', 'Fiji', 'Finland', 
             'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia', 'Georgia', 'Germany', 
             'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 
             'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 
             'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 
             'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 
             'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 
             'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
             'Mauritania', 'Mauritius', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 
             'Morocco', 'Mozambique', 'Myanmar', 'Nagorno-Karabakh Republic', 'Namibia', 'Nauru', 'Nepal', 
             'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 
             'Norfolk Island', 'North Korea', 'Northern Cyprus', 'United Kingdom Northern Ireland', 
             'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestine', 'Panama', 
             'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 
             'Puerto Rico', 'Qatar', 'Republic of China (Taiwan)', 'Republic of the Congo', 'Romania', 'Russia', 
             'Rwanda', 'Saint Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 
             'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Saudi Arabia', 
             'Scotland', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 
             'Slovenia', 'Solomon Islands', 'Somalia', 'Somaliland', 'South Africa', 'South Korea', 'South Ossetia', 
             'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 
             'São Tomé and Príncipe', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Transnistria', 
             'Trinidad and Tobago', 'Tristan da Cunha', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 
             'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom; England', 'United States', 
             'United States Virgin Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 
             'Vietnam', 'Wales', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe')

label_country = Label(win, text="country:").place(x=50, y =140)
var_coun.set("Select Country")
option_country = ttk.Combobox(win, value=countries, textvariable=var_coun)
option_country.current(0)
option_country.place(x=150, y=140, width=135)


label_language = Label(win, text="Language:").place(x=50, y =180)
c1 = ttk.Checkbutton(win, text="C", variable=var_c1)
c1.place(x=140, y=180)
c2=  ttk.Checkbutton(win, text="SQL", variable=var_c2)
c2.place(x=190, y=180)
c3= ttk.Checkbutton(win, text="OTHER", variable=var_c3)
c3.place(x=250, y=180)


gender = Label(win, text="Gender").place(x=50, y=220)
r1 = Radiobutton(win, text="Male", variable=radio_var_gender, value="Male").place(x=150, y=220)
r2= Radiobutton(win, text="Female", variable=radio_var_gender, value="Female").place(x=210, y=220)

button_submit=Button(win, text="Submit", background="green", command=database).place(x=80, y=260)
button_quit= Button(win, text="Quit", background="red", command=win.destroy).place(x=200, y=260)

win.mainloop()