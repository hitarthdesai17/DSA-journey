s="bcieigvufyrecb"
set1=set()
for i in s:
    if i not in set1:
        set1.add(i)
    else: print (i)

def first_letter(s):
    map={}
    for ch in s:
            map[ch]=map.get(ch,0)+1
            if(map[ch]==2):
                return(ch)
    return(None)
print(first_letter(s))
        