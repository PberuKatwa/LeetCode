# Problem 2: Assembly Line Process
# Scenario: A factory has an assembly line where each station knows only about the next station.

class AssemblyLine:
    def __init__(self,station):
        self.station = station
        self.next_station = None

line_1 = AssemblyLine("process")
line_2 = AssemblyLine("make")
line_3 = AssemblyLine("better")
line_4 = AssemblyLine("bet 3")

line_1.next_station = line_2
line_2.next_station = line_3
line_3.next_station =  line_4

current_line = line_1

while current_line:
    print(f"current line : {current_line.station} ")
    current_line = current_line.next_station
