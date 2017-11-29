from time import gmtime, strftime
class Debugger:
    error = True
    frontend = False
    backend = False

    @staticmethod
    def front_print(string):
        if Debugger.frontend:
            print("[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "][Front-end] " + string)

    @staticmethod
    def back_print(string):
        if Debugger.backend:
            print("[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "][Back-end] " + string)

    @staticmethod
    def display_error(string):
        if Debugger.error:
            print("[" + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "][Error] " + string)