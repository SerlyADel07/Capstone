import streamlit as st

st.markdown("# Tentang Cybersecurity 🔑🔒")
from PIL import Image
image = Image.open("https://drive.google.com/file/d/16mvfPgvI1EsP4NFcvSIlFJJUVKlU3pMe/view?usp=drive_link")

st.image(image, caption='''Gambar Cybersecurity (unsplash.com)''')
st.sidebar.markdown("Apa itu Cybersecurity?")
st.subheader("Apa itu Cyber Security?")
st.write ('''Cyber Security adalah Cybersecurity atau cyberspace security 
          adalah upaya yang dilakukan dalam menjaga kerahasiaan (confidentiality), 
          integritas (integrity), dan ketersediaan (availability) dari informasi 
          di cyberspace. Adapun cyberspace merujuk pada Komunikasi antar media 
          elektronik sering terjadi melalui jaringan komputer yang dapat terjadi 
          secara online serta melibatkan siapa saja, kapan saja dan dimana saja 
          hal itu terjadi. Tidak seperti batas negara yang mempunyai batasan tersendiri,
          cyberspace tidak mempunyai batasan dan hal ini menjadi pokok pembahasan 
          di dalam membentuk badan yang menanggulangi tindakan kejahatan yang 
          menggunakan jalur komunikasi tersebut''')
          
st.sidebar.markdown("Mengapa Cybersecurity Penting?")
st.subheader("Mengapa Cybersecurity Penting?")
st.write ('''Cybersecurity berfungsi untuk melindungi perangkat dan layanan online yang Anda
gunakan dari pencurian dan kerusakan data oleh pihak ketiga. Cybersecurity juga berguna untuk
mencegah akses tidak sah ke informasi yang ada di internet. Praktik ini memastikan data
tersebut hanya bisa diakses oleh orang-orang tertentu saja.
Di jaman yang serba digital ini, keberadaan cybersecurity memang sangat penting.
Sekarang internet sudah menjadi bagian mendasar dari kehidupan modern. Mulai dari
bersekolah, perbankan, belanja online, bekerja, hingga media sosial. Oleh karena itu, praktik
cybersecurity sangat penting untuk memastikan Anda tetap aman di internet.''')

st.sidebar.markdown("Bagaimana konsep dari cybersecurity?")
st.subheader("Bagaimana konsep dari cybersecurity?")
st.write ('''Secara umum cybersecurity mengacu pada praktik untuk dapat memastikan kerahasiaan
(confidentiality), integritas (integrity), dan ketersediaan (availability) informasi atau dikenal
sebagai CIA Triad.\n
● Kerahasiaan (Confidentiality), merupakan usaha untuk merahasiakan atau menyimpan
data yang dilakukan dengan cara mengontrol akses data untuk mencegah berbagai
pencurian maupun kebocoran data.\n
● Integritas (Integrity), merupakan upaya memberikan data secara konsisten, akurat, dan
terpercaya.\n
● Ketersediaan (Availability), mengacu pada ketersediaan data digital. Komponen
availability diantaranya meliputi ketersediaan sistem, aplikasi hingga data yang dapat
diakses.''')

st.sidebar.markdown("Jenis - Jenis Cybersecurity Threats")
st.subheader("Jenis - Jenis Cybersecurity Threats")
st.write ('''1 Malware 👾 \n 
Serangan malware adalah Cybersecurity Threats yang paling umum. Malware didefinisikan
sebagai perangkat lunak berbahaya, termasuk spyware, ransomware, virus, dan worm, yang
diinstal ke dalam sistem ketika pengguna mengklik tautan atau email berbahaya. Begitu
berada di dalam sistem, malware dapat memblokir akses ke komponen penting jaringan,
merusak sistem, mengumpulkan informasi rahasia, dan masih banyak lagi.\n 
2) Phising 🔏 \n 
Phishing merupakan salah satu serangan cyber yang sudah lama ada. Tekniknya adalah
dengan menggunakan komunikasi palsu seperti email dan telepon untuk mengelabui
penerimanya agar membuka dan menjalankan instruksi yang mereka berikan. Salah
satunya adalah dengan memberikan nomor kartu kredit. Jika data sudah mereka dapatkan,
data perbankan pengguna bisa digunakan secara tidak sah dan ini tentu sangat merugikan.\n 
3) Spear Phishing 🗝️ \n 
Spear phishing adalah bentuk serangan phishing yang lebih canggih di mana penjahat dunia
maya hanya menargetkan pengguna istimewa seperti administrator sistem.\n ''')

st.markdown("# Video Cybersecurity :lock:📽")
st.sidebar.markdown("Video Cybersecurity?")
st.write("Mari memahami cybersecurity lebih lanjut melalui video berikut ini. Siapkan catatanmu juga :satisfied: 📖🖊")
st.video("https://youtu.be/yMrkBURystg")
st.caption("SerlyDelvi Youtube Channel")

st.subheader("Malware 👾")
st.sidebar.markdown("Malware")
st.write ('''Salah satu cara untuk deteksi malicious website yaitu dengan “exploit” application 
            layer. Application layer adalah layer tertinggi dalam Open System Interconnection (OSI) layer. 
            Layer ini berfokus pada process-to-process communication melewati IP network dan 
            menyediakan layanan interface komunikasi dan user services. Application layer menyediakan 
            banyak layanan diantaranya: file transfer, network data sharing, web surfing, web chat, dan 
            email clients. Untuk membedakan malicious website dan yang bukan maka digunakan 
            metode klasifikasi. Klasifikasi merupakan proses untuk mengambil input dan akan dimasukkan 
            ke dalam kelas yang sudah ada. Metode ini dapat digunakan untuk memprediksi data baru. 
            Penelitian sebelumnya oleh Altaher (2017) yaitu mengklasifikasi phishing website
            menggunakan hybrid K-NN dan SVM dengan menggabungkan kedua algoritma tersebut 
            sehingga mendapatkan hasil akurasi sebesar 90.04%. Kemudian pada penelitian yang lain 
            tentang klasifikasi malicious website berdasarkan url features, diketahui bahwa penelitian 
            tersebut menggunakan algoritma Naïve Bayes dengan precision sebesar 87%. Pada 
            penelitian ini penulis mencoba untuk menggunakan algoritma K-Nearest Neighbour untuk 
            memprediksi malicious website.''')


