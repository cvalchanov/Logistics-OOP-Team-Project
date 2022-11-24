# Logistics App


### Logistics console application exercise for OOP in Python module in Telerik Academy

### Implemented functionalities:
### I. Login and Logout
    - Login Command - You need to login before you can do anything. Different user roles have different permissions and allowed functions. 
        Managers are like admins - they can do everything. Supervisors can't create or remove trucks and users. 
        Employees can't do what supervisors can't plus they can't view other users' info and can't remove customers.
        There are three built in users to start with:

        username:                       password:                       role:
        pesho1baby                      admin1234                       manager
        goshkohubaveca                  super1234                       supervisor
        sashoroman                      emp1234                         employee

        <cmd> <username> <password>

        login pesho1baby admin1234

    - Logout Command - Well, this one is pretty self-explanatory, isn't it? :D

        <cmd>

        logout

### II. Create
    - CreateRoute Command – creates delivery route and saves it in txt file for routes.

        <cmd > <YYYY-M-D> <H:MM> <abbreviation> <abbreviation>
        (Abbreviations could be more than two.)

        createroute 2022-2-23 6:00 MEL SYD
        
    - CreateDeliveryPackage Command – creates temporary delivery pack.

        <cmd > <weight> <customer_id> <abbreviation> <abbreviation>

        createdeliverypackage 45 1 MEL SYD

    - CreateCustomer Command - creates a customer and saves it in txt file for customers.

        <cmd> <first_name> <last_name> <phone_number> <email>
        (email is optional. If left out from the command input it will default to 'N/A')

        createcustomer Palqk Palqkov 123
        createcustomer Tigur Tigurov 000 roar@zoo.bg

    - CreateTruck Command - creates a truck, saves it in txt file for trucks and creates a new file with the truck ID in trucks folder.

        <cmd> <truck_brand> <truck_capacity> <truck_range> <availability>
        (Availability is optional. If left out from the command input it will default to 'YES')

        createtruck Optimus 100000 100000
        createtruck Prime 100000 100000 no

    - CreateUser Command - creates a user and saves it in txt file for users.

        <cmd> <username> <password> <first_name> <last_name> <phone_number> <user_role>

        createuser tigur tigur1234 Tigur Tigurov 000 supervisor
        createuser palqk palqk1234 Palqk Palqkov 123 employee

### III. Add
    - AddDeliveryPackage Command – adds temporary delivery pack to truck assigned to delivery route and saves it in txt file for the load of the truck.

        <cmd > <pack_id> <truck_id> <route_id>

        adddeliverypackage 3 1001 1

    - AddDeliveryPackageBulk Command -  adds bulk of packages to truck assigned to route and saves it in the txt file.

        <cmd> <truck_id> <rout_id> <pack_id> <pack_id> <pack_id>
        (IDs of the packages could be more than one)

        adddeliverypackagebulk 1 1 1 2 3 

    - AddTruckToRoute Command - adds an available truck to an existing route.

        <cmd> <truck_id> <route_id>

        addtruck 1001 1

### IV. Remove
    - RemoveCustomer Command - removes an existing customer from the customers txt file.

        <cmd> <customer_id>

        removecustomer 5

    - RemoveTruck Command - removes an existing truck from the trucks txt file and deletes the truck file in the trucks folder.

        <cmd> <truck_id>

        removetruck 1005

    - RemoveUser Command - removes an existing user from the users txt file.

        <cmd> <username>

        removeuser palqk

### V. View
    - ViewUnassignedPackages Command – shows all temporary/unassigned packages.

        <cmd>

        viewunassignedpackages

    - ViewRoutesByDestination Command – shows all routes going through or getting to a city.

        <cmd> <abbreviation>

        viewroutesbydestination SYD

    - ViewRoutesInProgress Command – shows all routes with trucks already on the road.

        <cmd>

        viewroutesinprogress

    - ViewCustomer Command - shows a specific customer.

        <cmd> <customer_id>

        viewcustomer 5

    - ViewTruck Command - shows a specific truck.

        <cmd> <truck_id>

        viewtruck 1005

    - ViewUser Command - shows a specific user.

        <cmd> <username>

        viewuser palqk

    - ViewAllCustomers Command - shows all customers.

        <cmd>

        viewallcustomers

    - ViewAllTrucks Command - shows all trucks.

        <cmd>

        viewalltrucks

    - ViewAvailableTrucks Command - shows all available trucks.

        <cmd>

        viewavailabletrucks

    - ViewTruckLoad Command - shows the current load on the truck.

        <cmd> <truck_id>

        viewtruckload 1001

    - ViewAllUsers Command - shows all users.

        <cmd>

        viewallusers

    - ViewLog Command - shows the log for the specified day.

        <cmd> <DD.MM.YYYY>

        viewlog 01.08.2022





### Due to validations, optimization, bug fixes and tests, work is still in progress.
