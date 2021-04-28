import sys
import glob


EXTENTION = '.txt.wx'

def check(search,data,f):
    modified = data[:]
    if data.isnumeric():
        modified = data.replace(search,'',1)
        
    else:
        for i in range(1,len(data)):
            if data[i].isalpha() and data[i-1].isnumeric():
                print('here')
                modified = data[:i]+" "+data[i:]
    f.seek(0)
    f.truncate()
    f.write(modified)

def main():

    #cheking requirements given
    search = None
    path = None
    try:
        path = sys.argv[2]
        path = path+'/' if path[-1]!='/' else path
    except:
        path = ''
        print("checking on the current directory")

    try: 
        search = sys.argv[1]
    except:
        print("provide searching file")
        return


    #main function starts
    
    all_files = glob.glob('%s**/*%s'%(path,EXTENTION),recursive=True)
    for file in all_files:

        with open(file,'r+') as f:
            data = f.read()
            if search in data:
                check(search,data,f)

if __name__ == "__main__":
    main()