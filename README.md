# Socket
socket programing via Python


![alt text](http://media.geeksforgeeks.org/wp-content/uploads/Socket-Programming-in-C-C-.jpg)

## Introduction
Socket programming is a way of connecting two nodes on a network to communicate with each other.
One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.

**For socket programming in Py, you have to install python first**
### Run
According to your Os you have to open the command lines. 
But first you have to run the server.py file to listen for connections.
The ip and port itself can be changed. it doesn't matter what it would be
On windows open cmd then type the description:
```
python server.py
```
You have these outputs as a result:
```
socket created
socket binded to 1111
Waiting for connection
```
after these outputs run the another file :
```
python client.py
```
Then you will have a connection and as a result :
```
Connected
```

**You have to run these files according to the location of your file in your PC.
Becides running these file on editors or IDEs required some Py and Running code extension in order to see the outputs**


