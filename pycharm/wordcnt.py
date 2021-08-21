f1 = open("C:/Users/dlwpg/oneDrive/바탕 화면/스터디/count_example.txt",'r')
lines = f1.readlines()
f2 = open("C:/Users/dlwpg/oneDrive/바탕 화면/스터디/wordcount.txt",'w')
sum_word =0
different_word =[]
dic_word = {}
count = 1
for a in range(0,len(lines)):
    value = lines[a].split(' ')
    if value[len(value)-1] is '\n':
        value.pop()
    sum_word +=len(value)
    for b in range(0,len(value)):
        different_word.append(value[b])

for a in range(0,len(different_word)):
    for b in range(1, len(different_word)):
            if different_word[a] is different_word[b]:
                count +=1
    dic_word[different_word[a]]=count
    count=1

print(different_word)
print(sum_word)
print(dic_word)