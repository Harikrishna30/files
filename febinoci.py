def febi1(n):
     a = 0
     b = 1
     while(a < n):
             print(a,end = ' ')
             a = b
             b = a + b
     print()
febi1(1000)
