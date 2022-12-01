import time
import datetime
from tkinter import *
import tkinter.messagebox 

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://employee-payroll-system-e0489-default-rtdb.firebaseio.com'
})

root=Tk()
root.title("Employee Payroll System")
root.geometry('1600x8000')
root.configure(background="light blue")

Tops=Frame(root,width=1350,height=50,bd=8,bg="light blue")
Tops.pack(side=TOP)

f1=Frame(root,width=600,height=600,bd=8,bg="light blue")
f1.pack(side=LEFT)
f2=Frame(root,width=300,height=700,bd=8,bg="light blue")
f2.pack(side=RIGHT)

fla=Frame(f1,width=600,height=180,bd=8,bg="light blue")
fla.pack(side=TOP)
flb=Frame(f1,width=300,height=600,bd=8,bg="light blue")
flb.pack(side=TOP)

lblinfo=Label(Tops,font=('CENTURY GOTHIC',45,'bold'),text="Employee Payment Management System",bd=10,fg="purple")
lblinfo.grid(row=0,column=0)

def exit():
  exit=tkinter.messagebox.askyesno("Employee Management System","Do you want to exit the system?")
  if exit>0:
    root.destroy()
    return

def reset():
  Name.set("")
  Address.set("")
  HoursWorked.set("")
  wageshour.set("")
  Payable.set("")
  Taxable.set("")
  NetPayable.set("")
  GrossPayable.set("")
  OverTimeBonus.set("")
  Employer.set("")
  EmployeeID.set("")
  txtpayslip.delete("1.0",END)
def enterinfo():
  txtpayslip.delete("1.0",END)
  txtpayslip.insert(END,"\t\tPay Slip\n\n")
  txtpayslip.insert(END,"Name :\t\t"+Name.get()+"\n\n")
  txtpayslip.insert(END,"Address :\t\t"+Address.get()+"\n\n")
  txtpayslip.insert(END,"Employer :\t\t"+Employer.get()+"\n\n")
  txtpayslip.insert(END,"Employee ID:\t\t"+EmployeeID.get()+"\n\n")
  txtpayslip.insert(END,"Hours Worked :\t\t"+HoursWorked.get()+"\n\n")
  txtpayslip.insert(END,"Net Payable :\t\t"+NetPayable.get()+"\n\n")
  txtpayslip.insert(END,"Wages per hour :\t\t"+wageshour.get()+"\n\n")
  txtpayslip.insert(END,"Tax Paid :\t\t"+Taxable.get()+"\n\n")
  txtpayslip.insert(END,"Payable :\t\t"+Payable.get()+"\n\n") 
def weeklywages():
  txtpayslip.delete("1.0",END)
  hoursworkedperweek=float(HoursWorked.get())
  wagesperhours=float(wageshour.get())
  
  paydue=wagesperhours*hoursworkedperweek
  paymentdue="INR",str('%.2f'%(paydue))
  Payable.set(paymentdue)
  
  tax=paydue*0.2
  taxable="INR",str('%.2f'%(tax))
  Taxable.set(taxable)
  
  netpay=paydue-tax
  netpays="INR",str('%.2f'%(netpay))
  NetPayable.set(netpays)
  
  if hoursworkedperweek > 40:
    overtimehours=(hoursworkedperweek-40)+wagesperhours*1.5
    overtime="INR",str('%.2f'%(overtimehours))
    OverTimeBonus.set(overtime)
  elif hoursworkedperweek<=40:
    overtimepay=(hoursworkedperweek-40)+wagesperhours*1.5
    overtimehrs="INR",str('%.2f'%(overtimepay))
    OverTimeBonus.set(overtimehrs)  
  return  

def savedata():
   ref = db.reference('info/')
   users_ref = ref.child('payslip')
   users_ref.push({'inside' : {
        'Name' : Name.get(),
        'Address' : Address.get(),
        'Employer' : Employer.get(),
        'Employee ID' : EmployeeID.get(),
        'Hours Worked' : HoursWorked.get(),
        'Net Payable' : NetPayable.get(),
        'Wages per hour' : wageshour.get(),
        'Tax Paid' : Taxable.get(),
        'Payable' : Payable.get()



    }
   }) 
    
