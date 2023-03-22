import numpy as np
import csv
import matplotlib as plt
import pandas as pd
import os

def Menu():
    Result = input("would you like to add, edit, or delete from your menu: ")
    if Result == "add":
        new = int(input("How many things would you like to add: "))
        for i in range(new):
            file = open("menu.csv", "a")
            food = input("New item: ")
            price = input("Price of new item: ")
            writer = csv.writer(file)
            writer.writerow([food, price])
    if Result == "edit":
       r = csv.reader(open('menu.csv'))
       lines = list(r)
       item_edit = int(input("Which number item would you like to edit: ")) - 1
       new_price = int(input("what is the new price of the  item: "))
       lines[item_edit][1] = new_price
       writer = csv.writer(open('menu.csv', 'w'))
       writer.writerows(lines)
    if Result == "delete":
        file_name = 'menu.csv'
        temp_file = 'temp.csv'
        item = input('Enter item you want to delete: ')
        with open(file_name, 'r') as input_file, open(temp_file, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                if item.lower() not in map(str.lower, row):
                    writer.writerow(row)
        os.remove(file_name)
        os.rename(temp_file, file_name)
def TP():
    Tipout = int(input("Total sales: ")) * .03
   
    BC = int(input("How many bussers were there: "))
    Busser_hours = np.zeros(BC)
    
    Total_Hours = 0
    
    for i in range(BC):
        Busser_hours[i] = int(input(f"how many hours did busser {i + 1} work: "))
        Total_Hours = Total_Hours + Busser_hours[i]

    a = int(input("Which busser would you like to know tipout for: "))

    TPout = ((Busser_hours[a-1] / Total_Hours) * Tipout) 
    return TPout

def Scheldule():
    function = input("would you like to add, delete, or edit shifts on the scheldule: ")
    if function == "add":
        days = int(input("How many days would you like to add "))
        for i in range(days):
            file = open("scheldule.csv", "a")
            date = input("what is the day of the week: ")
            date_c = input("what is the calendar date: ")
            shifts = int(input("how many people would you like to scheldule: "))
            writer = csv.writer(file)
            writer.writerow([date,date_c])
            sep = ('----------------')
            writer.writerow([sep])
            for j in range(shifts):
                name = input("name of worker: ")
                length = input("shift hours: ")
                writer = csv.writer(file)
                writer.writerow([name,length])
            space = (' ')
            writer.writerow([space])




print('')
print("                          Welcome to your YourRestuarant ")
print('')
print("---------------Menu---------------Scheldule---------------Tipout---------------BusinessTracking")
print('')
print("Menu: Call this function to add, delete or edit items to your menu that is in a seperate csv file")
print('')
print("Scheldule: Call this function to edit, delete, or add shifts to th scheldule in a csv file")
print('')
print("Tipout: call this function to calculate tipout for bussers based on sales and shifts worked")
print('')
print("Business Tracking: call this function to enter sales to track progress. Also view reviews")
action = input ("                          Input Function: ").lower()
if "menu" in action:
    Menu()
elif "tipout" in action:
    tipout = TP()
    print(tipout)
elif "scheldule" in action: 
    scheldule = Scheldule()
    print(scheldule)
