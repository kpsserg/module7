class WordsFinder:

    def __init__(self, *files_names):
        self.files_list = files_names
        # for file_name in files_names:
        #     self.file_name = files_names
        #     files.append(self.file_name)
        # print(self.files_list)

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
        results = []
        for key, value in self.all_words.items():
            for i in range(0, len(value)):
                if word.lower() in value[i].lower():
                    results.append(f"{word} найдено в файле {key}, {i + 1} слово в тексте")
                    break
        if not results:
            results.append("Not Found in all files")
        return "\n".join(results)


    def count(self, word):
        count = {}
        results = ''
        for key, value in self.all_words.items():
            count[key] = 0
            for i in range(0, len(value)):
                if word.lower() in value[i].lower():
                    count[key] += 1
        for k, v in count.items():
            results += (f"В файле {k} {word} найдено {v} раз(а)\n")
        return results

# проверка работы ч.1
finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())
print(finder1.find('TEXT'))
print(finder1.count('teXT'))

# проверка работы ч.2
# finder2 = WordsFinder('test_file3.txt')
# print(finder2.get_all_words())
# print(finder2.find('captain'))
# print(finder2.count('captain'))

# проверка работы ч.3
# finder3 = WordsFinder('test_file4.txt')
# print(finder3.get_all_words())
# print(finder3.find('if'))
# print(finder3.count('if'))

# проверка работы ч.4
# finder4 = WordsFinder('test_file5.txt')
# print(finder4.get_all_words())
# print(finder4.find('Child'))
# print(finder4.count('Child'))

# проверка работы ч.5
# finder5 = WordsFinder('test_file3.txt', 'test_file4.txt', 'test_file5.txt' )
# print(finder5.get_all_words())
# print(finder5.find('the'))
# print(finder5.count('the'))
