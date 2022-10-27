from src.models.delivery_package import DeliveryPackage


class TemporaryDataFactory:
    def find_unasigned_delivery_package(self, id):
        for pack in self._unassigned_packages:
            if pack.id == id:
                return pack
    
    def create_delivery_package(self, id, weight, customer_id, start_locion, end_location):
        dp = DeliveryPackage(id, weight, customer_id, start_locion, end_location)
        self._unassigned_packages.append(dp)

    def remove_from_un_packages(self, package: DeliveryPackage):
        for pack in self._unassigned_packages:
            if pack.id == package.id:
                self._unassigned_packages.remove(pack)