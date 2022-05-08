#Este fue un sudoku experimental que no me quedo tan bien pero me da la solucion al juego 
#no tiene pygame ni los valores inicializados a cero pero fue el unico que si me salio 
#el resultado no se ve tan bien ya que no puede lograr que me lo imprimiera en forma del tablero de sudoku 
#pero espero que ayude algo en la calificacion. 

tablero=tablero=[[5,3,0,0,7,0,0,0,0],
                 [6,0,0,1,9,5,0,0,0],
                 [0,9,8,0,0,0,0,6,0],
                 [8,0,0,0,6,0,0,0,3],
                 [4,0,0,8,0,3,0,0,1],
                 [7,0,0,0,2,0,0,0,6],
                 [0,6,0,0,0,0,2,8,0],
                 [0,0,0,4,1,9,0,0,5],
                 [0,0,0,0,0,0,0,7,9]]


class validessudoku:
    def __init__(self,tablero)->None:
        self.tablero=tablero
        self.lista_invertida=list()

    def general(self):
        assert len (self.tablero)==9,"El tablero ingresado no corresponde al formato 9x9"
        for fila in  self.tablero:
            assert len(fila)==9,"El tablero ingresado no corresponde al formato 9x9"

    def verificacion_filas(self,lista_a_revisar="tablero:general"):
        if lista_a_revisar=="tablero_general":
            lista_a_revisar=self.tablero
        for fila in lista_a_revisar:
            for elemento in fila:
                if elemento !=0:
                    assert fila.count(elemento)==1,"El tablero ingresado no es valido"

    def verificacion_columanas(self):
        for columnas_index in range(0,9):
            for row_index in range(0,9):
                self.lista_invertida.append(self.tablero[row_index][columnas_index])

            self.verificacion_filas([self.lista_invertida])
            self.lista_invertida.clear()
        
    def revision_subcuadros(self):
        self.revision_3_subcuadros(0,3)
        self.revision_3_subcuadros(3,6)
        self.revision_3_subcuadros(6,9)
    
    def revision_3_subcuadros(self,rango1,rango2):
        self.lista_invertida.clear()
        for row_index in range(0,9):
            if row_index==3 or row_index==6:
                self.lista_invertida.clear()
            for columnas_index in range(rango1,rango2):
                self.lista_invertida.clear()
                if len(self.lista_invertida)==9:
                    self.verificacion_filas([self.lista_invertida])
        
if __name__=="__main__":
    sudoku=validessudoku(tablero)
    sudoku.general()
    sudoku.verificacion_filas()
    sudoku.verificacion_columanas()
    sudoku.revision_subcuadros()
    print(tablero)
    print("El tablero de sudoku ingresado es valido")


    def es_valido_mover(grid,row,col,numero):
        for x in range(9):
            if grid[row][x]==numero:
                return False
        for x in range(9):
            if grid[x][col]==numero:
                return False
        corner_row=row-row%3
        corner_col=col-col%3
        for x in range(3):
            for y in range(3):
                if grid[corner_row+x][corner_col+y]== numero:
                    return False
        return True 
    def solucion(grid,row,col):
        if col==9:
            if row== 8:
                return True 
            row+=1
            col=0
    
        if grid[row][col]>0:
            return solucion(grid, row, col+1)
        for num in range(1,10):
            if es_valido_mover(grid, row, col, num):
                grid[row][col]=num
                if solucion(grid,row,col +1):
                    return True 
            grid[row][col]=0
        return False
    grid=[[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,0,0,0,7,9]]

    if solucion(grid,0,0):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=" ")
        print() 
    else:
        print("El sudoku no tiene solucion")

