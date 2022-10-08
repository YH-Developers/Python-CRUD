from tkinter import messagebox
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap

my_app=QtWidgets.QApplication([])
my_ui=uic.loadUi("Main.ui")


def convert():
    messagebox.showinfo("Information","Welcome User")
    
# main code here

# mainpage Submit button clicked
#my_ui.save_info.clicked.connect(convert)



# code for add district

my_ui.District.setPlaceholderText("Select District")
my_ui.District.addItem('Lahore')
my_ui.District.addItem('Attock')
my_ui.District.addItem('Mianwali')
my_ui.District.addItem('Bhawalpur')
my_ui.District.addItem('Chakwal')
my_ui.District.addItem('chiniot')
my_ui.District.addItem('Dera Ghazi khan')
my_ui.District.addItem('Fasilabad')
my_ui.District.addItem('Gujrat')
my_ui.District.addItem('Gujranwala')
my_ui.District.addItem('Hafizabad')
my_ui.District.addItem('Jehlam')
my_ui.District.addItem('Jhang')
my_ui.District.addItem('Kasur')
my_ui.District.addItem('Khanewal')
my_ui.District.addItem('Khushab')
my_ui.District.addItem('Layyah')
my_ui.District.addItem('Lodhran')
my_ui.District.addItem('Muzafarabad')
my_ui.District.addItem('Multan')
my_ui.District.addItem('Narowal')
my_ui.District.addItem('Ookara')
my_ui.District.addItem('Pakpatan')
my_ui.District.addItem('Raheem yar khan')
my_ui.District.addItem('Sahiwal')
my_ui.District.addItem('Sarghodha')
my_ui.District.addItem('Shiekupura')
my_ui.District.addItem('Sialkot')
my_ui.District.addItem('Toba Tekh singh')
my_ui.District.addItem('Vehari')

# code to add Tehsil
my_ui.comboBox.addItem('Lahore')
#code to add stamp type
my_ui.comboBox_2.setPlaceholderText("Select Stamp paper type")
my_ui.comboBox_2.addItem("Judicial") 
my_ui.comboBox_2.addItem("Non Judicial") 

# code for add Deed
my_ui.comboBox_3.setPlaceholderText("Select Deed")
my_ui.comboBox_3.addItem("Court Fee") 


# NAme
my_ui.AgentName.setPlaceholderText("Enter Your name")

my_ui.AgentCNIC.setPlaceholderText("Enter Your CNIC")


my_ui.AgentContact.setPlaceholderText("+923XXXXXXXXX")


my_ui.AgentEmail.setPlaceholderText("XXXXXXX@gmail.com")







# app show
my_ui.show()
my_app.exec()

