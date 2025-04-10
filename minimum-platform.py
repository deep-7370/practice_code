def platform(arival,departure):
    arival.sort()
    departure.sort()
    n=len(arival)
    ari=1
    count=1
    dep=0
    platform=1
    while ari<n and dep<n:
        if arival[ari]<=departure[dep]:
            ari+=1
            count+=1
            platform=max(platform,count) 
            
        else:
            dep+=1
            count-=1
           
    return platform

arival=[900,940,950,1100,1500,1800]
departure=[910,1200,1120,1130,1900,2000]
print(platform(arival,departure))
