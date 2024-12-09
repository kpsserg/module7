class WordsFinder:

    def __init__(self, *files_names):
        self.files_list = files_names

    def get_all_words(self):
        self.elements_for_deleting = {',': ' ', '.': ' ', '=': ' ', '!': ' ', '?': ' ', ';': ' ', ':': ' '}
        self.all_words = {}
        for files in self.files_list:
            with open(files, 'r', encoding='utf-8') as file:
                self.res = file.read().replace(' - ', ' ')
                self.tbl = self.res.maketrans(self.elements_for_deleting)
                self.res = self.res.translate(self.tbl).lower()
                # print(self.res)
                self.all_words[files] = self.res.split()
        return self.all_words

    def find(self, word):
        for key, value in self.all_words.items():
            for i in range(0, len(value)):
                if word in value[i]:
                    return f"{word} найдено в файле {key}, {i + 1} слово в тексте"

    def count(self, word):
        count = {}
        for key, value in self.all_words.items():
            count[key] = 0
            for i in range(0, len(value)):
                if word in value[i]:
                    count[key] += 1
        for k, v in count.items():
            if v > 0:
                return f"В файле {k} {word} найдено {v} раз(а)"


finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words())
finder2.find('te')
finder2.count('te')
finder1 = WordsFinder('test_file3.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder3 = WordsFinder('test_file4.txt')

print(finder3.get_all_words())
print(finder3.find('if'))
print(finder3.count('if'))
