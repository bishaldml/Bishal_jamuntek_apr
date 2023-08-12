import main

action = "start" 
while action != "exit" and action != "e": 
    action = input("Please enter your action (Insert-I, Delete-D, Search-s, Update-u, Display-Dis and Exit-e) ").lower() 
    hosp = main.Hospital(action)  
    hosp.PatientMgmt() 