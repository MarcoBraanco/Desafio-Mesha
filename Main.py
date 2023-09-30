from WebDev import InvoiceExtraction


invoiceExtraction = InvoiceExtraction()

tableData = invoiceExtraction.Start("https://rpachallengeocr.azurewebsites.net/")

print(tableData)