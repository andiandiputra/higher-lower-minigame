import random
import data
from data import logo, vs
import os

def get_data(a):
    index1 = random.randint(0, len(a)-1)
    index2 = random.randint(0, len(a)-1)
    while index1 == index2:
        index2 = random.randint(0, len(a)-1)
    return a[index1], a[index2]

def used_data(a=None, b=None):
    if not hasattr(used_data, 'used_data_list'):
        used_data.used_data_list = []
    if a is not None and a not in used_data.used_data_list:
        used_data.used_data_list.append(a)
    if b is not None and b not in used_data.used_data_list:
        used_data.used_data_list.append(b)
    
    return used_data.used_data_list

def get_new_data(a, b):
    new_index = random.randint(0, len(a)-1)
    while a[new_index] == b or a[new_index] in used_data():
        new_index = random.randint(0, len(a)-1)
    return a[new_index]

def clear():
    os.system('cls')

def display_comparison(a, b):
    print(f"A : {a['name']}, {a['description']}, from {a['country']} ")
    print(vs)
    print(f"B : {b['name']}, {b['description']}, from {b['country']}")

def comparison(a, b, c):
    answer_a = a['follower_count'] > b['follower_count']
    answer_b = a['follower_count'] < b['follower_count']
    if c == "a" and answer_a:
        return True
    elif c == "b" and answer_b:
        return True
    else:
        return False

def play_game(data):
    scores = 0
    data1, data2 = get_data(data)
    used_data(data1, data2)
    print(logo)

    while True:
        
        display_comparison(data1, data2)
        answer = input('Which side has more follower? A or B :').lower()

        if answer == 'exit':
            break
        if comparison(data1, data2, answer):
            scores += 1
            clear()
            print(f"\nYou're correct, your current score is {scores}")
            if answer == 'a':
                data2 = get_new_data(data, data1)
            elif answer == "b":
                data1 = data2
                data2 = get_new_data(data, data1)
            

        else:
            print(f"\nYou lose, your last score is {scores} ")
            print(f"The answers were : \nA has {data1['follower_count']} followers \nB has {data2['follower_count']} followers")

            break

play_game(data.data)
