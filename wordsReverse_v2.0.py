#��ת���ʣ�����I love China!" ��תΪChina! love I"��������Ҫ�����ո�
#˼·���Ƚ������ڷ�ת���ٽ������ַ�����ת

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
