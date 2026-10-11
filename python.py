"""
DATASETS REQUIRED BY THE PROGRAMS
Run this block once first. It creates the CSV files in the current folder.
(sales_data.csv is shared by Slip 5 and Slip 24)
"""

datasets = {
    "sales_data.csv": "Advertising_Budget,Sales,Amazon,Mesho,Flipcart\n934,4287,92,78,53\n1526,7167,144,115,95\n1997,8016,173,145,100\n2499,10581,229,160,139\n2968,13142,257,208,153\n3481,13882,290,220,195\n4038,16177,342,256,213\n4585,18516,386,287,239\n5026,21441,417,321,257\n5573,23054,464,349,275\n6006,25564,510,373,305\n6561,28238,539,403,335\n",
    "youtube_data.csv": "Likes,Views\n500,10455\n1000,19413\n1500,27551\n2000,36228\n2500,45579\n3000,55245\n3500,62277\n4000,71742\n4500,80663\n5000,90906\n",
    "salary_data.csv": "Years of Experience,Salary\n1,33487\n1.5,36364\n2,38045\n3,45966\n4,52853\n5,57569\n6,63611\n7,70912\n8,78495\n9,81641\n10,89967\n11,95494\n",
    "car_data.csv": "Car_Age,Selling_Price\n1,848741\n2,782258\n2,756495\n3,687152\n4,633564\n5,531338\n6,474059\n7,415966\n8,367850\n9,286074\n10,220845\n12,74203\n",
    "advertising.csv": "TV,Radio,Newspaper,Sales\n230,37,69,21.1\n44,39,45,11.7\n17,45,69,12.8\n151,41,58,17.0\n180,10,58,12.5\n8,48,75,13.4\n57,32,23,11.5\n120,19,11,12.5\n199,3,48,12.6\n66,11,26,7.8\n214,24,4,17.9\n23,35,65,11.1\n",
    "employee_data.csv": "Employee_ID,Name,Department,Salary\n101,Rahul,IT,45000\n102,Priya,HR,50000\n103,Amit,IT,\n104,Sneha,Finance,60000\n105,Neha,,48000\n102,Priya,HR,50000\n106,Kiran,IT,52000\n104,Sneha,Finance,60000\n107,Rajesh,HR,47000\n",
    "item.csv": "cost,type\n120,Grocery\n850,Electronics\n45,Stationery\n1500,Electronics\n300,Clothing\n75,Grocery\n60,Stationery\n999,Clothing\n220,Grocery\n1799,Electronics\n",
    "employee.csv": "Employee ID,Salary,Department\n1,45000,IT\n2,50000,HR\n3,60000,Finance\n4,,IT\n5,52000,\n6,48000,HR\n7,70000,IT\n",
}

for file_name, content in datasets.items():
    with open(file_name, "w") as f:
        f.write(content)

print("Dataset files created:", ", ".join(datasets))


"""
SLIP 1
Slip No: 1
"""

"""
Q1) A: Write a python program to show proper indentation using if statement.
"""
age = int(input("Enter your age: "))
if age >= 18:
 print("You are eligible to vote.")
else:
 print("You are not eligible to vote.")

"""
Q2) B: Write a python program to implement Water Jug Problem.
"""
from collections import deque

def water_jug(cap1, cap2, target):
    start = (0, 0)
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path

        if (a, b) in visited:
            continue
        visited.add((a, b))

        pour12 = min(a, cap2 - b)
        pour21 = min(b, cap1 - a)

        next_states = [
            (cap1, b), (a, cap2), (0, b), (a, 0),
            (a - pour12, b + pour12),
            (a + pour21, b - pour21)
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path + [state]))
    return None

path = water_jug(4, 3, 2)
print("Steps:")
if path:
    for state in path:
        print(state)
else:
    print("No solution found.")

"""
OR - Q2) B: Write a python program to design a Model-Based Agent that maintains an
    internal state of room cleanliness and decides actions based on both current
    perception and stored memory.
"""
memory = {"A": "Unknown", "B": "Unknown"}

location = input("Current room (A/B): ").strip().upper()
perception = input("Room status (Clean/Dirty): ").strip().capitalize()

if location not in memory or perception not in ["Clean", "Dirty"]:
    print("Invalid input.")
else:
    memory[location] = perception

    if perception == "Dirty":
        action = "Suck"
    elif location == "A":
        action = "Move Right"
    else:
        action = "Move Left"

    print("Updated memory:", memory)
    print("Action:", action)


"""
SLIP 2
Slip No: 2
"""

"""
Q1) A: Write a python program to implement Tower of Hanoi using recursion.
"""
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))
if n > 0:
    tower_of_hanoi(n, "A", "B", "C")
else:
    print("Enter a positive number.")

"""
Q2) B: Write a python program to implement Mini-Max Algorithm.
"""
def minimax(tree, node, maximizing):
    children = tree.get(node, [])

    if not children:
        return node

    values = [minimax(tree, child, not maximizing) for child in children]

    if maximizing:
        return max(values)
    return min(values)

tree = {
    "A": ["B", "C"],
    "B": [3, 5],
    "C": [2, 9]
}
print("Best value:", minimax(tree, "A", True))

"""
OR - Q2) B: Write a python program that predicts temperature based on the number of
    icecreams sold using Linear Regression Create Dataframe which contain temperature and
    number of icecream sold.
(answer not in your docx - added by me)
"""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Icecream_Sold": [20, 35, 50, 65, 80, 95, 110],
    "Temperature": [20, 23, 26, 29, 32, 35, 38]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Icecream_Sold"]]
y = df["Temperature"]

model = LinearRegression()
model.fit(X, y)

icecreams = int(input("\nEnter number of icecreams sold: "))

prediction = model.predict(pd.DataFrame({"Icecream_Sold": [icecreams]}))

print("Predicted Temperature:", round(prediction[0], 2), "°C")


"""
SLIP 3
Slip No: 3
"""

"""
Q1) A: Write a python program to simulate a simple reflex agent for fan control.
"""

def fan_agent(temperature):

    if temperature >= 30:
        return "Fan ON - High Speed"

    elif temperature >= 25:
        return "Fan ON - Low Speed"

    else:
        return "Fan OFF"


temperature = float(input("Enter room temperature: "))

action = fan_agent(temperature)

print("Room Temperature:", temperature, "°C")
print("Fan Action:", action)

