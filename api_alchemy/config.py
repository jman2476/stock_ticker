# General configuration parameters

from os import environ, path
from dotenv import load_dotenv, dotenv_values

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
env_vars = dotenv_values('.env')
print(basedir)

print(env_vars['FINNHUB_API_KEY'])

