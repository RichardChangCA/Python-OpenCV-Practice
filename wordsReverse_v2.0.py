#反转单词，将“I love China!" 反转为China! love I"或其他，要包含空格
#思路，先将单词内反转，再将整个字符串反转

def wordRever(word, start, end):
    while start != end and start != end + 1:
        word[start], word[end] = word[end], word[start]
        start = start + 1
        end = end - 1

str = "   I love China!   Me too!"
li = []
for i in str:
    li.append(i)
j = 0
while j < len(li):
    if li[j] != ' ':
        for k in range(j, len(li)):
            if li[k] != ' ':
                end = k
            else:
                break
        wordRever(li,j,end)
        j = end + 1
    else: j = j + 1
li = reversed(li)
print("".join(li))
