from selenium import webdriver
import time
import unittest
from selenium.webdriver import  Chrome, ChromeOptions
import smtplib
from email.mime.multipart import MIMEMultipart
from  email.mime.text import MIMEText
class Send_email:
    message = MIMEMultipart()
    message['From'] = 'medvedepam@gmail.com'
    message['To'] = 'testmybrain@mailinator.com'
    message['Subject'] = 'For test'

    body = ('This is body')
    body = MIMEText(body)
    smtpobj = smtplib.SMTP('smtp.gmail.com',587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    message.attach(body)
    smtpobj.login('medvedepam@gmail.com', 'qscesz123')
    smtpobj.sendmail('medvedepam@gmail.com', 'testmybrain@mailinator.com', message.as_string())

class test_MailTest(unittest.TestCase):

        def setUp(self):
            opts = ChromeOptions()
            opts.add_experimental_option("detach", True)

            self.driver = webdriver.Chrome('C:/Users/medbo/Downloads/chromedriver_win32/chromedriver.exe',options=opts)
            self.driver.get("https://www.mailinator.com/")

        def test_Check(self) :
            driver = self.driver
            email = driver.find_element_by_id("inboxfield")
            email.send_keys('testmybrain')
            subm = driver.find_element_by_xpath("//div[@class='input-group']/span")
            subm.click()
            froms = driver.find_element_by_xpath("//td[3]")
            subj = driver.find_element_by_xpath("//td[4]")
            actualfrom = froms.text
            actualsubject = subj.text
            froms.click()

            time.sleep(3)
            driver.switch_to.frame(driver.find_element_by_id("msg_body"))
            body = driver.find_element_by_xpath("//body").text


            assert actualfrom == "medvedepam@gmail.com"
            assert actualsubject == "For test"
            assert ("This is body" in body)


        def tearDown(self):
          self.driver.quit()

if  __name__ == "__main__":
        unittest.main()



