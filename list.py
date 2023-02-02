if __name__ == '__main__':
    N = int(input())
    liste=[]
    for i in range(0,N):
        metin=input().split(" ")
        if metin[0]=="insert":
          liste.insert(int(metin[1]),int(metin[2]))
        
        elif metin[0]=="print":
            print(liste)
            
        elif metin[0]=="remove":
            liste.remove(int(metin[1]))
        elif metin[0]=="append":
            liste.append(int(metin[1]))
        elif metin[0]=="sort":
            liste.sort()
        elif metin[0]=="pop":
            liste.pop()
        elif metin[0]=="reverse":
            liste.reverse()
