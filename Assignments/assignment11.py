import re

def main():
    
    file1 = open('output2.txt', 'w')
    
    date = f"08/19/2021"
    
    file1.write(date)
    
    print(file1)
    
    file1.close()
        
if __name__ == '__main__':
    main()