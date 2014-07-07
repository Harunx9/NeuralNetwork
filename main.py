# coding: utf-8
from LanguagesNN.CharCounterForNN import CharCounterForNN
from LanguagesNN.languages import LANGUAGES_SET, LANGUAGES_TEST

__author__ = 'Szymon Wanot and Paweł Siemienik'
from NetworkCore.simplenn import SimpleNN as NeuralNetwork
# import learningset


# class NnApp():
#     def __init__(self):
#         self.network = NeuralNetwork(2, 4, 1)
#
#     def run(self):
#         self.network.learn(1000, learningset.LEARNING_SET_XOR, 0.2, 0.1)
#         print "I'm learned"
#         self.network.test_learning(learningset.TEST_SET_XOR, True)


class LanguagesApp():
    @staticmethod
    def run():
        counter = CharCounterForNN(LANGUAGES_SET)

        counter.count()
        network = NeuralNetwork(len(counter.literals), 40, len(counter.languages))
        network.learn(2000, counter.data, 0.2, 0.1, 0.000001)
        print "I'm learned"

        i = 0
        while raw_input("Do you want add your test data? (y/n)") == "y":
            i += 1
            LANGUAGES_TEST.append(["USER no.%s" % i, raw_input("Write test USER no.%s" % i)])

        test_counter = CharCounterForNN(LANGUAGES_TEST)
        test_counter.count()

        for key, line in test_counter.probabilities.items():
            input_data = []
            for lit in counter.literals:
                if lit in line:
                    input_data.append(line[lit])
                else:
                    input_data.append(0)
            result = network.think(input_data)
            lang_no = result.index(max(result))
            print "TEST FOR %s (lang no. %s is %s ); FULL OUTPUT  %s " % (
                key,
                lang_no,
                counter.languages[lang_no],
                result,
            )


if __name__ == '__main__':
    LanguagesApp.run()
