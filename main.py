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
    table.add_column("Keterangan", style="cyan", justify="left")
    table.add_column("Data", style="green", justify="left")
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
    # Tulisan besar keren
    figlet = Figlet(font="slant")
    console.print(f"[bold blue]{figlet.renderText('SMART PAYROLL')}[/bold blue]")

    # Header program
    console.print(Panel.fit("[bold cyan]SISTEM PENGGAJIAN KARYAWAN TERPADU[/bold cyan]\n[bold green]PT Teknologi Masa Depan[/bold green]", border_style="yellow"))

    # Membuat objek perusahaan
    perusahaan = Perusahaan("PT Teknologi Masa Depan")

    # Membuat objek pegawai
    staff1 = Staff("Fitri Khairani", "STF001", "Pekanbaru", "081234567890", 3500000, 22, 10)
    supervisor1 = Supervisor("Rahmat Hidayat", "SPV001", "Bangkinang", "082222222222", 5000000, 1500000)
    manajer1 = Manajer("Sitorus", "MNG001", "Kampar", "083333333333", 8000000, 24, 15, 3000000, 1000000, 1500000)
    admin1 = AdminHRD("Aulia", "HRD001", "Pekanbaru", "084444444444", 4500000, 1200000)

    # Menambahkan pegawai ke perusahaan
    perusahaan.tambah_pegawai(staff1)
    perusahaan.tambah_pegawai(supervisor1)
    perusahaan.tambah_pegawai(manajer1)
    perusahaan.tambah_pegawai(admin1)

    # Menampilkan slip gaji
    cetak_slip_gaji(staff1)
    cetak_slip_gaji(supervisor1)
    cetak_slip_gaji(manajer1)
    cetak_slip_gaji(admin1)

    # Menampilkan seluruh data pegawai
    tampilkan_semua_pegawai(perusahaan)

    # Menampilkan total pengeluaran gaji
    console.print(Panel.fit("[bold magenta]TOTAL PENGELUARAN GAJI[/bold magenta]", border_style="red"))
    console.print(f"[bold green]Rp{perusahaan.total_pengeluaran_gaji():,}[/bold green]")