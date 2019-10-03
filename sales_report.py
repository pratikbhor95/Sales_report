
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

import pandas as pd
import xlrd

filename = input("enter the name of excel sheet")
Data1 = pd.read_excel((filename+".xlsx"),sheet_name=0,header=0)



df1 = DataFrame(Data1)
x = df1.iloc[:,0]
y = df1.iloc[:,-1]



with PdfPages('charts1.pdf') as export_pdf:

        plt.scatter(x,y, color='green')
        plt.title('sales per day', fontsize=10)
        plt.xlabel('Date', fontsize=8)
        plt.xticks(fontsize = 5, rotation='vertical')
        plt.ylabel('Sales', fontsize=8)
        plt.grid(True)
        export_pdf.savefig()
        plt.close()
              
        plt.plot(x,y, color='red', marker='o')
        plt.title('Sales per Day', fontsize=10)
        plt.xlabel('Date', fontsize=8)
        plt.xticks(fontsize = 5, rotation='vertical')
        plt.ylabel('Sales', fontsize=8)
        plt.grid(True)
        export_pdf.savefig()
        plt.close()
        

