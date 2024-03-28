import os
import subprocess
from pathlib import Path
import subprocess
class PenroseArray:
    #Holds array
    def __init__(self, array):
        self.array = array

    def generate_substance(self, file_name):
        #Get the absolute path of the file
        file_path = os.path.abspath(file_name)
        # if not os.path.isfile(file):
        #     raise FileNotFoundError
        length = len(self.array) - 1
        #the Initial lines that declare the array, elements, and predicates
        initial_variables = ["Array a_1 \n",
                             "Element e_i for i in [0,"+str(length)+"] \n",
                             "Index i_j for j in [0,"+str(length)+"] \n",
                             "IndexOf(e_j, i_j) for j in [0,"+str(length)+"] \n",
                             "In(e_i, a_1) for i in [0,"+str(length)+"] \n"]
        #Open the file for overwriting
        f = open(file_name, "w")
        #Write the inital variables
        f.writelines(initial_variables)
        #Write the element labels
        i_labels, e_labels = self.create_labels()
        f.writelines(i_labels)
        f.writelines(e_labels)
        f.close()

    def penrose_stack(self, file_name):
        #Run generate in case it has not been run yet
        self.generate_substance(file_name)
        #Store length for use in string creation
        length = len(self.array)
        #Open file for appending, most of it already written by generate
        f = open(file_name, "a")
        f.write("Top(e_"+str(length-1)+", i_"+str(length-1)+")\n")
        f.close()
        command = "npx @penrose/roger trio domain/array.domain style/stack.style stack_test.substance > stack_test.svg"

        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        # Print the output
        print("Command output:", result.stdout)        

    #this function highlights the middle index/indices for display in binary search
    def binary_search(self, file_name):
        #Run generate in case it has not been run yet
        self.generate_substance(file_name)
        #Store length for use in string creation
        length = len(self.array)
        #Open file for appending, most of it already written by generate
        f = open(file_name, "a")
        middle = length/2
        #Even length array
        if length%2 == 0:
            
            f.writelines([
                "Middle(e_"+str(int(middle-1))+","+"i_"+str(int(middle-1))+")\n",
                "Middle(e_"+str(int(middle))+","+"i_"+str(int(middle))+")\n"
            ])
        #Odd length array
        else:
            f.write("Middle(e_"+str(int(middle-.5))+","+"i_"+str(int(middle-.5))+")\n")
        f.close()


    def create_labels(self):
        #Declare empty arrays to fill with strings
        i_labels = [None]*len(self.array)
        e_labels = [None]*len(self.array)
        for i in range(len(self.array)):
            i_labels[i] = "Label i_"+str(i)+" $"+str(i)+"$\n"
        for i in range(len(self.array)):
            e_labels[i] = "Label e_"+str(i)+" $"+str(self.array[i])+"$\n"
        #Return an array for both index labels and element labels
        return i_labels, e_labels    
        
def main():
    array = [1, "Hello", "wooraaaaa", 3]
    example = PenroseArray(array)
    example.penrose_stack("stack_test.substance")
    
        

main()