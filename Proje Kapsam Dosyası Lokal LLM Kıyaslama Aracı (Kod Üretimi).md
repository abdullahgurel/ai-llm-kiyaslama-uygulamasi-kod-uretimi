

---

## Proje Kapsam Dosyası: Lokal LLM Kıyaslama Aracı (Kod Üretimi)

**1. Proje Adı:**  
Lokal LLM Kıyaslama Aracı: Kod Üretimi

**2. Proje Amacı:**  
Bu proje, kullanıcıların yerel olarak Ollama üzerinde çalışan LLaMA 3 ve Mistral büyük dil modellerini (LLM) kod üretme ve programlama sorularına yanıt verme yetenekleri açısından karşılaştırmalarını sağlayan bir Streamlit web uygulaması sunmayı amaçlamaktadır.

**3. Ana Özellikler:**

- **Model Seçimi:** Kullanıcıların LLaMA 3 ve Mistral modelleri arasında seçim yapabilmesi.

- **Chat Arayüzü:** Kullanıcıların sorularını girebileceği ve modellerden yanıt alabileceği interaktif bir sohbet arayüzü.

- **Ollama Entegrasyonu:** Yerel olarak çalışan Ollama servisi aracılığıyla LLM'lere erişim.
  
  - helper.py dosyası, Ollama ile iletişimi ve yanıt üretimini yönetir.
  
  - initialize_clients fonksiyonu, kullanılacak Ollama model adlarını tanımlar (llama3, mistral).
  
  - ollama_generate_response fonksiyonu, seçilen modele göre Ollama API'sine istek gönderir.

- **Sistem Mesajı:** Modellere "Sen uzman bir Python asistanısın." şeklinde bir sistem mesajı gönderilerek yanıtların bağlamı belirlenir.

- **Örnek Sorular:** Kullanıcıların hızlıca test yapabilmesi için önceden tanımlanmış programlama ve kod üretimi odaklı sorular listesi.

- **Manuel Soru Girişi:** Kullanıcıların kendi özel sorularını yazabilmesi.

- **Oturum Yönetimi (Session State):**
  
  - Sohbet geçmişi (st.session_state.messages) oturumlar arası korunur.
  
  - Model değiştirildiğinde sohbet geçmişi sıfırlanır (adjust_model_relations).

- **Hata Yönetimi:** Ollama'dan yanıt alınırken oluşabilecek temel hatalar yakalanır ve kullanıcıya bildirilir.

**4. Kullanılan Teknolojiler:**

- **Programlama Dili:** Python

- **Web Framework:** Streamlit

- **LLM Servisi:** Ollama (yerel)

- **Ollama Python Kütüphanesi:** ollama

- **Modüller:** helper.py (yardımcı fonksiyonlar için)

**5. Hedef Kitle:**

- Yerel LLM'leri (özellikle LLaMA 3 ve Mistral) kod üretimi yetenekleri açısından test etmek ve karşılaştırmak isteyen geliştiriciler.

- AI ve LLM meraklıları.

- Ollama ve Streamlit ile basit uygulamalar geliştirmek isteyenler.

**6. Ön Koşullar ve Kısıtlamalar:**

- **Ollama Kurulumu:** Kullanıcının sisteminde Ollama'nın kurulu ve çalışır durumda olması gerekmektedir.

- **Model İndirme:** llama3 ve mistral modellerinin Ollama aracılığıyla indirilmiş olması gerekmektedir (ollama pull llama3, ollama pull mistral).

- **Sistem Kaynakları:** Ollama ve seçilen modellerin çalışması için yeterli RAM ve CPU/GPU kaynağı gereklidir.

- Uygulama, Ollama servisinin varsayılan yerel adreste (http://localhost:11434) çalıştığını varsayar.

---

## Nasıl Çalıştırılır?

Bu Streamlit uygulamasını yerel makinenizde çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

**1. Dosyaların Hazırlanması:**

- Bir proje klasörü oluşturun (örneğin, ollama_streamlit_app).

- Aşağıdaki üç dosyayı bu klasörün içine kaydedin:
  
  - code_generation.py
  
  - helper.py
  
  - requirements.txt

**2. Sanal Ortam Oluşturma ve Aktifleştirme (Önerilir):**  
Bir sanal ortam (virtual environment) kullanmak, projenizin bağımlılıklarını sistem genelindeki Python kurulumunuzdan izole etmenizi sağlar.

- Proje klasörünüzün içindeyken terminali veya komut istemcisini açın.

- Sanal ortamı oluşturun:
  
        `python -m venv venv`

- Sanal ortamı aktifleştirin:
  
  - **Windows için:**
    
          `.\venv\Scripts\activate`

**3. Gerekli Kütüphanelerin Kurulumu:**  
Sanal ortam aktifken, requirements.txt dosyasında listelenen kütüphaneleri kurun:

      `pip install -r requirements.txt`



Bu komut, ollama ve streamlit kütüphanelerini sanal ortamınıza yükleyecektir.

**4. Ollama Kurulumu ve Model İndirme:**  
Bu uygulamanın çalışması için sisteminizde Ollama'nın kurulu ve çalışıyor olması gerekmektedir.

- **Ollama Kurulumu:**
  
  - Eğer Ollama kurulu değilse, resmi web sitesi olan [ollama.com](https://www.google.com/url?sa=E&q=https%3A%2F%2Follama.com%2F) adresinden işletim sisteminize uygun sürümü indirip kurun.
  
  - Kurulumdan sonra Ollama servisinin çalıştığından emin olun. Genellikle otomatik olarak başlar.

- **Modellerin İndirilmesi:**  
  Ollama servisi çalışırken, terminalde veya komut istemcisinde aşağıdaki komutları çalıştırarak LLaMA 3 ve Mistral modellerini indirin:
  
        `ollama pull llama3`



        `ollama pull mistral`



  Bu modellerin indirilmesi internet hızınıza ve model boyutlarına bağlı olarak zaman alabilir. İndirilen modelleri listelemek için ollama list komutunu kullanabilirsiniz.

**5. Uygulamanın Çalıştırılması:**  
Tüm önkoşullar tamamlandıktan ve sanal ortamınız aktifken, Streamlit uygulamasını başlatmak için proje klasörünüzün içindeyken terminalde şu komutu çalıştırın:

      `streamlit run code_generation.py`



Bu komut, Streamlit uygulamasını başlatacak ve varsayılan web tarayıcınızda genellikle http://localhost:8501 adresinde açacaktır.

**6. Kullanım:**

- Tarayıcıda açılan arayüzde, sol kenar çubuğundan (sidebar) LLaMA 3 veya Mistral modelini seçin.

- Yine kenar çubuğundan örnek bir soru seçebilir veya "Manuel Soru Yaz" seçeneğini işaretleyip ana chat giriş alanına kendi sorunuzu yazabilirsiniz.

- Modelden gelen yanıtlar sohbet ekranında görüntülenecektir.

**7. Sanal Ortamdan Çıkış (İşiniz Bittiğinde):**  
Uygulamayla işiniz bittiğinde ve terminali kapatmadan önce sanal ortamı devre dışı bırakmak için:

      `deactivate`



Bu komut sizi sisteminizin genel Python ortamına döndürecektir.


