"""
On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive
one of three instructions:

- "G": go straight 1 unit;
- "L": turn 90 degrees to the left;
- "R": turn 90 degrees to the right

Example 1:
Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to
(0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at
the origin.

Example 2:
Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.

Example 3:
Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...

Constraints:
1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
"""
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        offset_dict_L = {}
        
        offset_dict_L[(0, 1)] = (-1, 0)
        offset_dict_L[(0, -1)] = (1, 0)
        offset_dict_L[(1, 0)] = (0, 1)
        offset_dict_L[(-1, 0)] = (0, -1)
        
        offset_dict_R = {}
        
        offset_dict_R[(0, 1)] = (1, 0)
        offset_dict_R[(0, -1)] = (-1, 0)
        offset_dict_R[(1, 0)] = (0, -1)
        offset_dict_R[(-1, 0)] = (0, 1)
        
        cx = 0
        cy = 0
        
        c_offset = (0, 1)
        
        for i in instructions:
            if(i == 'G'):
                cx += c_offset[0]
                cy += c_offset[1]
            elif(i == 'L'):
                c_offset = offset_dict_L.get(c_offset)
            elif(i == 'R'):
                c_offset = offset_dict_R.get(c_offset)
                
        if(cx == 0 and cy == 0):
            return True
        elif(c_offset == (0, 1)):
            return False
        else:
            return True