import os

file_account="account.txt"
file_lock="lock.txt"
maxLoginTime=3

f1=file(file_account)
accountList=f1.readlines()
f1.close()

while True:
    userName=raw_input('User:')
    
    f2=file(file_lock)
    lockUserList=f2.readlines()
    lock_list=[]
    for line in lockUserList:
       lock_list.append(line.strip('\n').strip())
    f2.close()
    if userName in lock_list:          
            print "Sorry , You is locked"
            break

    for line in accountList:
        Line=line.split()
        loginSuccess=False
        print Line[0],Line[1]
        if userName==Line[0]: 
            for i in range(maxLoginTime):
                password=raw_input('password:')
                if password==Line[1]: #correct Password
                    print "Welcome %s" %userName
                    loginSuccess=True
                    break
            else:
                print "User %s is locked" %userName
                f2=file(file_lock,'a')
                f2.write("\n %s"%userName)
                f2.close()
                continue
            if loginSuccess == True:
                break
    if loginSuccess == True:
        break
                
                






