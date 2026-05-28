import math

# Gegebene mittlere Cones
middle_outer = (-1.5, -5.0, 0.0)
middle_inner = ( 1.5, -5.0, 0.0)

# Radien
r_inner = 15.25 / 2        # 7.625 m
r_outer = 21.25 / 2        # 10.625 m

# Abstand Zentren
center_distance = 18.25
half_center = center_distance / 2.0

# y-Koordinate des Kreis-Zentrums berechnen:
center_y = middle_inner[1] - r_inner

# X-Mittelpunkt
x_mid = middle_inner[0]

# Kreiszentren
center_left  = (x_mid - half_center, center_y, 0.0)
center_right = (x_mid + half_center, center_y, 0.0)

# Anzahl Cones
n_inner = 16
n_outer = 16


def generate_cones(center, radius, n, z=0.04):
    cx, cy, _ = center
    cones = []
    for k in range(n):
        theta = math.pi/2 + 2*math.pi*k/n
        x = cx + radius * math.cos(theta)
        y = cy + radius * math.sin(theta)
        cones.append((round(x,6), round(y,6), z))
    return cones


left_inner  = generate_cones(center_left,  r_inner, n_inner)
left_outer  = generate_cones(center_left,  r_outer, n_outer)
right_inner = generate_cones(center_right, r_inner, n_inner)
right_outer = generate_cones(center_right, r_outer, n_outer)

# JSON-Ausgabeformat
def print_json(cones):
    for x,y,z in cones:
        print(f'{{{x},{y},{z}}},')


print("// LEFT INNER")
print_json(left_inner)

print("// LEFT OUTER")
print_json(left_outer)

print("// RIGHT INNER")
print_json(right_inner)

print("// RIGHT OUTER")
print_json(right_outer)
