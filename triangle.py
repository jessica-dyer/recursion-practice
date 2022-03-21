from cmath import sqrt

def area_of_equilateral_triangle(side):
  area = (sqrt(3) / 4) * side**2
  return area

def area_of_sierpinski_step(base, number_of_steps):
  if number_of_steps == 0:
     return area_of_equilateral_triangle(base)
  else:
    return area_of_sierpinski_step(base*.5, number_of_steps - 1) * 3

print(area_of_sierpinski_step(10, 10))