class Mia_classe():
    cont=0
    def __init__ (self):
        Mia_classe.cont +=1

    @classmethod
    def istanze (cls):
        print(cls.cont)



m1 = Mia_classe()
m2 = Mia_classe()
print(Mia_classe.cont)
Mia_classe.istanze()


