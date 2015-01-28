import re
import os

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, Instantiate
import co2sensor


htmlResponseTemplate = ("<html>"
                        "<head>"
                        "<title>Sonde de CO2</title>"
                        "</head>"
                        "<body>"
                        "%(body)s"
                        "</body>"
                        "</html>")


@ComponentFactory(name='simple-servlet-factory')
@Instantiate('simple-servlet')
@Provides(specifications='pelix.http.servlet')
@Property('_path', 'pelix.http.path', "/co2")  # pv_systems/")
# dans l'architecture servir :
# completer avec 1 ou 2 :
# /predis/pv_sites/1 : inverter 2 + sensor card 0
# /predis/pv_sites/2 : inverter 1 + sensor card 1


class SimpleServletFactory(object):
    """
    Simple servlet factory
    """

    def __init__(self):
        self._path = None
        self.__sensor = co2sensor.Co2Sensor()
        self.__urlToFunDic = {
            re.compile('/co2/?$'): self.get_co2_value,
        }

    def bound(self, path, params):
        """
        Servlet bound to a path
        """
        self.bound.append(path)
        return True

    def unbound(self, path, params):
        """
        Servlet unbound from a path
        """
        self.unbound.append(path)
        return None

    def get_co2_value(self, reqPath):
        return 'Capteur indisponible' + reqPath


    def do_GET(self, request, response):
        """
        Handle a GET
        """
        reqPath = request.get_path()
        body = ''
        retcode = 500
        found = 0
        for pattern, func in self.__urlToFunDic.items():
            m = pattern.match(reqPath)
            if m:
                found = 1
                argDict = m.groupdict()
                argDict['reqPath'] = os.path.normpath(reqPath)
                body = func(**argDict)
                retcode = 200
                break
        if found == 0:
            retcode = 404
            body = "Page not found"
        content = htmlResponseTemplate % {'body': body}
        response.send_content(retcode, content)
        return


