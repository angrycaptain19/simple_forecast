from filestack import Client
import os


class ChartUpload():
    # Upload the plot file to cloud service
    # generate a URL on screen
    # input filename / cloud service info
    def __init__(self, api_key='AOMKqlY6qQZGLtJDBR4s7z'):
        self.api_key = api_key
        working_dir = os.getcwd()
        self.path = working_dir + '/file/' + 'Forecast_WMA.png'

    def share(self):
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.path)
        return new_filelink.url
