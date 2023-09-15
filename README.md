# LinePlanVisualization
A visualization tool for line plan based on matplotlib.<br>
According to our specified data structure, your line plan can be visualized easily, and also we provide a lot of parameters to adjust the appearance.


## Install
```python
pip install line_plan_visualization
```


## Usage
This tool consists of three main classes： PhysicalRailway, Lines and LinePlan.<br>
### PhysicalRailway
This class represents the physical railway to visualize.<br>
When creating an instance of PhysicalRailway, the fisrt parameter you need to pass in should be ```str``` type representing the name of the railway. The second parameter should be ```dict``` type which the keys are  ```str``` type representing the names of stations and the values are ```str``` type representing stations' levels. The level should be one of "high", "medium" and "low".
The order of the stations in the dictionary is the order of the visualization.
```python
# an instance of class PhysicalRailway 
example_pr = PhysicalRailWay("Beijing-Shanghai High-Speed Raiway",  # railway name
                             {"BJN": "high",  # stations names and levels in order
                              "LF": "low",
                              "TJN": "high",
                              "CZX": "medium",
                              "DZD": "medium",
                              "JNX": "high",
                              "TA": "medium",
                              "QFD": "medium",
                              "TZD": "low",
                              "ZZ": "low",
                              "XZD": "high",
                              "SZD": "low",
                              "BBN": "medium",
                              "DY": "low",
                              "CZ": "low",
                              "NJN": "high",
                              "ZJN": "medium",
                              "DYB": "low",
                              "CZB": "medium",
                              "WXD": "medium",
                              "SZB": "medium",
                              "KSN": "medium",
                              "SHHQ": "high"})
```
### Lines
This class represents the train lines operating on the physical railway.<br>
When creating an instance of Lines, the only parameter you need to pass in should be ```dict``` type which the keys are  ```int``` type representing the IDs of lines(Sequentiality is not enforced) and the values are ```list``` type only containing 0 and 1 for no stop and stop at the station corresponding to the physical railway.
```python
# 50 lines are randomly generated and lineIDs do not have to start at 0 or are ordered
lines = {}
for idx in range(25):
    lines[idx] = [random.randint(0, 1) for _ in range(len(example_pr))]  # len(example_pr) returns the num of stations

# an instance of class Lines
example_lines = Lines(lines)
```

### LinePlan
This class combines PyhsicalRailway and Lines.
When creating an instance of LinePlan, the only two parameters you need to pass in are an instance of PhysicalRailway and an instance of Line.
```python
# an instance of class LinePlan
example_lp = LinePlan(example_pr, example_lines)
```
Now the line plan can be visualized by calling the function ```draw```.
```python
example_lp.draw()
```

However, the default appearance parameters may not be appropriate for your line plan, you can also pass in some custom parameters. See documentation of function ```draw``` for details. Overall, they are similar to the syntax and usage of matplotlib.
```python
example_lp.draw(figsize=(23, 25),
                lines_color='blue')
```
Make sure that the function  ```show``` is called after the function ```save```, otherwise your saved image will be blank(For some unknown reasons, the saved image is the real one, the displayed image are indicative only, if you reckon the displayed image is ugly, you may wish to take a look at the saved image).
```python
example_lp.save("fig\\testimage.png")
example_lp.show()
```

