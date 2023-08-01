# test_module3.py

from car import Car

def test_car_class():
    # Create an instance of the Car class
    car1 = Car("Toyota", "Camry", 2022)

    # Test get_description() method
    assert car1.get_description() == "2022 Toyota Camry"

    # Test start_engine() method
    assert car1.start_engine() == "Engine started."

    print("All test cases passed successfully.")

if __name__ == "__main__":
    test_car_class()

