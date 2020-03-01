
def écriture():
    fichier = open("fichier.txt", "a")
    fichier.write("\n Toto")
    return

def lecture():
    fichier = open("fichier.txt", "a") 
    print(fichier.read())
    return

if __name__ == '__main__':
    écriture()
    lecture()
    
                   

    
    
