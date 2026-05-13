from pegawai import Pegawai

# 1. Kelas Turunan: Staff (Pewarisan dari Pegawai)
class Staff(Pegawai):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur):
        # Memanggil konstruktor kelas induk
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
    
    def tampilkan_data(self):
        data_induk = super().tampilkan_data()
        return data_induk + f"""
        Jabatan      : Staff
        Hari Kerja   : {self.hari_kerja} hari
        Jam Lembur   : {self.jam_lembur} jam
        Uang Makan   : Rp{self.hitung_uang_makan():,}
        Uang Lembur  : Rp{self.hitung_lembur():,}
        Gaji Total   : Rp{self.hitung_gaji():,}
        """

# 2. Kelas Manajer ((Turunan Staff -> Multilevel Inheritance))
class Manajer(Staff): 
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur, bonus_jabatan, tunjangan_transport, tunjangan_kesehatan):
        # Memanggil konstruktor kelas Staff
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur)
        self.bonus_jabatan = bonus_jabatan
        self.tunjangan_transport = tunjangan_transport
        self.tunjangan_kesehatan = tunjangan_kesehatan

    def hitung_gaji(self):
        # Menggunakan super() untuk mengambil total gaji Staff + bonus khusus manajer
        return super().hitung_gaji() + self.bonus_jabatan + self.tunjangan_transport + self.tunjangan_kesehatan

    def tampilkan_data(self):
    data_induk = Pegawai.tampilkan_data(self)
    return data_induk + f"""
    Jabatan            : Manajer
    Hari Kerja         : {self.hari_kerja} hari
    Jam Lembur         : {self.jam_lembur} jam
    Uang Makan         : Rp{self.hitung_uang_makan():,}
    Uang Lembur        : Rp{self.hitung_lembur():,}
    Bonus Jabatan      : Rp{self.bonus_jabatan:,}
    Tunj. Transport    : Rp{self.tunjangan_transport:,}
    Tunj. Kesehatan    : Rp{self.tunjangan_kesehatan:,}
    Gaji Total         : Rp{self.hitung_gaji():,}
    """
    
# 3. Kelas Supervisor (Turunan Langsung Pegawai)
class Supervisor(Pegawai):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, bonus_tim):
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok)
        self.bonus_tim = bonus_tim

    def hitung_gaji(self):
        return self.gaji_pokok + self.bonus_tim
    
    def tampilkan_data(self):
        data_induk = super().tampilkan_data()
        return data_induk + f"""
        Jabatan     : Supervisor
        Bonus Tim   : Rp{self.bonus_tim:,}
        Gaji Total  : Rp{self.hitung_gaji():,}
        """

# 4. Kelas AdminHRD (Turunan Langsung Pegawai)
class AdminHRD(Pegawai):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok, tunjangan_admin):
        super().__init__(nama, id_pegawai, alamat, no_hp, gaji_pokok)
        self.tunjangan_admin = tunjangan_admin

    def hitung_gaji(self):
        return self.gaji_pokok + self.tunjangan_admin

    def tampilkan_data(self):
        data_induk = super().tampilkan_data()
        return data_induk + f"""
        Jabatan     : Admin HRD
        Tunj. Admin : Rp{self.tunjangan_admin:,}
        Gaji Total  : Rp{self.hitung_gaji():,}
        """    