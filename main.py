import turtle as turtle_module
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# print(colors)

# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [ (216, 162, 94), (239, 212, 87), (217, 122, 165), (168, 77, 43), (207, 220, 230), (115, 175, 222), (210, 225, 212), (212, 84, 132), (60, 127, 62), (68, 43, 37), (72, 107, 213), (241, 167, 190), (161, 56, 105), (231, 83, 61), (67, 86, 143), (77, 165, 64), (126, 191, 168), (34, 86, 40), (164, 195, 44), (130, 43, 32), (215, 182, 174), (167, 210, 195), (183, 27, 57), (163, 210, 215), (22, 100, 103), (173, 183, 223), (40, 68, 36), (76, 62, 50)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()