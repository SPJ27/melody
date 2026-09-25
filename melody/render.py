from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))

def render(file, variables={}):
    res = env.get_template(file).render(variables)
    return res