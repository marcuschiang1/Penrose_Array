import os
from pathlib import Path
import subprocess
class PenroseArray:
    def __init__(self, array):
        self.array = array

    def generate_substance(self, file_name):
        file_path = os.path.abspath(file_name)
        # if not os.path.isfile(file):
        #     raise FileNotFoundError
        length = len(self.array) - 1
        initial_variables = ["Array a_1 \n",
                             "Element e_i for i in [0,"+str(length)+"] \n",
                             "Index i_j for j in [0,"+str(length)+"] \n",
                             "IndexOf(e_j, i_j) for j in [0,"+str(length)+"] \n",
                             "In(e_i, a_1) for i in [0,"+str(length)+"] \n"]
        f = open(file_name, "w")
        f.writelines(initial_variables)
        i_labels, e_labels = self.create_labels()
        f.writelines(i_labels)
        f.writelines(e_labels)
        f.close()

    def binary_search(self, file_name):
        self.generate_substance(file_name)
        length = len(self.array)
        f = open(file_name, "a")
        middle = length/2
        #Even length array
        if length%2 == 0:
            
            f.writelines([
                "Middle(e_"+str(int(middle-1))+","+"i_"+str(int(middle-1))+")\n",
                "Middle(e_"+str(int(middle))+","+"i_"+str(int(middle))+")"
            ])
        #Odd length array
        else:
            f.write("Middle(e_"+str(int(middle-.5))+","+"i_"+str(int(middle-.5))+")")
        f.close()


    def create_labels(self):
        i_labels = [None]*len(self.array)
        e_labels = [None]*len(self.array)
        print(i_labels)
        for i in range(len(self.array)):
            i_labels[i] = "Label i_"+str(i)+" $"+str(i)+"$\n"
        for i in range(len(self.array)):
            e_labels[i] = "Label e_"+str(i)+" $"+str(self.array[i])+"$\n"
        return i_labels, e_labels    
        
def main():
    array = [1,"hi",3, 4]
    example = PenroseArray(array)
    example.binary_search("binary_search.substance")
    print(array)
    
        

main()