def print_pizza_area(pizza_diameter):
    pi_val = 3.14159265
    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    print('{:.1f} inch pizza is {:.3f} inches squared'.format(pizza_diameter, pizza_area))

print_pizza_area(10)

def print_pizza_volume(pizza_diameter, pizza_height):
    pi_val = 3.14159265

    pizza_radius = pizza_diameter / 2.0
    pizza_area = pi_val * pizza_radius * pizza_radius
    pizza_volume = pizza_area * pizza_height
    print('{:.1f} x {:.1f} inch pizza is {:.3f} inches cubed.'.format(pizza_diameter, pizza_height, pizza_volume))

print_pizza_volume(5,2)