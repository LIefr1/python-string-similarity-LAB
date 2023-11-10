import unittest
from strsimpy.optimal_string_alignment_test import TestOptimalStringAlignment
from strsimpy.cosine_test import TestCosine
from strsimpy.damerau_test import TestDamerau
from strsimpy.jaccard_test import TestJaccard
from strsimpy.damerau_test import TestDamerau
from strsimpy.jaro_winkler_test import TestJaroWinkler
from strsimpy.levenshtein_test import TestLevenshtein
from strsimpy.longest_common_subsequence_test import LongestCommonSubsequenceTest
from strsimpy.metric_lcs_test import TestMetricLCS
from strsimpy.ngram_test import TestNGram
from strsimpy.qgram_test import TestQGram
from strsimpy.sift4_test import SIFT4Test

def main():
    tests = [
        TestCosine(),
        TestDamerau(),
        TestJaccard(), 
        TestJaroWinkler(), 
        TestLevenshtein(),
        TestMetricLCS(), 
        TestNGram(), 
        TestQGram(),
        TestOptimalStringAlignment(), 
        LongestCommonSubsequenceTest(),
        SIFT4Test() 
    ]
    for test in tests:
        print(test)

if __name__ == "__main__":
    unittest.main(verbosity=3)