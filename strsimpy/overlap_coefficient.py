from .shingle_based import ShingleBased
from .string_distance import NormalizedStringDistance
from .string_similarity import NormalizedStringSimilarity


class OverlapCoefficient(ShingleBased, NormalizedStringDistance, NormalizedStringSimilarity):

    def __init__(self, k=3):
        super().__init__(k)

    def distance(self, s0, s1):
        return 1.0 - self.similarity(s0, s1)


    def similarity(self, s0, s1):
        if s0 is None:
            raise TypeError("Argument s0 is NoneType.")
        if s1 is None:
            raise TypeError("Argument s1 is NoneType.")
        if s0 == s1:
            return 1.0
        union = set()
        #получение профилей строк
        profile0, profile1 = self.get_profile(s0), self.get_profile(s1)
        #добавление ключей профилей в сет(неизменяемый список)
        for k in profile0.keys():
            union.add(k)
        for k in profile1.keys():
            union.add(k)
        #расчёт разцницы между общей длины строк и длины сета
        inter = int(len(profile0.keys()) + len(profile1.keys()) - len(union))
        #расчёт коэфициента пересечений
        return inter / min(len(profile0), len(profile1))
