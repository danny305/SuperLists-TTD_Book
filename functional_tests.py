from selenium import webdriver


browser =webdriver.Firefox()

try:
    response = browser.get('http://localhost:8000')
    assert 'Django' in browser.title
    print('Congrats a Django web app opened on FireFox!!')


except:
    print('Django website did not open')

