# inplemetar una calculadora que pida dos numeros y un a operacion,vamos a usar la figura de switch...case y luegocon if...elif...else.

#calculadora basica

num_1= float(input("primer numero a operar:"))
num_2 = float(input("segundo numer a operar"))
operador = input("que operacion vas hacer?(+,-,*,/):")

# como asi que switch y case ?
# switch y case condicionales ,donde se evalua un parametro, buleano y se va a direccionar inmediatamente segun los casos definidos
match operador:
    case "+":
        print("resultado",num_1 + num_2)
    case "-":
        print("resultado", num_1 - num_2)
    case "*":
        print("resultado", num_1 * num_2)
    case "/":
        if num_2 != 0:
           print("resultado", num_1 / num_2)
        else:
            print("Resultado no válido")
    case _:
        print("resultado no valido")
       
    