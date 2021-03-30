import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_syo_edullisesti_kateisella_kasvattaa_rahamaaraa_oikein(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_kateisella_kasvattaa_rahamaaraa_oikein(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_edullisesti_kateisella_vaihtoraha_on_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(480)
        self.assertEqual(vaihtoraha, 240)

    def test_syo_maukkaasti_kateisella_vaihtoraha_on_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(800)
        self.assertEqual(vaihtoraha, 400)

    def test_syo_edullisesti_kateisella_kasvattaa_edullisia(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella_kasvattaa_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kateisella_maksu_ei_riittava_kassapaate_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_maksu_ei_riittava_kassapaate_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kortilla_velottaa_kortilta_oikein_kortilla_riittavasti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-240)

    def test_syo_maukkaasti_kortilla_velottaa_kortilta_oikein_kortilla_riittavasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 1000-400)

    def test_syo_edullisesti_kortilla_ei_velota_kortilta_jos_kortilla_liian_vahan(self):
        maksukortti = Maksukortti(230)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 230)
        
    def test_syo_maukkaasti_kortilla_ei_veloita_kortilta_jos_kortilla_liian_vahan(self):
        maksukortti = Maksukortti(390)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 390)
    
    def test_syo_edullisesti_kortilla_riittava_summa_kasvattaa_edullisia(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_riittava_summa_kasvattaa_maukkaita(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_maksu_ei_muuta_kassapaatteen_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_maksu_ei_muuta_kassapaatteen_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortille_ladataan_rahaa_kortin_saldo_muuttuu_kassan_summa_nousee(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 10)
        self.assertEqual(self.maksukortti.saldo, 1010)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100010)

    def test_kortille_ladataan_negatiivista_rahamaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -10)    
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)