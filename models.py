from db import base
from sqlalchemy import Column, String, Date, TIMESTAMP, text, ForeignKey, Boolean, SmallInteger, Integer

class Pasien(base):
    __tablename__ = 'pasien'

    id_pasien = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    nik = Column(String, nullable=False)
    nama_pasien = Column(String, nullable=False)
    tgl_lahir = Column(Date, nullable=False)
    jns_kelamin = Column(String, nullable=False)
    alamat = Column(String, nullable=False)
    no_hp = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Poli(base):
    __tablename__ = 'poli'

    id_poli = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    nama_poli = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Dokter(base):
    __tablename__ = 'dokter'

    id_dokter = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    nama_dokter = Column(String, nullable=False)
    id_poli = Column(String, ForeignKey('poli.id_poli'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Kunjung(base):
    __tablename__ = 'kunjungan'

    id_kunjung = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    tgl_kunjung = Column(Date, nullable=False)
    id_pasien = Column(String, ForeignKey('pasien.id_pasien'), nullable=False)
    id_dokter = Column(String, ForeignKey('dokter.id_dokter'), nullable=False)
    no_antre = Column(String)
    status = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class User(base):
    __tablename__ = 'users'

    id_user = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    username = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Periksa(base):
    __tablename__ = 'periksa'

    id_periksa = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    id_kunjung = Column(String, ForeignKey('kunjungan.id_kunjung'), nullable=False)
    tinggi_badam = Column(SmallInteger)
    berat_badan = Column(SmallInteger)
    suhu = Column(SmallInteger)
    tekanan_darah = Column(String)
    keluhan = Column(String)
    diagnosa = Column(String)
    terapi = Column(String)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Obat(base):
    __tablename__ = 'obat'

    id_obat = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    nama_obat = Column(String, index=True)
    harga_obat = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Resep(base):
    __tablename__ = 'resep'

    id_resep = Column(String, primary_key=True, nullable=False, index=True, server_default=text('gen_random_uuid()'))
    id_periksa = Column(String, ForeignKey('periksa.id_periksa'))
    id_obat = Column(String, ForeignKey('obat.id_obat'))
    jumlah_obat = Column(SmallInteger)
    aturan_pakai = Column(String)
    total_harga = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))