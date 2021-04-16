income = input("input your total yearly income");
if int(income) <= 0 :
    print("Please re-enter. Income should not be under 0")
    
if int(income) >0 :
    print("your total income is:",income);
    MPF = int(income) *0.05
    if MPF >18000:
        MPF = 18000
        print("Your MPF deduction is", MPF)
    else:
        print("Your MPF deduction is", MPF)
    Netinc = int(income) - MPF
    print("Your Net Total income is", Netinc)
    Deduct = 132000
    NCT = Netinc - Deduct
    print("Your Net Chargeable Income is", NCT)
    if NCT <=0:
        print("Your Net Charagble income is 0")
        tax = 0
        print("your taxes this year is ", tax)
    if NCT < 50000 and NCT > 0:
        tax = NCT * 0.02
        print("your taxes this year is ", tax)
    i = 0
    rate = 0.02
    cal = 0
    if NCT > 200000:
        remain = (NCT - 200000)
        NCT = NCT - remain
        remain = remain * 0.17 
        while NCT > 50000 :
            NCT = NCT- 50000
            i += 1
            cal = cal + (50000*rate)
            rate = rate +0.04
        else: 
            if i == 1:
                cal = cal+ (NCT *0.06)
            if i == 2:
                cal = cal+ (NCT *0.1)
            if i == 3:
                cal = cal+ (NCT *0.14)
        cal = cal + remain
        print("Your taxes this year is", cal)
    else:
        while NCT > 50000 :
            NCT = NCT- 50000
            i += 1
            cal = cal + (50000*rate)
            rate = rate +0.04
        else: 
            if i == 1:
                cal = cal+ (NCT *0.06)
            if i == 2:
                cal = cal+ (NCT *0.1)
            if i == 3:
                cal = cal+ (NCT *0.14)
        print("Your taxes this year is", cal )   
    wife = input("Do you have a wife? Y/N")
    if wife == "N" :
        print("The program end here")
    if wife == "Y" :
        incomew = input("input your wife total yearly income");
        if int(incomew) <= 0 :
            print("Please re-enter. Income should not be under 0")
    
        if int(incomew) >0 :
            print("your wife total income is:",incomew);
            MPFw = int(incomew) *0.05
            if MPFw >18000:
                MPFw = 18000
                print("Your wife MPF deduction is", MPFw)
            else:
                print("Your wife MPF deduction is", MPFw)
        Netincw = int(incomew) - MPFw
        print("Your wife Net Total income is", Netincw)
        Deduct = 132000
        NCTw = Netincw - Deduct
        print("Your wife Net Chargeable Income is", NCTw)
        if NCTw <=0:
            print("Your wife Net Charagble income is 0")
            tax = 0
            print("your wife taxes this year is ", tax)
        if NCTw < 50000 and NCTw > 0:
            tax = NCTw * 0.02
            print("your wife taxes this year is ", tax)
        i = 0
        rate = 0.02
        calw = 0
        if NCTw > 200000:
            remain = (NCTw - 200000)
            NCTw = NCTw - remain 
            remain = remain * 0.17
            while NCTw > 50000 :
                NCTw = NCTw- 50000
                i += 1
                calw = calw + (50000*rate)
                rate = rate +0.04
            else: 
                if i == 1:
                    calw = calw+ (NCTw *0.06)
                if i == 2:
                    calw = calw+ (NCTw *0.1)
                if i == 3:
                    calw = calw+ (NCTw *0.14)
                calw = calw + remain
                print("Your wife taxes this year is", calw )
        else:
            while NCTw > 50000 :
                NCTw = NCTw- 50000
                i += 1
                calw = calw + (50000*rate)
                rate = rate +0.04
            else: 
                if i == 1:
                    calw = calw+ (NCTw *0.06)
                if i == 2:
                    calw = calw+ (NCTw *0.1)
                if i == 3:
                    calw = calw+ (NCTw *0.14)
                print("Your wife taxes this year is", calw)   

        joint = int(income) + int(incomew)
        MPFj = MPF + MPFw
        Deductj = Deduct *2
        NCTj = joint - MPFj -Deductj
        i = 0
        rate = 0.02
        calj = 0
        if NCTj > 200000:
            remain = (NCTj - 200000)
            NCTj = NCTj - remain
            remain = remain *0.17 
            while NCTj > 50000 :
                NCTj = NCTj - 50000
                i += 1
                calj = calj + (50000*rate)
                rate = rate +0.04
            else: 
                if i == 1:
                    calj = calj + (NCTj *0.06)
                if i == 2:
                    calj = calj + (NCTj *0.1)
                if i == 3:
                    calj = calj + (NCTj *0.14)
                calj = calj + remain
                print("Your joint taxes this year is", calj)
        else:
            while NCTj > 50000 :
                NCTj = NCTj- 50000
                i += 1
                calj = calj + (50000*rate)
                rate = rate +0.04
            else: 
                if i == 1:
                    calj = calj + (NCTj *0.06)
                if i == 2:
                    calj = calj + (NCTj *0.1)
                if i == 3:
                    calj = calj + (NCTj *0.14)
                print("Your joint taxes this year is", calj) 
        total = cal + calw
        print("Your seperated tax total is ",total) 
        if calj < total :
            print("Joint Assessment should be use")
        else:
            print("Seperate Taxation sohuld be use")    