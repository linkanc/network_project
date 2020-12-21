from websocket_server import WebsocketServer
import time
#coding=utf-8 
# Called for every client connecting (after handshake)
def new_client(client, server):
    #print("New client connected and was given id %d" % client['id'])
    fr = open("log.txt",'r',encoding = "utf-8")
    st = fr.readlines()
    fr.close()

    #print(st)
    for i in range(5):
        server.send_message(client, st[len(st) - 5 + i])



# Called for every client disconnecting
def client_left(client, server):
    print("Visitors(%s) disconnected" % client['address'][0])


# Called when a client sends a message
def message_received(client, server, message):
    if len(message) > 200:
        message = message[:200]+'..'
    
    print(message)
    #message = str.encode(message)

    fr = open("log.txt",'r', encoding = "utf-8")
    st = fr.readlines()
    fr.close()

    st.pop(0)
    st.append("Visitors(%s) said: %s at %s \n" % (client['address'][0], message, str(time.ctime())))
    #print("Visitors(%d) said: %s" % (client['id'], message))
    #print(st)
    for i in range(5):
        server.send_message(client, st[len(st) - 5 + i])
    fw = open("log.txt", 'w', encoding = "utf-8")
    for i in range(len(st)):
        fw.write(st[i])
    fw.close()


PORT=5050
server = WebsocketServer(PORT, host = '0.0.0.0')
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)

server.set_fn_message_received(message_received)
server.run_forever()