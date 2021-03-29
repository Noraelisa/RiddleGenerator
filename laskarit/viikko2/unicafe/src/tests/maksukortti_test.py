import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")

    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")   

    def test_ota_rahaa_vahentaa_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")

    def test_ota_rahaa_ei_vie_saldoa_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(16)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1") 

    def test_ota_rahaa_ilmoittaa_riittavatko_rahat(self):
        if self.maksukortti.ota_rahaa(self.maksukortti.saldo < 10):
            return False
        elif self.maksukortti.ota_rahaa(self.maksukortti.saldo > 10):
            return True