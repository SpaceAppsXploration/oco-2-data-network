__author__ = 'lorenzo@pramantha.net'

import os
import platform
import h5py
import tornado.web


PATH = os.path.dirname(__file__)
DATA = os.path.join(PATH, '../OCO2')


class Demo(tornado.web.RequestHandler):
    """
    Demo Handler for XOCO2 by square of the map
    url: /xoco2/by/square/{latitude}/{longitude}
    """
    @staticmethod
    def make_path(filename):
        """
        tool to define the h5 file path
        """
        path = DATA
        if platform.system() == 'Linux' or platform.system() == 'Darwin':
            # linux path
            path += '/'
            return path + filename
        # windows path
        path += '\\'
        return path + filename

    def check_inputs(self, lat, long):
        """
        Check if values are coordinates
        """
        try:
            lat, long = float(lat), float(long)
            if not -90.0 <= lat <= 90.0 or not -180.0 <= long <= 180.0 :
                raise ValueError('OutOfRange')
            print(lat, long)
            return True
        except ValueError as v:
            # wrong coordinates
            print(v)
            return self.redirect("/error?v=" + str(v))

    def get(self, lat, long):
        """
        Handle GET
        """
        if self.check_inputs(lat, long):
            # --------------------------------------------
            # Demo code
            NAME = 'oco2_L2StdGL_02675a_150101_B6000r_150411233719.h5'
            FS = self.make_path(NAME)

            f = h5py.File(FS, 'r', libver='earliest')
            # --------------------------------------------

            #
            # GEOquery the JSONs in MongoDB
            #

            f.close()

            return self.write({
                "exit_code": 0,
                "type" : "Feature",
                "geometry" : {
                    "type" : "polygon",
                    "coordinates" : [
                        [
                            0,
                            0
                        ],
                        [
                            0,
                            0
                        ],
                        [
                            0,
                            0
                        ],
                        [
                            0,
                            0
                        ]
                    ]
                },
                "properties": {
                    "xco2": 0,
                    "altitude": 0,
                }
            })


class ErrorHandler(tornado.web.RequestHandler):
    """
    Generates an error response with status_code for all requests.
    """
    def write_error(self, status_code, **kwargs):
        if status_code in [403, 404, 500, 503]:
            error = {
                "error": "Some error occurred.",
                "exit code": 1,
                "http": int(status_code)
            }
            return self.write(error)
        else:
            error = {
                "error": "Wrong coordinates format. It should be http://{url}/{latitude}/{longitude}",
                "exit code": 1,
                "http": 200
            }

            if self.get_query_argument('v') == 'OutOfRange':
                error["error"] = "Latitude or Longitude in wrong range"

            return self.write(error)
            #
            # write() automatically sets the Content-Type as application/json
            # http://tornado.readthedocs.org/en/latest/web.html#tornado.web.RequestHandler.write
            #

    def get(self, *args, **kwargs):
        return self.write_error(self._status_code)

