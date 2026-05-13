from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import print
from pyfiglet import Figlet

from jabatan import Staff, Supervisor, Manajer, AdminHRD
from perusahaan import Perusahaan

console = Console()

def cetak_slip_gaji(objek_pegawai):
    table = Table(title="Slip Gaji Pegawai", show_lines=True)
    table.add_column("Keterangan", style="cyan")
    table.add_column("Data", style="green")
    table.add_row("ID Pegawai", objek_pegawai.id_pegawai)
    table.add_row("Nama", objek_pegawai.nama)
    table.add_row("Alamat", objek_pegawai.alamat)
    table.add_row("No HP", objek_pegawai.no_hp)
    table.add_row("Gaji Pokok", f"Rp{objek_pegawai.gaji_pokok:,}")
    table.add_row("Total Gaji", f"Rp{objek_pegawai.hitung_gaji():,}")
    console.print(table)

def tampilkan_semua_pegawai(perusahaan):
    table = Table(title="Data Seluruh Pegawai", show_lines=True)
    table.add_column("ID", style="cyan")
    table.add_column("Nama", style="green")
    table.add_column("Alamat")
    table.add_column("No HP")
    table.add_column("Total Gaji", style="yellow")
    for pegawai in perusahaan.daftar_pegawai:
        table.add_row(pegawai.id_pegawai, pegawai.nama, pegawai.alamat, pegawai.no_hp, f"Rp{pegawai.hitung_gaji():,}")
    console.print(table)

if __name__ == "__main__":
    figlet = Figlet(font="slant")
    console.print(f"[bold blue]{figlet.renderText('SMART PAYROLL')}[/bold blue]")
    console.print(Panel.fit("[bold cyan]SISTEM PENGGAJIAN KARYAWAN TERPADU[/bold cyan]\n[bold green]PT Teknologi Masa Depan[/bold green]", border_style="yellow"))

    perusahaan = Perusahaan("PT Teknologi Masa Depan")

    while True:
        print("\n" + "="*50)
        print("MENU UTAMA")
        print("="*50)
        print("1. Tambah Pegawai")
        print("2. Tampilkan Semua Pegawai")
        print("3. Total Pengeluaran Gaji")
        print("4. Keluar")

        pilihan = input("\nMasukkan pilihan: ")

        if pilihan == "1":
            print("\nPilih Jabatan:")
            print("1. Staff")
            print("2. Supervisor")
            print("3. Manajer")
            print("4. Admin HRD")
            jabatan = input("Masukkan pilihan jabatan: ")

            nama = input("Nama Pegawai            : ")
            id_pegawai = input("ID Pegawai              : ")
            alamat = input("Alamat                  : ")
            no_hp = input("No HP                   : ")
            gaji_pokok = int(input("Gaji Pokok              : ").replace(".", ""))

            if jabatan == "1":
                hari_kerja = int(input("Jumlah Hari Kerja       : ").replace(".", ""))
                jam_lembur = int(input("Jumlah Jam Lembur       : ").replace(".", ""))
                pegawai = Staff(nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur)

            elif jabatan == "2":
                bonus_tim = int(input("Bonus Tim               : ").replace(".", ""))
                pegawai = Supervisor(nama, id_pegawai, alamat, no_hp, gaji_pokok, bonus_tim)

            elif jabatan == "3":
                hari_kerja = int(input("Jumlah Hari Kerja       : ").replace(".", ""))
                jam_lembur = int(input("Jumlah Jam Lembur       : ").replace(".", ""))
                bonus_jabatan = int(input("Bonus Jabatan           : ").replace(".", ""))
                tunjangan_transport = int(input("Tunjangan Transport     : ").replace(".", ""))
                tunjangan_kesehatan = int(input("Tunjangan Kesehatan     : ").replace(".", ""))
                pegawai = Manajer(nama, id_pegawai, alamat, no_hp, gaji_pokok, hari_kerja, jam_lembur, bonus_jabatan, tunjangan_transport, tunjangan_kesehatan)

            elif jabatan == "4":
                tunjangan_admin = int(input("Tunjangan Admin         : ").replace(".", ""))
                pegawai = AdminHRD(nama, id_pegawai, alamat, no_hp, gaji_pokok, tunjangan_admin)

            else:
                print("\nPilihan jabatan tidak valid!")
                continue

            perusahaan.tambah_pegawai(pegawai)
            print("\n[bold green]Pegawai berhasil ditambahkan![/bold green]")
            cetak_slip_gaji(pegawai)

        elif pilihan == "2":
            tampilkan_semua_pegawai(perusahaan)

        elif pilihan == "3":
            console.print(Panel.fit("[bold magenta]TOTAL PENGELUARAN GAJI[/bold magenta]", border_style="red"))
            console.print(f"[bold green]Rp{perusahaan.total_pengeluaran_gaji():,}[/bold green]")

        elif pilihan == "4":
            print("\nTerima kasih telah menggunakan program.")
            break

        else:
            print("\nPilihan tidak valid!")