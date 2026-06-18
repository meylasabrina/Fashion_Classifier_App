# 👗 StyleScan – Fashion Style Classifier

![Status](https://img.shields.io/badge/Status-100%25%20Selesai-success)
![Theme](https://img.shields.io/badge/Tema-AI%20for%20Smart%20Recommendation%20Systems-blue)
![Program](https://img.shields.io/badge/Program-Pijak%20x%20IBM%20Skillsbuild-orange)

**StyleScan** adalah aplikasi berbasis web yang memanfaatkan teknologi *Machine Learning* untuk mengklasifikasikan gaya busana (*fashion style*) dari citra *outfit* secara otomatis. Proyek ini dikembangkan oleh tim **PJK-RM117** sebagai bagian dari Capstone Project program Pijak in collaboration with IBM Skillsbuild.

🔗 **Live Demo Aplikasi:** [fashionclassifierapp.streamlit.app](https://fashionclassifierapp.streamlit.app/)[cite: 1]

---

## 📌 Ringkasan Eksekutif

Banyak pengguna internet mengalami kesulitan dalam mengidentifikasi dan menamai gaya busana dari *outfit* yang mereka lihat di media sosial. Akibatnya, mereka kesulitan menemukan kata kunci (*keywords*) yang tepat saat ingin mencari produk serupa di platform *e-commerce*. 

**StyleScan** hadir untuk mengatasi masalah tersebut melalui:
1. **Model CNN Multi-Label:** Mengembangkan model berbasis *Convolutional Neural Network* (CNN) menggunakan arsitektur EfficientNetB0 / ResNet50 yang mampu mendeteksi gaya fashion secara akurat[cite: 1].
2. **Pendekatan Multi-Label Classification:** Menggunakan fungsi aktivasi *Sigmoid* untuk mengakomodasi satu *outfit* yang memiliki lebih dari satu kategori gaya busana sekaligus[cite: 1].
3. **Penyedia Kata Kunci Terstruktur:** Membantu pengguna mengonversi persepsi visual menjadi terminologi *fashion* yang relevan untuk mempermudah pencarian belanja *online*[cite: 1].

---

## 📸 Antarmuka Produk

Aplikasi ini mengintegrasikan fungsi *backend* (inferensi model) dan *frontend* (antarmuka pengguna) dalam satu *framework* Python menggunakan **Streamlit**[cite: 1].

### 1. Halaman Unggah Gambar
image_9ef5a5.png

### 2. Hasil Klasifikasi Gaya Fashion beserta Confidence Score
image_9ef5c4.png

---

## 🛠️ Arsitektur & Teknologi

* **Framework Antarmuka:** Streamlit[cite: 1]
* **Arsitektur Model:** CNN (EfficientNetB0 / ResNet50)[cite: 1]
* **Fungsi Aktivasi:** Sigmoid (Multi-label classification)[cite: 1]
* **Dataset Utama:** [DeepFashion (Multi-Label Category Classification)](https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)[cite: 1]
* **Metrik Evaluasi:** Precision, Recall, dan F1-Score per label[cite: 1]

---

## 💻 Panduan Instalasi Lokal

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi StyleScan di perangkat lokal Anda.

### 1. Kloning Repositori GitHub
Buka terminal atau Git Bash, kemudian klon repositori ini[cite: 1]:
```bash
git clone [https://github.com/meylasabrina/Fashion_Classifier_App.git](https://github.com/meylasabrina/Fashion_Classifier_App.git)
cd Fashion_Classifier_App

