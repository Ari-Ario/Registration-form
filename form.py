from tkinter import *
import sqlite3
from tkinter import messagebox

win= Tk()
win.title("FORM")
win.geometry("350x300")

def database():
    first = entry_firstname.get()
    second= entry_lastname.get()
    dob = entry_birthday.get()
    var_con = var.get()
    var1= var_c1 if c1==True else ""
    var2= var_c2 if c2==True else ""
    var3= var_c3 if c3==True else ""
    var4 = radio_var.get()
    #conn= sqlite3.connect("Form.db")
    line =f"{first},{second},{dob},{var_con},{var1},{var2},{var3},{var4}\n"
    with open("sth.txt", mode="a", encoding="utf-8") as file:
        file.write(line)

    messagebox.showinfo("Congratulation", "You have registered successfully")


firstname= StringVar()
lastname= StringVar()
birthday= StringVar()
var= StringVar()
var_c1 = "English"
var_c2= "Kurdish"
var_c3= "Other"
radio_var= StringVar()

label_heading = Label(win, text="REGISTRATION FORM", font="Currier", relief=SOLID).place(x=75, y=15)

label_firstname = Label(win, text="First Name:").place(x=50, y =50)
entry_firstname = Entry(win, width=16, textvariable=firstname)
entry_firstname.place(x=150, y=50)

label_lastname = Label(win, text="Last Name:").place(x=50, y =80)
entry_lastname = Entry(win, width=16, textvariable=lastname)
entry_lastname.place(x=150, y=80)

label_birthday = Label(win, text="Birthday:").place(x=50, y =110)
entry_birthday = Entry(win, width=16, textvariable=birthday)
entry_birthday.place(x=150, y=110)

countries = ['Abkhazia', 'Afghanistan', 'Akrotiri and Dhekelia', 'Albania', 'Algeria', 
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
             'Vietnam', 'Wales', 'Wallis and Futuna', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

label_country = Label(win, text="country:").place(x=50, y =140)
option_country = OptionMenu(win , var, *countries)
option_country.place(x=150, y=140, width=135)
var.set("Select Country")

label_language = Label(win, text="Language:").place(x=50, y =180)
c1 = Checkbutton(win, text="C", variable=var_c1).place(x=140, y=180)
c2=  Checkbutton(win, text="SQL", variable=var_c2).place(x=190, y=180)
c3= Checkbutton(win, text="OTHER", variable=var_c3).place(x=250, y=180)


gender = Label(win, text="Gender").place(x=50, y=220)
r1 = Radiobutton(win, text="Male", variable=radio_var, value="Male").place(x=150, y=220)
r2= Radiobutton(win, text="Female", variable=radio_var, value="Female").place(x=210, y=220)

button_submit=Button(win, text="Submit", background="green", command=database).place(x=80, y=260)
button_quit= Button(win, text="Quit", background="red", command=win.destroy).place(x=200, y=260)

win.mainloop()