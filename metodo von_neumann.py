""" Realizar el ejercicio con una semilla cuyo número inicial es 9731 deben aparecer los 100 primeros números producto de la aplicación de dicho método
# >  [ 100, ]  8100 16810000   última línea de su código. """



def  von_neumann(seed):
    for i in range(1,101):
        cuadrado= seed * seed
        valor_string=str(cuadrado)
        while len(valor_string) < 8:
            valor_string= "0" + valor_string
        
        total=valor_string[2:6]
        seed=int(total)
        print(f" {i}: {valor_string}-----> {seed}")
        
von_neumann(9731)
            