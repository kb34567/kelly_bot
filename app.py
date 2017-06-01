import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '386505229:AAFAZ1vmnCFho8KyK7w0RIqbMGcoCe2u6Mg'
WEBHOOK_URL = 'https://d941699a.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'garbage',
        'taichung',
        'tcmovietime',
        'tcmoviestory',
        'storyortime',
        'cast',
        'video',
        'ok',
        'backMovie',
        'backgarbage'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },        
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'garbage',
            'conditions': 'is_going_to_garbage'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6',
                'garbage',
                'taichung',
                'tcmovietime',
                'tcmoviestory',
                'storyortime',
                'cast',
                'video',
                'ok',
                'backMovie',
                'backgarbage'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'go_garbage',
            'source': [
                'backgarbage'
            ],
            'dest': 'garbage'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'backgarbage',
            'conditions': 'is_going_to_backgarbage'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'backgarbage',
            'conditions': 'is_going_to_backgarbage'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'backgarbage',
            'conditions': 'is_going_to_backgarbage'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'backgarbage',
            'conditions': 'is_going_to_backgarbage'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'backgarbage',
            'conditions': 'is_going_to_backgarbage'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'backgarbage',
            'conditions': 'is_going_to_backgarbage'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'taichung',
            'conditions': 'is_going_to_taichung'
        },
        {
            'trigger': 'advance',
            'source': 'taichung',
            'dest': 'storyortime',
            'conditions': 'is_going_to_storyortime'
        },
        {
            'trigger': 'advance',
            'source': 'storyortime',
            'dest': 'tcmoviestory',
            'conditions': 'is_going_to_tcmoviestory'
        },
        {
            'trigger': 'advance',
            'source': 'storyortime',
            'dest': 'tcmovietime',
            'conditions': 'is_going_to_tcmovietime'
        },
        {
            'trigger': 'advance',
            'source': 'storyortime',
            'dest': 'cast',
            'conditions': 'is_going_to_cast'
        },
        {
            'trigger': 'advance',
            'source': 'storyortime',
            'dest': 'video',
            'conditions': 'is_going_to_video'
        },
        {
            'trigger': 'advance',
            'source': 'storyortime',
            'dest': 'ok',
            'conditions': 'is_going_to_ok'
        },
        {
            'trigger': 'advance',
            'source': 'storyortime',
            'dest': 'backMovie',
            'conditions': 'is_going_to_backMovie'
        },
        {
            'trigger': 'go_movie_choose',
            'source': [
                'tcmoviestory',
                'tcmovietime',
                'cast',
                'video'
            ],
            'dest': 'storyortime'
        },
        {
            'trigger': 'back_to_movie',
            'source': [
                'backMovie'
            ],
            'dest': 'taichung'
        },


    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()   
