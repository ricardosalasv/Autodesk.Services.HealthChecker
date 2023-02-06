from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"

def main():

    services_status = {}
    
    driver = webdriver.Chrome(PATH)

    driver.get("https://health.autodesk.com")

    services = driver.find_elements(By.CLASS_NAME, "adsk-component")

    # Filter out elements that do not have "component-id" attribute
    services = list(filter(lambda x: x.get_attribute("component-id"), services))

    # Create a dictionary with the service name as key and the status as value
    for service in services:

        service_name = service.find_element(
            By.CLASS_NAME, "adsk-component-name"
        ).find_element(By.TAG_NAME, "a").text
        
        service_status = service.find_element(
            By.CLASS_NAME, "adsk-component-status"
        ).get_attribute("component-status")

        services_status[service_name] = service_status

    driver.quit()

    return services_status

if __name__ == "__main__":

    print(main())
