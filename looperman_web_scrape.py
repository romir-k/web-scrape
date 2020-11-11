import requests
import bs4
import smtplib

site = 'https://www.looperman.com/loops'
response = requests.get(site)
soup = bs4.BeautifulSoup(response.text, 'html.parser')

link_list = []

for div_class in soup.find_all('div', {'class': 'tag-wrapper'}):
    for trap in div_class.find_all('a', string="Trap Loops" or "Hip Hop Loops"):
        href_list = list(div_class)
        href_list_string = [str(item) for item in href_list]
        link = ""
        for i in range(0, len(href_list_string)):
            if "MB" in href_list_string[i] and "Drum Loops" not in href_list_string[i]:
                link = href_list[i].get('href')
                link_list.append(link)


def send_email(body):
    sender = 'rkf3686@gmail.com'
    receiver = 'rkf3686@gmail.com'
    loops = 'Loops'
    message = f'Subject: {loops}\n\n{body}'
    password = input('Enter your password: ')
    try:
        obj = smtplib.SMTP('smtp.gmail.com:587')
        obj.ehlo()
        obj.starttls()
        obj.login('rkf3686@gmail.com', password)
        obj.sendmail(sender, receiver, message)
        print('Email sent.')
        obj.quit()
    except smtplib.SMTPException:
        print('Email did not send.')


send_email(link_list)
