from selenium import webdriver
import time


class Mywhatsapp:
    toWhome=""
    message=""
    def __init__(self,toWhome,message):
        self.toWhome=toWhome
        self.message=message
        

    
    def SendMessage(self):
        driver = webdriver.Chrome()
        driver.get('https://web.whatsapp.com/')
        
        print(f'To whom - {self.toWhome}')
        print(f'Message - {self.message}')
        myUsers=['xyx','Girishwani','abc','Bot']
        print(self.toWhome in myUsers)
        time.sleep(15)
        if self.toWhome in myUsers:
            
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(self.toWhome))
            user.click()
            
            
            message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
            message_box.send_keys(self.message)    
            
            message_box = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
            message_box.click()
            # driver.close()
        else : 
            return False 
        
        return True


# Mywhatsapp('Girishwani','.').SendMessage()
        




# input('Enter anything after scanning QR code')
# name="Girishwani"


# message_box = driver.find_element_by_xpath('//div[@class="_3uMse"]')
# message_box.send_keys('Tu bharla ka courseware ')

# # //*[@id="main"]/footer/div[1]/div[2]/div/div[2]

# # //*[@id="main"]/footer/div[1]/div[2]/div/div[1]

# message_box = driver.find_element_by_xpath('//button[@class="_1U1xa"]')
# message_box.click()

