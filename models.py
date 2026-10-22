from db import base
from sqlalchemy import Column, String, Date, TIMESTAMP, text, ForeignKey, Boolean

class Pasien(base):
    __tablename__ = 'pasien'

    id_pasien = Column(String, primary_key=True, nullable=False, index=True, server_default=text('uuidv4()'))
    nik = Column(String, nullable=False)
    nama_pasien = Column(String, nullable=False)
    tgl_lahir = Column(Date, nullable=False)
    jns_kelamin = Column(String, nullable=False)
    alamat = Column(String, nullable=False)
    no_hp = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Poli(base):
    __tablename__ = 'poli'

    id_poli = Column(String, primary_key=True, nullable=False, index=True, server_default=text('uuidv4()'))
    nama_poli = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Dokter(base):
    __tablename__ = 'dokter'

    id_dokter = Column(String, primary_key=True, nullable=False, index=True, server_default=text('uuidv4()'))
    nama_dokter = Column(String, nullable=False)
    id_poli = Column(String, ForeignKey('poli.id_poli'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Kunjung(base):
    __tablename__ = 'kunjungan'

    id_kunjung = Column(String, primary_key=True, nullable=False, index=True, server_default=text('uuidv4()'))
    tgl_kunjung = Column(Date, nullable=False)
    id_pasien = Column(String, ForeignKey('pasien.id_pasien'), nullable=False)
    id_dokter = Column(String, ForeignKey('dokter.id_dokter'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class User(base):
    __tablename__ = 'users'

    id_user = Column(String, primary_key=True, nullable=False, index=True, server_default=text('uuidv4()'))
    username = Column(String, nullable=False, index=True, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)