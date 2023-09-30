import openpyxl
from datetime import datetime
import os

class ExcelFunctions:
    def __init__(self):
        self.columnNames = {1:"ID", 2: "Invoice Number", 3:"invoice Date", 4:"First Name", 5:"Last Name",
                6:"Company Name", 7:"Role in Company", 8:"Email", 9:"Address", 10: "Phone Number"}
        self.currentPath = os.getcwd()
        print("teste")
        
        
    def CreateExcel(self):
        self.wb = openpyxl.Workbook()
        self.ws = self.wb.active
        self.ws.title = "Invoice Data"

    
    def WriteExcel(self, data):
        self.CreateExcel()

        headerRow = [self.columnNames[col] for col in range(1, len(self.columnNames) + 1)]
        self.ws.append(headerRow)


        for chave, valor in data.items():
            self.ws.append([chave] + valor)


        nowTimeStamp = datetime.now().strftime("%d.%m.%Y - %Hh %Mm %Ss")
        filePath = f"{self.currentPath}\\Data\\Invoice extraction data - {nowTimeStamp}.xlsx"
        self.wb.save(filePath)

        return filePath


    def ReadExcel(self, file_path):

        self.wb = openpyxl.load_workbook(file_path)

        self.ws = self.wb.active
        data = {}
        for row in self.ws.iter_rows(min_row=2, values_only=True):
            chave = row[0]
            valores = list(row[1:])
            data[chave] = valores

        return data