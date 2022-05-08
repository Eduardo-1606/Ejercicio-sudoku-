from operator import truediv
import random
import numpy as np 



class cuerpo():
    def __init__(self):
        self.cuerposudoku=[]
        self.punteo=0
    
    def Generandocuerpo(self):

       self.cuerposudoku=[[0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0,0]]
     
    def niveldejuego(self):
        
        bandera=False
        while bandera==False:
            print("while")
            self.cuerposudoku[0][2]= random.randrange(1,9)
            self.cuerposudoku[2][5]= random.randrange(1,9)
            self.cuerposudoku[6][5]= random.randrange(1,9)
            
          
            cumplio= self.recorriendocuerpo(self.cuerposudoku)
            if cumplio == True:
                bandera=True
                
    def recorriendocuerpo(self,cuerposu):
        banderaglobal=True
        for filas in cuerposu:
            bandera=self.validanoserepite(filas)
            if bandera==True:
                print("no se repiten datos",filas)
            else:
                print("se repiten datos",filas)
                banderaglobal=False
        return banderaglobal
        
    
    def validanoserepite(self,arregloindividual):
        for i in arregloindividual:
            if i!=0:
                if arregloindividual.count(i)>1:
                   return False 
        return True
    

grid=[[0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0]]
def possible(row,column,number):
    global grid 
    for x in range(0,9):
        if grid[row][x]==number:
            return False 
    x0=(column//3)*3
    y0=(row//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j]==number:
                 return False 
    return True 
def solve():
    global grid 
    for row in range(0,9):
        for column in range(0,9):
            if grid[row][column]==0:
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column]=number
                        solve()
                        grid[row][column]=0
                return
    print(np.matrix(grid))
    input("No se puede solucionar ") 
solve()




    

                
    

        
             