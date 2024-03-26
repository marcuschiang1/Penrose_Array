import os
from pathlib import Path
class PenroseArray:
    def __init__(self, array):
        self.array = array

    def generate(self, file_name):
        file_path = os.path.abspath(file_name)
        # if not os.path.isfile(file):
        #     raise FileNotFoundError
        length = len(self.array) - 1
        initial_variables = ["Array a_1 \n",
                             "Element e_i for i in [0,"+str(length)+"] \n",
                             "Index i_j for j in [0,"+str(length)+"] \n",
                             "IndexOf(e_j, i_j, j) for j in [0,"+str(length)+"] \n",
                             "In(e_j, a_1) for i in [0,"+str(length)+"] \n"]
        f = open(file_name, "w")
        f.writelines(initial_variables)
        i_labels, e_labels = self.create_labels()
        f.writelines(i_labels)
        f.writelines(e_labels)
    
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
    array = [10,"hello","wdd",50000,50,60,70,80]
    example = PenroseArray(array)
    example.generate("test2.substance")
    print(array)
    
        

main()