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
        self.wb.save(f"{self.currentPath}\\Data\\Invoice extraction data - {nowTimeStamp}.xlsx")


    def ReadExcel(self, file_path):

        self.wb = openpyxl.load_workbook(file_path)

        self.ws = self.wb.active
        data = {}
        for row in self.ws.iter_rows(min_row=2, values_only=True):
            chave = row[0]
            valores = list(row[1:])
            data[chave] = valores

        return data

teste = ExcelFunctions()

# dicTeste = {
#     '1': ['uh0cxfg6j2kx7gvktyrtn', '17-11-2023'],
#     '2': ['ag0c2uekmdqmxpp06qg66', '13-09-2023'],
#     '3': ['km23ab4siyfujnoc3lstma', '24-08-2023'],
#     '4': ['4rjy5cnxgkhph7md4cj837', '18-11-2023'],
#     '5': ['r0a3ygoq0joi28nswvszj', '17-10-2023'],
#     '6': ['0d0p9bezgdp74gx0kvh862r', '06-10-2023'],
#     '7': ['hsq959j2qcji12tbcoj7', '24-09-2023'],
#     '8': ['2ac0cf8ajht2roz6ia9sdr', '03-08-2023'],
#     '9': ['cncjglcaxrhb1d9uhfyrv7', '01-11-2023'],
#     '10': ['uv68e7r8kwsf45xe0erm', '17-09-2023'],
#     '11': ['guvmyv9y72shfq8ba5429d', '22-09-2023'],
#     '12': ['vrnoy6p3ur4ejvnjrzz06', '19-11-2023']
# }
# for chave, valor in dicTeste.items():
#     valor.extend([f'item1_{chave}', f'item2_{chave}', f'item3_{chave}', f'item4_{chave}', f'item5_{chave}', f'item6_{chave}', f'item7_{chave}', f'item8_{chave}'])


# teste.WriteExcel(dicTeste)

teste.ReadExcel(r"C:\Users\marco\Desktop\Desafio - Mesha\Desafio-Mesha\Data\Invoice extraction data - 30.09.2023 - 15h 33m 25s.xlsx")



