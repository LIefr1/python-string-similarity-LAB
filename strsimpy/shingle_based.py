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

#библиотека поддержки регулярных выражений
import re
#регулярное выражение поиска любого пробела в строке
_SPACE_PATTERN = re.compile("\\s+")


class ShingleBased:
    #инициализатор класса, с переменной к, поумолчанию имеет занчение 3
    def __init__(self, k=3):
        self.k = k
    #метод позволяющий получит переменную к
    def get_k(self):
        return self.k

    #метод получиения "профиля", метод принимает одну переменную
    def get_profile(self, string):
        #инициализация переменной "shingles", которая является словарем
        shingles = dict()
        #инициализация переменной "no_space_str", в которую передаётся без пробельная пользовательская строка, посланная при вызове метода
        no_space_str = _SPACE_PATTERN.sub(" ", string)

        #здесь ищеться частота появления символов в строке
        for i in range(len(no_space_str) - self.k + 1):
            shingle = no_space_str[i:i + self.k]
            old = shingles.get(shingle)
            if old:
                shingles[str(shingle)] = int(old + 1)
            else:
                shingles[str(shingle)] = 1
        return shingles
