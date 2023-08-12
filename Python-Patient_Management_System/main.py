class Hospital:
    '''
    Patient Management System 
    '''
    def __init__(self,action): 
        self.action = action 
    
    def PatientMgmt(self): 
            
        #INSERTION OPERATION 
        if self.action == "insert" or self.action == "i":
            pid = input("Enter PID : ") 
            #Check for duplicate value for PID 
            pdf = open("patient.data","r") 
            pd = pdf.readlines() 
            x = 0 

            if len(pd) > 0: 

                for sdata in pd: 
                    s1 = sdata.find(pid)
                    # print(s1)
                    if s1 >= 0:
                        x = 1 
                        #continue 
                # print(x)
                if x == 1: 
                    print("The Patient ID: ",pid," Already exists")
                else: 
                    pdf.close()
                    pname = input("Enter Patient Name : ")
                    padd = input("Enter Patient Address : ")
                    pdf = open("patient.data","a") 
                    #pdf.write("\n")         
                    pdf.write(pid + ":" + pname + ":" + padd)
                    pdf.write("\n")
                    pdf.close()
                    
            else:
                pdf.close()
                pname = input("Enter Patient Name : ")
                padd = input("Enter Patient Address : ")
                pdf = open("patient.data","a")   
                #pdf.write("\n")       
                pdf.write(pid + ":" + pname + ":" + padd)
                pdf.write("\n")
                pdf.close()
                #break
        
        
        #DELETION OPERATION
        elif self.action == "delete"or self.action == "d":
        
            pid = input("Enter PID : ")
            pdf = open("patient.data","r+")
            pd = pdf.readlines()
            pdf.seek(0)
            for patdata in pd:
                s1 = patdata.find(pid)
                if s1 == 0:
                    print("Patient Deleted: ",patdata)
            
            pd = pdf.readlines()
            pdf.seek(0)
            pdf.truncate()
            
            for data in pd:
                s1 = data.find(pid)
                if s1 != 0:
                    pdf.write(data)
            pdf.close()


        # SEARCH OPERATION
        elif self.action == "search"or self.action == "s":
            pid = input("Enter PID : ")
            pdf = open("patient.data","r")
            pd = pdf.readlines()
            x = 0
            for data in pd:
                s1 = data.find(pid)
                if s1 >= 0:
                    print("Patient is : ",data)
                    pdf.close()
                    x = 1
                    break
            if x == 0:
                print("No Such Patient")
          
        # UPDATE OPERATION
        elif self.action == "update"or self.action == "u":
            pid = input("Enter PID : ")
            pdf = open("patient.data","r")
            pd = pdf.readlines()
            x = 0
            for data in pd:
                s1 = data.find(pid)
                if s1 >= 0:
                    print("Patient is : ",data)
                    ndata = input("Enter new data set :")                    
                    pdf.close()
                    
                    pdf = open("patient.data","r+")
                    pd = pdf.readlines()
                    pdf.seek(0)
                    pdf.truncate()

                    for data in pd:
                        s1 = data.find(pid)
                        if s1 != 0:
                            pdf.write(data)        
                            
                    pdf.write(ndata)        
                    pdf.close()
                    
                    
                    x = 1
                    break
            if x == 0:
                print("No Such Patient")
            
        #DISPLAY PATIENT DATA 
        if self.action == "display" or self.action == "dis":
            File = open("patient.data","r")
            contents = File.read() 
            print(contents)
            File.close()