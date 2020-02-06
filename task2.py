f = open('hits.txt', 'r') 
hits = f.read()
hits = hits.split()  #разбил на отдельные элементы списка
ip = []
for k in range(1,len(hits),3):
    ip.append(hits[k])          #парсинг ip адресов в массив ip
freq = []    #список, в который будет записываться частота появления каждого ip-адреса в массиве ip
ipset = set(ip) #DISTINCT ip
ipset = list(ipset)  #Обратно в список
#print(len(ipset),'\n',len(ip))
a = []      #массив, в который будет вписан ответ
for k in range(len(ipset)):
    freq.append(ip.count(ipset[k]))
freq.sort()
freq.reverse() # - теперь этот массив отсортирован по убыванию
for k in range(len(ipset)):
    if ip.count(ipset[k]) == freq[0]: # если встречаем самый популярный массив, то вписываем его в ответ
        a.append(ipset[k])
    elif ip.count(ipset[k]) == freq[1]: # если встречаем второй по популярности массив, вписываем в ответ (и т.д.)
        a.append(ipset[k])
    elif ip.count(ipset[k]) == freq[2]:
        a.append(ipset[k])
    elif ip.count(ipset[k]) == freq[3]:
        a.append(ipset[k])
    elif ip.count(ipset[k]) == freq[4]:
        a.append(ipset[k])
a = set(a) # для исключения повторов, при этом ip-адреса не будут расположены по убыванию частоты вхождений, но этого в задании и не требуется
print(a) 
#ans ['154.157.157.156'] ['82.146.232.163'] ['226.247.119.128', '194.78.107.33'] ['21.143.243.182'] - это ip адреса, расположенные по убыванию частоты вхождений
f.close