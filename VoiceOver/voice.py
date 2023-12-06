from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
number_of_drivers = int(input("Enter the number of drivers : " ))
time_to_refresh =10
url = 'https://www.youtube.com/watch?v=Ip_zMt5zEKE'
drivers =[]
for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(ChromeDriverManager().install()))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(number_of_drivers):
        drivers[i].refresh()