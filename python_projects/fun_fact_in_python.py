import json
import requests
import os
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    os.system('cls')
    put_html(
            '<p align="left">'
            '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
            '</p>'
        )

    url = "https://uselessfacts.jsph.pl/random.json?language=en"

    responce=requests.get(url).text

    fact=json.loads(responce)['text']

    style(put_text(fact), 'color:blue; font-size: 30px')

    put_buttons(
            [dict(label='Click me', value='outline-success', color='outline-success')],
            onclick=get_fun_fact
        )


if __name__ == '__main__':
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    hold()
    