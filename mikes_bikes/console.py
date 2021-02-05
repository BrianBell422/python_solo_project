import pdb
from models.bike import Bike
from models.manufacturer import Manufacturer

import repositories.bike_repository as bike_repository
import repositories.manufacturer_repository as manufacturer_repository


bike_repository.delete_all()
manufacturer_repository.delete_all()


manufacturer1 = Manufacturer("Honda", "Japan", "Motocross")
manufacturer_repository.save(manufacturer1)

manufacturer2 = Manufacturer("Kawasaki", "Japan", "Motocross")
manufacturer_repository.save(manufacturer2)

manufacturer3 = Manufacturer("Yamaha", "Japan", "Road")
manufacturer_repository.save(manufacturer3)


bike1 = Bike("Honda", "CR125", "Motocross", 2500, 5000)
bike_repository.save(bike1)

bike2 = Bike("Kawasaki", "KXF250", "Motocross", 3000, 6000)
bike_repository.save(bike2)

bike3 = Bike("Yamaha", "R1", "Road", 3500, 7000)
bike_repository.save(bike3)


pdb.set_trace()