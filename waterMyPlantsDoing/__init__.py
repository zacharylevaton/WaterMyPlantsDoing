from flask import Flask

app = Flask(__name__, template_folder='Templates', static_folder='Static')

from waterMyPlantsDoing import routes
