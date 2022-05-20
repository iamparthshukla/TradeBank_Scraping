from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
from time import sleep

PATH = "/Users/parth/PycharmProjects/TradeBank_Scraping/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://tradestat.commerce.gov.in/eidb/icntcomq.asp")

# final dataframe

df_Final = pd.DataFrame()

# list of countries
countries = driver.find_elements_by_xpath('//*[@id="select3"]/option')
countries_list = []
for i in range(len(countries)):
    countries_list.append(countries[i].text)
# print(countries_list)

# actions
for country in countries_list:
    hsLevel = Select(driver.find_element_by_id("hslevel"))          # 8-digit HSCode
    allEntriesButton = driver.find_element_by_id("radioDAll")       # all-entries button
    select = Select(driver.find_element_by_id("select3"))           # country selection
    submitButton = driver.find_element_by_id("button1")             # submit button
    usdButton = driver.find_element_by_id("radiousd")             # USD button
    # debugging
    # print("Selecting Main Menu Values")
    sleep(1)
    select.select_by_visible_text(country)
    hsLevel.select_by_visible_text('8 Digit Level')
    allEntriesButton.click()
    usdButton.click()
    submitButton.click()

    sleep(2)


    # print("Selecting Table Values")
    hsCode = driver.find_elements_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[2]/font")
    commodity = driver.find_elements_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[3]/font")
    data1 = driver.find_elements_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[4]/font")
    data2 = driver.find_elements_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[5]/font")
    data3 = driver.find_elements_by_xpath("/html/body/div/div[2]/div/table/tbody/tr/td[6]/font")

    result_list = []

    for i in range(len(data2) - 1):                                   # -1 so that 'total' row is excluded
        temp = {'HSCode': hsCode[i].text,
                'Commodity': commodity[i].text,
                '2020-2021': data1[i].text,
                '2021-2022(Apr-Feb)': data2[i].text,
                '%Growth': data3[i].text,
                'Country': country}
        result_list.append(temp)
    df_data = pd.DataFrame(result_list)
    df_Final = df_Final.append(df_data)

    # debugging
    # print(df_Final)
    # print("One iteration complete.")

    driver.back()

df_Final.to_excel('Imports_TradeBank_Scraping.xlsx', index=False)

# print("S.No   "+"HSCode   "+"Commodity   "+"2020-2021   "+"2021-2022(Apr-Feb)   "+"%Growth")



