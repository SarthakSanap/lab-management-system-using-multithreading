from multiprocessing import Process

from FinalGUI import main
from ServerNew import Server

def GUI_Function():
    main()

def Server_Function():
    server = Server()

with open('OnPCs.txt', 'w') as f:
    f.write("")
with open('ShutdownPC.txt', 'w') as f:
    f.write("")
with open('TaskPC.txt', 'w') as f:
    f.write("")
with open('TaskDetail.txt', 'w') as f:
    f.write("")
with open("BrowserOnPCs.txt", "w") as f:
    f.write("")
with open("USBConnectedPCs.txt", "w") as f:
    f.write("")
with open('CloseBrowserPCNames.txt', 'w') as f:
    f.write("")



if __name__ == "__main__":
    p1 = Process(target=GUI_Function)
    p2 = Process(target=Server_Function)
    p1.start()
    p2.start()
    p1.join()
    p2.join()