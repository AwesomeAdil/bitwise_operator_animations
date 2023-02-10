import time
import turtle
import sys

if len(sys.argv) != 3:
    exit()
vivax=turtle.Turtle()
vivax.speed(10)
def Multiple_Squares(length, colour, dis, fc, bit):
  vivax.fillcolor(fc)
  # start the filling color
  vivax.begin_fill()
  vivax.setx(dis)
  vivax.pencolor(colour)
  vivax.pensize(4)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.forward(length)
  vivax.right(90)
  vivax.end_fill()
  vivax.setheading(360)
  x, y = vivax.position()
  vivax.setx(x + 7)
  vivax.write(bit, font=("Verdana", 50, "normal"))
  vivax.setx(x)
  vivax.ht()

n = 16


vivax.penup()
scale = 16 ## equals to hexadecimal
num_of_bits = 8

mask = bin(int(sys.argv[2], scale))[2:].zfill(n)
vivax.setx(-400)
vivax.sety(0)

for i in range(n):
    vivax.setx(vivax.position()[0] + 7)
    vivax.write(mask[i], font=("Verdana", 50, "normal"))
    vivax.setx(vivax.position()[0] - 7)
    vivax.setx(vivax.position()[0] + 50)


vivax.setx(-400)
vivax.sety(50)
vivax.pendown()

for i in range(n):
  Multiple_Squares(50,"black", -400 + 50 * i, "red" if int(mask[i] or int(sys.argv[1][i])) else "gray", sys.argv[1][i])

vivax.penup()
vivax.setx(-400)
vivax.sety(-75)

res = ""
for i in range(n):
    vivax.setx(vivax.position()[0] + 7)
    vivax.write("1" if (int(mask[i]) or int(sys.argv[1][i])) else "0" , font=("Verdana", 50, "normal"))
    vivax.setx(vivax.position()[0] - 7)
    vivax.setx(vivax.position()[0] + 50)
    res += "1" if (int(mask[i]) or int(sys.argv[1][i])) else "0"

print(res)

time.sleep(4)
