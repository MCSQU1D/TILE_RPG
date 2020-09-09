
global Workplace_List
global Sales_Dict
global Accounting_Dict
global Shipping_Dict


Sales_Dict = [
#["Job", Int_req, Str_req, Chm_req, Pay]
["Sales", 40, 0, 40, 40],
["Head of Floor", 75, 0, 60, 75],
["Head of Sales", 100, 0, 75, 100]
]

Accounting_Dict = [
["Accountant", 80, 0, 0, 50],
["Head of Accounting", 100, 0, 0, 100]
]

Shipping_Dict = [
["Stacker", 0, 25, 0, 20],
["Forklift Driver", 25, 50, 0, 35],
["Head of Shipping", 30, 75, 0, 60]
]


Stats_Dict = {
    "intelligence" : 10,
    "strength" : 15,
    "charm" : 15,
    "karma" : 0
}

money = 0
ButtonLocationPrintHolder = input("Button: ")
Sales_Job = "None"


#EXIT




def Work(Work_Location):
    global ButtonLocationPrintHolder
    Job = Work_Location

    if Work_Location = "Sales"


    #EXIT
    if ButtonLocationPrintHolder == "button1":
        ButtonLocationPrintHolder = "holder"
        scene = maps[current_map]

    #WORK
    if ButtonLocationPrintHolder == "button2":
        ButtonLocationPrintHolder = "Holder"
        if Job == "None":
            #PrintGeneral("Apply for a Job")
            print("Apply for a Job")
        else:
            for i in Work_Dict:
                if Job == i[0]:
                    #PrintGeneral("Earnt: " + str(i[4]))
                    print("Earnt: " + str(i[4]))
                    money += i[4]
    #PROMOTION
    if ButtonLocationPrintHolder == "button3":
        ButtonLocationPrintHolder = "Holder"
        a = 0
        for i in Work_Dict:
            a += 1
            if i[0] == Job:
                holda = Sales_Dict[a]
                if Stats_Dict["intelligence"] >= holda[1]:
                    #PrintGeneral("Promoted")
                    print("Promoted")
            else:
                print("Must have job here")
    #APPLY
    if ButtonLocationPrintHolder == "button5":
        ButtonLocationPrintHolder = "Holder"
        if Work_Dict == "None":
            for i in Work_Dict:
                if Stats_Dict["intelligence"] >= i[1]:
                    Job = i[0]
                    #PrintGeneral("Hired")
                    print("Hired")
                else:
                    #PrintGeneral("Rejected")
                    print("Rejected")
        else:
            #PrintGeneral("Already have a Job here")
            print("Already have a Job here")
