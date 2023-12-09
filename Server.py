import socket
from threading import Thread
from colorama import Fore

class Helpers:
    yellow = Fore.YELLOW
    green = Fore.GREEN
    blue = Fore.LIGHTBLUE_EX
    cyan = Fore.CYAN
    red = Fore.RED

v1 = "0.0.0.0";
v2 = 5001;
v3 = set();
v4 = socket.socket();
v4.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
v4.bind((v1,v2));
v4.listen();

channelData = {}

print(r"""
   _____ _                 __        ________          __  __  _            
  / ___/(_)___ ___  ____  / /__     / ____/ /_  ____ _/ /_/ /_(_)___  ____ _
  \__ \/ / __ `__ \/ __ \/ / _ \   / /   / __ \/ __ `/ __/ __/ / __ \/ __ `/
 ___/ / / / / / / / /_/ / /  __/  / /___/ / / / /_/ / /_/ /_/ / / / / /_/ / 
/____/_/_/ /_/ /_/ .___/_/\___/   \____/_/ /_/\__,_/\__/\__/_/_/ /_/\__, /  
                /_/                                                /____/   
    """)
print(f"{Helpers.cyan}[DEBUG] Server started! Listening on {v1}:{v2}");

def listenClients(x1,x2):
    while True:
        try:
            isSend = True
            i1 = x1.recv(2048).decode();
            i2 = i1 # Decrypt Message

            split = i2.split("~");
            
            if (split[0] == "/login"):
                isSend = False

                username = split[1]
                channel = split[2]

                if channel in channelData:
                    pass
                else:
                    channelData[f'{channel}'] = {
                        "userADDR": []
                    }
                channelData[f'{channel}']['userADDR'].append(x1)
                
                for x in channelData[f'{channel}']['userADDR']:
                    if channel == "":
                        channel = "0"

                    x.send(f"{username} joined the channel!\n".encode())
                    print(f"{Helpers.blue}[CLIENT] Received packet, ID: 3201, Name: joinChannel, Channel: {channel}");
                    print(f"{Helpers.yellow}[CLIENT] {v6} username set '{username}'");
            else:
                message_content = split[0]
                encrypted_content = message_content # Encrypt Message
                channel_id = split[1]
                
                for x in channelData[f'{channel_id}']['userADDR']:
                    x.send(f"{encrypted_content}\n".encode())
                    print(f"{Helpers.blue}[CLIENT] Received packet, ID: 2048, Name: sendMessage, Contents: {encrypted_content}, Client: {v6}");
        except Exception as e:
            try:
                channelData[f'{channel}']['userADDR'].remove(x1)

                for x in channelData[f'{channel}']['userADDR']:
                    x.send(f"{username} left the channel!\n".encode())

                v3.remove(x1);
                break
            except:
                print(f"{Helpers.cyan}[DEBUG] Client disconnected! {v6}");
                break
        else:
            pass

while True:
    v5, v6 = v4.accept();
    print(f"{Helpers.cyan}[DEBUG] New client connection! {v6}");
    v3.add(v5)
    v7 = Thread(target=listenClients, args=(v5, v6,));
    v7.daemon = True;
    v7.start();

for cs in client_sockets:
    cs.close()

s.close()
