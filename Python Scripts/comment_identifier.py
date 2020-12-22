x = input('Comment : ')

l1 = x.split(' ')

print(l1)


for i in range(0, len(l1)):
    if 'fuck' or 'shit' or 'fck' or 'ass' or 'hole' in l1:
        l1[i] = l1[i].replace('fuck', '***')
        l1[i] = l1[i].replace('shit', '***')
        l1[i] = l1[i].replace('fck', '***')
        l1[i] = l1[i].replace('asshole', '***')
    else:
        pass


print(l1)

input("Press any key to close")
