cats_data = [('Фродо', 3, 'Анна', 'Самохина'),
  ('Вася', 4, 'Алексей', 'Егоров')]
#def everything_for_your_cat(cats_data):
cats_data_1 = []
if cats_data == []:
    our_str = ''
else:
        our_str = f"{cats_data[0][2]} {cats_data[0][3]}: {cats_data[0][0]}, {cats_data[0][1]}"
        while cats_data > []:
            for i in range(1, len(cats_data)):
                if cats_data[0][2] in cats_data[i] and cats_data[0][3] in cats_data[i]:
                    our_str = f"{our_str}, {cats_data[i][0]}, {cats_data[i][1]}"
                    cats_data_1.append(cats_data[i])
            del cats_data[0]
            result = []
            for k in cats_data:
                if k not in cats_data_1:
                    result.append(k)
            cats_data = result
            cats_data_1 = []
            if cats_data > []:
                our_str = f"{our_str}\n{cats_data[0][2]} {cats_data[0][3]}: {cats_data[0][0]}, {cats_data[0][1]}"
print(our_str)
#    return our_str
