# Author: Abdulhakim Haliru
# June, 2013.
# CTO @ Le Proghrammeen Solutions Ltd.
# http://www.leproghrammeen.com
# http://github.com/hakimkal
#scripting environment python
"""
A python script to extract phone numbers from text and csv files and convert into nigerian dialing code format for bulksms purpose.
e.g: 2348032123456
This python script has been tested on ubuntu linux 12.04  and windows 8
just call pntrimmer.py "phone.txt"

your file could have phone numbers in this format on each line
08023533208
8051650965
+2347031246878
*************

"""

import time , os , csv , sys , random
class Pne():
    
    
    def __init__(self,fn):
        self.fname = fn
         
        file_ext  = os.path.splitext(os.path.basename(self.fname))[1]
        """
        Get the file extension and call appropriate function
        """
        print str(self)
        if file_ext == '.csv' or file_ext == 'xls' or file_ext == ".xlsx":
            self.read_csv() #csvfile reader
        elif file_ext == '.txt':
            self.ofile(self.fname) #textfile reader
        else:
            print "Invalid file type specified"
            
    def read_csv(self):
        try:
            with open(self.fname, "rb") as freader:
                fcontent = csv.reader(freader, delimiter=" ")
                self.numholder = []
                for number in fcontent:
                    self.numholder.append("".join(number) + "\n")
        except IOError:
            print "Invalid CSV File specified!!!"

       

        self.create_text_file()
    
    
    
    def __str__(self):
        return repr("File: " + self.fname)
    
    
    def ofile(self, f):
        self.tf = f
        
        try:
            fl = open(self.tf,'r')
        except IOError:
            print "Invalid Text File specified!!!"
            sys.exit(1)
    
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
        if os.name  != 'nt':
            tod = str(time.strftime('%s')) + ".txt"
            
        else:
            tod = str(pow(random.random(),7)).split(".")
            tod = tod[1] + ".txt"

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
             elif n[0:3] == "234":
				 if len(n) == 14:
					 newfl.write(n) 
             #else:
                 #newfl.write(n)
        
        print "Your file has been extracted to the file \'" + tod + "\'"
        
        print "exiting script...."
        sys.exit(1)

def main(fn = None):
    if len(sys.argv) == 2:
        #print len(sys.argv)
        #p = Pne('arc.alhaji.csv')
        #p = Pne('chinyere_phone.txt')
        p = Pne(sys.argv[1])
        
    elif len(sys.argv) == 1 and fn != None:
        p = Pne(fn)
    else:
        
        print "No file specified for extraction and formatting to any Nigerian Telco Operator's network compatible Format!!!"
        sys.exit(1)

filename = None
if __name__ == "__main__":
    main(filename)
    
#1372023269
#1372023281
