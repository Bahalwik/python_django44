from datetime import datetime

class User_filter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META
        with open('board/middleware/users_info.txt', 'a') as file:
            file.writelines(('Дата и время события: ' + str(datetime.now())) + ' || ' +
                            ('Метод запроса: ' + ip['REQUEST_METHOD']) + ' || ' +
                            ('запрошенный URL: ' + ip['PATH_INFO']) + ' || ' + ('HTTP метод: ' + ip['SERVER_PROTOCOL'])
                            + '\n')

        response = self.get_response(request)

        return response
