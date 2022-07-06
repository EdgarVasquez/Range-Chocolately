from example_package_Edgar1098586 import main

if __name__ == '__main__':
    try:
         print("Bienvenido a nuestra aplicacion par saber diferentes metodos de operar rangos")
         print("Nuestro menu es el siguiente\n 1.Contains \n 2.Equals \n 3.Overlaps \n 4.EndPoints")
         resultado = int(input())
         print("Ingrese el primer rango")
         R1 = main.Range(input())
         if resultado != 4:
            print("Ingrese el segundo rango")
            R2 = main.Range(input())
         if resultado == 1:
             R3 = main.Range.ContainsRange(R1,R2)
         elif resultado == 2:
             R3 = main.Range.EqualRanges(R1,R2)
         elif resultado == 3:
             R3 = main.Range.OverLapsRange(R1,R2)
         elif resultado == 4:
             R3 = main.Range.Endpoint(R1)
             print(R3)
             input()
    except:
         print("An exception occurred")
