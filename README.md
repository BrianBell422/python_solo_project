RUNNING INSTRUCTIONS:

Clone repository to local working directory

cd python_solo_project > mikes_bikes, to open in VSCode enter into terminal: code .

To create the db enter into terminal: createdb mikes_bikes

To execute PSQL script, enter in terminal: psql -d mikes_bikes -f ./db/mikes_bikes.sql 

To populate our db tables enter into terminal: python3 console.py

To run flask enter into terminal: flask run




BRIEF:

Shop Inventory
Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.


MVP

The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.

The inventory should track manufacturers, including a name and any other appropriate details.

The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.

This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and 

tables as appropriate to your project.

Show an inventory page, listing all the details for all the products in stock in a single view.

As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.

Inspired by

eBay, Amazon (back end only), Magento


Possible Extensions

Calculate the markup on items in the store, and display it in the inventory

Filter the inventory list by manufacturer. For example, provide an option to view all books in stock by a certain author.

Categorise your items. Books might be categorised by genre (crime, horror, romance...) and cars might be categorised by type (SUV, coupé, hatchback...). Provide an option to filter the inventory list by these 
categories.

Mark manufacturers as active/deactivated. Deactivated manufacturers will not appear when creating new products.




TECHNOLOGIES USED:

Python 3

HTML

CSS

VSCode

Trello

Draw.io

SQL

Psycopg2

Flask

Postico

Fontawesome

Google fonts

![Screenshot 2021-04-09 at 11 05 19](https://user-images.githubusercontent.com/74567808/114203594-37f26d00-9950-11eb-990e-d06e5c3f9857.png)

![Screenshot 2021-04-09 at 11 05 40](https://user-images.githubusercontent.com/74567808/114203615-3c1e8a80-9950-11eb-99be-83281c6956d9.png)

![Screenshot 2021-04-09 at 11 05 57](https://user-images.githubusercontent.com/74567808/114203625-3d4fb780-9950-11eb-8aba-c93a282cbb32.png)

![Screenshot 2021-04-09 at 11 06 22](https://user-images.githubusercontent.com/74567808/114203628-3de84e00-9950-11eb-9590-90e684dac525.png)

![Screenshot 2021-04-09 at 11 06 36](https://user-images.githubusercontent.com/74567808/114203631-3e80e480-9950-11eb-8292-d0dbdae289c7.png)

![Screenshot 2021-04-09 at 11 06 54](https://user-images.githubusercontent.com/74567808/114203636-3f197b00-9950-11eb-9a50-5430011832fe.png)

![Screenshot 2021-04-09 at 11 07 05](https://user-images.githubusercontent.com/74567808/114203637-3fb21180-9950-11eb-9d80-7e8451f73860.png)

![Screenshot 2021-04-09 at 11 07 17](https://user-images.githubusercontent.com/74567808/114203639-404aa800-9950-11eb-985e-d84a720dda54.png)
