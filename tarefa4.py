import math

class SuperficieInicial:
    def __init__(self):
        self.largura=int(input("Introduza a largura da superfície: "))
        self.comprimento=int(input("Introduza o comprimento da superfície: "))
    
    def inicio(self):
        sup=[[0]*self.largura]*self.comprimento
        return sup
    
    def AreaSuperficie(self):
        return(self.largura*self.comprimento)

class Figuras:
    sup=SuperficieInicial()
    AreaDisponivel=sup.AreaSuperficie()
    lista_figuras=[]
    L={} #largura
    C={} #comprimento
    R={} #raio
    X={} #posição x
    Y={} #posição y

    def __init__(self):
        self.l=0
        self.c=0
        self.r=0
        self.matriz=self.sup.inicio()
    
    def menu(self):
        opçao=int(input("""
        Menu:
        1. Adicionar figura
        2. Mover figura
        3. Rodar figura
        4. Lista de figuras
        5. Número de figuras
        6. Área ocupada pelas figuras
        7. Área disponível
        8. Sair
        """))
        if opçao==1:
            self.opçao()
        elif opçao==2:
            self.mover()
        elif opçao==3:
            self.rodar()
        elif opçao==4:
            self.lista()
            self.menu()
        elif opçao==5:
            self.numeroFiguras()
            self.menu()
        elif opçao==6:
            self.areaOcupada()
            self.menu()
        elif opçao==7:
            self.areaDisponivel()
            self.menu()
        elif opçao==8:
            print("Adeus!!")
        else:
            print("Opção inválida")
            self.menu()
        
    def opçao(self):
        option=str(input("Quer introduzir um retâgulo (r) ou um círculo (c)?: "))
        if option=="c":
            self.nome=str(input("Nome da figura: "))
            self.r=int(input("Raio do círculo: "))
            self.xfig=int(input("Posição do círculo em relação ao eixo dos xx: "))
            self.yfig=int(input("Posição do círculo em relação ao eixo dos yy:  "))
            self.circulo(self.nome,self.r,self.xfig,self.yfig)
        elif option=="r":
            self.nome=str(input("Nome da figura: "))
            self.l=int(input("Largura do retângulo: "))
            self.c=int(input("Comprimento do retângulo: "))
            self.xfig=int(input("Posição do retângulo em relação ao eixo dos xx: "))
            self.yfig=int(input("Posição do retângulo em relação ao eixo dos yy: "))
            self.retangulo(self.nome,self.l,self.c,self.xfig,self.yfig)
        else:
            print("A opção selecionada não é válida!")
            self.menu()
        
    def retangulo(nome,self,l,c,xfig,yfig):
        verificaçao=True
        if xfig+l <= self.sup.largura and yfig+c <= self.sup.comprimento:
            for i in range(yfig,yfig+c):
                for j in range(xfig,xfig+l):
                    if self.matriz[i][j]!=0:
                        verificaçao=False
            if verificaçao==False:
                print("Não é possível introduzir a figura!")
                self.menu()
            else:
                for i in range(self.c):
                    for j in range(self.l):
                        self.matriz[i+yfig][j+xfig]=nome
                print("Figura introduzida com sucesso")
                self.L[nome]=l
                self.C[nome]=c
                self.lista_figuras.append(nome)
                self.X[nome]=xfig
                self.Y[nome]=yfig
                areafig=l*c
                self.areaDisponivel=self.areaDisponivel-areafig
                self.menu()
        else:
            print("Impossível introduzir a figura!")
            self.menu()
            
    def circulo(nome,self,r,xfig,yfig):
        verificaçao=True
        if xfig+r<=self.sup.largura and xfig-r>=0 and yfig+r<=self.sup.altura and yfig-r>=0:
            for i in range(xfig-r,xfig+r):
                for j in range(yfig-r,yfig+r):
                    if self.matriz[i][j]!=0:
                        verificaçao=False
            if verificaçao==False:
                print("Não é possível introduzir a figura!")
                self.menu()
            else:
                for i in range(xfig-r,xfig+r):
                    for j in range(yfig-r,yfig+r):
                        if (j-xfig)**2+(i-yfig)**2<r**2:
                            self.matriz[i][j]=nome
                print("Figura introduzida com sucesso")
                self.R[nome]=r
                self.X[nome]=xfig
                self.Y[nome]=yfig
                self.lista_figuras.append(nome)
                areafig=math.pi*self.r**2
                self.areaDisponivel=self.areaDisponivel-areafig
                self.menu()
        else:
            print("Impossível introduzir a figura!")
            self.menu()
        
    def mover(self):
        verificaçao=True
        option=str(input("Deseja mover um retângulo (r) ou um círculo (c)? : "))
        if option=="c":
            nome_mover=str(input("Nome do círculo: "))
            for i in range(len(self.lista_figuras)):
                if nome_mover==self.lista_figuras[i]:
                    r=self.R[nome_mover]
                    xfig=int(input("Nova abcissa: "))
                    yfig=int(input("Nova ordenada: "))
                    for i in range(xfig-r,xfig+r):
                        for j in range(yfig-r,yfig+r):
                            if self.matriz[i][j]!=0:
                                if self.matriz[i][j]!= nome_mover:
                                    verificaçao==False
                                    break
                    if verificaçao==False:
                        print("Impossível mover a figura!")
                        self.menu()
                    else:
                        for i in range(len(self.matriz)):
                            for j in range(len(self.matriz[i])):
                                if self.matriz[i][j]==nome_mover:
                                    self.matriz[i][j]=0
                        self.circulo(nome_mover,r,xfig,yfig)
            else:
                print("A figura não existe!")
                self.menu()
        elif option=="r":
            nome_mover=str(input("Nome do retângulo: "))
        for i in range(len(self.lista_figuras)):
            if nome_mover==self.lista_figuras[i]:
                l=self.L[nome_mover]
                c=self.C[nome_mover]
                xfig=int(input("Nova abcissa do ponto inicial: "))
                yfig=int(input("Nova ordenada do ponto inicial: "))
                verificaçao==True
                for i in range(yfig,c+yfig):
                    for j in range(xfig,xfig+l):
                        if self.matriz[i][j]!=0:
                            if self.matriz[i][j]!=nome_mover:
                                verificaçao==False
                                break
                if verificaçao==False: 
                    print("Impossivel mover a figura!")
                    self.menu()
                else:
                    for i in range(len(self.matriz)):
                        for j in range(len(self.matriz[i])):
                            if self.matriz[i][j]==nome_mover:
                                self.matriz[i][j]=0 
                    self.retangulo(c,l,xfig,yfig,nome_mover)
            else:
                print("A figura não existe.")
                self.menu()
        else:
            print("Escolha inválida")
            self.menu()
        
    def rodar(self):
        verificaçao=False
        option=str(input("Deseja rodar um círculo (c) ou um retângulo (r)? "))
        if option=="c":
            print("A rotação de um círculo sobre ele próprio não alterará nada.")
            self.menu()               
        elif option=="r":
            nome_rodar=str(input("Nome do retângulo:")) 
            for i in range(len(self.lista_figuras)):
                if nome_rodar==self.lista_figuras[i]:
                    l=self.L[nome_rodar] 
                    c=self.C[nome_rodar]
                    xfig=self.X[nome_rodar] 
                    yfig=self.Y[nome_rodar]            
                    for i in range(yfig,l+yfig): 
                        for j in range(xfig,xfig+c): 
                            if self.matriz[i][j]!=0:
                                if self.matriz[i][j]!=nome_rodar:
                                    verificaçao==True
                                    break
                    if verificaçao==True: 
                        print("Impossivel rodar a figura!")
                        self.menu()
                    else:            
                        for i in range(len(self.matriz)):
                            for j in range(len(self.matriz[i])):
                                if self.matriz[i][j]==nome_rodar:
                                    self.matriz[i][j]=0
                        self.retangulo(c,l,self.X[nome_rodar],self.Y[nome_rodar],nome_rodar)
        
    def lista(self):
        print("A lista de figuras na superfície: ", self.lista_figuras)
        
    def numeroFiguras(self):
        print("Existem", len(self.lista_figuras), "figuras na superfície")
        
    def areaDisponivel(self):
        return self.areaDisponivel
        
    def areaOcupada(self):
        return self.sup.areaSuperficie()-self.areaDisponivel()
        




