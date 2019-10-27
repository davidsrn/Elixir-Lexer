import subprocess
print("---------------------------------------------------------------------------------------------------------")
print("Test de archivo vacio")
print("---------------------------------------------------------------------------------------------------------")

subprocess.call(["python", "parser.py", "0"])
print("---------------------------------------------------------------------------------------------------------")
print("Test de definicion de contante y variable con operaciones")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "4"])


print("---------------------------------------------------------------------------------------------------------")
print("Test de programa con ciclos unidos")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "10"])


print("---------------------------------------------------------------------------------------------------------")
print("Test con definicion de variable en lugar incorrecto ")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "20"])

print("---------------------------------------------------------------------------------------------------------")
print("Test que utiliza una cadena, variable y constante en un lugar que no esta permitido y con un ciclo incorrecto.")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "14"])

print("---------------------------------------------------------------------------------------------------------")
print("Test para asignar el valor a una variable que no corresponde con su tipo.")
print("Como la asignacion es dinamica un ejemplo de sumar un int con un string")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "21"])


print("---------------------------------------------------------------------------------------------------------")
print("Test para llamar un metodo usando una clase que no contenga tal metodo:")
print("Como no usa clases un ejemplo de llamar una funcion inexistente")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "22"])

print("---------------------------------------------------------------------------------------------------------")
print("Test de variable fuera de scope")
print("---------------------------------------------------------------------------------------------------------")
subprocess.call(["python", "parser.py", "17"])

print("---------------------------------------------------------------------------------------------------------")
print("Mas codigos pueden ser probados ejecutando python2 parser.py \"numero de test\"")
print("Actualmente hay de 0 a 22 pruebas dentro de la capeta tests")
print("---------------------------------------------------------------------------------------------------------")
