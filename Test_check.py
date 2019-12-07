import unittest

class MojTest(unittest.TestCase):
    #Przypadek testowy

    def setUp ( self ):

    # Przygotowanie do testu
    # Warunki wstepne
        print("Tutaj bedziemy cos testowac")

    def tearDown(self):
    #Sprzatanie po tescie
        print ("Test zakonczony")

    def testGoogleSearch(self):
    #Szukaj
        pass

if (__name__ == '__main__'):
    unittest.main()
