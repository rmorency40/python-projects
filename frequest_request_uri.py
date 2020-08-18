#! /usr/bin/env python3

def frequest_requested_uri(list):
    count = {}
    new_list = []
    for ele in list:
        new_list.append(ele.split(' ')[2])
    for uri in new_list:
        if uri in count:
             count[uri] += 1
        else:
            count[uri] = 1
    frequent_requested_uri  = max(count.items(), key=lambda x: x[1])        
    return frequent_requested_uri                   
                        
                        
#Driver codes

list = ['2016-10-10T13:56:04 172.16.0.9 /css/style.css',
         '2016-10-10T13:55:36 127.0.0.1 /favicon.ico',
         '2016-10-10T13:56:01 10.0.8.14 /index.html',
         '2016-10-10T13:56:04 172.16.0.4 /css/style.css',
         '2016-10-10T13:56:33 172.16.0.7 /favicon.ico',
         '2016-10-10T13:56:33 172.16.0.4 /favicon.ico',
         '2016-10-10T13:57:10 10.0.8.14 /update.php',
         '2016-10-10T13:57:34 10.0.0.4 /favicon.ico']
print(frequest_requested_uri(list))                       
                        
