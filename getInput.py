import fileinput

def main():
    # entrada de dados por arquivo
    indata = []
    for line in fileinput.input(files='in.txt'):
        indata.append(line.rstrip('\n'))

    interval = indata[2].split(' ')
    del indata[-1]
    Amin, Amax = interval
    Kmax, R = indata

    # casting
    Kmax = int(Kmax)
    R = int(R)
    Amin = int(Amin)
    Amax = int(Amax)

    if(Kmax < 5):
        print("*****************")
        print("Erro - De acordo com as especificações, Kmax deve ser maior ou igual à 5.")
        print("Abortando execução")
        print("*****************")
        exit()

    return Amin, Amax, Kmax, R