"""
Q2) B: Write a python program to develop fitness predictors using Random Forest
    Classification to predict whether a person is FIT or UNFIT based on: Age, Exercise
    Hours per Week Accept the input from user and predict for multiple people.
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Exercise_Hours": [6, 5, 7, 4, 3, 2, 1, 0],
    "Fitness": ["FIT", "FIT", "FIT", "FIT",
                "UNFIT", "UNFIT", "UNFIT", "UNFIT"]
})

print("Training Dataset:")
print(df)

X = df[["Age", "Exercise_Hours"]]
y = df["Fitness"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X, y)

n = int(input("\nEnter number of people: "))

for i in range(n):
    print("\nPerson", i + 1)

    age = int(input("Enter age: "))
    hours = float(input("Enter exercise hours per week: "))

    person = pd.DataFrame({
        "Age": [age],
        "Exercise_Hours": [hours]
    })

    prediction = model.predict(person)[0]

    print("Fitness Status:", prediction)

"""
OR - Q2) B: Write a python program to simulate n-Queens problem.
"""

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col

            if solve_n_queens(board, row + 1, n):
                return True

            board[row] = -1

    return False

n = int(input("Enter the value of N: "))

board = [-1] * n

if solve_n_queens(board, 0, n):
    print("Solution found!")
else:
    print("No solution exists.")


"""
SLIP 4
Slip No: 4
"""

"""
Q1) A: Write a python program to predict if a Person is Eligible to Vote (Age ≥ 18) using
    simple Logistic Classification. Accept person age from user.
"""

from sklearn.linear_model import LogisticRegression

X = [[10], [15], [17], [18], [20], [25], [30]]
y = [0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

age = int(input("Enter your age: "))

prediction = model.predict([[age]])

if prediction[0] == 1:
    print("Person is Eligible to Vote.")
else:
    print("Person is Not Eligible to Vote.")

"""
Q2) B: Write a python program to Implement Alpha-Beta Pruning .
"""

def alpha_beta(depth, node, is_max, values, alpha, beta):

    if depth == 2:
        return values[node]

    if is_max:
        best = -999

        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i,
                             False, values, alpha, beta)

            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in range(2):
            val = alpha_beta(depth + 1, node * 2 + i,
                             True, values, alpha, beta)

            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 10, 9, 1, 2, 0, -1]

result = alpha_beta(0, 0, True, values, -999, 999)

print("Optimal value:", result)

"""
OR - Q2) B: Write a Python program to Plot a scatter graph of sepal length vs sepal width
    for the Iris dataset. Label the axes and add a title.
(answer not in your docx - added by me)
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

plt.scatter(X[:, 0], X[:, 1])

plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Length vs Sepal Width (Iris Dataset)")

plt.show()


"""
SLIP 5
Slip No: 5
"""

"""
Q1) A: Write a python program to visualize a dataset using scatter plot for sales_data.csv
    containing Advertising_Budget, Sales.
"""
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sales_data.csv")

plt.scatter(data["Advertising_Budget"], data["Sales"])

plt.xlabel("Advertising Budget")
plt.ylabel("Sales")
plt.title("Advertising Budget vs Sales")

plt.show()

"""
Q2) B: Apply Linear Regression on a YouTube Video dataset to predict video views using
    relevant video attributes. Visualize the relationship between the predictor and target
    variable using a scatter plot and regression line.
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv("youtube_data.csv")

X = data[["Likes"]]
y = data["Views"]

model = LinearRegression()
model.fit(X, y)

likes = int(input("Enter number of likes: "))
predicted_views = model.predict([[likes]])

print("Predicted Views:", int(predicted_views[0]))

plt.scatter(X["Likes"], y, label="Actual Data")

plt.plot(X["Likes"], model.predict(X), color="red",
         label="Regression Line")

plt.xlabel("Likes")
plt.ylabel("Views")
plt.title("YouTube Likes vs Views - Linear Regression")
plt.legend()
plt.show()

"""
OR - Q2) B: Write a pyhton program to create a simple chatbot using predefined rules to
    respond to user inputs.
"""

print("Chatbot: Hello! Welcome to my chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Chatbot: Hello! How are you?")

    elif user == "how are you":
        print("Chatbot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Chatbot: I am a simple chatbot.")

    elif user == "what is ai":
        print("Chatbot: AI stands for Artificial Intelligence.")

    elif user == "thank you":
        print("Chatbot: You are welcome!")

    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")


"""
SLIP 6
Slip No: 6
"""

"""
Q1) A: Write a python program to implement Hill Climbing Algorithm .
"""

def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        current_value = -(current - 3)**2 + 9
        left_value = -(left - 3)**2 + 9
        right_value = -(right - 3)**2 + 9

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, current_value


start = int(input("Enter starting point: "))

point, value = hill_climbing(start)

print("Best point:", point)
print("Maximum value:", value)

"""
Q2) B: Write a python program to Plot a scatter graph of petal length vs petal width for
    the Iris dataset. Label the axes and add a title.
(answer not in your docx - added by me)
"""
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

plt.scatter(X[:, 2], X[:, 3])

plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.title("Petal Length vs Petal Width (Iris Dataset)")

plt.show()

"""
OR - Q2) B: Write a python program to implement the Alpha–Beta pruning with depth limit
    and heuristic.
(same program as Slip 21 Q1)
"""

def heuristic(node):
    return node


def alpha_beta(node, depth, alpha, beta, maximizing_player):

    if depth == 0:
        return heuristic(node)

    children = [node - 2, node - 1, node + 1, node + 2]

    if maximizing_player:
        best_value = float("-inf")

        for child in children:
            value = alpha_beta(
                child, depth - 1, alpha, beta, False
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value

    else:
        best_value = float("inf")

        for child in children:
            value = alpha_beta(
                child, depth - 1, alpha, beta, True
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                break

        return best_value


print("===== Alpha-Beta Pruning =====")

initial_value = int(input("Enter initial value: "))
depth = int(input("Enter depth limit: "))

result = alpha_beta(
    initial_value,
    depth,
    float("-inf"),
    float("inf"),
    True
)

print("\nBest heuristic value:", result)


"""
SLIP 7
Slip No: 7
"""

"""
Q1) A: Write a python program to create a DataFrame containing Employee Name, Department
    and Salary. Display the employees who satisfy all the following conditions: Department
    = ‘IT’, Salary > 50000, and Employee Name contains the letter ‘a’.
(answer not in your docx - added by me)
"""
import pandas as pd

data = {
    "Employee Name": ["Amit", "Sneha", "Rahul", "Priya", "Kiran", "Rajesh"],
    "Department": ["IT", "IT", "HR", "IT", "Finance", "IT"],
    "Salary": [60000, 45000, 70000, 55000, 52000, 40000]
}

df = pd.DataFrame(data)

print("All Employees:")
print(df)

result = df[
    (df["Department"] == "IT") &
    (df["Salary"] > 50000) &
    (df["Employee Name"].str.contains("a", case=False))
]

print("\nEmployees satisfying all conditions:")
print(result)

"""
Q2) B: Write a python program to simulate a Model-Based Agent for Smart Home Security. A
    smart home security system monitors the main door. The agent should use both the
    previous door status and the current door status to decide the appropriate security
    action. The door can have two states: OPEN / CLOSED The program should accept the
    previous and current door status from the user and display the appropriate action.
    Display an error message if the user enters any value other than OPEN or CLOSED.
