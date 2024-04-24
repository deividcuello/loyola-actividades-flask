from app import app

# from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, session


@app.route('/')
@app.route('/index')
def index():
     
    # username_input = input('Usuario: ')
    # pwd_input = input('Password: ')
    # # create webdriver object
    # driver = webdriver.Firefox()
    # # get google.co.in
    # driver.get("https://campusvirtual.ipl.edu.do/psp/cs92pro/?cmd=login&languageCd=ESP&")


    # username = driver.find_element(By.ID,"userid")
    # password = driver.find_element(By.ID,"pwd")
    # continue_button = driver.find_element(By.XPATH, value="//input[@value='Conectar']")

    # print(username_input)
    # print(pwd_input)
    # username.send_keys(username_input)
    # password.send_keys(pwd_input)
    # continue_button.click()
    # # time.sleep(5)

    # student_center = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.ID, 'SCC_TASKAPP_WRK_PTGP_TILE_LIVDAT_2'))
    #     )                                           
    # # student_center = driver.find_element(By.ID,"win0groupletPTNUI_LAND_REC_GROUPLET$9")
    # student_center.click()
    # time.sleep(5)
    # soup = BeautifulSoup(driver.page_source, 'html.parser')

    # data = []

    # tasks = soup.find_all('table')[1]
    # for task in tasks.find_all("tr", {"class": "psc_rowact"}):
    #     name = (task.find("a", {"class": "ps-link"}).getText())
    #     status = (task.find("td", {"class": "STATUS"}).find("span", {"class": "ps_box-value"}).getText())
    #     data.append({'name': name, 'status': status})

#     data = [{'name': '1er Seminario', 'status': 'Finalizado'},
# {'name': '1era Actividad Cocurricular', 'status': 'Finalizado'},
# {'name': '1era Vista Técnica', 'status': 'Finalizado'},
# {'name': '2da Actividad Cocurricular', 'status': 'Finalizado'},
# {'name': '2da Visita Técnica', 'status': 'Finalizado'},
# {'name': '2do Seminario', 'status': 'Iniciado'},
# {'name': '400 Horas de Pasantía', 'status': 'Iniciado'},
# {'name': '8 Niveles de inglés', 'status': 'Finalizado'},
# {'name': 'Proyectos integradores', 'status': 'Finalizado'},
# {'name': 'Seminario de Empredimiento', 'status': 'Finalizado'}]


    # user = {'username': 'Miguel'}

    # data = [{'name': '1er Seminario', 'status': 'Finalizado'},
    #             {'name': '1era Actividad Cocurricular', 'status': 'Finalizado'},
    #             {'name': '1era Vista Técnica', 'status': 'Finalizado'},
    #             {'name': '2da Actividad Cocurricular', 'status': 'Finalizado'},
    #             {'name': '2da Visita Técnica', 'status': 'Finalizado'},
    #             {'name': '2do Seminario', 'status': 'Iniciado'},
    #             {'name': '400 Horas de Pasantía', 'status': 'Iniciado'},
    #             {'name': '8 Niveles de inglés', 'status': 'Finalizado'},
    #             {'name': 'Proyectos integradores', 'status': 'Finalizado'},
    #             {'name': 'Seminario de Empredimiento', 'status': 'Finalizado'}]
                
    # return render_template("index.html", len = len(data), data = data)  
    return render_template("index.html")  


@app.route('/actividades', methods=['POST'])
def calculate():
    if request.method == 'POST':
        # data = [{'name': '1er Seminario', 'status': 'Finalizado'},
        #         {'name': '1era Actividad Cocurricular', 'status': 'Finalizado'},
        #         {'name': '1era Vista Técnica', 'status': 'Finalizado'},
        #         {'name': '2da Actividad Cocurricular', 'status': 'Finalizado'},
        #         {'name': '2da Visita Técnica', 'status': 'Finalizado'},
        #         {'name': '2do Seminario', 'status': 'Iniciado'},
        #         {'name': '400 Horas de Pasantía', 'status': 'Iniciado'},
        #         {'name': '8 Niveles de inglés', 'status': 'Finalizado'},
        #         {'name': 'Proyectos integradores', 'status': 'Finalizado'},
        #         {'name': 'Seminario de Empredimiento', 'status': 'Finalizado'}]
        username_input = str(request.form.get('username', 0))
        password_input = str(request.form.get('password', 0))


        options = FirefoxOptions()
        options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.get("https://campusvirtual.ipl.edu.do/psp/cs92pro/?cmd=login&languageCd=ESP&")


        username = driver.find_element(By.ID,"userid")
        password = driver.find_element(By.ID,"pwd")
        continue_button = driver.find_element(By.XPATH, value="//input[@value='Conectar']")

        username.send_keys(username_input.strip())
        password.send_keys(password_input)
        continue_button.click()
        # time.sleep(5)

        try:
            student_center = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'SCC_TASKAPP_WRK_PTGP_TILE_LIVDAT_2'))
            ) 

        except:      
            return render_template('index.html', len = 0, data = [], is_data=False)                                  
        # student_center = driver.find_element(By.ID,"win0groupletPTNUI_LAND_REC_GROUPLET$9")
        student_center.click()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        data = []

        tasks = soup.find_all('table')[1]
        for task in tasks.find_all("tr", {"class": "psc_rowact"}):
            name = (task.find("a", {"class": "ps-link"}).getText())
            status = (task.find("td", {"class": "STATUS"}).find("span", {"class": "ps_box-value"}).getText())
            data.append({'name': name, 'status': status})

        driver.quit()
        print('data es',data)
        # data_results = data
        # session['data_results'] = data_results
        # session['username'] = username
        # session['password'] = password

        return render_template('index.html', len = len(data), data = data, is_data=True)