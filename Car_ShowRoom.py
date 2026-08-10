class Car:

    def __init__(self, car_id, brand, model, year, color, price, mileage):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price
        self.mileage = mileage
        self.status = "Available"
        self.customer = None

    def display_car(self):
        print("----- Car Details -----")
        print(f"Car ID     = {self.car_id}")
        print(f"Brand      = {self.brand}")
        print(f"Model      = {self.model}")
        print(f"Year       = {self.year}")
        print(f"Color      = {self.color}")
        print(f"Price      = {self.price}")
        print(f"Mileage    = {self.mileage}")
        print(f"Status     = {self.status}")
        print()


class Showroom:

    def __init__(self):
        self.cars = []
        self.customers = []
        self.sales = []
        self.sale_id = 1

    def add_sale(self, sale):
        self.sales.append(sale)

    def view_sales(self):
        for sale in self.sales:
            sale.display_sale()

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_customer(self):
        print("===== Available Customer =====")

        for customer in self.customers:
            customer.display_customer()

    def add_car(self, car):
        self.cars.append(car)

    def view_cars(self):
        print("===== Available Cars =====")

        for car in self.cars:
            car.display_car()

    def search_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                car.display_car()
                return

        print("Car not found!")

    def remove_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                print("Car removed successfully!")
                return

        print("Car not found!")

    def update_car(self, car_id):

        for car in self.cars:

            if car.car_id == car_id:

                print("""
1. Update Color
2. Update Mileage
3. Update Model
4. Update Price
""")

                choice = int(input("Enter your choice: "))

                if choice == 1:
                    new_color = input("Enter new color: ")
                    car.color = new_color

                elif choice == 2:
                    new_mileage = input("Enter new mileage: ")
                    car.mileage = new_mileage

                elif choice == 3:
                    new_model = input("Enter new model: ")
                    car.model = new_model

                elif choice == 4:
                    new_price = int(input("Enter new price: "))
                    car.price = new_price

                else:
                    print("Invalid choice!")
                    return

                print("Car updated successfully!")
                return

        print("Car not found!")

    def sell_car(self, car_id, customer_id):

        for car in self.cars:
            if car.car_id == car_id:
                break
        else:
            print("Car not found!")
            return

        if car.status == "Sold":
            print("Car already sold!")
            return

        for customer in self.customers:
            if customer.customer_id == customer_id:
                break
        else:
            print("Customer not found!")
            return

        car.status = "Sold"
        car.customer = customer

        sale = Sale(
            self.sale_id,
            car,
            customer,
            car.price
        )

        self.sales.append(sale)
        self.sale_id += 1

        print("Car sold successfully!")

    def sold_car(self):

        found = False

        for car in self.cars:

            if car.status == "Sold":

                found = True

                print("*** Sold Cars ***")
                car.display_car()
                car.customer.display_customer()

        if not found:
            print("No car found!")

    def save_cars(self):

        with open("car.txt", "w+") as f:

            for car in self.cars:

                f.write(
                    f"{car.car_id},{car.brand},{car.model},"
                    f"{car.year},{car.color},{car.price},"
                    f"{car.mileage},{car.status}\n"
                )

    def load_cars(self):

        with open("car.txt", "r") as f:

            for line in f:

                data = line.strip().split(",")

                car = Car(
                    int(data[0]),
                    data[1],
                    data[2],
                    int(data[3]),
                    data[4],
                    int(data[5]),
                    data[6]
                )

                car.status = data[7]

                self.cars.append(car)


class Customer:

    def __init__(self, customer_id, name, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.address = address

    def display_customer(self):
        print("____Customer Details____")
        print(f"Customer ID = {self.customer_id}")
        print(f"Customer Name = {self.name}")
        print(f"Customer Phone = {self.phone}")
        print(f"Customer Address = {self.address}")


class Sale:

    def __init__(self, sale_id, car, customer, sale_price):
        self.sale_id = sale_id
        self.car = car
        self.customer = customer
        self.sale_price = sale_price

    def display_sale(self):
        print("_____ Sale Details _____")
        print(f"Sale ID = {self.sale_id}")
        print(f"Car = {self.car.brand} {self.car.model}")
        print(f"Customer = {self.customer.name}")
        print(f"Sale Price = {self.sale_price}")


# Creating Car objects

car2 = Car(
    2,
    "Honda",
    "Civic",
    2025,
    "Black",
    2500000,
    "25000 km"
)


# Creating Customer object

customer = Customer(
    1,
    "Hadi",
    "030",
    "Rawalpindi"
)


# Creating Showroom object

showroom = Showroom()


# Main Menu

while True:

    print("""

     CAR SHOWROOM MANAGEMENT SYSTEM

1. Add Car     2. View Cars    3. Search Car
4. Remove Car   5. Update Car   6. Add Customer
7. View Customer    8. Sell Car 9. View Sold Cars
10. View Sales  11. Save Cars   12. Load Cars
                0. Exit

""")

    choice = int(input("Enter your choice: "))


    # Add Car

    if choice == 1:

        car_id = int(input("Enter Car ID: "))
        brand = input("Enter Car Brand: ")
        model = input("Enter Car Model: ")
        year = int(input("Enter Car Year: "))
        color = input("Enter Car Color: ")
        price = input("Enter Car Price: ")
        mileage = input("Enter Car Mileage: ")

        car = Car(
            car_id,
            brand,
            model,
            year,
            color,
            price,
            mileage
        )

        showroom.add_car(car)

        print("Car added successfully!")


    # View Cars

    elif choice == 2:

        showroom.view_cars()


    # Search Car

    elif choice == 3:

        car_id = int(input("Enter Car ID: "))

        showroom.search_car(car_id)


    # Remove Car

    elif choice == 4:

        car_id = int(input("Enter Car ID: "))

        showroom.remove_car(car_id)


    # Update Car

    elif choice == 5:

        car_id = int(input("Enter Car ID: "))

        showroom.update_car(car_id)


    # Add Customer

    elif choice == 6:

        customer_id = int(input("Enter Customer ID: "))
        name = input("Enter Customer Name: ")
        phone = input("Enter Customer Phone: ")
        address = input("Enter Customer Address: ")

        customer = Customer(
            customer_id,
            name,
            phone,
            address
        )

        showroom.add_customer(customer)

        print("Customer added successfully!")


    # View Customer

    elif choice == 7:

        showroom.view_customer()


    # Sell Car

    elif choice == 8:

        car_id = int(input("Enter Car ID: "))
        customer_id = int(input("Enter Customer ID: "))

        showroom.sell_car(car_id, customer_id)


    # View Sold Cars

    elif choice == 9:

        showroom.sold_car()


    # View Sales

    elif choice == 10:

        showroom.view_sales()


    # Save Cars

    elif choice == 11:

        showroom.save_cars()

        print("Cars saved successfully!")


    # Load Cars

    elif choice == 12:

        showroom.load_cars()

        print("Cars loaded successfully!")


    # Exit

    elif choice == 0:

        print("Program closed!")
        break


    # Invalid Choice

    else:

        print("Invalid choice!")