(answer not in your docx - added by me)
"""

previous = input("Enter previous door status (OPEN/CLOSED): ").strip().upper()
current = input("Enter current door status (OPEN/CLOSED): ").strip().upper()

if previous not in ["OPEN", "CLOSED"] or current not in ["OPEN", "CLOSED"]:
    print("Error: Please enter only OPEN or CLOSED.")

else:
    print("\nPrevious Door Status:", previous)
    print("Current Door Status:", current)

    if previous == "CLOSED" and current == "OPEN":
        action = "ALERT - Door has been opened! Sound alarm and notify owner."
    elif previous == "OPEN" and current == "OPEN":
        action = "WARNING - Door is still open. Send reminder."
    elif previous == "OPEN" and current == "CLOSED":
        action = "Door closed. System is secure."
    else:
        action = "Door remains closed. No action required."

    print("Security Action:", action)

"""
OR - Q2) B: Write a python program to implement Breadth First Search (BFS) for graph
    traversal. Display the traversal order starting from a given source vertex.
(answer not in your docx - added by me)
"""
from collections import deque

def bfs(graph, start):
    visited = [start]
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = input("Enter source vertex: ").upper()

if start in graph:
    print("BFS Traversal:", bfs(graph, start))
else:
    print("Invalid vertex")


"""
SLIP 8
Slip No: 8
"""

"""
Q1) A: Write a python program to simulate the Monkey Banana Problem. Initialize the
    monkey's position, perform the necessary actions to reach the banana, and use
    conditional statements to determine whether the goal state has been achieved.
(answer not in your docx - added by me)
"""

monkey = "Door"
box = "Window"
banana = "Center"
on_box = False
has_banana = False

print("Initial State:")
print("Monkey at:", monkey)
print("Box at:", box)
print("Banana at:", banana)
print()

if monkey != box:
    monkey = box
    print("Action: Monkey walks to the box at", box)

if box != banana and monkey == box:
    box = banana
    monkey = banana
    print("Action: Monkey pushes the box to", banana)

if monkey == box and not on_box:
    on_box = True
    print("Action: Monkey climbs on the box")

if on_box and box == banana:
    has_banana = True
    print("Action: Monkey grabs the banana")

if has_banana:
    print("\nGoal state achieved: Monkey has the banana!")
else:
    print("\nGoal state not achieved.")

"""
Q2) B: Write a python program to implement a Logistic Regression classifier for Diabetes
    Prediction. Train the model using a sample dataset and predict the diabetes status
    (Diabetic/Non-Diabetic) for multiple persons based on Fasting Blood Sugar, Post-Meal
    Blood Sugar, Age, and BMI.
