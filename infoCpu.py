import psutil

def infocpu():
    print("le pourcentage d'ocupation du processeur est :", psutil.cpu_percent(interval=1, percpu=True))
    print("nombre de processeur logiue :", psutil.cpu_count(logical=True))