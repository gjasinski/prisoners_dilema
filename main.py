import statistics
from Random import Random
from TitForTat import TitForTat
from TitForTatWithForgiveness import TitForTatWithForgiveness
from Handshake import Handshake
from Pavlov import Pavlov

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
        print("Error" + str(action_1) + " " + str(action_2))
        raise


    def __run_single(self, strategy_1, strategy_2, file_name):
        self.points_1 = 0
        self.points_2 = 0
        strategy_1.clean()
        strategy_2.clean()
        #f = open("data/" + file_name + '.csv', 'w')
        #f.write(str(strategy_1) + "," + str(strategy_2) + "\n")
        str_1 = strategy_1.decide_first()
        str_2 = strategy_2.decide_first()
        self.__add_points(str_1, str_2)
        #f.write(str(self.points_1) + "," + str(self.points_2) + "\n")
        print(str_1 + "," + str_2 + "," + str(self.points_1) + "," + str(self.points_2))

        for i in range(99):
            str_1, str_2 = strategy_1.decide(str_2), strategy_2.decide(str_1)
            self.__add_points(str_1, str_2)
            print(str_1 + "," + str_2 + "," + str(self.points_1) + "," + str(self.points_2))
        #    f.write(str(self.points_1) + "," + str(self.points_2) + "\n")
        #f.close()
    
    def run(self, strategy_1, strategy_2):
        res1 = []
        res2 = []
        file_name = str(strategy_1) + "_" + str(strategy_2)
        f = open("data/" + file_name + '.csv', 'a+')
        f_min = open('data/min.csv', 'a+')
        f_max = open('data/max.csv', 'a+')
        f_avg = open('data/avg.csv', 'a+')
        f_stddev = open('data/stddev.csv', 'a+')
        f.write(str(strategy_1) + "," + str(strategy_2) + "\n")
        for i in range(10):
            self.__run_single(strategy_1, strategy_2, file_name + "_" + str(i))
            f.write(str(self.points_1) + "," + str(self.points_2) + "\n")
            res1 = res1 + [self.points_1]
            res2 = res2 + [self.points_2]
        #f = open("data/" + file_name + '_res.csv', 'w')
        #f.write("min," + str(min(res1)) + "," + str(min(res2)) + "\n")
        #f.write("max," + str(max(res1)) + "," + str(max(res2)) + "\n")
        #f.write("avg," + str(sum(res1)/len(res1)) + "," + str(sum(res2)/len(res2)) + "\n")
        #f.write("stddev," + str(statistics.stdev(res1)) + "," + str(statistics.stdev(res2)) + "\n")
        f_min.write(str(strategy_1) + " vs " + str(strategy_2) + ";" + str(min(res1)) + "\n")
        f_min.write(str(strategy_2) + " vs " + str(strategy_1) + ";" + str(min(res2)) + "\n")

        f_max.write(str(strategy_1) + " vs " + str(strategy_2) + ";" + str(max(res1)) + "\n")
        f_max.write(str(strategy_2) + " vs " + str(strategy_1) + ";" + str(max(res2)) + "\n")

        f_avg.write(str(strategy_1) + " vs " + str(strategy_2) + ";" + str(sum(res1)/len(res1)) + "\n")
        f_avg.write(str(strategy_2) + " vs " + str(strategy_1) + ";" + str(sum(res2)/len(res2)) + "\n")

        f_stddev.write(str(strategy_1) + " vs " + str(strategy_2) + ";" + str(statistics.stdev(res1)) + "\n")
        f_stddev.write(str(strategy_2) + " vs " + str(strategy_1) + ";" + str(statistics.stdev(res2)) + "\n")
        


if __name__ == "__main__":
    experiment = Experiment()
    random_str = Random()
    tit_for_tat = TitForTat()
    tit_for_tat_with_forgiveness = TitForTatWithForgiveness()

    #Random
    experiment.run(random_str, random_str)
    experiment.run(random_str, tit_for_tat)
    experiment.run(random_str, tit_for_tat_with_forgiveness)
    experiment.run(random_str, Handshake())
    experiment.run(random_str, Pavlov())

    experiment.run(tit_for_tat, tit_for_tat)
    experiment.run(random_str, tit_for_tat_with_forgiveness)
    experiment.run(tit_for_tat, Handshake())
    experiment.run(random_str, Pavlov())

    experiment.run(tit_for_tat_with_forgiveness, tit_for_tat_with_forgiveness)
    experiment.run(tit_for_tat_with_forgiveness, Handshake())
    experiment.run(tit_for_tat_with_forgiveness, Pavlov())

    experiment.run(Handshake(), Handshake())
    experiment.run(tit_for_tat_with_forgiveness, Pavlov())

    experiment.run(Pavlov(), Pavlov())
