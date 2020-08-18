#!.usr/bin/env python3


def frequent_accessed_urls(list):
    counts = {}
    newlist = []
    #count = 0
    for element in list:
        newlist.append(element.split(' ')[2])
        #print(newlist)
    for url in newlist:
        if url in counts:
            counts[url] += 1
        else:
            counts[url] = 1
    print(counts)
    frequent_accessed_url = max(counts.items(), key=lambda x : x[1])
    #frequent_requested_url = max(zip(counts.values(), counts.keys()))
    return frequent_accessed_url



#Driver codes

list1 = ['2016-10-10T13:56:04 172.16.0.9 /css/style.css',
         '2016-10-10T13:55:36 127.0.0.1 /favicon.ico',
         '2016-10-10T13:56:01 10.0.8.14 /index.html',
         '2016-10-10T13:56:04 172.16.0.4 /css/style.css',
         '2016-10-10T13:56:33 172.16.0.7 /favicon.ico',
         '2016-10-10T13:56:33 172.16.0.4 /favicon.ico',
         '2016-10-10T13:57:10 10.0.8.14 /update.php',
         '2016-10-10T13:57:34 10.0.0.4 /favicon.ico']
print(frequent_accessed_urls(list1))


def frequent_access_uri(l_list):
    dict = {}
    for uri in l_list:
        if dict.get(uri.split(' ')[2]):
            dict[uri.split(' ')[2]] += 1
        else:
            dict[uri.split(' ')[2]] = 1
    frequent_accessed_uri = max(dict.items(), key=lambda z : z[1])        
            
    return frequent_accessed_uri

print("***************++++++++++++++==============########################")

#Driver codes

list1 = ['2016-10-10T13:56:04 172.16.0.9 /css/style.css',
         '2016-10-10T13:55:36 127.0.0.1 /favicon.ico',
         '2016-10-10T13:56:01 10.0.8.14 /index.html',
         '2016-10-10T13:56:04 172.16.0.4 /css/style.css',
         '2016-10-10T13:56:33 172.16.0.7 /favicon.ico',
         '2016-10-10T13:56:33 172.16.0.4 /favicon.ico',
         '2016-10-10T13:57:10 10.0.8.14 /update.php',
         '2016-10-10T13:57:34 10.0.0.4 /favicon.ico']
print(frequent_access_uri(list1))    
                   
