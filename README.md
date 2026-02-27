Siap, mengerti! Kamu ingin versi **Full Markdown Code Block** dari awal sampai akhir tanpa ada gangguan teks penjelasan di luarnya agar bisa langsung di-copy-paste total.

Berikut adalah isi file `README.md` kamu:

```markdown
# Flask User & Task Management System

Proyek ini adalah API untuk manajemen pengguna (User) dan tugas (Task) yang dibangun menggunakan **Flask**. Proyek ini menerapkan **3-Tier Architecture** (Route -> Service -> Repository) untuk menjaga pemisahan tanggung jawab kode yang bersih dan profesional.



## 📁 Struktur Folder
Struktur proyek mengikuti pola arsitektur berikut:
- **`app/models/`**: Definisi skema database menggunakan SQLAlchemy (Data Tier).
- **`app/repositories/`**: Lapisan data untuk query database mentah.
- **`app/services/`**: Lapisan logika bisnis dan validasi data (Logic Tier).
- **`app/routes/`**: Definisi endpoint API menggunakan Blueprints (Presentation Tier).
- **`app/utils/`**: Utilitas tambahan untuk standarisasi format response.

## 🛠️ Instalasi & Setup

1. **Clone Repositori**
   ```bash
   git clone <repository-url>
   cd flask-user-management

```

2. **Instal Dependensi**
Proyek ini menggunakan `pipenv`. Pastikan Pipenv sudah terinstal di sistem kamu.
```bash
pipenv install

```


3. **Aktifkan Virtual Environment**
```bash
pipenv shell

```


4. **Inisialisasi Database**
Jalankan perintah berikut untuk migrasi database SQLite:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

```


5. **Jalankan Aplikasi**
```bash
python run.py

```



## 🚀 Dokumentasi API

Semua endpoint diawali dengan prefix `/api`.

### 👤 User Endpoints

| Method | Endpoint | Deskripsi |
| --- | --- | --- |
| `POST` | `/api/users` | Membuat user baru (Email harus unik) |
| `GET` | `/api/users` | Mendapatkan semua daftar user |
| `GET` | `/api/users/<id>` | Mendapatkan detail informasi satu user |
| `PUT` | `/api/users/<id>` | Memperbarui data user (Name/Email) |
| `DELETE` | `/api/users/<id>` | Menghapus user dari sistem |
| `GET` | `/api/users/<id>/tasks` | Mendapatkan daftar tugas milik user tertentu |

### 📝 Task Endpoints

| Method | Endpoint | Deskripsi |
| --- | --- | --- |
| `GET` | `/api/tasks` | Mendapatkan semua daftar tugas |
| `POST` | `/api/tasks` | Membuat tugas baru (Wajib mencantumkan `user_id`) |
| `GET` | `/api/tasks/<id>` | Mendapatkan detail informasi satu tugas |
| `PUT` | `/api/tasks/<id>` | Memperbarui data tugas (Title/Desc/Status) |
| `DELETE` | `/api/tasks/<id>` | Menghapus tugas dari sistem |

## 📦 Tech Stack

Sesuai dengan `Pipfile`, proyek ini menggunakan:

* **Flask**: Framework web mikro.
* **Flask-SQLAlchemy**: ORM (Object Relational Mapper).
* **Flask-Migrate**: Alat migrasi database.
* **Python-dotenv**: Pengelolaan environment variables.
* **Marshmallow**: Serialisasi dan validasi data.
* **Pytest**: Framework pengujian aplikasi.