import yaml

with open('./config.yml') as f:
    conf = yaml.load(f, yaml.FullLoader)

server = conf.get('server')
database = conf.get('database')