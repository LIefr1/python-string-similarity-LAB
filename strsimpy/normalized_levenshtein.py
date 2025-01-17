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

from .string_distance import NormalizedStringDistance
from .string_similarity import NormalizedStringSimilarity
from .levenshtein import Levenshtein


class NormalizedLevenshtein(NormalizedStringDistance, NormalizedStringSimilarity):

    #инициализация класса, и переменной в которой содержиться экземпляр класса Levenshtein
    def __init__(self):
        self.levenshtein = Levenshtein()
    #Вычисляет нормализоанную дистацию Левенштайна
    def distance(self, s0, s1):
        #Проверка на тип
        if s0 is None:
            raise TypeError("Argument s0 is NoneType.")
        if s1 is None:
            raise TypeError("Argument s1 is NoneType.")
        #Проверка на равество 
        if s0 == s1:
            return 0.0
        #переменная предствляет максимальную длину из двух строк
        m_len = max(len(s0), len(s1))
        #если длина ноль, возвращает ноль иначе получает длину по Левенштайну и нормализирует ее, 
        # путём деления на максимальную длину
        if m_len == 0:
            return 0.0
        return self.levenshtein.distance(s0, s1) / m_len
    
    #оцениват схожеть строк
    def similarity(self, s0, s1):
        return 1.0 - self.distance(s0, s1)
