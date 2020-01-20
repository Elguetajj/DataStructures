# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup 
from flask import Flask, request, jsonify


def calculateFuel(arr):
    total = 0
    for i in arr:
        total += (int(i)//3)-2
    return total


# options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir=C:\\Users\\elgue\\AppData\\Local\\Google\\Chrome\\User Data")
# options.add_argument("user-")
# driver = webdriver.Chrome('C:/Users/elgue/chromedriver.exe', options=options)

# driver.get("https://adventofcode.com/2019/day/1/input")
# content = driver.page_source
# soup = BeautifulSoup(content, features='html.parser')

# print (soup.text)

# inputarr = soup.text.split('\n')
# inputarr.remove('')
# print(inputarr)
# print(calculateFuel(inputarr))

app = Flask(__name__)

@app.route('/fuel', methods= ['POST'])
def home():
    data = request.get_json(force=True)
    return jsonify({'fuelNeeded': calculateFuel(data['load'])})



if __name__ == "__main__":
    app.run(debug=True,port=8080)