(answer not in your docx - added by me)
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Fasting_Sugar": [85, 90, 95, 100, 105, 126, 135, 150, 160, 110, 140, 92],
    "PostMeal_Sugar": [120, 130, 125, 140, 150, 200, 220, 250, 260, 160, 210, 128],
    "Age": [25, 30, 28, 35, 40, 50, 55, 60, 65, 38, 52, 27],
    "BMI": [22, 24, 23, 26, 27, 31, 33, 35, 36, 28, 32, 23],
    "Diabetic": [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

print("Training Dataset:")
print(df)

X = df[["Fasting_Sugar", "PostMeal_Sugar", "Age", "BMI"]]
y = df["Diabetic"]

model = LogisticRegression(max_iter=10000)
model.fit(X, y)

n = int(input("\nEnter number of persons: "))

for i in range(n):
    print("\nPerson", i + 1)

    fasting = float(input("Enter Fasting Blood Sugar: "))
    post_meal = float(input("Enter Post-Meal Blood Sugar: "))
    age = int(input("Enter Age: "))
    bmi = float(input("Enter BMI: "))

    person = pd.DataFrame({
        "Fasting_Sugar": [fasting],
        "PostMeal_Sugar": [post_meal],
        "Age": [age],
        "BMI": [bmi]
    })

    prediction = model.predict(person)[0]

    if prediction == 1:
        print("Status: Diabetic")
    else:
        print("Status: Non-Diabetic")

"""
OR - Q2) B: Write a python program for DataFrame of employees with Salary and Experience:
    If Experience < 3 years, increase salary by 10%, else increase by 5%. and display
    updated DataFrame.
"""
import pandas as pd

data = {
    "Employee": ["Amit", "Sneha", "Rahul", "Priya"],
    "Salary": [40000, 50000, 60000, 45000],
    "Experience": [2, 5, 3, 1]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df["Updated Salary"] = df.apply(
    lambda row: row["Salary"] * 1.10
    if row["Experience"] < 3
    else row["Salary"] * 1.05,
    axis=1
)

print("\nUpdated DataFrame:")
print(df)


"""
SLIP 9
Slip No: 9
"""

"""
Q1) A: Write a program to create a DataFrame which contains a person name and age ,Sort a
    DataFrame in ascending order of Age
"""
import pandas as pd

data = {
    "Name": ["Rahul", "Sneha", "Amit", "Priya", "Kiran"],
    "Age": [25, 22, 30, 20, 28]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df = df.sort_values(by="Age")

print("\nDataFrame sorted by Age:")
print(df)

"""
Q2) B: Write a program to implement the Blocks World Problem. Represent the initial and
    goal states of a set of blocks, perform valid block movements according to the problem
    constraints and display each intermediate state until the goal configuration is
    achieved.
"""

blocks = {
    "A": "B",
    "B": "Table",
    "C": "Table"
}

goal = {
    "A": "Table",
    "B": "C",
    "C": "Table"
}

def display_state():
    print("A ->", blocks["A"])
    print("B ->", blocks["B"])
    print("C ->", blocks["C"])
    print()

print("Initial State:")
display_state()

if blocks["A"] == "B":
    blocks["A"] = "Table"
    print("Move A from B to Table")
    display_state()

if blocks["B"] == "Table" and blocks["C"] == "Table":
    blocks["B"] = "C"
    print("Move B from Table to C")
    display_state()

if blocks == goal:
    print("Goal State Achieved!")
else:
    print("Goal State Not Achieved.")

"""
OR - Q2) B: Write a program to implement Depth First Search (DFS) for graph traversal.
    Display the traversal order f starting from a given source vertex.
"""

def dfs(graph, vertex, visited):
    visited.append(vertex)

    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = input("Enter source vertex: ").upper()

if start in graph:
    visited = []
    dfs(graph, start, visited)
    print("DFS Traversal:", visited)
else:
    print("Invalid vertex")


"""
SLIP 10
Slip No: 10
"""

"""
Q1) A: Write a program to separate the features and target variable from a dataset. Split
    the dataset into training and testing sets display the shapes of the original dataset,
    training dataset, and testing dataset. Use any suitable dataset.
"""
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

X = df.drop("target", axis=1)
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Original Dataset Shape:", df.shape)
print("Training Dataset Shape:", X_train.shape)
print("Testing Dataset Shape:", X_test.shape)

"""
Q2) B: Write a program to implement the Prisoner's Dilemma using a predefined payoff
    matrix. The program should accept the strategies of two prisoners (Cooperate or
    Defect), evaluate the corresponding payoffs, and display the outcome. Ensure that
    appropriate validation is performed for invalid inputs.
"""

payoff = {
    ("Cooperate", "Cooperate"): (3, 3),
    ("Cooperate", "Defect"): (0, 5),
    ("Defect", "Cooperate"): (5, 0),
    ("Defect", "Defect"): (1, 1)
}

p1 = input("Enter Prisoner 1 strategy (Cooperate/Defect): ").capitalize()
p2 = input("Enter Prisoner 2 strategy (Cooperate/Defect): ").capitalize()

if p1 not in ["Cooperate", "Defect"] or p2 not in ["Cooperate", "Defect"]:
    print("Invalid input! Please enter only Cooperate or Defect.")

else:
    payoff1, payoff2 = payoff[(p1, p2)]

    print("\nPrisoner 1 Strategy:", p1)
    print("Prisoner 2 Strategy:", p2)
    print("Prisoner 1 Payoff:", payoff1)
    print("Prisoner 2 Payoff:", payoff2)

    if p1 == "Cooperate" and p2 == "Cooperate":
        print("Outcome: Both prisoners cooperate.")
    elif p1 == "Defect" and p2 == "Defect":
        print("Outcome: Both prisoners defect.")
    elif p1 == "Defect" and p2 == "Cooperate":
        print("Outcome: Prisoner 1 defects and Prisoner 2 cooperates.")
    else:
        print("Outcome: Prisoner 1 cooperates and Prisoner 2 defects.")

"""
OR - Q2) B: Write a python program to solve the N-Queens problem using a backtracking
    approach. Display one valid arrangement of N queens on an N × N chessboard such that
    no two queens attack each other
"""

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False

    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


n = int(input("Enter value of N: "))

board = [-1] * n

if solve(board, 0, n):
    print("\nOne valid arrangement:")

    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists.")


"""
SLIP 11
Slip No: 11
"""

"""
Q1) A: Write a python program to read the salary_data.csv dataset, train a Linear
    Regression model using Years of Experience as the feature and Salary as the target and
    predict the salary for a new employee.
"""
import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("salary_data.csv")

X = data[["Years of Experience"]]
y = data["Salary"]

model = LinearRegression()
model.fit(X, y)

years = float(input("Enter Years of Experience: "))

salary = model.predict([[years]])

print("Predicted Salary:", salary[0])

"""
Q2) B: Write a python program to implement the Water Jug Problem.
"""
from collections import deque

jug1 = 4
jug2 = 3

goal = 2

start = (0, 0)

queue = deque([start])
visited = {start}

while queue:
    a, b = queue.popleft()

    print("Jug 1:", a, "Jug 2:", b)

    if a == goal:
        print("Goal achieved!")
        break

    states = [
        (jug1, b),
        (a, jug2),
        (0, b),
        (a, 0),
        (a - min(a, jug2 - b), b + min(a, jug2 - b)),
        (a + min(b, jug1 - a), b - min(b, jug1 - a))
    ]

    for state in states:
        if state not in visited:
            visited.add(state)
            queue.append(state)

"""
OR - Q2) B: Write a python program using Logistic Regression to detect credit card fraud
    using the following features: Transaction Amount, Card Age (in years), Transaction
    Time (023),Location Match Score (0–100),Online Transaction (1 = Yes, 0 = No),Train the
    model and predict fraud (1) or legit (0) based on user input.
"""
import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Amount": [100, 500, 2000, 50, 1500, 3000, 80, 2500, 120, 1800],
    "Card_Age": [5, 4, 1, 8, 2, 1, 7, 2, 6, 1],
    "Time": [10, 14, 23, 9, 22, 2, 11, 1, 15, 23],
    "Location_Match": [90, 80, 20, 95, 30, 10, 85, 15, 90, 25],
    "Online": [0, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    "Fraud": [0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Amount", "Card_Age", "Time", "Location_Match", "Online"]]

y = df["Fraud"]

model = LogisticRegression()
model.fit(X, y)

print("\nEnter transaction details:")

amount = float(input("Transaction Amount: "))
card_age = float(input("Card Age (years): "))
time = float(input("Transaction Time (0-23): "))
location = float(input("Location Match Score (0-100): "))
online = int(input("Online Transaction (1=Yes, 0=No): "))

new_transaction = [[amount, card_age, time, location, online]]
prediction = model.predict(new_transaction)

if prediction[0] == 1:
    print("\nPrediction: Fraud")
else:
    print("\nPrediction: Legit")


"""
SLIP 12
Slip No: 12
"""

"""
Q1) A: Write a python program to read the car_data.csv dataset and visualize the
    relationship between Car_Age and Selling_Price using a Scatter Plot.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car_data.csv")

print(df.head())

plt.scatter(df["Car_Age"], df["Selling_Price"])

plt.title("Car Age vs Selling Price")
plt.xlabel("Car Age")
plt.ylabel("Selling Price")

plt.grid(True)

plt.show()

"""
Q2) B: Write a python program to implement the Prisoner's Dilemma using a predefined
    payoff matrix. The program should accept the strategies of two prisoners (Cooperate or
    Defect), evaluate the corresponding payoffs and display the outcome. Ensure that
    appropriate validation is performed for invalid inputs.
"""
payoff_matrix = {
("Cooperate", "Cooperate"): (3, 3),
("Cooperate", "Defect"): (0, 5),
("Defect", "Cooperate"): (5, 0),
("Defect", "Defect"): (1, 1)
}

p1 = input("Enter strategy for Prisoner 1 (Cooperate/Defect): ")
p2 = input("Enter strategy for Prisoner 2 (Cooperate/Defect): ")

p1 = p1.strip().capitalize()
p2 = p2.strip().capitalize()

if p1 not in ["Cooperate", "Defect"] or p2 not in ["Cooperate", "Defect"]:
    print("Invalid input. Please enter Cooperate or Defect.")
else:
    payoff1, payoff2 = payoff_matrix[(p1, p2)]


print("\n--- Prisoner's Dilemma Result ---")
print("Prisoner 1 Strategy:", p1)
print("Prisoner 2 Strategy:", p2)
print("Prisoner 1 Payoff:", payoff1)
print("Prisoner 2 Payoff:", payoff2)

if p1 == "Cooperate" and p2 == "Cooperate":
    print("Outcome: Both prisoners cooperate.")
elif p1 == "Defect" and p2 == "Defect":
    print("Outcome: Both prisoners defect.")
elif p1 == "Cooperate" and p2 == "Defect":
    print("Outcome: Prisoner 1 cooperates, Prisoner 2 defects.")
else:
    print("Outcome: Prisoner 1 defects, Prisoner 2 cooperates.")

"""
OR - Q2) B: Write a python program to simulate a Vacuum Cleaner Agent. The agent should
    accept the current location and the cleanliness status of the room as input and decide
    whether to move to another location, clean the room, or remain in the current
    location. Display the agent’s action based on the given conditions.
"""
location = input("Enter current location (A/B): ").upper()
status = input("Enter room status (Clean/Dirty): ").lower()

valid_location = location == "A" or location == "B"
valid_status = status == "clean" or status == "dirty"

print("\n--- Vacuum Cleaner Agent ---")

print("Current Location:", location)
print("Room Status:", status)

print("Invalid location" if not valid_location else "")
print("Invalid room status" if not valid_status else "")

action = "Invalid input"

if valid_location and valid_status and status == "dirty": action = "Clean the room"
if valid_location and valid_status and status == "clean" and location == "A": action = "Move to location B"
if valid_location and valid_status and status == "clean" and location == "B": action = "Move to location A"

print("Agent Action:", action)


"""
SLIP 13
Slip No: 13
"""

"""
Q1) A: Write a python program to check whether a given number is an Armstrong Number using
    a user-defined function.
"""
def is_armstrong(number):
    original_number = number
    digits = len(str(number))
    sum = 0

    while number > 0:
        digit = number % 10
        sum = sum + digit ** digits
        number = number // 10

    if sum == original_number:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if is_armstrong(num):
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")

"""
Q2) B: Write a python program to implement a Goal-Based Agent that finds a target object
    in a predefined environment.
"""

environment = ["Book", "Pen", "Bag", "Laptop", "Bottle", "Mobile"]

def goal_based_agent(target):
    print("Searching for:", target)

    for position, obj in enumerate(environment):
        print("Agent checks:", obj)

        if obj.lower() == target.lower():
            print("Goal achieved!")
            print(target, "found at position", position)
            return

    print("Goal not achieved.")
    print(target, "not found in the environment.")


target = input("Enter the target object: ")

goal_based_agent(target)

"""
OR - Q2) B: Write a python program to manage multiple student records using a dictionary
    and display the topper based on percentage.
