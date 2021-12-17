
lines = 'target area: x=85..145, y=-163..-108'
test_lines = 'target area: x=20..30, y=-10..-5'
# target = ((20, 30), (-10,-5))
target = ((85, 145), (-163,-108))

valid_vels = set()
max_height = 0
for x in range(1000):
    for y in range(-1000, 1000):
        x_vel, y_vel = x, y
        x_pos, y_pos = 0, 0
        apex = 0
        while x_pos <= target[0][1] and y_pos >= target[1][0]:
            if target[0][0] <= x_pos <= target[0][1] and target[1][0] <= y_pos <= target[1][1]:
                max_height = max(max_height, apex)
                valid_vels.add((x, y))
                break
            x_pos += x_vel
            y_pos += y_vel
            x_vel = max(x_vel-1, 0)
            y_vel -= 1
            apex = max(apex, y_pos)

print('Part one: ',max_height)
print('Part two: ', len(valid_vels))