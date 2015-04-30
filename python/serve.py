__author__ = 'lorenzo@pramantha.net'

import tornado
import os.path
import tornado.ioloop as ioloop
import tornado.web as web

from python.apis.endpoints import Demo, ErrorHandler

settings = {
    # "static_path": os.path.join(PATH, 'OCO2')
    "re_floating": "-?[0-9]+\.?[0-9]+",
}

if __name__ == '__main__':
    import logging
    logging.getLogger().setLevel(logging.DEBUG)

    app = web.Application(
        [(r"/xoco2/by/square/([-\+]?[0-9]+\.?[0-9]+)/([-\+]?[0-9]+\.?[0-9]+)", Demo),
         (r"/error", ErrorHandler),
         (r"/(.*)", ErrorHandler),
         ],
        # (r"/static/(.*)", web.StaticFileHandler, {"path": settings['static_path']}),
        **settings
    )
    port = 3001
    app.listen(port)
    print("Tornado " + tornado.version + " Running at port " + str(port))
    ioloop.IOLoop.instance().start()
