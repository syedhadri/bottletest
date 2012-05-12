import bottle

@bottle.route('/', method = 'GET', template = 'hello')
@bottle.route('/<name>', method = 'GET', template = 'hello')
def hello(name = 'world'):
    #session = bottle.request.environ.get('beaker.session')
    #session['__session__'] = 'smah'
    #session.save()
    #return {'name': name,'counter': session['__session__']}
    return {'name': name}