#Declaring Variables
Name=StringVar()
Address=StringVar()
HoursWorked=StringVar()
wageshour=StringVar()
Payable=StringVar()
Taxable=StringVar()
NetPayable=StringVar()
GrossPayable=StringVar()
OverTimeBonus=StringVar()
Employer=StringVar()
EmployeeID=StringVar()
TimeOfOrder=StringVar()
DateOfOrder=StringVar()

DateOfOrder.set(time.strftime("%d/%m/%Y"))

#Label Widget 
lblName=Label(fla,text="Name",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=0,column=0)
lblAddress=Label(fla,text="Address",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=0,column=2)
lblEmployer=Label(fla,text="Employer",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=1,column=0)
lblEmployeeID=Label(fla,text="Employee ID",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=1,column=2)
lblHoursWorked=Label(fla,text="Hours Worked",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=2,column=0)
lblHourlyRate=Label(fla,text="Hourly Rate",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=2,column=2)
lblTax=Label(fla,text="Tax",font=('CASLON',16,'bold'),bd=18,anchor='w',fg="teal",bg="light blue").grid(row=3,column=0)
lblOverTime=Label(fla,text="OverTime",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=3,column=2)
lblGrossPay=Label(fla,text="GrossPay",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=4,column=0)
lblNetPay=Label(fla,text="Net Pay",font=('CASLON',16,'bold'),bd=18,fg="teal",bg="light blue").grid(row=4,column=2)

#Entry Widget
etxname=Entry(fla,textvariable=Name,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxname.grid(row=0,column=1)

etxaddress=Entry(fla,textvariable=Address,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxaddress.grid(row=0,column=3)

etxemployer=Entry(fla,textvariable=Employer,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxemployer.grid(row=1,column=1)

etxhoursworked=Entry(fla,textvariable=HoursWorked,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxhoursworked.grid(row=2,column=1)

etxwagesperhours=Entry(fla,textvariable=wageshour,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxwagesperhours.grid(row=2,column=3)

etxnin=Entry(fla,textvariable=EmployeeID,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxnin.grid(row=1,column=3)

etxgrosspay=Entry(fla,textvariable=Payable,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxgrosspay.grid(row=4,column=1)

etxnetpay=Entry(fla,textvariable=NetPayable,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxnetpay.grid(row=4,column=3)

etxtax=Entry(fla,textvariable=Taxable,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxtax.grid(row=3,column=1)

etxovertime=Entry(fla,textvariable=OverTimeBonus,font=('CASLON',16,'bold'),bd=16,width=18,justify='left')
etxovertime.grid(row=3,column=3)

#Text Widget 
payslip=Label(f2,textvariable=DateOfOrder,font=('CASLON',21,'bold'),fg="teal",bg="light blue").grid(row=0,column=0)
txtpayslip=Text(f2,height=18,width=30,bd=14,font=('CASLON',13,'bold'),fg="teal",bg="light blue")
txtpayslip.grid(row=1,column=0)

#Buttons 
btnsalary=Button(flb,text='Weekly Salary',padx=16,pady=16,bd=8,font=('CASLON',16,'bold'),width=12,fg="teal",bg="light blue",command=weeklywages).grid(row=0,column=0)

btnreset=Button(flb,text='Reset',padx=16,pady=16,bd=8,font=('CASLON',16,'bold'),width=12,command=reset,fg="teal",bg="light blue").grid(row=0,column=1)

btnpayslip=Button(flb,text='View Payslip',padx=16,pady=16,bd=8,font=('CASLON',16,'bold'),width=12,command=enterinfo,fg="teal",bg="light blue").grid(row=0,column=2)

btnexit=Button(flb,text='Exit System',padx=16,pady=16,bd=8,font=('CASLON',16,'bold'),width=12,command=exit,fg="teal",bg="light blue").grid(row=0,column=3)

btnexit=Button(flb,text='Save Data',padx=16,pady=16,bd=8,font=('CASLON',16,'bold'),width=12,command=savedata,fg="teal",bg="light blue").grid(row=1,column=3)

root.mainloop()


