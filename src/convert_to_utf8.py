import sys
def main():

    with open(sys.argv[1],'rb') as f:
        lines = f.read()
    decodedData = lines.decode('ISO-8859-1')
    with open(sys.argv[2],'w') as e:
        e.write(decodedData)

if __name__ == '__main__':
    main()
