def capacity_of_triangle_with_base(base_width):
  if base_width == 1:
    return 1
  return base_width + capacity_of_triangle_with_base(base_width - 1)

print(capacity_of_triangle_with_base(6))