"""

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    percentage = float(input("Enter percentage: "))

    students[name] = percentage

print("\nStudent Records:")
for name, percentage in students.items():
    print(name, ":", percentage, "%")

topper = max(students, key=students.get)

print("\nTopper:")
print("Name:", topper)
print("Percentage:", students[topper], "%")


"""
SLIP 14
Slip No: 14
"""

"""
Q1) A: Write a python program to create two sets and perform Union, Intersection,
    Difference and Symmetric Difference operations.
"""
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))

print("Intersection:", set1.intersection(set2))

print("Difference (Set1 - Set2):", set1.difference(set2))

print("Symmetric Difference:", set1.symmetric_difference(set2))

"""
Q2) B: Write a python program to implement a Utility-Based Agent that selects the best
    action based on the highest utility value.
"""

actions = {
    "Go by Bus": 60,
    "Go by Train": 80,
    "Go by Car": 70,
    "Go by Bike": 50
}

print("Available Actions and Utility Values:")

for action, utility in actions.items():
    print(action, ":", utility)

best_action = max(actions, key=actions.get)
highest_utility = actions[best_action]

print("\nBest Action:", best_action)
print("Highest Utility:", highest_utility)

"""
OR - Q2) B: Write a python program using user-defined functions to calculate Simple
    Interest and Compound Interest and display the difference between them.
"""
def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si


def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    ci = amount - principal
    return ci


principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest (%): "))
time = float(input("Enter Time (in years): "))

si = simple_interest(principal, rate, time)
ci = compound_interest(principal, rate, time)

difference = abs(ci - si)

print("\nSimple Interest:", round(si, 2))
print("Compound Interest:", round(ci, 2))
print("Difference:", round(difference, 2))


"""
SLIP 15
Slip No: 15
"""

"""
Q1) A: Write a python program to accept a string and count the number of vowels,
    consonants, digits, and special characters.
"""
text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special_characters = 0

for ch in text:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special_characters += 1

print("\nNumber of Vowels:", vowels)
print("Number of Consonants:", consonants)
print("Number of Digits:", digits)
print("Number of Special Characters:", special_characters)

"""
Q2) B: Write a python program to implement matrix addition, subtraction and transpose
    using nested lists.
"""

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8, 9],
    [10, 11, 12]
]

addition = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    addition.append(row)

subtraction = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] - B[i][j])
    subtraction.append(row)

transpose = []
for j in range(len(A[0])):
    row = []
    for i in range(len(A)):
        row.append(A[i][j])
    transpose.append(row)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

print("\nMatrix Addition:")
for row in addition:
    print(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)

print("\nTranspose of Matrix A:")
for row in transpose:
    print(row)

"""
OR - Q2) B: Write a python program to perform NumPy statistical operations (minimum,
    maximum, mean, median, and standard deviation) on a given dataset.
"""
import numpy as np

data = np.array([10, 20, 30, 40, 50, 60, 70])

minimum = np.min(data)
maximum = np.max(data)
mean = np.mean(data)
median = np.median(data)
standard_deviation = np.std(data)

print("Dataset:", data)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", round(standard_deviation, 2))


"""
SLIP 16
Slip No: 16
"""

"""
Q1) A: Write a python program to create a tuple of integers and display the largest,
    smallest, and average of its elements.
"""
numbers = (10, 20, 30, 40, 50)

largest = max(numbers)
smallest = min(numbers)

average = sum(numbers) / len(numbers)

print("Tuple:", numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)
print("Average:", average)

"""
Q2) B: Write a python program to implement a menu-driven Student Record Management System
    using user-defined functions.
"""

students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    percentage = float(input("Enter Percentage: "))

    students[roll_no] = {
        "name": name,
        "percentage": percentage
    }

    print("Student record added successfully!")


def display_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records:")
    for roll_no, details in students.items():
        print("Roll No:", roll_no)
        print("Name:", details["name"])
        print("Percentage:", details["percentage"])
        print("------------------------")


def search_student():
    roll_no = input("Enter Roll Number to search: ")

    if roll_no in students:
        print("\nStudent Found!")
        print("Roll No:", roll_no)
        print("Name:", students[roll_no]["name"])
        print("Percentage:", students[roll_no]["percentage"])
    else:
        print("Student record not found.")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student record deleted successfully!")
    else:
        print("Student record not found.")


while True:
    print("\n===== Student Record Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")

"""
OR - Q2) B: Write a python program to merge two dictionaries. If duplicate keys exist, add
    their values and display the updated dictionary.
"""
dict1 = {
    "A": 10,
    "B": 20,
    "C": 30
}

dict2 = {
    "B": 15,
    "C": 25,
    "D": 40
}

merged = dict1.copy()

for key, value in dict2.items():
    if key in merged:
        merged[key] = merged[key] + value
    else:
        merged[key] = value

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

print("\nUpdated Dictionary:", merged)


"""
SLIP 17
Slip No: 17
"""

"""
Q1) A: Write a python program to create a list of integers and display the second largest
    element.
"""
numbers = [10, 25, 45, 30, 60, 50]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("List:", numbers)
print("Second Largest Element:", second_largest)

"""
Q2) B: Write a python program to implement a Model-Based Agent for Smart Traffic Signal
    Control by maintaining previous and current traffic density before deciding the signal
    status.
"""

previous_density = 0

def traffic_signal(previous, current):
    print("\nPrevious Traffic Density:", previous)
    print("Current Traffic Density:", current)

    if current > 70:
        signal = "GREEN - High traffic, allow vehicles to move"
    elif current > previous:
        signal = "GREEN - Traffic density is increasing"
    elif current < 30:
        signal = "RED - Low traffic, stop vehicles"
    else:
        signal = "YELLOW - Maintain normal traffic flow"

    return signal


n = int(input("Enter number of traffic readings: "))

for i in range(n):
    current_density = int(input("\nEnter current traffic density (0-100): "))

    signal = traffic_signal(previous_density, current_density)

    print("Signal Status:", signal)

    previous_density = current_density

"""
OR - Q2) B: Write a python program to perform Linear Regression using a suitable dataset
    and predict the output for user-defined input values.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Years_Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [25000, 28000, 32000, 35000, 40000,
               45000, 50000, 55000, 60000, 65000]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

