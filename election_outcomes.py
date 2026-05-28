def election_outcomes(arr):
    A_elector=B_elector=0
    for i in arr:
        if i=="A":
            A_elector+=1
        elif i=="B":
            B_elector+=1
    if A_elector>B_elector:
        return  "A_elector win",A_elector
    elif B_elector>A_elector:
        return "B_elector win",B_elector
    else:
        return "coaliation government"
    
ae="ABAAAABBBAAAABABABA"
print(election_outcomes(ae))
    