from doubly_linked_list import *

# encoding: utf-8

'''Funções 1-Fatia 2-Insere string na Lista Duplamente Encadeada 3- Multiplica de 2 em 2  '''


def split_str_2_2(string):
    lista = []
    c = 0
    if len(string) % 2 == 1:
        lista.append(string[0])
        c += 1
    lista += [string[i:i + 2] for i in range(c, len(string), 2)]
    return lista


def insert_str_list(list_str):
    doubly_list = DoublyLinkedList()
    for i in list_str:
        doubly_list.add_end("".join(i))
    return doubly_list


def multiply_2_2(num1, num2):
    str_num_1 = split_str_2_2(num1)
    str_num_2 = split_str_2_2(num2)
    doubly_list1 = insert_str_list(str_num_1)
    doubly_list2 = insert_str_list(str_num_2)
    doubly_list_result = DoublyLinkedList()
    tail1 = doubly_list1.end
    tail_result1 = None
    num_result = []

    while tail1 is not None:
        tail2 = doubly_list2.end
        n1 = int(tail1.data)
        tail_result2 = tail_result1
        while tail2 is not None:
            n2 = int(tail2.data)
            result = n1 * n2
            if tail_result2 is not None:
                result += int(tail_result2.data)
                buffer = result // 100
                result -= buffer * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                tail_result2.data = str(result)
                if tail_result2.prev is None:
                    if tail2.prev is not None:
                        doubly_list_result.add_begin(str(buffer))
                    else:
                        if buffer != 0:
                            doubly_list_result.add_begin(str(buffer))
                else:
                    tail_result2.prev.data = str(buffer + int(tail_result2.prev.data))
            elif doubly_list_result.begin is not None:
                result += int(doubly_list_result.begin.data)
                buffer = result // 100
                result -= buffer * 100
                if result // 10 == 0:
                    result = "0" + str(result)
                doubly_list_result.begin.data = (str(result))
                if tail2.prev is not None:
                    doubly_list_result.add_begin(str(buffer))
                elif buffer != 0:
                    doubly_list_result.add_begin(str(buffer))
            else:
                buffer = result // 100  # pega só a parte inteira da divisão do numero salvo no result por 100
                result -= buffer * 100  # subtrai o result do valor salvo no buffer*100 e guarda em result
                if result // 10 == 0:  # se a parte inteira do result for 0
                    result = "0" + str(result)  # adiciona 0+ o que estiver em result
                doubly_list_result.add_begin(str(result))
                doubly_list_result.add_begin(str(buffer))
            if tail_result2 is not None:
                tail_result2 = tail_result2.prev
            tail2 = tail2.prev
        tail_result1 = doubly_list_result.end.prev if tail_result1 is None else tail_result1.prev
        tail1 = tail1.prev
    while not doubly_list_result.empty():
        num_result += doubly_list_result.pop_begin()
    num_result = "".join(num_result).lstrip('0')  # passa a lista pra string e retira zero a esquerda (leading zeros)
    return num_result
