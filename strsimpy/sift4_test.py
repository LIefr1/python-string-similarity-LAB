import unittest

from .sift4 import SIFT4


class SIFT4Test(unittest.TestCase):

    def testSIFT4(self):
        s = SIFT4()
        
        results = [
            ({5:'asd'}, 'And this is another string', 5, 11.0),
            ('Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Amet Lorm ispum dolor sit amet, consetetur adixxxpiscing elit.', 10, 12.0)
        ]

        for a, b, offset, res in results:
            self.assertEqual(res, s.distance(a, b, maxoffset=offset))


if __name__ == "__main__":
    unittest.main()
