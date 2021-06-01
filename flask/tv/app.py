
import sys
import yaml

with open("/home/richet/TradingSystem/config/directories.yaml", "r") as ymlfile:
    dirs = yaml.load(ymlfile)

directories = dirs["module_directories"]
for d in directories : 
    sys.path.insert(0, directories[d])


from flask import Flask
import DB
import modules
import richetmodule
import Bybit
import Bitmex
import Alarm

app = Flask(__name__)

@app.route('/')
def index():
    return "<span style='color:red'>I am app" + DB.name + modules.name + richetmodule.name + Bybit.name + Bitmex.name + Alarm.name  + "</span>"