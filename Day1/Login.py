
file_account="account.txt"
file_lock="lock.txt"
maxLoginTime=3

for LoginTime in range(maxLoginTime):
    userName=raw_input("UserName:")
    password=raw_input("Password:")
    if len(userName.strip())!= 0 and len(password.strip())!=0:
        loginSuccess = False   
        f1=file("file_account","r")
        for line in f1.readline():
            line=line.split()
            if userName==line[0] and password==line[1]:
                #login success
                print "welcome %s" %userName
                loginSuccess = True
                f1.close()
                break
            else:
                continue
        if loginSuccess==True:
            break
        else:
            continue
    else:
        continue
else:
    print"Your account is Locked"   
    f2=file(file_account)
    
        
                
            
            
            
            
            
        
    
    
    
    
    
    
    