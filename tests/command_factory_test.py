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
from src.core.command_factory import CommandFactory
import unittest


def factory_and_data():
    app_data = ApplicationData()
    factory = CommandFactory(app_data)

    return factory, app_data


class CommandFactoryShould(unittest.TestCase):
    def test_create_raisesError_invalidCommand(self):

        input_line = 'Pesho e palqk'
        factory, app_data = factory_and_data()

        with self.assertRaises(ValueError):
            command = factory.create(input_line)

    def test_create_createsViewUnassignedPackagesCommand_withCorrectParams(self):

        input_line = 'viewunassignedpackages'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewUnassignedPackagesCommand)
        self.assertEqual(app_data, command._app_data)

    def test_create_createsAddDeliveryPackageBulkCommand_withCorrectParams(self):

        input_line = 'adddeliverypackagebulk 1001 1 1 2'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, AddDeliveryPackageBulkCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1001', '1', '1', '2'], command._params)

    def test_create_createsAddDeliveryPackageCommand_withCorrectParams(self):

        input_line = 'adddeliverypackage 1 1 1001'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, AddDeliveryPackageCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1', '1', '1001'], command._params)

    def test_create_createsCreateTruckCommand_withCorrectParams(self):

        input_line = 'createtruck Pesho 1 1'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, CreateTruckCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['Pesho', '1', '1'], command._params)

    def test_create_createsCreateDeliveryPackageCommand_withCorrectParams(self):

        input_line = 'createdeliverypackage 1000 1 Pesho Gosho'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, CreateDeliveryPackageCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1000', '1', 'Pesho', 'Gosho'], command._params)

    def test_create_createsCreateRouteCommand_withCorrectParams(self):

        input_line = 'createroute 1 2 Pesho Gosho'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, CreateRouteCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1', '2', 'Pesho', 'Gosho'], command._params)

    def test_create_createsViewAvailableTrucksCommand_withCorrectParams(self):

        input_line = 'viewavailabletrucks'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewAvailableTrucksCommand)
        self.assertEqual(app_data, command._app_data)

    def test_create_createsViewTruckCommand_withCorrectParams(self):

        input_line = 'viewtruck 1001'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewTruckCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1001'], command._params)

    def test_create_createsViewAllTrucksCommand_withCorrectParams(self):

        input_line = 'viewalltrucks'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewAllTrucksCommand)
        self.assertEqual(app_data, command._app_data)

    def test_create_createsCreateCustomerCommand_withCorrectParams(self):

        input_line = 'createcustomer Pesho Peshov 112 tigar@zoo.bg'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, CreateCustomerCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['Pesho', 'Peshov', '112', 'tigar@zoo.bg'], command._params)

    def test_create_createsViewCustomerCommand_withCorrectParams(self):

        input_line = 'viewcustomer 1'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewCustomerCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1'], command._params)

    def test_create_createsViewAllCustomersCommand_withCorrectParams(self):

        input_line = 'viewallcustomers'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewAllCustomersCommand)
        self.assertEqual(app_data, command._app_data)

    def test_create_createsAddTruckToRouteCommand_withCorrectParams(self):

        input_line = 'addtruck 1001 1'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, AddTruckToRouteCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1001', '1'], command._params)

    def test_create_createsCreateUserCommand_withCorrectParams(self):

        input_line = 'createuser pesho1baby admin1234 Pesho Peshov 911 manager'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, CreateUserCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['pesho1baby', 'admin1234', 'Pesho', 'Peshov', '911', 'manager'], command._params)

    def test_create_createsViewUserCommand_withCorrectParams(self):

        input_line = 'viewuser pesho1baby'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewUserCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['pesho1baby'], command._params)

    def test_create_createsViewAllUsersCommand_withCorrectParams(self):

        input_line = 'viewallusers'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewAllUsersCommand)
        self.assertEqual(app_data, command._app_data)

    def test_create_createsViewTruckLoadCommand_withCorrectParams(self):

        input_line = 'viewtruckload 1001'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewTruckLoadCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1001'], command._params)

    def test_create_createsLoginCommand_withCorreactParams(self):

        input_line = 'login pesho1baby admin1234'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, LoginCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['pesho1baby', 'admin1234'], command._params)

    def test_create_createsLogoutCommand_withCorrectParams(self):

        input_line = 'logout'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, LogoutCommand)
        self.assertEqual(app_data, command._app_data)

    def test_create_createsRemoveCustomerCommand_withCorrectParams(self):

        input_line = 'removecustomer 1'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, RemoveCustomerCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1'], command._params)

    def test_create_createsRemoveTruckCommand_withCorrectParams(self):

        input_line = 'removetruck 1001'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, RemoveTruckCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['1001'], command._params)

    def test_create_createsRemoveUserCommand_withCorrectParams(self):

        input_line = 'removeuser pesho1baby'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, RemoveUserCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['pesho1baby'], command._params)

    def test_create_createsViewLogCommand_withCorrectParams(self):

        input_line = 'viewlog 30.07.2022'
        factory, app_data = factory_and_data()

        command = factory.create(input_line)

        self.assertIsInstance(command, ViewLogCommand)
        self.assertEqual(app_data, command._app_data)
        self.assertEqual(['30.07.2022'], command._params)        