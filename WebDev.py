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
    

    def QuitDriver(self):
        self.driver.quit()  
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
        tablevalues = self.GetTableValues()
        self.sel.QuitDriver()
        return tablevalues


    
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
                tempValues = ["Marco", "Branco", "mesha. techonolgy",
                              "RPA Developer (Python)", "marco.branco@somosmesha.com",
                              "Ribeirao Preto - SP", "16 997561188"]
                
                tableValues[rowText[0]].extend(tempValues)

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
                            "textCongratulations": "//div[contains(@class, 'congratulations')]",
                            "startButton": "//button[text()='Start']"}
        
        self.sel = SeleniumActions()

    def Start(self, webUrl, values):
        self.sel.startBrowser()
        self.sel.OpenUrl(webUrl)
        self.FillForm(values)
    

    def GetElement(self, element, formatValue = ""):
        if formatValue != "":
            return self.elementsDic[element].format(formatValue)

        return self.elementsDic[element]

    def FillForm(self, values):
        startButton = self.sel.FindElement(self.GetElement("startButton"))
        startButton.click()



        for chave, valor in values.items():

            try:
                finishedText = self.sel.FindElement(self.GetElement("textCongratulations"))
                break
            except:
                pass

            firstName = self.sel.FindElement(self.GetElement("inputFirstName"))
            firstName.send_keys(valor[2])
            
            lastName = self.sel.FindElement(self.GetElement("inputLastName"))
            lastName.send_keys(valor[3])

            company = self.sel.FindElement(self.GetElement("inputCompanyName"))
            company.send_keys(valor[4])

            roleCompany = self.sel.FindElement(self.GetElement("inputRoleCompany"))
            roleCompany.send_keys(valor[5])
            
            email = self.sel.FindElement(self.GetElement("inputEmail"))
            email.send_keys(valor[6])

            address = self.sel.FindElement(self.GetElement("inputAddress"))
            address.send_keys(valor[7])

            phoneNumber = self.sel.FindElement(self.GetElement("inputPhoneNumber"))
            phoneNumber.send_keys(valor[8])

            buttonSubmit = self.sel.FindElement(self.GetElement("buttonSubmit"))
            buttonSubmit.click()