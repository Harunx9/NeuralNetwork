__author__ = 'Siemienik'

import languages as dataset


class CharCounterForNN():
    def __init__(self, input_data):
        self.literals = []
        self.probabilities = {}
        self.languages = []
        self.input_data = input_data
        self.data = []

    def count(self):
        """
            Count probabilities for chars in languages
        """
        for lang in self.input_data:
            self.probabilities[lang[0]] = {}
            self.languages.append(lang[0])
            for ch in lang[1].lower():
                if ch in self.probabilities[lang[0]]:
                    self.probabilities[lang[0]][ch] += 1
                else:
                    self.probabilities[lang[0]][ch] = 1
                    if not ch in self.literals:
                        self.literals.append(ch)

            count = len(lang[1])

            for key, value in self.probabilities[lang[0]].items():
                self.probabilities[lang[0]][key] = 1.0 * value / count
        data = []
        i = 0
        for key, line in self.probabilities.items():
            input_data = []
            for lit in self.literals:
                if lit in line:
                    input_data.append(line[lit])
                else:
                    input_data.append(0)
            output_data = [-1] * len(self.languages)
            output_data[self.languages.index(key)] = 1
            data.append([input_data, output_data])
        self.data = data
        return data


if __name__ == '__main__':
    counter = CharCounterForNN(dataset.LANGUAGES_SET)
    print counter.count()
    print counter.languages
    print len(counter.languages)
    print counter.probabilities
    print len(counter.probabilities)
    print counter.literals
    print len(counter.literals)
