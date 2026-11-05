from datetime import date
from pydantic import BaseModel

# Pasien
class PasienBase(BaseModel):
    nik: str
    nama_pasien: str
    tgl_lahir: date
    jns_kelamin: str
    alamat: str
    no_hp: str

    class Config:
        from_attributes = True

class CreatePasien(PasienBase):
    pass

class ResponePasien(PasienBase):
    id_pasien: str

    class Config:
        from_attributes = True

# Dokter
class DokterBase(BaseModel):
    nama_dokter: str
    id_poli: str

    class Config:
        from_attributes = True

class CreateDokter(DokterBase):
    pass

class ResponeDokter(DokterBase):
    id_dokter: str

    class Config:
        from_attributes = True

# Poli
class PoliBase(BaseModel):
    nama_poli: str

    class Config:
        from_attributes = True

class CreatePoli(PoliBase):
    pass

class ResponePoli(PoliBase):
    id_poli: str

    class Config:
        from_attributes = True

#Kunjung
class KunjungBase(BaseModel):
    tgl_kunjung: date
    id_pasien: str
    id_dokter: str
    no_antre: str
    status: str

    class Config:
        from_attributes = True

class CreateKunjung(KunjungBase):
    pass

class ResponeKunjung(KunjungBase):
    id_kunjung: str

    class Config:
        from_attributes = True

# User

class CreateUser(BaseModel):
    username: str
    password: str

class ResponeUser(BaseModel):
    id_user: str
    username: str

    class Config:
        from_attributes = True

# Token

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

# Periksa

class PeriksaBase(BaseModel):
    id_kunjung: str
    tinggi_badan: int
    berat_badan: int
    tekanan_darah: str
    suhu: int
    keluhan: str
    diagnosa: str
    terapi: str

    class Config:
        from_attributes = True

class CreatePeriksa(PeriksaBase):
    pass

class ResponePeriksa(PeriksaBase):
    id_periksa: str

    class Config:
        from_attributes = True

# Obat

class ObatBase(BaseModel):
    nama_obat: str
    harga_obat: int

    class Config:
        from_attributes = True

class CreateObat(ObatBase):
    pass

class ResponeObat(ObatBase):
    id_obat: str

    class Config:
        from_attributes = True

# Resep

class ResepBase(BaseModel):
    id_periksa: str
    id_obat: str
    jumlah_obat: int
    aturan_pakai: str
    harga_total: int

    class Config:
        from_attributes = True

class CreateResep(ResepBase):
    pass

class ResponeResep(ResepBase):
    id_resep: str

    class Config:
        from_attributes = True