width = 20
height = 15
snake = [[width // 2, height // 2]]
direction = [1, 1]
head = [width // 2, height // 2]
frame = [[' '] * width + ['\n']] * height
frame[head[1]][head[0]] = 'S'

while True:
    head[0] = head[0] + direction[0]
    head[1] = head[1] + direction[1]
    if head[0] > width:
        head[0] = 0
    elif head[0] < 0:
        head[0] = width
    if head[1] > height:
        head[1] = 0
    elif head[1] < 0:
        head[1] = height
    
    frame[head[1]][head[0]] = "S"
    for line in frame:
        print(''.join(line))
    