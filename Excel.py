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
        
        for chave, valor in data.items():
            valor.extend([f'item1_{chave}', f'item2_{chave}', f'item3_{chave}', f'item4_{chave}', f'item5_{chave}', f'item6_{chave}', f'item7_{chave}',f'item8_{chave}'])


        headerRow = [self.columnNames[col] for col in range(1, len(self.columnNames) + 1)]
        self.ws.append(headerRow)


        for chave, valor in data.items():
            self.ws.append([chave] + valor)


        nowTimeStamp = datetime.now().strftime("%d.%m.%Y - %Hh %Mm %Ss")
        self.wb.save(f"{self.currentPath}\\Data\\Invoice extraction data -{nowTimeStamp}.xlsx")