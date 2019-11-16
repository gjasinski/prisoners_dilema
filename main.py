from Random import Random
from TitForTat import TitForTat

class Experiment:
    def __init__(self):
        self.points_1 = 0
        self.points_2 = 0

    def __add_points(self, action_1, action_2):
        if action_1 == 'C' and action_2 == 'C':
            self.points_1 = self.points_1 + 3
            self.points_2 = self.points_2 + 3
            return
        if action_1 == 'D' and action_2 == 'D':
            self.points_1 = self.points_1 + 1
            self.points_2 = self.points_2 + 1
            return
        if action_1 == 'C' and action_2 == 'D':
            self.points_2 = self.points_2 + 5
            return

        if action_1 == 'D' and action_2 == 'C':
            self.points_1 = self.points_1 + 5
            return
        raise


    def __run_single(self, strategy_1, strategy_2, file_name):
        self.points_1 = 0
        self.points_2 = 0
        f = open("data/" + file_name + '.csv', 'w')
        f.write(str(strategy_1) + ";" + str(strategy_2) + "\n")
        str_1 = strategy_1.decide_first()
        str_2 = strategy_2.decide_first()
        self.__add_points(str_1, str_2)
        f.write(str(self.points_1) + ";" + str(self.points_2))

        for i in range(99):
            str_1, str_2 = strategy_1.decide(str_2), strategy_2.decide(str_1)
            self.__add_points(str_1, str_2)
            print(str_1 + ";" + str_2 + ";" + str(self.points_1) + ";" + str(self.points_2))
            f.write(str(self.points_1) + ";" + str(self.points_2) + "\n")
        f.close()
    
    def run(self, strategy_1, strategy_2):
        file_name = str(strategy_1) + "_" + str(strategy_2)
        f = open("data/" + file_name + '.csv', 'w')
        f.write(str(strategy_1) + ";" + str(strategy_2) + "\n")
        for i in range(10):
            self.__run_single(strategy_1, strategy_2, file_name + "_" + str(i))
            f.write(str(self.points_1) + ";" + str(self.points_2) + "\n")


if __name__ == "__main__":
    experiment = Experiment()
    random_str = Random()
    tit_for_tat = TitForTat()

    experiment.run(random_str, random_str)
    experiment.run(random_str, tit_for_tat)

    experiment.run(tit_for_tat, tit_for_tat)
    