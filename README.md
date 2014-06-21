Secure-Chat
===========

**Note:** This chat software should only be used as a simulator to experiment with different ciphers, and the OpenSSL library in general. Despite the name, this is not a secure chat client.

The SSL/TLS chat client is a chat client implemented using python and Qt (PyQt). The chat is P2P, but a centralized name-server is used to find other users.

To run the chat client, do the following:
- Run nameserver.py on the name-server
- Edit the IP in nameclient.py (on the clients) to the IP of the name-server
- Run main.py on the clients

The available cipers in the settings window can easily be changed by editing the ciphers-array in the UserPref class.

## Class Diagram
![alt tag](images/class_diagram.png)


## GUI Elements

#### UserPref
![alt tag](images/gui/userpref.png)

#### UserSelect
![alt tag](images/gui/userselect.png)

#### Chat
![alt tag](images/gui/chat.png)
