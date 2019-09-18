#coding=utf-8
# -*- coding: UTF-8 -*-
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import config
import requests
import json


# A request corresponds to the RequestHandler information and method
class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        # The content of the server's response to the browser
        try:
            for i in data_dict:
                data = i['DATA']
                B071_12 = int(data['B071_12'])
                B084_24 = int(data['B084_24'])
                B083_24 = int(data['B083_24'])
                B043_24 = int(data['B043_24'])
                if B071_12 <= 5 and B084_24 <= 5 and B083_24 <= 5 and B043_24 >= 2:
                    responseData = {
                        "CODE": 1,
                        "MSG": "处理成功",
                        "PHONE": i['PHONE'],
                        "DATA": {
                            "SCORE": ""
                        }
                    }
                    self.write(responseData)
                    self.set_header('Content-Type', 'text/plain;charset=utf-8')

                else:
                    responseData = {
                        "CODE": 0,
                        "MSG": "参数验证失败",
                        "PHONE": i['PHONE'],
                        "DATA": {}
                    }
                    self.write(responseData)
                    self.set_header('Content-Type', 'text/plain;charset=utf-8')

        except:
            try:
                data = data_dict["DATA"]
                B071_12 = int(data['B071_12'])
                B084_24 = int(data['B084_24'])
                B083_24 = int(data['B083_24'])
                B043_24 = int(data['B043_24'])
                if B071_12 <= 5 and B084_24 <= 5 and B083_24 <= 5 and B043_24 >= 2:
                    responseData = {
                        "CODE": 1,
                        "MSG": "处理成功",
                        "PHONE": data_dict['PHONE'],
                        "DATA": {
                            "SCORE": ""
                        }
                    }
                    self.write(responseData)
                    self.set_header('Content-Type', 'text/plain;charset=utf-8')
                    # self.set_header('Content-Type', 'application/json;charset=utf-8')

                else:
                    responseData = {
                        "CODE": 0,
                        "MSG": "参数验证失败",
                        "PHONE": data_dict['PHONE'],
                        "DATA": {}
                    }
                    self.write(responseData)
                    self.set_header('Content-Type', 'text/plain;charset=utf-8')

            except:
                pass

    def post(self):
        self.write('hello word post')


if __name__ == '__main__':
    # Global parameter definition
    # Runs server on a given port
    tornado.options.define('port', default=8208, type=int)
    tornado.options.define('itcast', default=[], type=str, multiple=True)

    url = "8208/houselai/"
    # Send get request
    response = requests.get(url)
    # Gets the returned json data
    # data_str = response.json()
    # To get the data
    data_dict = json.loads(response)

    print(tornado.options.options.itcast)
    print(tornado.options.options.port)

    app = tornado.web.Application([(r"/", IndexHandler)], **config.settings)
    # app.listen(8208)
    # Create the server instance and bind the server port
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(tornado.options.options.port)

    tornado.ioloop.IOLoop.current().start()
