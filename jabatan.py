from pegawai import Pegawai

class Staff(Pegawai):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur):
        # Memanggil init Kakek (Pegawai)
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok)
        self.hari_kerja = hari_kerja
        self.jam_lembur = jam_lembur
        self.tarif_makan = 25000
        self.tarif_lembur = 50000

    def hitung_uang_makan(self):
        return self.hari_kerja * self.tarif_makan

    def hitung_lembur(self):
        return self.jam_lembur * self.tarif_lembur

    def hitung_gaji(self):
        return self.gaji_pokok + self.hitung_uang_makan() + self.hitung_lembur()

class Manajer(Staff): 
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur, bonus_jabatan, tunjangan_transport, tunjangan_kesehatan):
        # REVISI: Memanggil init Ayah (Staff)
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur)
        self.bonus_jabatan = bonus_jabatan
        self.tunjangan_transport = tunjangan_transport
        self.tunjangan_kesehatan = tunjangan_kesehatan

    def hitung_gaji(self):
        # Menggunakan super() untuk mengambil total gaji Staff + bonus khusus manajer
        return super().hitung_gaji() + self.bonus_jabatan + self.tunjangan_transport + self.tunjangan_kesehatan

    def tampilkan_data(self):
        return super().tampilkan_data() + "\nJabatan    : Manajer"

class Supervisor(Pegawai):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, bonus_tim):
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok)
        self.bonus_tim = bonus_tim

    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus_tim

class AdminHRD(Pegawai):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, tunjangan_admin):
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok)
        self.tunjangan_admin = tunjangan_admin

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan_admin