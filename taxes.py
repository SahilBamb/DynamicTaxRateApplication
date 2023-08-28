import requests
from bs4 import BeautifulSoup


def getTaxInfo():
    # Make a request to the website
    response = requests.get('https://www.nerdwallet.com/article/taxes/state-income-tax-rates')

    # Parse the HTML response
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table you want to scrape
    table = soup.find('table')

    # Find all the rows in the table
    rows = table.find_all('tr')


    data_list = []
    pos_states = []
    for row in rows[:-1]:
        cells = row.find_all("td")
        data = {}
        if cells:
            for i in range(len(cells)):
                if (i == 0): pos_states.append(cells[i].text.strip())
                data["column"+str(i)+"_header"] = cells[i].text.strip()
            data_list.append(data.copy())

    final_dict = {
        "table_data": data_list
    }

    pos_states = pos_states[:-1]
    return (pos_states, final_dict)

def getStates():
    return getTaxInfo()[0]

def getAllInfo():
    return getTaxInfo()[1]

def getStateInfo(state):
    allInfo = getAllInfo()
    for info in allInfo['table_data']:
        if info['column0_header'] == state:
            return info
    else:
        return {"column0_header" : "No Info Available"}


type(getStateInfo('Alaska'))
