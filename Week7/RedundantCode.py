
pi_val = 3.14159265

pizza_diameter_1 = 12.0
circle_radius_1 = pizza_diameter_1 / 2.0
circle_area_1 = pi_val * circle_radius_1 * circle_radius_1

pizza_diameter_2 = 14.0
circle_radius_2 = pizza_diameter_2 / 2.0
circle_area_2 = pi_val * circle_radius_2 * circle_radius_2

total_pizza_area = circle_area_1 + \
                  circle_area_2
print("total pizza area: ", round(total_pizza_area,2))

def calc_circle_area(circle_diameter):
    pi_val = 3.14159265
    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius * circle_radius
    return circle_radius

pizza_diameter_1 = 12
pizza_diameter_2 = 14
total_pizza_area = calc_circle_area(pizza_diameter_1) +\
            calc_circle_area(pizza_diameter_2)
print('A 12 and 14 inch pizza has', end=' ')
print('{:.2f}'.format(total_pizza_area), end=' ')
print('inches squared combined.')
