import bottle
import os
import random



@bottle.route('/')
def static():
    return "the server is running~"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
	'head_type': "tongue",
	'tail_type': "fat-rattle"
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    
    directions = ['up', 'down', 'left', 'right']
    direction = random.choice(directions)

    #food = data['food']['data'][0]
    #snakeHead = data['body']['data'][0]

    #if food.x - snakeHead.x > 0:
    #    direction = 'right'

    #print(snakeHead, food)
    print(direction)
    return {
        'move': direction,
        'taunt': 'battlesnake-python!'
    }


# Expose WSGI app (so gunicorn can find it)
#application = bottle.default_app()

#if __name__ == '__main__':
#    bottle.run(
#        application,
#        host=os.getenv('IP', '0.0.0.0'),
#        port=os.getenv('PORT', '8080'),
#        debug = True)
