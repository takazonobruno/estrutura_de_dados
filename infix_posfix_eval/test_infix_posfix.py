from infixposfix import *

# encoding: utf-8
comentario = """
Desenvolver um programa que lê uma expressão aritmética como:
((2 + 3 ) * (5 + 2) ) * ((3 + 8 - 2 )  * (2 + 3)  * (3 + 4) )
Em seguida, converte a expressão para a notação Pós-Fixada:
2 3 + 5 2 + * 3 8 + 2 - 2 3 + * 3 4 + * *

* Que elimina a necessidade de parênteses. Se durante o processo de conversão, seu programa detectar parênteses 
desbalanceados ou uso de dois operadores aritméticos seguidos, ele deve parar e avisar que houve erro. 
* Em seguida, seu programa deve avaliar (calcular) a expressão Pós-Fixada. 

Para ambas as atividades, você deve usar uma pilha na forma de lista encadeada.
O programa deverá receber os dados como entrada fornecida pelo usuário.\n"""
print('\033[34m', comentario, '\033[m')

infixa = input("Digite a expressão infixa: ")
posfixa = postfix(infixa)

print(infixa)
print(posfixa)
final = evaluate(posfixa)
print(f"O resultado do calculo é: {final}")
