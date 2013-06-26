# Author: Abdulhakim Haliru
# June, 2013.
# CTO @ Le Proghrammeen Solutions Ltd.
# http://www.leproghrammeen.com
# http://github.com/hakimkal
#scripting environment python
"""
A python script to extract phone numbers from text and csv files and convert into nigerian dialing code format for bulksms purpose.
e.g: 2348032123456
This python script has been tested on ubuntu linux 12.04  and windows
just call pntrimmer.py "phone.txt"

your file could have phone numbers in this format on each line
08023533208
8051650965
+2347031246878
*************

"""

import time , os , csv , sys
class Pne():
    
    
    def __init__(self,fn):
        self.fname = fn
         
        file_ext  = os.path.splitext(os.path.basename(self.fname))[1]
        """
        Get the file extension and call appropriate function
        """
        if file_ext == '.csv' or file_ext == 'xls' or file_ext == ".xlsx":
            self.read_csv() #csvfile reader
        elif file_ext == '.txt':
            self.ofile(self.fname) #textfile reader
        else:
            print "Invalid file type specified"
            
    def read_csv(self):
        
        with open(self.fname, "rb") as freader:
            fcontent = csv.reader(freader, delimiter=" ")
            self.numholder = []
            for number in fcontent:
                self.numholder.append("".join(number) + "\n")
            self.create_text_file()
    
    
    
    def __str__(self):
        return repr(os.path.splitext(os.path.basename(self.fname))[1])
    
    
    def ofile(self, f):
        self.tf = f
        fl = open(self.tf,'r')
        print "Reading " +  self.tf + "..."
       
        self.numholder = [] 
        for number in fl:
            if number != None:
                self.numholder.append(number)
        
        self.create_text_file()
     
     
                 
    """
    create text file with timestamp  and write the numbers in correct format of 234
    """             
    
    def create_text_file(self):
        
        #for v in  set(self.numholder):
            #print len(v) , v
        tod = time.strftime('%s') + ".txt"
        newfl = open(tod,"a+")
        
        #print tod
        for n in set(self.numholder):
             if n.startswith("0") :
                #print n
                d = "234" + n[1:]
                #print len(d) , d
                if len(d) == 14:
                    newfl.write(d)
             elif n.startswith("+"):
                 #print len(n) , n[1:]
                 if len(n[1:]) == 14 :
                     newfl.write(n[1:])
                     
             elif n.startswith("8"):
                 d = "234"+n
                # print len(d) , d
                 if len(d) == 14 :
                     newfl.write(d)    
             #else:
                 #newfl.write(n)
        
        print "Your file has been extracted to the file \'" + tod + "\'"
        
        print "exiting script...."
        sys.exit(1)

def main():
    if len(sys.argv) == 2:
        #print len(sys.argv)
        p = Pne(sys.argv[1])
    else:
        
        print "No file specified for extraction and formatting to any Nigerian Telco Operator's network compatible Format!!!"
        sys.exit(1)


if __name__ == "__main__":
    main()
    
#1372023269
#1372023281