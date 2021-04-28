this solution is based on the following question:
    a) There are a number of files across directories, recursively.
    b) In all these directores, *.txt.wx files exist.
    c) a file may have entries such as numbers ranging from 0-9,  a the examples of    1) 0000000000000000000000000000, 800908090020805004080950809508809508095081010 or numb immediately followed by alphabets, as in 02mAvEyitam . This is structure across the directories.
    d) There are three aims to your program
        a) identify the NAME OF THE FILE THAT HAS GIVEN I NUMBERS (I HAVE A SEPARATFILE AS INPUT FILE THAT CONS OF THE INPUT FOR SEARCH)
        b) After identification of the name of the file, delete given input number(length of the numbers may range,  two, as in 00, to 5000, 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 ---------000000 from the given inpudirectory
        c) If the input file has a number immediately followe alphabets (withouspace), identify the name of the  and insert a single white space betweenumber alphabets, as  02 mAvEyitam.


you can run this by
    python3 <filename>.py <number to search> <directory to search>
if you run file in current directory then run
    python3 <filename>.py <number to search> <directory to search>

you can change the deleting option recursively by using following line in the line of 10
    modified = data.replace(search,'')

you change the extension by setting 
    EXTENTION = '.extention'