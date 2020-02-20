def calc_circle_area(circle_diameter):
    pi_val = 3.14159265

    circle_radius = circle_diameter / 2.0
    circle_area = pi_val * circle_radius * circle_radius
    return circle_area
7
def pizza_calories(pizza_diameter):
    calories_per_square_inch = 16.7    # Regular crust pepperoni pizza

    total_calories = calc_circle_area(pizza_diameter) * calories_per_square_inch
    return total_calories

print('12 inch pizza has {:.2f} calories.'.format(pizza_calories(12.0)))
print('14 inch pizza has {:.2f} calories.'.format(pizza_calories(14.0)))

def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet

def steps_to_calories(num_steps):
    steps_per_minute = 70.0
    calories_per_minute_walking = 3.5

    minutes = num_steps / steps_per_minute
    calories = minutes * calories_per_minute_walking
    return calories

steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print('Feet:', feet)

calories = steps_to_calories(steps)
print('Calories:', calories)