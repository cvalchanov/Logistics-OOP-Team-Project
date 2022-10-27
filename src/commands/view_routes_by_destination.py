from src.core.application_data import ApplicationData


class ViewRoutesByDestinationCommand:
    def __init__(self, params, app_data: ApplicationData) -> None:
        self._app_data = app_data
        self._params = params

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')
        if len(self._params) != 1:
            raise ValueError('Invalid input')

        abbreviation = self._params[0]
        routes_in_progress = self._app_data.find_routes_by_condition(self._app_data.condition_destination, abbreviation.upper())

        if routes_in_progress:
            output = '\n'.join([f'{x + 1}. {routes_in_progress[x].info()}' for x in range(len(routes_in_progress))])
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed routs to {abbreviation}')
            return output
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - No routes to {abbreviation}')
        return f'No routes to destination {abbreviation}'