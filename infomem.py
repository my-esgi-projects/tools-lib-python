import psutil

def infoMemory():
    print("memoire total :", psutil.virtual_memory().total)
    print("memoire disponible :", psutil.virtual_memory().available)