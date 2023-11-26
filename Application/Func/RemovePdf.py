import os


def RemoveArq(caminho) :
    dir = caminho
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    return