X = df[["Years_Experience"]]
y = df["Salary"]

model = LinearRegression()
model.fit(X, y)

years = float(input("\nEnter Years of Experience: "))

prediction = model.predict([[years]])

print("Predicted Salary:", round(prediction[0], 2))

plt.scatter(X, y, label="Actual Data")
plt.plot(X, model.predict(X), label="Regression Line")

plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression: Experience vs Salary")
plt.legend()
plt.show()


"""
SLIP 18
Slip No: 18
"""

"""
Q1) A: Write a python program to check whether a given string is a Palindrome.
"""
text = input("Enter a string: ")

reverse_text = text[::-1]

if text == reverse_text:
    print("The given string is a Palindrome.")
else:
    print("The given string is not a Palindrome.")

"""
Q2) B: Write a python program to implement DataFrame operations on employee records,
    including sorting, filtering and updating records using the Pandas library.
"""
import pandas as pd

data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Neha"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [45000, 50000, 55000, 60000, 48000]
}

df = pd.DataFrame(data)

print("Original Employee Records:")
print(df)

sorted_df = df.sort_values(by="Salary", ascending=False)

print("\nEmployees Sorted by Salary:")
print(sorted_df)

filtered_df = df[df["Salary"] > 50000]

print("\nEmployees with Salary Greater Than 50000:")
print(filtered_df)

df.loc[df["Employee_ID"] == 102, "Salary"] = 55000

print("\nEmployee Records After Updating Salary:")
print(df)

"""
OR - Q2) B: Develop a python program to demonstrate the Perception → Decision → Action
    cycle by simulating an Intelligent Agent in a simple environment.
"""

def intelligent_agent(environment):

    print("\nPerception:", environment)

    if environment == "Dirty":
        decision = "Clean the room"
    else:
        decision = "Move to another room"

    print("Decision:", decision)

    if decision == "Clean the room":
        print("Action: Vacuum cleaner is cleaning the room.")
    else:
        print("Action: Vacuum cleaner moves to another room.")


print("===== Intelligent Agent Simulation =====")

environment = input("Enter environment condition (Dirty/Clean): ")

environment = environment.capitalize()

intelligent_agent(environment)


"""
SLIP 19
Slip No: 19
"""

"""
Q1) A: Write a python program to implement the Tic-Tac-Toe game.
"""

board = [" " for i in range(9)]


def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


print("===== TIC-TAC-TOE GAME =====")
print("Player 1 = X")
print("Player 2 = O")

for turn in range(9):

    display_board()

    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"

    print("Player", player, "turn")

    while True:
        position = int(input("Enter position (1-9): ")) - 1

        if position >= 0 and position < 9 and board[position] == " ":
            board[position] = player
            break
        else:
            print("Invalid position! Try again.")

    if check_winner(player):
        display_board()
        print("Player", player, "wins!")
        break

else:
    display_board()
    print("The game is a Draw!")

"""
Q2) B: Write a python program to load the Diabetic in built dataset, convert it into a
    Data frames and display the first 7 rows and the shape of the dataset.
"""
import pandas as pd
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()

df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)

print("First 7 rows of the Diabetes Dataset:")
print(df.head(7))

print("\nShape of the Dataset:")
print(df.shape)

"""
OR - Q2) B: Write a python program to using Logistic Regressions to detect credit card
    fraud using the following features: Transaction Amount ,Card Age( calculated into
    years), Transaction Time(0-23),Location Matching scores(0-100),Online Transcation
    (0=NO,1=Yes)Train the model and predict fraud(1) or legit (0) based on user input.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Transaction_Amount": [100, 5000, 200, 10000, 150, 7000,
                           300, 12000, 250, 9000, 180, 6000],

    "Card_Age": [5, 1, 4, 0.5, 6, 1,
                 3, 0.2, 7, 1, 5, 0.8],

    "Transaction_Time": [10, 23, 12, 2, 14, 1,
                         11, 3, 15, 0, 13, 2],

    "Location_Match_Score": [95, 20, 90, 10, 85, 25,
                             92, 5, 88, 15, 93, 30],

    "Online_Transaction": [0, 1, 0, 1, 0, 1,
                           0, 1, 0, 1, 0, 1],

    "Fraud": [0, 1, 0, 1, 0, 1,
              0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[[
    "Transaction_Amount",
    "Card_Age",
    "Transaction_Time",
    "Location_Match_Score",
    "Online_Transaction"
]]

y = df["Fraud"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

print("\nEnter Transaction Details")

amount = float(input("Transaction Amount: "))
card_age = float(input("Card Age (in years): "))
transaction_time = int(input("Transaction Time (0-23): "))
location_score = float(input("Location Matching Score (0-100): "))
online = int(input("Online Transaction (0=No, 1=Yes): "))

new_transaction = pd.DataFrame({
    "Transaction_Amount": [amount],
    "Card_Age": [card_age],
    "Transaction_Time": [transaction_time],
    "Location_Match_Score": [location_score],
    "Online_Transaction": [online]
})

prediction = model.predict(new_transaction)[0]

print("\nPrediction:")

if prediction == 1:
    print("Fraud Transaction (1)")
else:
    print("Legit Transaction (0)")


"""
SLIP 20
Slip No: 20
"""

"""
Q1) A: Write a python program for Multiple Linear Regression that loads data from a CSV
    file to predict Sales based on Advertising Budget (TV, Radio, Newspaper).
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("advertising.csv")

print("Dataset:")
print(df.head())

X = df[["TV", "Radio", "Newspaper"]]

y = df["Sales"]

model = LinearRegression()

model.fit(X, y)

print("\nRegression Coefficients:")
print("TV:", model.coef_[0])
print("Radio:", model.coef_[1])
print("Newspaper:", model.coef_[2])
print("Intercept:", model.intercept_)

tv = float(input("\nEnter TV Advertising Budget: "))
radio = float(input("Enter Radio Advertising Budget: "))
newspaper = float(input("Enter Newspaper Advertising Budget: "))

new_data = pd.DataFrame({
    "TV": [tv],
    "Radio": [radio],
    "Newspaper": [newspaper]
})

prediction = model.predict(new_data)

print("\nPredicted Sales:", round(prediction[0], 2))

"""
Q2) B: Write a python program clean the dataset by handling missing and duplicate values
    use any Dataset: a. Check missing values b. Check duplicated rows. c. Remove
    duplicates d. Store cleaned dataset in a new CSV file.
"""
import pandas as pd

df = pd.read_csv("employee_data.csv")

print("Original Dataset:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

df = df.drop_duplicates()

numeric_columns = df.select_dtypes(include="number").columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].mean())

text_columns = df.select_dtypes(include="object").columns

for column in text_columns:
    df[column] = df[column].fillna("Unknown")

