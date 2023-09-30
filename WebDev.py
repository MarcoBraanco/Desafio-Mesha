from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumActions:
        
    def startBrowser(self):
        self.driver = webdriver.Chrome()

    def OpenUrl(self, webUrl):
        self.driver.get(webUrl)

    def FindElement(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element
    
    def FindElements(self, xpath):
        element = self.driver.find_elements(By.XPATH, xpath)
        return element
    
class InvoiceExtraction:

    def __init__(self):
        self.elementsDic = {"mainTable" :       "//table[@id='tableSandbox']",
                            "pageButtons":      "//a[@class='paginate_button ']",
                            "pageButton" :      "//a[@data-dt-idx='{}']"}
        
        self.sel = SeleniumActions()

    def GetElement(self, element, formatValue = ""):
        if formatValue != "":
            return self.elementsDic[element].format(formatValue)
    
        return self.elementsDic[element]
        

    def Start(self, webUrl):
        self.sel.startBrowser()
        self.sel.OpenUrl(webUrl)
        self.GetTableValues()

    
    def CheckTotalPages(self):
        pageButtons = self.sel.FindElements(self.GetElement("pageButtons"))

        buttonText = pageButtons[-1].text

        return int(buttonText)

    
    def GetTableValues(self):
        tableElement = self.sel.FindElement(self.GetElement("mainTable"))
        tableValues = {}
        pageNumber = self.CheckTotalPages()
        for i in range(1, pageNumber+1):
            for row in tableElement.find_elements(By.TAG_NAME, "tr"):
                rowText = row.text.split()
                if rowText[0] == "#": continue
                tableValues[rowText[0]] = rowText[1:]

            if i == pageNumber:
                pageButton = self.sel.FindElement(self.GetElement("pageButton", formatValue=i))

            pageButton = self.sel.FindElement(self.GetElement("pageButton", formatValue=i+1))
            pageButton.click()
        
        return tableValues

class InputForm:
    def __init__(self):
        self.elementsDic = {"inputCompanyName" :       "//input[@ng-reflect-name='labelCompanyName']",
                            "inputPhoneNumber":      "//input[@ng-reflect-name='labelPhone']",
                            "inputLastName":      "//input[@ng-reflect-name='labelLastName']",
                            "inputFirstName":      "//input[@ng-reflect-name='labelFirstName']",
                            "inputAddress":      "//input[@ng-reflect-name='labelAddress']",
                            "inputRoleCompany":      "//input[@ng-reflect-name='labelRole']",
                            "inputEmail":      "//input[@ng-reflect-name='labelEmail']",
                            "buttonSubmit":     "//input[@type= 'submit']",
                            "textCongratulations": "//div[contains(@class, 'congratulations')]"}
        
        self.sel = SeleniumActions()

    def GetElement(self, element, formatValue = ""):
        if formatValue != "":
            return self.elementsDic[element].format(formatValue)

        return self.elementsDic[element]

    def FillForm(self, values):
        firstName = self.sel.FindElement(self.GetElement("inputFirstName"))
        firstName.text = "Marco"


teste = InvoiceExtraction()
teste.Start("https://rpachallengeocr.azurewebsites.net/")