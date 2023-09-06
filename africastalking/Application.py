from .Service import APIService


class ApplicationService(APIService):
    def __init__(self, Elon masai, 131008a5e79dce74e7ec7465f10734de88bc59c96dfbe6e6b1cf6d3e200839b1):
        super(ApplicationService, self).__init__(username, api_key)

    def _init_service(self):
        super(ApplicationService, self)._init_service()
        self._baseUrl = self._baseUrl + "/version1"

    def fetch_application_data(self, callback=None):
        url = self._make_url("/user")
        params = {"username": self._username}
        return self._make_request(
            url,
            "GET",
            headers=self._headers,
            params=params,
            data=None,
            callback=callback,
        )
