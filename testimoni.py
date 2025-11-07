<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Galeri Foto Amerta</title>
    <style>
      /* --- CSS STYLES --- */
      body {
        font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #e9ebee;
        color: #333;
        line-height: 1.6;
      }

      .container {
        max-width: 1200px;
        margin: 30px auto;
        padding: 0 25px;
      }

      header {
        text-align: center;
        padding: 60px 0;
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 40px;
      }

      header h1 {
        margin: 0;
        color: #2c3e50;
        font-size: 3.2em;
        letter-spacing: -1px;
      }

      header p {
        color: #7f8c8d;
        font-size: 1.3em;
        margin-top: 15px;
        max-width: 700px;
        margin-left: auto;
        margin-right: auto;
      }

      .gallery-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
      }

      .gallery-item {
        background-color: #ffffff;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        cursor: pointer;
      }

      .gallery-item:hover {
        transform: translateY(-8px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.12);
      }

      .gallery-item img {
        width: 100%;
        height: 220px;
        object-fit: cover;
        display: block;
        border-bottom: 1px solid #eee;
        transition: transform 0.3s ease;
      }

      .gallery-item:hover img {
        transform: scale(1.03);
      }

      .gallery-item-info {
        padding: 20px;
      }

      .gallery-item-info h3 {
        margin-top: 0;
        margin-bottom: 10px;
        color: #34495e;
        font-size: 1.5em;
      }

      .gallery-item-info p {
        color: #95a5a6;
        font-size: 1em;
        line-height: 1.6;
      }

      /* Lightbox (Modal) Styles */
      .lightbox-modal {
        display: none; /* Hidden by default */
        position: fixed;
        z-index: 1000;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0, 0, 0, 0.8);
        justify-content: center;
        align-items: center;
        animation: fadeIn 0.3s ease-out;
      }

      .lightbox-content {
        position: relative;
        background-color: #fefefe;
        margin: auto;
        padding: 0;
        border-radius: 10px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
        width: 80%;
        max-width: 900px;
        animation: zoomIn 0.3s ease-out;
        display: flex;
        flex-direction: column;
        max-height: 90vh;
      }

      .lightbox-content img {
        width: 100%;
        height: auto;
        max-height: 70vh;
        object-fit: contain;
        border-top-left-radius: 10px;
        border-top-right-radius: 10px;
      }

      .lightbox-caption {
        padding: 20px;
        text-align: center;
        color: #333;
        font-size: 1.1em;
        line-height: 1.5;
        max-height: 20vh;
        overflow-y: auto;
      }

      .close-button {
        color: #aaa;
        position: absolute;
        top: 15px;
        right: 25px;
        font-size: 35px;
        font-weight: bold;
        cursor: pointer;
        transition: color 0.3s;
      }

      .close-button:hover,
      .close-button:focus {
        color: #f44336;
        text-decoration: none;
        cursor: pointer;
      }

      footer {
        text-align: center;
        padding: 40px 0;
        margin-top: 60px;
        background-color: #2c3e50;
        color: #ecf0f1;
        font-size: 1em;
        border-top: 1px solid #34495e;
      }

      @keyframes fadeIn {
        from {
          opacity: 0;
        }
        to {
          opacity: 1;
        }
      }

      @keyframes zoomIn {
        from {
          transform: scale(0.9);
          opacity: 0.8;
        }
        to {
          transform: scale(1);
          opacity: 1;
        }
      }

      @media (max-width: 768px) {
        header h1 {
          font-size: 2.5em;
        }
        .gallery-grid {
          grid-template-columns: 1fr;
        }
      }
    </style>
  </head>
  <body>
    <header>
      <div class="container">
        <h1>Momen AMERTA</h1>
        <p>
          Jelajahi koleksi foto AMERTA yang merekam kegabutan dan cerita dari
          berbagai pengalamanya🤔.
        </p>
      </div>
    </header>

    <div class="container">
      <div class="gallery-grid">
        <div
          class="gallery-item"
          data-src="https://i.ibb.co.com/bRNb96Ms/Whats-App-Image-2025-11-06-at-14-35-57-56b9bd19.jpg"
          data-caption="orang gila yang sedang berkumpul ."
        >
          <img
            src="https://i.ibb.co.com/YTf0sNFc/Whats-App-Image-2025-11-06-at-14-35-57-56b9bd19.jpg"
            alt="AMERTA FAMILY"
          />
          <div class="gallery-item-info">
            <h3>orang orang gawah</h3>
            <p>memory lama.</p>
          </div>
        </div>

        <div
          class="gallery-item"
          data-src="https://i.ibb.co.com/n80nh8RP/Whats-App-Image-2025-11-06-at-14-35-56-6f404568.jpg"
          data-caption="Lanskap kota yang mempesona di malam hari, dengan gemerlap cahaya dan gedung-gedung pencakar langit."
        >
          <img
            src="https://i.ibb.co.com/n80nh8RP/Whats-App-Image-2025-11-06-at-14-35-56-6f404568.jpg"
            alt="Lanskap Kota Malam"
          />
          <div class="gallery-item-info">
            <h3>Ulang Tahun Surya  </h3>
            <p>keluarga adam dan hawa.</p>
          </div>
        </div>

        <div
          class="gallery-item"
          data-src="https://i.ibb.co.com/FbFTkvv0/Whats-App-Image-2025-11-06-at-14-35-56-be8696cb.jpg"
          data-caption="Potret harimau yang agung dengan tatapan mata yang tajam, melambangkan kekuatan dan keindahan alam liar."
        >
          <img
            src="https://i.ibb.co.com/FbFTkvv0/Whats-App-Image-2025-11-06-at-14-35-56-be8696cb.jpg"
            alt="Harimau Liar"
          />
          <div class="gallery-item-info">
            <h3>Basket Ball Time</h3>
            <p>Tidak Terkalahkan.</p>
          </div>
        </div>

        <div
          class="gallery-item"
          data-src="https://i.ibb.co.com/XxMZ6X7F/Whats-App-Image-2025-11-06-at-14-35-56-09b9c716.jpg"
          data-caption="Hidangan pasta dengan saus tomat segar, basil, dan keju parmesan, siap disantap."
        >
          <img
            src="https://i.ibb.co.com/XxMZ6X7F/Whats-App-Image-2025-11-06-at-14-35-56-09b9c716.jpg"
            alt="Hidangan Pasta"
          />
          <div class="gallery-item-info">
            <h3>Hari Santri tapi kita bukan santri </h3>
            <p>6 7.</p>
          </div>
        </div>

        <div
          class="gallery-item"
          data-src="https://i.ibb.co.com/fVQXDgp8/Whats-App-Image-2025-11-06-at-14-35-57-5cf0e7de.jpg"
          data-caption="bocah anomali,ga jelas."
        >
          <img
            src="https://i.ibb.co.com/fVQXDgp8/Whats-App-Image-2025-11-06-at-14-35-57-5cf0e7de.jpg"
            alt="Core Amerta"
          />
          <div class="gallery-item-info">
            <h3>Bersama king drawing </h3>
            <p>Kedamaian dalam setiap ada dia.</p>
          </div>
        </div>

        <div
          class="gallery-item"
          data-src="https://i.ibb.co.com/4nYVvXtm/Whats-App-Image-2025-11-06-at-14-35-57-4e731b51.jpg"
          data-caption="Pemandangan matahari terbenam yang dramatis di pantai, dengan langit jingga dan siluet pohon kelapa."
        >
          <img
            src="https://i.ibb.co.com/4nYVvXtm/Whats-App-Image-2025-11-06-at-14-35-57-4e731b51.jpg"
            alt="Matahari Terbenam Pantai"
          />
          <div class="gallery-item-info">
            <h3>Anak Baden Powell</h3>
            <p>
              orang keren jangan di lawan.
            </p>
          </div>
        </div>
      </div>
    </div>

    <footer>
      <div class="container">
        <p>&copy; 2024-2025 Galeri Foto Amerta ❤.</p>
      </div>
    </footer>

    <div id="lightbox" class="lightbox-modal">
      <span class="close-button">&times;</span>
      <div class="lightbox-content">
        <img id="lightbox-img" src="" alt="Gambar Diperbesar" />
        <div id="lightbox-caption" class="lightbox-caption"></div>
      </div>
    </div>

    <script>
      document.addEventListener("DOMContentLoaded", function () {
        const galleryItems = document.querySelectorAll(".gallery-item");
        const lightbox = document.getElementById("lightbox");
        const lightboxImg = document.getElementById("lightbox-img");
        const lightboxCaption = document.getElementById("lightbox-caption");
        const closeButton = document.querySelector(".close-button");

        galleryItems.forEach((item) => {
          item.addEventListener("click", function () {
            lightbox.style.display = "flex"; // Tampilkan lightbox
            lightboxImg.src = this.dataset.src; // Ambil URL gambar besar
            lightboxCaption.textContent = this.dataset.caption; // Ambil keterangan
            document.body.style.overflow = "hidden"; // Nonaktifkan scroll halaman utama
          });
        });

        closeButton.addEventListener("click", function () {
          lightbox.style.display = "none";
          document.body.style.overflow = ""; // Aktifkan scroll
        });

        // Tutup saat mengklik di luar gambar
        lightbox.addEventListener("click", function (e) {
          if (e.target === lightbox) {
            lightbox.style.display = "none";
            document.body.style.overflow = "";
          }
        });

        // Tutup dengan tombol Escape
        document.addEventListener("keydown", function (e) {
          if (e.key === "Escape" && lightbox.style.display === "flex") {
            lightbox.style.display = "none";
            document.body.style.overflow = "";
          }
        });
      });
    </script>
  </body>
</html>