class Solution:
    def isPathCrossing(self, path: str) -> bool:
        positions = {(0,0):1 } 
        curX = 0
        curY = 0
        for c in path:
            if c == 'N':
                curY += 1
                positions[(curX,curY)] = 1 + positions.get((curX,curY),0)
            elif c == 'S':
                curY -= 1
                positions[(curX,curY)] = 1 + positions.get((curX,curY),0)
            elif c == 'E':
                curX += 1
                positions[(curX,curY)] = 1 + positions.get((curX,curY),0)
            else:
                curX -= 1
                positions[(curX,curY)] = 1 + positions.get((curX,curY),0)

        for key in positions:
            if positions[key] > 1:
                return True
        return False