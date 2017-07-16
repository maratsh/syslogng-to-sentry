class LogDestination(object):
    def open(self):
        """Open a connection to the target service"""
        return True

    def close(self):
        """Close the connection to the target service"""
        pass

    def is_opened(self):
        """Check if the connection to the target is able to receive messages"""
        return True

    def init(self):
        """This method is called at initialization time"""
        return True

    def deinit(self):
        """This method is called at deinitialization time"""
        pass

    def send(self, msg):
        """Send a message to the target service
        It should return True to indicate success, False will suspend the
        destination for a period specified by the time-reopen() option."""
        pass


class SentryDestination(LogDestination):
    def __init__(self):
        self.code_map = dict(
            debug=[7],
            info=[5,6],
            warning=[4],
            error=[3],
            fatal=[0,1,2]
        )
        self.keys = [
            "LEVEL",
            "PID",
            "SOURCE",
            "FACILITY",
            "SOURCEIP",
            "HOST",
            "HOSTID",
            "HOST_FROM",
            "PROGRAM"

        ]


    def init(self, options):
        from raven import Client
        self.DSN = options['DSN']
        self.client = Client(self.DSN)
        return True

    def open(self):
        return True

    def close(self):
        return True

    def deinit(self):
        return True

    def _code_to_level(self, code):

        """
                   Numerical         Severity
             Code

              0       Emergency: system is unusable
              1       Alert: action must be taken immediately
              2       Critical: critical conditions
              3       Error: error conditions
              4       Warning: warning conditions
              5       Notice: normal but significant condition
              6       Informational: informational messages
              7       Debug: debug-level messages

               Sentry is aware of levels:

               * debug (the least serious) 7
               * info 5-6
               * warning 4
               * error 3
               * fatal (the most serious) 0-2

               :param code: numerical code
               :return: level in string

        """

        level = 'fatal'
        code_num=int(code)
        for map_level, map_codes in self.code_map.items():
            if code_num in map_codes:
                level = map_level

        return level

    def send(self, msg):
        tags = {}
        try:
            for key in self.keys:
                if key in msg.keys():
                  tags[key] = msg[key]

            for key, value in msg.items():
                if ".SDATA." in key:
                    tags[key] = value

            level = self._code_to_level(msg['LEVEL_NUM'])
        except Exception, e:
            self.client.captureException(e)
        self.client.captureMessage(message=msg['MESSAGE'], level=level, tags=tags)
        return True
