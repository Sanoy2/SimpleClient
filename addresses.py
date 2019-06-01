def synchronous(argument):
    path = "{0}/http/uuid/{1}".format(get_server_address(),argument)
    return path


def asynchronous(argument):
    path = "{0}/http/response/{1}".format(get_server_address(),argument)
    return path


def get_server_address():
    return "localhost:8080"