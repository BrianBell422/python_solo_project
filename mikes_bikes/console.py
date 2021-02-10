import pdb
from models.bike import Bike
from models.manufacturer import Manufacturer

import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository

bike_repository.delete_all()
manufacturer_repository.delete_all()


manufacturer1 = Manufacturer("Honda", "Japan", "Off road")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Kawasaki", "Japan", "Off road")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Yamaha", "Japan", "On Road")
manufacturer_repository.save(manufacturer3)

manufacturer4 = Manufacturer("KTM", "Austria", "Off road")
manufacturer_repository.save(manufacturer4)

manufacturer5 = Manufacturer("Ducati", "Japan", "On road")
manufacturer_repository.save(manufacturer5)

manufacturer6 = Manufacturer("Harley Davidson", "USA", "On Road")
manufacturer_repository.save(manufacturer6)


bike1 = Bike(manufacturer1, "CR125", "Motocross", 2500, 5000, 1)
bike_repository.save(bike1)

bike2 = Bike(manufacturer2, "KX250X", "Enduro", 3000, 5200, 5)
bike_repository.save(bike2)

bike3 = Bike(manufacturer3, "R1", "Road Race", 3500, 6000, 2)
bike_repository.save(bike3)

bike4 = Bike(manufacturer4, "SXF350", "Motocross", 3500, 6800, 0)
bike_repository.save(bike4)

bike5 = Bike(manufacturer5, "748R", "Road Race", 4500, 8200, 7)
bike_repository.save(bike5)

bike6 = Bike(manufacturer6, "Sportster", "Cruiser Road", 4000, 8000, 1)
bike_repository.save(bike6)


pdb.set_trace()