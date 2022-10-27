from src.models.constants.user_roles import UserRoles
from src.core.application_data import ApplicationData


class ViewRoutesInProgressCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data

    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')

        if self._app_data.logged_user.user_role != UserRoles.MANAGER:
            raise ValueError('Employees can\'t remove customers')

        routes_in_progress = self._app_data.find_routes_by_condition(self._app_data.condition_in_progress)

        if routes_in_progress:
            output = '\n'.join([f'{x + 1}. {routes_in_progress[x].in_progress_info()}' for x in range(len(routes_in_progress))])
            self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed routs in progress')
            return output
        self._app_data.update_log(f' - {self._app_data.logged_user.username} - no routs in progress')
        return 'No routes in progress'
    