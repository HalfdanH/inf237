import sys
import math
n, k, q = map(int, sys.stdin.readline().split())




def real():

    for i in range(q):
        u, v = map(int, sys.stdin.readline().split())
        u_copy = u
        v_copy = v
        u_depth = 0
        while u != 1:
            u = (u-2)//(k)+1
            u_depth += 1
            

        v_depth = 0
        while v != 1:
            v = (v-2)//(k)+1
            v_depth += 1
            



        steps = 0
        while u_depth != v_depth:
            if  v_depth > u_depth:
                v_copy = (v_copy-2)//(k)+1#(v_copy+2)//(k+1)
                v_depth -=1

            
            if  u_depth > v_depth:
                u_copy = (u_copy-2)//(k)+1
                u_depth -=1
        

            steps += 1
        #print(v_copy, u_copy)
        while u_copy != v_copy:
            u_copy = (u_copy-2)//(k)+1
            v_copy = (v_copy-2)//(k)+1
            steps+= 2
        
        print(steps)

real()
