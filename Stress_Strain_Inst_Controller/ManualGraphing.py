from matplotlib import pyplot as plt
import pandas as pd
import sys
import os

def process_arg():
    arg = sys.argv

    filename = ""

    if len(arg)>1:
        filename = arg[1]
    return filename

def get_data(filename):
    data = None
    while data == None:
        if not filename.endwith(".xlsx"):
            print("File is not excel.")
            filename = input("Excel filename: ")
            continue
        try:
            data = pd.read_excel(filename)
        except:
            print("Error: file not working!")
            filename = input("Excel filename: ")
            data = None

    return data

def xy_data(data):
    columns = data.columns

    sel_col = []

    while True:
        print(columns)
        columns_txt = input("Pick two columns (A[x-axis], B[y-axis]): ")
        sel_col = columns_txt.split(sep = ", ")

        if len(sel_col) != 2:
            print("Invalid: two columns not picked.")
            continue
    
        valid_col = True

        for col in sel_col:
            if col not in columns:
                valid_col = False
                break
    
        if not valid_col:
            continue
    
        return sel_col, data[sel_col].to_numpy()

def main(filename):
    fn = filename
    while True:
        data = get_data(fn)
        col, xy = xy_data(data)
        plt.xlabel(col[0])
        plt.ylabel(col[1])
        plt.plot(xy)
        plt.show()

        again = ""
        while True:
            again = input("Again?(y/n)")
            if again == "y":
                break
            elif again == "n":
                return
            else:
                continue
        
        plt.close()

        fn = input("Excel filename: ")

        


filename = process_arg()
main(filename)



        


