#importing everything from tkinter module
import tkinter as tk
from tkinter import *
from tkinter import ttk

#creating a GUI main page
main_page = tk.Tk()
main_page.title('BOOK MY TRIP')
main_page.geometry('700x700')
main_page.configure(background="orange")

#creating a button and placing it inside the GUI main page
book_now=Button(main_page,text="BOOK NOW",command=main_page.destroy).pack(side='top')
#starting the GUI main page
main_page.mainloop()

#creating a GUI details page
details_page = tk.Tk()
details_page.title('BOOK MY TRIP')
details_page.geometry('700x700')
details_page.configure(background="orange")

#using the label widget to display text
ttk.Label(details_page, text = "Train Reservation system",  font=("Helvetica", 20, "bold")).grid(row = 0, column = 1)

#using the label widget to display text
ttk.Label(details_page, text = "Enter boarding city").grid(row = 5, column = 0, padx=9, pady=24)

#using the concept of combobox for selecting boarding city
boardingcity = ttk.Combobox(details_page, width = 27, values = ["Ahmedabad","Surat","Indore","Mumbai","Pune","Jaipur","Udaipur","Rajkot"])
boardingcity.grid(column = 1, row = 5)
#adding the combobox list by using current()
boardingcity.current()

#using the label widget and combobox list for selecting destination city
ttk.Label(details_page, text = "Enter destination city").grid(row = 6, column = 0, padx=9, pady=24)
destinationcity = ttk.Combobox(details_page, width = 26, values = ["Ahmedabad","Surat","Indore","Mumbai","Pune","Jaipur","Jodhpur","Vadodra"])
destinationcity.grid(column = 1, row = 6)
destinationcity.current()

#using the label widget for entering the Date
ttk.Label(details_page, text = "Date (DD/MM/YYYY)").grid(row = 7, column = 0, padx=9, pady=24)
date = tk.Entry(details_page,width=26)
date.grid(column = 1, row = 7)

#using the label widget for entering the name
ttk.Label(details_page, text = "Enter your Name").grid(row = 8, column = 0, padx=9, pady=24)
name = tk.Entry(details_page,width=26)
name.grid(column = 1, row = 8)

#using the label widget for entering the age
ttk.Label(details_page, text = "Enter your Age").grid(row = 9, column = 0, padx=9, pady=24)
age = tk.Entry(details_page,width=26)
age.grid(row=9,column=1)

#using the label widget and combobox list for selecting the birth preference
ttk.Label(details_page, text = "Enter birth preference").grid(row = 10, column = 0, padx=9, pady=24)
birth_pref = ttk.Combobox(details_page, width = 26, values = ["Lower","Middle","Upper","Side Lower","Side Upper"])
birth_pref.grid(column = 1, row = 10)
birth_pref.current()

#using the label widget and combobox list for selecting the class preference
ttk.Label(details_page, text = "Enter class").grid(row = 11, column = 0, padx=9, pady=24)
class_pref = ttk.Combobox(details_page, width = 26, values = ["Non AC (SL)","1st AC","2nd AC","3rd AC"])
class_pref.grid(column = 1, row = 11)
class_pref.current()

#using the label widget and combobox list for entering gender
ttk.Label(details_page, text = "Gender").grid(row = 12, column = 0, padx=9, pady=24)
gender = ttk.Combobox(details_page, width = 26, values = ["Male","Female","Other"])
gender.grid(column = 1, row = 12)
gender.current()

#using the label widget for entering the mobile number
tk.Label(details_page, text = "Enter your 10 digit Mobile Number").grid(row = 13, column = 0, padx=9, pady=24)
mobile_no = tk.Entry(details_page,width=26)
mobile_no.grid(row=13,column=1)

#creating a button for payment and placing it inside the GUI details page
enter_to_pay = Button(details_page,text="Click here to pay",command=details_page.destroy).grid(row = 14,column=0)
#starting the GUI details page
details_page.mainloop()

