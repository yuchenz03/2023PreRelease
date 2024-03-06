graph = {
'A': ('C','B'),
'B': ('A','C','D','E'),
'C': ('A','B','F','D'),
'D': ('C','E','B','H'),
'E': ('B','D'),
'F': ('C','G'),
'G': ('F',),
'H': ('D',)
}
for i in graph.keys():
    print(i)
    
print("?".isalpha())
print("hello"[:-1])
hello = "word"
hello.upper()
print(hello.upper())