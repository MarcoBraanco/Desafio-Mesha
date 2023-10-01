from WebDev import InvoiceExtraction, InputForm
from Excel import ExcelFunctions

class Main:
    def Run():
        invoiceExtraction = InvoiceExtraction()
        excelFunctions = ExcelFunctions()

        tableData = invoiceExtraction.Start("https://rpachallengeocr.azurewebsites.net/")


        if type(tableData) is not dict:
            excelFunctions.WriteLog(tableData, r"C:\Users\marco\Desktop\Desafio - Mesha\Desafio-Mesha\Logs\Logs robo MESHA.txt")


        filePath = excelFunctions.WriteExcel(tableData)

        dataFromExcel = excelFunctions.ReadExcel(filePath)

        inputForm = InputForm()

        updateItemStatus = inputForm.Start("https://rpachallenge.com/", dataFromExcel)

        for chave, valor in updateItemStatus.items():
            excelFunctions.UpdateStatusExcel(chave, filePath, valor)

        excelFunctions.CheckStatus(filePath)