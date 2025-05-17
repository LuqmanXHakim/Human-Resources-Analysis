# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan memiliki lebih dari 1.000 karyawan yang tersebar di berbagai wilayah. Meskipun telah berkembang menjadi perusahaan berskala besar, perusahaan ini menghadapi tantangan serius dalam aspek manajemen sumber daya manusia, terutama dalam mengelola tingkat retensi karyawan. Salah satu indikator utama dari permasalahan ini adalah tingginya tingkat attrition, yaitu persentase karyawan yang meninggalkan perusahaan dalam periode tertentu. Saat ini, Jaya Jaya Maju mencatatkan attrition rate lebih dari 10%, yang tergolong tinggi untuk perusahaan dengan jumlah karyawan besar. Tingginya attrition dapat berdampak negatif terhadap produktivitas, peningkatan biaya rekrutmen dan pelatihan, serta terganggunya stabilitas operasional perusahaan.

### Permasalahan Bisnis

Sebagai perusahaan edutech multinasional yang telah berdiri sejak tahun 2000 dan mempekerjakan lebih dari 1000 karyawan di seluruh Indonesia, Jaya Jaya Maju dihadapkan pada tantangan serius dalam manajemen sumber daya manusia. Salah satu isu yang mencuat adalah tingginya tingkat attrition karyawan, yang melebihi angka 10%.

Fenomena ini tidak hanya mencerminkan potensi masalah dalam retensi karyawan, tetapi juga berdampak langsung pada kenaikan biaya operasional, khususnya dalam proses rekrutmen, pelatihan, dan adaptasi karyawan baru. Selain itu, attrition yang tinggi turut berkontribusi terhadap menurunnya efisiensi kerja dan penurunan kualitas layanan kepada pengguna.

Untuk itu, perusahaan perlu segera mengidentifikasi pola-pola yang memicu attrition, memahami faktor utama yang mendorong karyawan keluar, serta merancang strategi berbasis data untuk meningkatkan tingkat retensi dan keberlanjutan organisasi secara keseluruhan.

### Cakupan Proyek

1. Eksplorasi dan Pemahaman Data (Data Understanding)
- Mengumpulkan data historis yang berkaitan dengan status karyawan (bertahan atau keluar), mencakup atribut seperti demografi, kinerja, tingkat kepuasan kerja, dan faktor lainnya.

- Menganalisis struktur dan jenis data untuk memahami konteks dan skema informasi yang tersedia.

2. Persiapan dan Pra-pemrosesan Data (Data Preparation)
- Membersihkan dataset dari nilai kosong, data redundan, atau inkonsistensi yang dapat mengganggu proses analisis.

- Melakukan transformasi data seperti encoding pada kolom kategori, normalisasi skala, serta pemilihan fitur penting yang berpengaruh terhadap prediksi attrition.

- Menganalisis korelasi antar fitur untuk menemukan hubungan signifikan.

3. Pembuatan Model Machine Learning
- Membagi data menjadi data pelatihan dan data pengujian untuk memastikan evaluasi yang objektif.

- Membangun beberapa model prediktif dengan target variabel attrition, dan menyetel hyperparameter masing-masing model.

- Menggunakan pendekatan pembelajaran terawasi untuk mengidentifikasi pola-pola penting.

4. Evaluasi Model
- Mengukur performa model menggunakan data pengujian dengan metrik seperti akurasi, precision, recall, dan F1-score.

- Membandingkan hasil dari beberapa model untuk memilih yang paling optimal.

5. Deployment
- Model terbaik yang dipilih untuk di-deploy adalah Random Forest karena performanya yang stabil dan kemampuannya menangani data non-linear.

- Model ini akan diintegrasikan ke dalam sistem produksi sehingga dapat digunakan oleh pengguna untuk memprediksi kemungkinan karyawan keluar berdasarkan input data terbaru.

### Persiapan

Sumber data:
```
https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-for-hr-retaining-valuable-employees/
```
Setup environment:

```
Tools yang telah digunakan:
- Python (pandas, numpy, matplotlib, seaborn, scikit-learn)
- Metabase (untuk visualisasi dashboard)
- Jupyter Notebook (untuk eksplorasi dan modelling)
```

## Setup menggunakan Google colab 
```
!pip install -r requirements.txt
```
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.11.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup dengan pipenv (alternatif)
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install --python 3.11.9
pipenv shell
pip install -r requirements.txt
```

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
- action item 2
