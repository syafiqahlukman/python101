'''Tuple is type of data structure. Its a container where we can store different value
Tuple is immutable, it cant be changed or modified. You cannot change, add elements.'''

#example 1
#coordinates = (4,5)
#coordinates[1]=10 #error because cant change it
#print (coordinates[1])

#example2
# define list of servers, each of element in the list is a tuple. (inside [] is list)
# each tuple contains 3 info: IP, hostname, status of server 
servers = [("192,168.1.1", "server1.com", "active"),
           ("192,168.1.2", "server2.com", "inactive"),
           ("192,168.1.3", "server3.com", "active")]

#display list of servers
def display_servers(servers): #define a function where we told python the instruction of this particular program
    print("List of servers:") #the function prints a header
    for server in servers: #then loops through each server in the list and print the ip, hostname, status
        print(f"IP Address: {server[0]}, Hostname: {server[1]}, Status: {server[2]}")
    print()
display_servers(servers)

#add a new server
new_server = ("192.168.1.4", "server4.com", "inactive")
servers.append(new_server)
print("Added new server:")
display_servers(servers)












''' 
Tuple vs List
Tuple: use when want data to remains constant throughout the program - database records, configuration settings
Lists: collection of items that can change over time - maintaning list of users, shopping cart

'''