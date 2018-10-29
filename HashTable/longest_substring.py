string = 'killingmachine'

def longest_substring_withM(string, m):
    count = 0
    index = 0
    table = {}
    Sum = 0
    Max_Sum = 0
    while index < len(string):
        if count <= m-1:
            table[string[index]] = index
            count += 1
            Sum += 1
        else:
            if string[index] in table:
                table[string[index]] = index
                Sum += 1
            else:
                change = min(table, key=table.get)
                print('change ',change)
                Max_Sum = max(Sum,Max_Sum)
                Sum = index - table[change]
                del(table[change])
                table[string[index]] = index
        index += 1
    Max_Sum = max(Sum,Max_Sum)
    return Max_Sum

print(longest_substring_withM(string,3))
