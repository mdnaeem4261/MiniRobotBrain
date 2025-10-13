# MiniRobotBrain - Simple Robot Simulator on 5x5 grid

# Robot's initial state
robot_position = [0, 0]  # [x, y], bottom-left corner
robot_direction = "North"  # Facing North

# Function to turn robot
def turn(direction):
    global robot_direction
    turns = ["North", "East", "South", "West"]
    idx = turns.index(robot_direction)
    if direction == "right":
        robot_direction = turns[(idx + 1) % 4]
    elif direction == "left":
        robot_direction = turns[(idx - 1) % 4]

# Function to move robot
def move():
    global robot_position, robot_direction
    x, y = robot_position
    if robot_direction == "North" and y < 4:
        y += 1
    elif robot_direction == "South" and y > 0:
        y -= 1
    elif robot_direction == "East" and x < 4:
        x += 1
    elif robot_direction == "West" and x > 0:
        x -= 1
    else:
        print("Cannot move further in this direction!")
    robot_position = [x, y]

# Function to report robot status
def report():
    print(f"Robot is at {tuple(robot_position)}, facing {robot_direction}")

# Main loop
print("Welcome to MiniRobotBrain!")
print("Commands: move, left, right, report, exit")

while True:
    command = input("Enter command: ").lower()
    if command == "move":
        move()
    elif command == "left" or command == "right":
        turn(command)
    elif command == "report":
        report()
    elif command == "exit":
        print("Exiting MiniRobotBrain. Bye!")
        break
    else:
        print("Unknown command! Try move, left, right, report, exit.")

