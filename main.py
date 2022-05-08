#unificar pygame con logica de sudoky y frontend
#importando las clases
import logicasudoku
import frontendsudoku


#inicializando las clases
logica= logicasudoku.cuerpo()
pg.init()
main()
pg.quit()
  
#Generando el cuerpo del sudoku
logica.Generandocuerpo()
#obteniendo el cuerdo del sudoku
tempralcuerpo= logica.cuerposudoku
#recorriendo el cuerpo que se asigno en la variable tempralcuerpo

logica.niveldejuego()
solucion=logica.print_sudoku()
logica.print_sudoku()

