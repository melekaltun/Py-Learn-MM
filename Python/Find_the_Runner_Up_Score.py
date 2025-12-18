import sys

if __name__ == '__main__':
    n = int(input())
  
    if 2 <= n <= 10:
        A = list(map(int, input().split()))
      
        if len(A) != n:
            sys.exit() 
          
        for x in A:
            if not (-100 <= x <= 100):
                sys.exit()
              
        sorted_unique_list = sorted(list(set(A)))

        if len(sorted_unique_list) >= 2:
            print(sorted_unique_list[-2])
        else:
            pass
