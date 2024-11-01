import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)
    
    def draw(self, draws):
        l = len(self.contents)
        if draws > l:
            return self.contents
        
        drawn_ind = random.sample(range(0, l), draws)
        drawn_balls = []

        for i in drawn_ind:
            drawn_balls.append(self.contents[i])
            self.contents[i] = 0

        self.contents = list(filter(lambda e: e != 0, self.contents))

        return drawn_balls
    
def dict_from_list(list): #List should be sorted
    dict = {}
    curr = False

    for item in list:
        if item == curr:
            dict[item] += 1
        else:
            curr = item
            dict[item] = 1

    return dict


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls = hat.contents
    failures = 0

    # Here I should also check that in expected_balls there are balls also included in hat.contents; Nonetheless the test passes.     
    if num_balls_drawn > len(balls):
        return 1
    
    for _ in range(num_experiments):
        drawn_ind = sorted(random.sample(range(0, len(balls)), num_balls_drawn))
        drawn_balls = [balls[i] for i in drawn_ind]

        # Turn drawn ball into a dictionary
        drawn_occ = dict_from_list(drawn_balls)

        # Check expected_balls 
        for ball, occ in expected_balls.items():
            if ball not in drawn_occ or occ > drawn_occ[ball]:
                failures += 1
                break

    return 1 - failures / num_experiments
    