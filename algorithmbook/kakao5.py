P = 0
B = 1


class Builder:

    def __init__(self):
        self.pillars = []
        self.beams = []

    def add_structure(self, x, y, type):
        if self.check_sustainability(x, y, type):
            if type == P:
                self.pillars.append([x, y, type])
            else:
                self.beams.append([x, y, type])

    def delete_structure(self, x, y, type):
        related = []
        if type == P:
            self.pillars.remove([x, y, type])

            if [x, y+1, P] in self.pillars:
                related.append([x, y+1, P])
            if [x-1, y+1, B] in self.beams:
                related.append([x-1, y+1, B])
            if [x, y+1, B] in self.beams:
                related.append([x, y+1, B])

            is_sustainable = all(self.check_sustainability(*structure) for structure in related) if related else True

            if is_sustainable:
                return
            else:
                self.pillars.append([x, y, type])
                return

        if type == B:
            self.beams.remove([x, y, type])

            if [x, y, P] in self.pillars:
                related.append([x, y, P])
            if [x+1, y, P] in self.pillars:
                related.append([x+1, y, P])
            if [x-1, y, B] in self.beams:
                related.append([x-1, y, B])
            if [x+1, y, B] in self.beams:
                related.append([x+1, y, B])

            is_sustainable = all(self.check_sustainability(*structure) for structure in related) if related else True

            if is_sustainable:
                return
            else:
                self.beams.append([x, y, type])
                return

    def check_sustainability(self, x, y, type):
        checker = 0  # check if it is sustainable
        if type == P:
            if y == 0:
                checker = 1
            if self.pillars.count([x, y-1, P]):
                checker = 1
            if self.beams.count([x-1, y, B]) or self.beams.count([x, y, B]):
                checker = 1

        else:
            if self.pillars.count([x, y - 1, P]) or self.pillars.count([x + 1, y - 1, P]):
                checker = 1
            if self.beams.count([x - 1, y, B]) and self.beams.count([x + 1, y, B]):
                checker = 1

        if checker:
            return True
        else:
            return False

    def get_structure(self):
        return sorted(self.beams + self.pillars)


def solution(n, build_frame):
    builder = Builder()

    for frame in build_frame:
        if frame[3] == 0:
            builder.delete_structure(*frame[:3])
        else:
            builder.add_structure(*frame[:3])

    return builder.get_structure()

result = solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]])
print(result)