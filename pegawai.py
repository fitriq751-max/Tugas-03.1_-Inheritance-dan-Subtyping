from abc import ABC, abstractmethod

# ==================================================
# KELAS INDUK UTAMA
# ==================================================
class Pegawai(ABC):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.alamat = alamat
        self.no_hp = no_hp
        self.gaji_pokok = gaji_pokok

    def tampilkan_data(self):
        return f"""
        ID Pegawai   : {self.id_pegawai}
        Nama         : {self.nama}
        Alamat       : {self.alamat}
        No HP        : {self.no_hp}
        Gaji Pokok   : Rp{self.gaji_pokok:,}
        """

    @abstractmethod
    def hitung_gaji(self):
        pass