print("\nCleaned Dataset:")
print(df)

df.to_csv("cleaned_employee_data.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_employee_data.csv'")

"""
OR - Q2) B: Write a program to for DataFrame of customer with Salary and Experience: If
    Experience < 5 years, increase salary by 11.5%, else increase by 6.5%. and display
    updated DataFrame.
"""
import pandas as pd

data = {
    "Customer": ["Rahul", "Priya", "Amit", "Sneha", "Neha"],
    "Experience": [2, 4, 6, 8, 3],
    "Salary": [30000, 35000, 45000, 50000, 40000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

def update_salary(row):
    if row["Experience"] < 5:
        return row["Salary"] * 1.115
    else:
        return row["Salary"] * 1.065

df["Updated_Salary"] = df.apply(update_salary, axis=1)

print("\nUpdated DataFrame:")
print(df)


"""
SLIP 21
Slip No: 21
"""

"""
Q1) A: Write a python program python program to implement the Alpha–Beta pruning with
    depth limit and heuristic
"""

def heuristic(node):
    return node


def alpha_beta(node, depth, alpha, beta, maximizing_player):

    if depth == 0:
        return heuristic(node)

    children = [node - 2, node - 1, node + 1, node + 2]

    if maximizing_player:
        best_value = float("-inf")

        for child in children:
            value = alpha_beta(
                child, depth - 1, alpha, beta, False
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value

    else:
        best_value = float("inf")

        for child in children:
            value = alpha_beta(
                child, depth - 1, alpha, beta, True
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                break

        return best_value


print("===== Alpha-Beta Pruning =====")

initial_value = int(input("Enter initial value: "))
depth = int(input("Enter depth limit: "))

result = alpha_beta(
    initial_value,
    depth,
    float("-inf"),
    float("inf"),
    True
)

print("\nBest heuristic value:", result)

"""
Q2) B: write a python program to load item.csv containing cost and type of item and
    perform basic data exploration: a. Display the first four rows of item dataset b.
    Print the shape of the dataset. c. Show column names. d. Identify missing values e.
    Display dataset info
"""
import pandas as pd

df = pd.read_csv("item.csv")

print("First 4 Rows of Item Dataset:")
print(df.head(4))

print("\nShape of the Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nComplete Dataset:")
print(df)

"""
OR - Q2) B: Write a python program to simulate a Goal-Based Agent for a simple navigation
    problem. The agent should accept the current location and goal location as input and
    determine the next action required to move toward the goal. Display the current state,
    goal state, and selected action.
"""

def goal_based_agent(current, goal):

    if current == goal:
        return "Goal Reached"

    if current == "A":
        if goal == "B":
            return "Move Right"
        elif goal == "C":
            return "Move Down"

    elif current == "B":
        if goal == "A":
            return "Move Left"
        elif goal == "C":
            return "Move Down"

    elif current == "C":
        if goal == "A":
            return "Move Up"
        elif goal == "B":
            return "Move Right"

    return "No valid action"


print("===== Goal-Based Navigation Agent =====")
print("Available Locations: A, B, C")

current_location = input("Enter current location: ").upper()
goal_location = input("Enter goal location: ").upper()

action = goal_based_agent(current_location, goal_location)

print("\nCurrent State:", current_location)
print("Goal State:", goal_location)
print("Selected Action:", action)


"""
SLIP 22
Slip No: 22
"""

"""
Q1) A: Write a python programs to solve the Blocks World Problem.
"""

def display(blocks):
    print("Current State:", blocks)


def move_block(blocks, block, destination):
    blocks.remove(block)
    blocks.append(block)

    print("Move", block, "to", destination)
    display(blocks)


print("===== BLOCKS WORLD PROBLEM =====")

initial = input("Enter initial blocks order (example: ABC): ").upper()

goal = input("Enter goal blocks order (example: CBA): ").upper()

blocks = list(initial)
goal_blocks = list(goal)

print("\nInitial State:", blocks)
print("Goal State:", goal_blocks)

for i in range(len(goal_blocks)):

    desired_block = goal_blocks[i]

    if blocks[i] != desired_block:

        position = blocks.index(desired_block)

        while position > i:
            block_above = blocks[position - 1]

            blocks[position], blocks[position - 1] = \
                blocks[position - 1], blocks[position]

            print("\nMove", desired_block, "above", block_above)
            print("Current State:", blocks)

            position -= 1

if blocks == goal_blocks:
    print("\nGoal State Reached!")
else:
    print("\nGoal State Not Reached.")

"""
Q2) B: Write a python program to load employee.csv containing Employee ID, Salary, and
    Department dataset and perform basic data exploration. a. Display the first four rows
    of the dataset. b. Print the shape of the dataset. c. Show column names. d. Identify
    missing values. e. Display dataset information.
"""
import pandas as pd

df = pd.read_csv("employee.csv")

print("First 4 Rows of the Dataset:")
print(df.head(4))

print("\nShape of the Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
df.info()

"""
OR - Q2) B: Write a python program that predicts the price of a house using a dataset that
    includes Area (sq.ft) and Number of Bedrooms as input features from the user. Use
    Multiple Linear Regression to build the prediction model.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 5, 5],
    "Price": [2500000, 2900000, 3500000, 4100000,
              4700000, 5200000, 6000000, 6800000]
}

df = pd.DataFrame(data)

print("House Dataset:")
print(df)

X = df[["Area", "Bedrooms"]]

y = df["Price"]

model = LinearRegression()

model.fit(X, y)

print("\nEnter House Details:")
area = float(input("Enter Area (sq.ft.): "))
bedrooms = int(input("Enter Number of Bedrooms: "))

new_house = pd.DataFrame({
    "Area": [area],
    "Bedrooms": [bedrooms]
})

predicted_price = model.predict(new_house)

print("\nPredicted House Price: ₹", round(predicted_price[0], 2))


"""
SLIP 23
Slip No: 23
"""

"""
Q1) A: Write a python program to predict if a student is Eligible to take admission (marks
    ≥ 50) using simple Logistic Classification. Accept student marks from user.
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Marks": [30, 35, 40, 45, 48, 50, 55, 60, 65, 70, 75, 80],
    "Eligible": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Marks"]]

y = df["Eligible"]

model = LogisticRegression()
model.fit(X, y)

marks = float(input("Enter student marks: "))

prediction = model.predict([[marks]])[0]

if prediction == 1:
    print("Student is Eligible for Admission.")
else:
    print("Student is Not Eligible for Admission.")

"""
Q2) B: Develop a program to perform different list methods such as add (append), extend,
    insert, remove and delete elements and display the updated list after each operation.
"""

numbers = [10, 20, 30, 40]

print("Original List:", numbers)

numbers.append(50)
print("\nAfter append(50):", numbers)

numbers.extend([60, 70])
print("After extend([60, 70]):", numbers)

numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

numbers.remove(30)
print("After remove(30):", numbers)

del numbers[1]
print("After deleting element at index 1:", numbers)

"""
OR - Q2) B: Design a Model-Based Agent that maintains an internal state of soil moisture
    and weather conditions. Based on the current sensor readings and stored memory, the
    agent decides whether to water the plants.
"""

previous_moisture = 50
previous_weather = "Normal"


def plant_agent(current_moisture, current_weather):

    global previous_moisture, previous_weather

    print("\n--- Agent Status ---")
    print("Previous Soil Moisture:", previous_moisture, "%")
    print("Previous Weather:", previous_weather)
    print("Current Soil Moisture:", current_moisture, "%")
    print("Current Weather:", current_weather)

    if current_moisture < 30 and current_weather != "Rainy":
        action = "WATER THE PLANTS"

    elif current_moisture < 40 and previous_moisture < 40:
        action = "WATER THE PLANTS"

    elif current_weather == "Rainy":
        action = "DO NOT WATER - Rain expected"

    else:
        action = "DO NOT WATER - Soil moisture is sufficient"

    previous_moisture = current_moisture
    previous_weather = current_weather

    return action


print("===== Smart Plant Watering Agent =====")

moisture = float(input("Enter current soil moisture (0-100): "))

print("\nWeather Options: Sunny, Cloudy, Rainy, Normal")
weather = input("Enter current weather condition: ").capitalize()

decision = plant_agent(moisture, weather)

print("\nDecision:", decision)


"""
SLIP 24
Slip No: 24
"""

"""
Q1) A: Write a python program for Multiple Linear Regression that loads data from a CSV
    file to predict Sales based on Advertising Budget (Amazon,Mesho ,Flipcart)
"""

import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("sales_data.csv")

print("Advertising and Sales Dataset:")
print(df)

X = df[["Amazon", "Mesho", "Flipcart"]]

y = df["Sales"]

model = LinearRegression()

model.fit(X, y)

print("\nRegression Coefficients:")
print("Amazon:", model.coef_[0])
print("Mesho:", model.coef_[1])
print("Flipcart:", model.coef_[2])
print("Intercept:", model.intercept_)

print("\nEnter Advertising Budget:")

amazon = float(input("Amazon Budget: "))
mesho = float(input("Mesho Budget: "))
flipcart = float(input("Flipcart Budget: "))

new_data = pd.DataFrame({
    "Amazon": [amazon],
    "Mesho": [mesho],
    "Flipcart": [flipcart]
})

predicted_sales = model.predict(new_data)

print("\nPredicted Sales:", round(predicted_sales[0], 2))

"""
Q2) B: Write a python program using Decision Tree Classification to predict the type of
    vegetables (Leafy vegetables or fruit vegetabels) based on the following features: it
    is leafy vegetabels or not, how to grow vegetables : grow from flower = 1,otherwise 0
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "Is_Leafy": [1, 1, 1, 1, 0, 0, 0, 0],
    "Grows_From_Flower": [0, 0, 0, 0, 1, 1, 1, 1],
    "Vegetable_Type": [
        "Leafy Vegetable",
        "Leafy Vegetable",
        "Leafy Vegetable",
        "Leafy Vegetable",
        "Fruit Vegetable",
        "Fruit Vegetable",
        "Fruit Vegetable",
        "Fruit Vegetable"
    ]
}

df = pd.DataFrame(data)

print("Vegetable Dataset:")
print(df)

X = df[["Is_Leafy", "Grows_From_Flower"]]

y = df["Vegetable_Type"]

model = DecisionTreeClassifier(random_state=42)

model.fit(X, y)

print("\nEnter Vegetable Details")

leafy = int(input("Is it a leafy vegetable? (1=Yes, 0=No): "))
flower = int(input("Does it grow from a flower? (1=Yes, 0=No): "))

new_vegetable = pd.DataFrame({
    "Is_Leafy": [leafy],
    "Grows_From_Flower": [flower]
})

prediction = model.predict(new_vegetable)

print("\nPredicted Vegetable Type:", prediction[0])

"""
OR - Q2) B: Write a python program to develop fitness predictors using Random Forest
    Classification to predict whether a person is FIT or UNFIT based on: Age, Exercise
    Hours per Week Accept the input from user and predict for multiple people
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

data = {
    "Age": [18, 20, 22, 25, 28, 30, 35, 40, 45, 50,
            21, 24, 27, 32, 38],

    "Exercise_Hours": [5, 6, 7, 8, 6, 5, 4, 3, 2, 1,
                       7, 8, 6, 4, 2],

    "Fitness": ["FIT", "FIT", "FIT", "FIT", "FIT",
                "FIT", "FIT", "UNFIT", "UNFIT", "UNFIT",
                "FIT", "FIT", "FIT", "UNFIT", "UNFIT"]
}

df = pd.DataFrame(data)

print("Training Dataset:")
print(df)

X = df[["Age", "Exercise_Hours"]]

y = df["Fitness"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

n = int(input("\nEnter number of people: "))

people = []

for i in range(n):
    print("\nEnter details for Person", i + 1)

    age = int(input("Enter Age: "))
    exercise = float(input("Enter Exercise Hours per Week: "))

    people.append([age, exercise])

new_data = pd.DataFrame(
    people,
    columns=["Age", "Exercise_Hours"]
)

predictions = model.predict(new_data)

print("\n===== FITNESS PREDICTION =====")

for i in range(n):
    print(
        "Person", i + 1,
        "- Age:", new_data.iloc[i]["Age"],
        ", Exercise Hours:", new_data.iloc[i]["Exercise_Hours"],
        "=>", predictions[i]
    )


"""
SLIP 25
Slip No: 25
"""

"""
Q1) A: Write a python program to manage multiple student records using a dictionary and
    determine the topper based on percentage
"""

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    roll_no = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    percentage = float(input("Enter Percentage: "))

    students[roll_no] = {
        "Name": name,
        "Percentage": percentage
    }

print("\n===== Student Records =====")

for roll_no, details in students.items():
    print("Roll No:", roll_no)
    print("Name:", details["Name"])
    print("Percentage:", details["Percentage"])
    print("------------------------")

topper_roll = max(
    students,
    key=lambda x: students[x]["Percentage"]
)

print("\n===== Topper =====")
print("Roll No:", topper_roll)
print("Name:", students[topper_roll]["Name"])
print("Percentage:", students[topper_roll]["Percentage"])

"""
Q2) B: Write a python program to simulate n-Queens problem.
"""

def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):

    for i in range(row):
        if board[i][col] == 1:
            return False

    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):

    if row == n:
        return True

    for col in range(n):

        if is_safe(board, row, col, n):

            board[row][col] = 1

            if solve_n_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


n = int(input("Enter the value of N: "))

board = [[0 for j in range(n)] for i in range(n)]

if solve_n_queens(board, 0, n):
    print("\nSolution:")
    print_board(board, n)
else:
    print("\nNo solution exists.")

"""
OR - Q2) B: Write a python program to create a DataFrame which contains a person name and
    age ,Sort a DataFrame in ascending order of Age .
"""
import pandas as pd

data = {
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Neha"],
    "Age": [25, 19, 32, 22, 28]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

sorted_df = df.sort_values(by="Age", ascending=True)

print("\nDataFrame Sorted by Age:")
print(sorted_df)