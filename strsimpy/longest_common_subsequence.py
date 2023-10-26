# Copyright (c) 2018 luozhouyang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from .string_distance import StringDistance


class LongestCommonSubsequence(StringDistance):
    
    #нахожение дистанции
    def distance(self, s0, s1):
        #Проверка на пустой тип
        if s0 is None:
            raise TypeError("Argument s0 is NoneType.")
        if s1 is None:
            raise TypeError("Argument s1 is NoneType.")
        #Проверка на равенство
        if s0 == s1:
            return 0.0
        #Ответ
        return len(s0) + len(s1) - 2 * self.length(s0, s1)

    #метод нахождения длины
    @staticmethod
    def length(s0, s1):
        if s0 is None:
            raise TypeError("Argument s0 is NoneType.")
        if s1 is None:
            raise TypeError("Argument s1 is NoneType.")
        #Обявление переменных содержащих длину строк
        s0_len, s1_len = len(s0), len(s1)
        #Объявление переменных x,y с значениями входных строк без последнего элемента
        x, y = s0[:], s1[:]
        #Обявление матрицы и заполнение её нулями, размерностью строк = длинна второй строки + 1, столбцов = длина первой строк + 1 
        matrix = [[0] * (s1_len + 1) for _ in range(s0_len + 1)]
        #Итерация по матрице
        for i in range(1, s0_len + 1):
            for j in range(1, s1_len + 1):
                #если два символа в строках равны
                if x[i - 1] == y[j - 1]:
                    # то значение матрицы на индексе [i][j] будет равно значению матрицы на предъидущем элементе +1  
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    #иначе значение матрицы на текущем индексе равно максимальному значению из элементов на индексе [i][j - 1] или [i - 1][j]
                    matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])
        #Возвращает последний элемент
        return matrix[s0_len][s1_len]
