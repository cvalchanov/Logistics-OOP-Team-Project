from src.commands.view_routes_by_destination import ViewRoutesByDestinationCommand
from src.commands.view_routes_in_progress import ViewRoutesInProgressCommand
from src.commands.view_unassigned_packages import ViewUnassignedPackagesCommand
from src.commands.add_delivery_package_bulk import AddDeliveryPackageBulkCommand
from src.core.application_data import ApplicationData
from src.commands.add_delivery_package import AddDeliveryPackageCommand
from src.commands.create_truck_command import CreateTruckCommand
from src.commands.create_delivery_package import CreateDeliveryPackageCommand
from src.commands.create_route import CreateRouteCommand
from src.commands.view_available_trucks_command import ViewAvailableTrucksCommand
from src.core.data_files_manager import DataFilesManager
from src.commands.view_truck_command import ViewTruckCommand
from src.commands.view_all_trucks_command import ViewAllTrucksCommand
from src.commands.create_customer_command import CreateCustomerCommand
from src.commands.view_customer_command import ViewCustomerCommand
from src.commands.view_all_customers_command import ViewAllCustomersCommand
from src.commands.add_truck_to_route_command import AddTruckToRouteCommand
from src.commands.create_user_command import CreateUserCommand
from src.commands.view_user_command import ViewUserCommand
from src.commands.view_all_users_command import ViewAllUsersCommand
from src.commands.view_truck_load_command import ViewTruckLoadCommand
from src.commands.login_command import LoginCommand
from src.commands.logout_command import LogoutCommand
from src.commands.remove_customer_command import RemoveCustomerCommand
from src.commands.remove_truck_command import RemoveTruckCommand
from src.commands.remove_user_command import RemoveUserCommand
from src.commands.view_log_command import ViewLogCommand

class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._data_files = DataFilesManager()
        self._app_data = data

    def create(self, input_line:str):
        cmd, *params = input_line.split()

        if cmd.lower() == 'adddeliverypackage':
            return AddDeliveryPackageCommand(params, self._app_data)
        if cmd.lower() == 'adddeliverypackagebulk':
            return AddDeliveryPackageBulkCommand(params, self._app_data)
        if cmd.lower() == 'createtruck':
            return CreateTruckCommand(params, self._app_data)
        if cmd.lower() == 'createdeliverypackage':
            return CreateDeliveryPackageCommand(params, self._app_data)
        if cmd.lower() == 'createroute':
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == 'viewavailabletrucks':
            return ViewAvailableTrucksCommand(self._app_data)
        if cmd.lower() == 'addtruck':
            return AddTruckToRouteCommand(params, self._app_data)
        if cmd.lower() == 'viewtruck':
            return ViewTruckCommand(params, self._app_data)
        if cmd.lower() == "viewalltrucks":
            return ViewAllTrucksCommand(self._app_data)
        if cmd.lower() == 'createcustomer':
            return CreateCustomerCommand(params, self._app_data)
        if cmd.lower() == 'viewcustomer':
            return ViewCustomerCommand(params, self._app_data)
        if cmd.lower() == 'viewallcustomers':
            return ViewAllCustomersCommand(params, self._app_data)
        if cmd.lower() == 'viewunassignedpackages':
            return ViewUnassignedPackagesCommand(self._app_data)
        if cmd.lower() == 'createuser':
            return CreateUserCommand(params, self._app_data)
        if cmd.lower() == 'viewuser':
            return ViewUserCommand(params, self._app_data)
        if cmd.lower() == 'viewallusers':
            return ViewAllUsersCommand(self._app_data)
        if cmd.lower() == 'viewtruckload':
            return ViewTruckLoadCommand(params, self._app_data)
        if cmd.lower() == 'viewroutesbydestination':
            return ViewRoutesByDestinationCommand(params, self._app_data)
        if cmd.lower() == 'viewroutesinprogress':
            return ViewRoutesInProgressCommand(self._app_data)
        if cmd.lower() == 'login':
            return LoginCommand(params, self._app_data)
        if cmd.lower() == 'logout':
            return LogoutCommand(self._app_data)
        if cmd.lower() == 'removeuser':
            return RemoveUserCommand(params, self._app_data)
        if cmd.lower() == 'removetruck':
            return RemoveTruckCommand(params, self._app_data)
        if cmd.lower() == 'removecustomer':
            return RemoveCustomerCommand(params, self._app_data)
        if cmd.lower() == 'viewlog':    
            return ViewLogCommand(params, self._app_data)
            
        raise ValueError(f'Invalid command name: {cmd}!')
