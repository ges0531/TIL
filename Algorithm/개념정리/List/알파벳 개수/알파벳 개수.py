import sys

sys.stdin = open('input.txt', 'r')

S = input()
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print_list = [0]*len(alphabet_list)
for i in S:
    print_list[alphabet_list.index(i)] += 1
print(' '.join(map(str, print_list)))