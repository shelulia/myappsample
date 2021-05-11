
import json


class Configurator:
    def __init__(self, environment):
        #print(str(environment))
        with open('conf.json', 'r') as f:
            self.config = json.load(f)
        self.config = self.config[environment]


    def get_database_url(self):
        return self.config["database"]


    def get_test_data_folder(self):
        return self.config["test_data_folder"]