#!/usr/bin/env python
import sys
def printLine(s,i,i2):
    print '%s\t%s' % (s,i*100/i2)

def main():
    old_key = ""
    score = 0
    num_msg = 0
    
    for line in sys.stdin:
        
        key, value = line.strip().split('\t', 1)
        if old_key != key and old_key != "":
            printLine(old_key,score,num_msg)
            score = 0
            num_msg = 0 

        old_key = key
        score += int(value)
        num_msg += 1

    printLine(old_key,score,num_msg)

if __name__ == '__main__':
    main()
    

    