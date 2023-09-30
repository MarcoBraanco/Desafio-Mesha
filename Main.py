from WebDev import InvoiceExtraction, InputForm
from Excel import ExcelFunctions


invoiceExtraction = InvoiceExtraction()

tableData = invoiceExtraction.Start("https://rpachallengeocr.azurewebsites.net/")

excelFunctions = ExcelFunctions()

filePath = excelFunctions.WriteExcel(tableData)

dataFromExcel = excelFunctions.ReadExcel(filePath)

inputForm = InputForm()

inputForm.Start("https://rpachallenge.com/", dataFromExcel)