import random
import sys
class field:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        matrix = [[0] * X for i in range(Y)]
        self.matrix = matrix
    def display(self):
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                print(self.matrix[i][j], end=' ')
            print()
        print()

class point:
    def __init__(self, X,Y):
        self.X0 = random.randint(0, X-1)
        self.Y0 = random.randint(0, Y-1)

class characted:
    def __init__(self,X0,Y0):
        self.X0 = X0
        self.Y0 = Y0
    def move (self, moved):
            self.X1 = self.X0
            self.Y1 = self.Y0
            if moved == 'w':
                self.Y0 -= 1
            elif moved == 'a':
                self.X0 -= 1
            elif moved == 's':
                self.Y0 += 1
            elif moved == 'd':
                self.X0 +=  1
            else:
                print('Некорректное направление')
    def border(self,X,Y):
        if self.Y0 >= Y or self.X0 >= X or self.Y0 < 0 or self.X0 < 0:
            self.X0 = self.X1
            self.Y0 = self.Y1
class monster(characted):
    def __init__(self,X0,Y0):
        super().__init__(X0,Y0)
def the_end(m):
    if m == 2:
        print('Игра окончена! Монстер победил!')
        sys.exit()

def main():
    field1 = field(4, 4)
    point1 = point(field1.X,field1.Y)
    point2 = point(field1.X, field1.Y)
    characted1 = characted(point1.X0, point1.Y0)
    monster1 = monster(point2.X0, point2.Y0)
    while True:
        field1.matrix[characted1.Y0][characted1.X0] = 1
        field1.matrix[ monster1.Y0][ monster1.X0] = 2
        field1.display()
        the_end(field1.matrix[characted1.Y0][characted1.X0])
        field1.matrix[characted1.Y0][characted1.X0] = 0
        field1.matrix[monster1.Y0][monster1.X0] = 0
        moved = input('Введите напраление "w", "a", "s", "d" или (-) чтобы закончить: ')
        if moved == '-':
            break
        characted1.move(moved)
        characted1.border(field1.X, field1.Y)
        m = ('w','a','s','d')
        monster1.move(m[random.randint(0, 3)])
        monster1.border(field1.X, field1.Y)



main()
