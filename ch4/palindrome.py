def pallindrome():
    p_candidate = input("type your pallindrome candidate : ")
    print('here is your pallindrome',p_candidate)
    p_candidate = p_candidate.lower()
    print('after lowering characters ==>',p_candidate)

    isp_candidate = True
    p1 = 0
    p2 = len(p_candidate)-1
    while isp_candidate and p1<p2:
        if p_candidate[p1].isalpha():
            if p_candidate[p2].isalpha():
                if p_candidate[p1]==p_candidate[p2]:
                    p1 = p1 + 1
                    p2 = p2 - 1
                else:
                    isp_candidate = False
                    return isp_candidate
            else:
                p2 = p2-1
        else :
            p1 = p1+1

    


    return isp_candidate

pallindrome()