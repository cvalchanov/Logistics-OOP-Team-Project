
from src.core.application_data import ApplicationData


class ViewUnassignedPackagesCommand:
    def __init__(self, app_data: ApplicationData) -> None:
        self._app_data = app_data
    
    def execute(self):
        if self._app_data.logged_user == None:
            raise ValueError('You need to log in first')
            
        if len(self._app_data.unassigned_packages) == 0:
            return 'No unassigned delivery packages'

        self._app_data.update_log(f' - {self._app_data.logged_user.username} - viewed unassigned packages')        
        return '\n'.join(map(str, self._app_data.unassigned_packages))