#defining a function named payment
def payment():

    #defining a function named debit card
    def debit_card():

        #destroying the GUI page: payment options
        payment_options.destroy()

        #creating a GUI payment details page
        payment_details = tk.Tk()
        payment_details.title('BOOK MY TRIP')
        payment_details.geometry('700x700')
        payment_details.configure(background="orange")

        #using the label widget for entering the card number
        tk.Label(payment_details, text = "Enter your 8 digit card number").grid(row = 3, column = 0, padx=9, pady=24)
        card_no = tk.Entry(payment_details,width=26)
        card_no.grid(row=3,column=1)

        #using the label widget for entering the name on card
        tk.Label(payment_details, text = "Name on card").grid(row = 4, column = 0, padx=9, pady=24)
        name_on_card = tk.Entry(payment_details,width=26)
        name_on_card.grid(row=4,column=1)

        #using the label widget for entering the expiry date of card
        tk.Label(payment_details, text = "Enter expiry date in MM/YY format").grid(row = 5, column = 0, padx=9, pady=24)
        exp_date = tk.Entry(payment_details,width=26)
        exp_date.grid(row=5,column=1)

        #using the label widget for entering the CVV code
        tk.Label(payment_details, text = "CVV").grid(row = 6, column = 0, padx=9, pady=24)
        cvv = tk.Entry(payment_details,width=26)
        cvv.grid(row=6,column=1)

        #creating a button for confirmation of payment and placing it inside the GUI payment details page
        conf_pay = Button(payment_details,text="Confirm Payment",command=payment_details.destroy).grid(row = 8,column=0)

    #defining a function named upi
    def upi():

        #destroying the GUI page: payment options
        payment_options.destroy()

        #creating a GUI payment details page
        payment_details = tk.Tk()
        payment_details.title('BOOK MY TRIP')
        payment_details.geometry('700x700')
        payment_details.configure(background="orange")

        #using the label widget for entering the 6 digit UPI ID
        tk.Label(payment_details, text = "Enter your 6 digit UPI Id").grid(row = 3, column = 0, padx=9, pady=24)
        upi_id=tk.Entry(payment_details,width=26)
        upi_id.grid(row=3,column=1)

        #using the label widget and concept of combobox for selecting the payment gateway
        ttk.Label(payment_details, text = "Payment Gateway").grid(row = 4, column = 0, padx=9, pady=24)
        pay_gateway = ttk.Combobox(payment_details, width = 26, values = ["Paytm","Google Pay","Bhim UPI"])
        pay_gateway.grid(column = 1, row = 4)
        pay_gateway.current()

        #using the label widget for entering the 4 digit UPI pin
        tk.Label(payment_details, text = "Enter 4 digit UPI PIN").grid(row = 5, column = 0, padx=9, pady=24)
        upi_pin = tk.Entry(payment_details,width=26)
        upi_pin.grid(row=5,column=1)

        #creating a button for confirmation of payment and placing it inside the GUI payment details page
        conf_pay = Button(payment_details,text="Confirm Payment",command=payment_details.destroy).grid(row = 8,column=0)

    #defining a function named net bank
    def net_bank():

        #destroying the GUI page: payment options
        payment_options.destroy()

        #creating a GUI payment details page
        payment_details = tk.Tk()
        payment_details.title('BOOK MY TRIP')
        payment_details.geometry('700x700')
        payment_details.configure(background="orange")

        #using the label widget for entering the name of bank
        tk.Label(payment_details, text = "Name of Bank").grid(row = 3, column = 0, padx=9, pady=24)
        bank_name = tk.Entry(payment_details,width=26)
        bank_name.grid(row=3,column=1)

        #using the label widget for entering the User ID
        tk.Label(payment_details, text = "Enter your User Id").grid(row = 4, column = 0, padx=9, pady=24)
        user_id = tk.Entry(payment_details,width=26)
        user_id.grid(row=4,column=1)

        #using the label widget for entering the password
        tk.Label(payment_details, text = "Enter your Password").grid(row = 5, column = 0, padx=9, pady=24)
        pswd = tk.Entry(payment_details,width=26)
        pswd.grid(row=5,column=1)

        #creating a button for confirmation of payment and placing it inside the GUI payment details page
        conf_pay = Button(payment_details,text="Confirm Payment",command=payment_details.destroy).grid(row = 8,column=0)

    #creating a GUI payment options page
    payment_options = tk.Tk()
    payment_options.title('BOOK MY TRIP')
    payment_options.geometry('700x700')
    payment_options.configure(background="orange")

    #creating options for mode of payment through Buttons
    option1 = Button(payment_options,text="DEBIT CARD",command=debit_card).grid(row=1,column=0)
    option2 = Button(payment_options,text="UPI",command=upi).grid(row=2,column=0)
    option3 = Button(payment_options,text="NET BANKING",command=net_bank).grid(row=3,column=0)

    #starting the GUI payment options page
    payment_options.mainloop()

#calling the payment function
payment()

#creating a GUI exit page
exit_page = tk.Tk()
exit_page.title('BOOK MY TRIP')
exit_page.geometry('700x700')
exit_page.configure(background="orange")

#using the label widget to display text
ttk.Label(exit_page, text = "Congratulations! Your Booking has been confirmed", font=("Helvetica", 20, "bold")).grid(row = 0, column = 1)
ttk.Label(exit_page, text = "Have a safe and happy journey!!!!",  font=("Helvetica", 14, "bold")).grid(row = 2, column = 1)

#starting the GUI exit page
exit_page.mainloop()
