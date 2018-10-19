from genetic import knapsack
from Item import Item



def inputs():
    my_answers = []
    f = open("input.txt", "r")
    n_test_cases = int(f.readline())
    for i in range(n_test_cases):
        n_items = int(f.readline())
        # print(n_items+1)
        knapsack_size = int(f.readline())
        items = []
        for j in range(n_items):
            line = list(map(int, f.readline().split()))
            items.append(Item(line[0], line[1]))
        my_answers.append(knapsack(knapsack_size, items))
    return my_answers


def answers():
    f = open("output.txt", "r")
    return list(map(int, f.read().split()))


if __name__ == '__main__':
    right_answers = answers()
    my_answers = inputs()
    correct_cnt = 0
    for i in range(len(my_answers)):
        print("Right answer:", right_answers[i], "My answer:", my_answers[i].get_fitness(), end="")
        if right_answers[i] == my_answers[i].get_fitness():
            correct_cnt += 1
            print("👍")
        else:
            print()
        # my_answers[i].print_items()
    print(correct_cnt, "out of", len(my_answers), "correct", correct_cnt/len(my_answers) * 100, "%")
