<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Badminton Club</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <!-- Header / Beranda -->
    <header class="bg-primary text-white text-center py-4">
        <h1>Badminton Club</h1>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="container">
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav mx-auto">
                        <li class="nav-item"><a class="nav-link active" href="#home">Beranda</a></li>
                        <li class="nav-item"><a class="nav-link" href="#pendaftaran">Pendaftaran</a></li>
                        <li class="nav-item"><a class="nav-link" href="#daftar-atlet">Daftar Atlet</a></li>
                        <li class="nav-item"><a class="nav-link" href="#detail-tempat">Detail Tempat</a></li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <!-- Beranda Section -->
    <section id="home" class="py-5 bg-light text-center">
        <div class="container">
            <h2 class="display-4">Selamat Datang di Brahrang Badminton Club!</h2>
            <p class="lead">Temukan semangat bermain badminton bersama kami di klub terbaik di kota Anda.</p>
        </div>
    </section>

    <!-- Pendaftaran Section -->
    <section id="pendaftaran" class="py-5">
        <div class="container">
            <h2 class="display-5 text-center">Pendaftaran Anggota Baru</h2>
            <div class="row justify-content-center">
                <div class="col-md-6">
                    <form id="registrationForm" class="p-4 border rounded">
                        <div class="mb-3">
                            <label for="name" class="form-label">Nama Lengkap:</label>
                            <input type="text" class="form-control" id="name" name="name" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label">Email:</label>
                            <input type="email" class="form-control" id="email" name="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="phone" class="form-label">Nomor Telepon:</label>
                            <input type="tel" class="form-control" id="phone" name="phone" required>
                        </div>
                        <button type="submit" class="btn btn-primary w-100">Daftar</button>
                    </form>
                    <p id="confirmationMessage" class="mt-3 text-success text-center"></p>
                </div>
            </div>
        </div>
    </section>

    <!-- Daftar Atlet Section -->
    <section id="daftar-atlet" class="py-5 bg-light">
        <div class="container">
            <h2 class="display-5 text-center">Daftar Atlet</h2>
            <table class="table table-bordered table-striped">
                <thead class="bg-primary text-white">
                    <tr>
                        <th>Nama</th>
                        <th>Usia</th>
                        <th>Jenis Kelamin</th>
                        <th>Prestasi</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Biriant Reynard</td>
                        <td>15</td>
                        <td>Laki-laki</td>
                        <td>Juara 1 Tournament Home 2023</td>
                    </tr>
                    <tr>
                        <td>Luis Fernandes</td>
                        <td>16</td>
                        <td>Laki-Laki</td>
                        <td>Juara 2 tournament Home 2024</td>
                    </tr>
                    <tr>
                        <td>Cristian Gautama</td>
                        <td>16</td>
                        <td>Laki-laki</td>
                        <td>Juara 1 Tournament Home 2024</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </section>

    <!-- Detail Tempat Section -->
    <section id="detail-tempat" class="py-5">
        <div class="container">
            <h2 class="display-5 text-center">Detail Tempat</h2>
            <div class="row">
                <div class="col-md-6">
                    <h3>Lokasi Lapangan</h3>
                    <p>Kami berlokasi di Brahrang di gang Basket.</p>
                    <ul>
                        <li>Alamat: Jl. Jenderal Gatot Subroto No.534, Suka Maju, Kec. Binjai Bar., Kota Binjai, Sumatera Utara 20719</li>
                        <li>Fasilitas: 2 Lapangan Indoor, Area Parkir</li>
                        <li>Jam Operasional: Senin,Rabu,Jumat,Sabtu (17:30 - 20:30)</li>
                    </ul>
                </div>
                <div class="col-md-6">
                    <h3>Peta Lokasi</h3>
                    <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d7963.826884212904!2d98.43571230769157!3d3.6072844761447636!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3030d66150c79df7%3A0x9f3ff6829811f5c0!2sLapangan%20Brahrang%20Club!5e0!3m2!1sen!2sid!4v1727057277391!5m2!1sen!2sid" width="100%" height="300" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
                </div>
            </div>
        </div>
    </section>

    <!-- Penutup (Footer) -->
    <footer class="bg-primary text-white text-center py-3">
        <p>&copy; 2024 Badminton Club. All Rights Reserved.</p>
        <p>Instagram: <a href="pb.Brahrang.club" class="text-white">pb.Brahrang.club</a> | Telepon: +62 812 6028 6294</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script src="js/script.js"></script>
</body>
</html>
