class Perusahaan:

    def __init__(self, nama_perusahaan):
        self.nama_perusahaan = nama_perusahaan
        self.daftar_pegawai = []

    def tambah_pegawai(self, pegawai):
        self.daftar_pegawai.append(pegawai)

    def tampilkan_semua_pegawai(self):

        print("\n")
        print("=" * 50)
        print("DATA SELURUH PEGAWAI")
        print("=" * 50)

        for pegawai in self.daftar_pegawai:

            print("\n" + "-" * 50)

            print(pegawai.tampilkan_data())

            print(
                f"Total Gaji : Rp{pegawai.hitung_gaji():,}"
            )

    def total_pengeluaran_gaji(self):

        total = 0

        for pegawai in self.daftar_pegawai:
            total += pegawai.hitung_gaji()

        return total
    