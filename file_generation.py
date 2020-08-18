#! /usr/bin/env python3

# generate of file

def main():
    # open a file for writing and create it if it does not exist
    f = open('newfile001.txt', 'w+')

# write some lines of data in teh file

for i in range(20):
    f.write("This is line %d\r\n" % (i+1))

f.close()


if __name__ == "__main__":
    main()

    
