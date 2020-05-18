class Joystick:
    def __init__(self, string):
        self.string = string
        self.result = ['A'] * len(string)
        self.cursor = 0
        # self.visited = [0] * len(string)
        self.counter = 0

    def count_move(self, alphabet):
        ascil_number = ord(alphabet)
        if ascil_number < 78:
            return ascil_number - ord('A')
        else:
            return ord('Z') - ascil_number + 1

    def move_cursor(self):
        c = 1
        nearest = -1

        while nearest == -1:
            forward = (self.cursor + c) % len(self.string)
            backward = self.cursor - c + len(self.string) if self.cursor - 1 < 0 else self.cursor - c
            # print(self.result, forward, backward, nearest)
            if forward == backward:
                if self.string[backward] != self.result[backward]:
                    self.cursor = backward
                    self.counter += c
                return
            if all(self.string[s] != self.result[s] for s in (forward, backward)):
                nearest = forward
                break
            elif self.string[backward] != self.result[backward]:
                nearest = backward
                break
            elif self.string[forward] != self.result[forward]:
                nearest = forward
                break
            c += 1

        self.cursor = nearest
        self.counter += c

    def change(self):
        s = self.string[self.cursor]
        if s != self.result[self.cursor]:
            self.counter += self.count_move(s)
            self.result[self.cursor] = s

        while ''.join(self.result) != self.string:
            self.move_cursor()
            s = self.string[self.cursor]
            self.counter += self.count_move(s)
            self.result[self.cursor] = s
        return self.counter


def solution(name):
    joystick = Joystick(name)
    answer = joystick.change()
    return answer

if __name__ == '__main__':
    print(solution('CANAAAAANAN'))

