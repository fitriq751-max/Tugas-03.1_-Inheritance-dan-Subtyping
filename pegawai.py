from abc import ABC, abstractmethod

class Pegawai(ABC):
    def __init__(self, nama, id_pegawai, alamat, no_hp, gaji_pokok):
        self.nama = nama
        self.id_pegawai = id_pegawai
        self.alamat = alamat
        self.no_hp = no_hp
        self.gaji_pokok = gaji_pokok

    def tampilkan_data(self):
        return (
            f"ID Pegawai : {self.id_pegawai}\n"
            f"Nama       : {self.nama}\n"
            f"Alamat     : {self.alamat}\n"
            f"No HP      : {self.no_hp}\n"
            f"Gaji Pokok : Rp{self.gaji_pokok:,}"
        )

    @abstractmethod
    def hitung_gaji(self):
        pass