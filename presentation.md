### 📌 **SLIDE 1: TIÊU ĐỀ BÀI THUYẾT TRÌNH**

#### 🖥️ **Nội dung hiển thị trên Slide:**
* **Tiêu đề chính:** BẢO MẬT ĐÁM MÂY (CLOUD SECURITY)
* **Chủ đề chính:** Dữ liệu · Mã hóa · Hạ tầng · PaaS · SaaS · Máy chủ ảo · Kiểm soát bảo mật
* **Người thực hiện:** Nông Văn Tình
* **Thông điệp mở đầu:** *"Khi đưa hệ thống lên Cloud, mô hình bảo mật cũng hoàn toàn thay đổi."*

---

#### 🎙️ **Kịch bản lời nói dẫn dắt (Speaker Notes):**

> "Xin chào thầy và các anh chị học viên. Tiếp theo, mình xin được trình bày về đề tài: **Bảo mật điện toán đám mây (Cloud Security)**.
>
> Ngày nay, việc dịch chuyển dữ liệu và ứng dụng lên đám mây đang trở thành xu hướng tất yếu của các doanh nghiệp. Tuy nhiên, có một thực tế là: **khi đưa hệ thống lên Cloud, mô hình bảo mật truyền thống đã hoàn toàn thay đổi**. Ranh giới bảo vệ không còn gói gọn trong các bức tường lửa nội bộ, mà phần lớn dữ liệu và hạ tầng đã chuyển sang nằm dưới sự kiểm soát của bên thứ ba.
>
> Vậy làm thế nào để chúng ta vừa tận dụng được tính linh hoạt của đám mây, vừa bảo vệ an toàn cho tài sản dữ liệu của mình? Trong bài trình bày hôm nay, mình sẽ cùng mọi người lần lượt khám phá các khái niệm bảo mật cốt lõi, các kỹ thuật mã hóa hiện đại, cho đến chiến lược bảo vệ hạ tầng, ứng dụng và máy chủ ảo trên Cloud."


# 📌 SLIDE 2: MỤC LỤC TRÌNH BÀY

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### NỘI DUNG CHÍNH

**1. NỀN TẢNG BẢO MẬT ĐÁM MÂY**

* Cloud Security & các vấn đề đặc thù
* Shared Responsibility Model
* Bộ ba bảo mật CIA

**2. BẢO VỆ DỮ LIỆU TRÊN CLOUD**

* Vòng đời & các trạng thái của dữ liệu
* Data-in-Transit & Metadata
* Privacy, Integrity, Location & Availability

**3. MẬT MÃ NÂNG CAO CHO CLOUD**

* Attribute-Based Encryption (ABE)
* Fully Homomorphic Encryption (FHE)
* Searchable Encryption (SE)

**4. BẢO VỆ HẠ TẦNG & VÙNG TIN CẬY**

* Public Cloud vs Private Cloud
* Network Security & Misconfiguration
* Trust Zones & IAM

**5. BẢO MẬT ỨNG DỤNG & MÁY CHỦ**

* IaaS, PaaS & SaaS
* Access Control, SSO & OS Hardening
* Virtual Server Security

**6. KIỂM SOÁT & PHÒNG THỦ ĐA LỚP**

* Deterrent Controls
* Preventive Controls
* Detective Controls
* Corrective Controls

Speaker Notes — Slide 2: Mục lục trình bày

> “Để hiểu một cách tổng thể về bảo mật trong môi trường Cloud, bài trình bày của mình sẽ đi theo **6 phần**, bắt đầu từ nền tảng và sau đó đi dần xuống các lớp bảo vệ cụ thể.
>
> **Phần thứ nhất là Nền tảng bảo mật đám mây.**
> Mình sẽ bắt đầu bằng việc làm rõ Cloud Security là gì, sau đó xem xét **mô hình trách nhiệm chia sẻ** giữa nhà cung cấp dịch vụ Cloud và khách hàng. Cuối phần này, chúng ta sẽ sử dụng **bộ ba CIA** để xác định những mục tiêu cốt lõi của bảo mật.
>
> **Phần thứ hai là Bảo vệ dữ liệu trên Cloud.**
> Ở đây, chúng ta sẽ nhìn vào dữ liệu trong các trạng thái khác nhau, từ lúc truyền qua mạng cho đến khi được lưu trữ và xử lý. Đồng thời, mình sẽ đề cập đến các vấn đề như **metadata, quyền riêng tư, tính toàn vẹn, vị trí và tính sẵn sàng của dữ liệu**.
>
> **Phần thứ ba là Mật mã nâng cao cho Cloud.**
> Đây là phần trọng tâm của bài. Chúng ta sẽ xuất phát từ một câu hỏi:
>
> *“Nếu muốn Cloud lưu trữ và xử lý dữ liệu, nhưng không muốn Cloud nhìn thấy dữ liệu gốc, thì chúng ta có thể làm gì?”*
>
> Từ câu hỏi đó, mình sẽ lần lượt giới thiệu **ABE, FHE và Searchable Encryption**, với mỗi kỹ thuật giải quyết một nhu cầu bảo mật khác nhau.
>
> **Phần thứ tư là Bảo vệ hạ tầng và vùng tin cậy.**
> Sau khi nói về dữ liệu, chúng ta sẽ chuyển sang lớp hạ tầng: sự khác biệt giữa Public Cloud và Private Cloud, các rủi ro về mạng và cấu hình, sau đó là **Trust Zones và IAM** để kiểm soát phạm vi truy cập.
>
> **Phần thứ năm là Bảo mật ứng dụng và máy chủ.**
> Phần này sẽ liên hệ với ba mô hình dịch vụ **IaaS, PaaS và SaaS**, đồng thời xem xét các cơ chế như kiểm soát truy cập, SSO, gia cố hệ điều hành và bảo vệ máy chủ ảo.
>
> Cuối cùng, **phần thứ sáu là Kiểm soát và phòng thủ đa lớp**.
> Mình sẽ tổng hợp lại toàn bộ những cơ chế vừa trình bày thành bốn nhóm: **răn đe, phòng ngừa, phát hiện và khắc phục**, qua đó cho thấy Cloud Security không phụ thuộc vào một công nghệ duy nhất mà là sự kết hợp của nhiều lớp bảo vệ.
>
> Và bây giờ, chúng ta sẽ bắt đầu với câu hỏi nền tảng thứ nhất: **Cloud Security là gì, và khi đưa hệ thống lên Cloud thì trách nhiệm bảo mật được phân chia như thế nào?**”

# 📌 SLIDE 3: NỀN TẢNG BẢO MẬT ĐÁM MÂY

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Cloud Security là gì?

**Cloud Security** là tập hợp các **công nghệ, chính sách, quy trình và biện pháp kiểm soát** nhằm bảo vệ:

* 🔐 **Dữ liệu**
* 🖥️ **Ứng dụng**
* 🌐 **Hạ tầng**
* 👤 **Danh tính & quyền truy cập**

**Đặc thù của Cloud:**

> Tài nguyên được vận hành trên hạ tầng của CSP → trách nhiệm bảo mật được **chia sẻ** giữa nhà cung cấp và khách hàng.

---

### 2. Shared Responsibility Model

| CSP – Security **OF** the Cloud       | Khách hàng – Security **IN** the Cloud            |
| ------------------------------------- | ------------------------------------------------- |
| 🏢 Trung tâm dữ liệu & hạ tầng vật lý | ⚙️ Cấu hình tài nguyên                            |
| 🖥️ Phần cứng & mạng nền tảng         | 👤 Danh tính & quyền truy cập                     |
| 🔧 Hạ tầng/dịch vụ do CSP cung cấp    | 🗄️ Dữ liệu & ứng dụng                            |
| 🔒 Bảo mật nền tảng Cloud             | 🛡️ Các biện pháp bảo vệ do khách hàng triển khai |

> **Ranh giới trách nhiệm thay đổi theo IaaS → PaaS → SaaS.**

**❓ Câu hỏi:** Nếu dữ liệu trên Cloud bị rò rỉ, ai chịu trách nhiệm?

**→ Không có một câu trả lời duy nhất: cần xác định nguyên nhân và ranh giới trách nhiệm của dịch vụ đang sử dụng.**

---

### 3. Mục tiêu bảo mật: CIA Triad

| 🔒 Confidentiality                               | 🛡️ Integrity                        | ⚡ Availability                                         |
| ------------------------------------------------ | ------------------------------------ | ------------------------------------------------------ |
| Chỉ người được phép mới có thể truy cập dữ liệu. | Dữ liệu không bị thay đổi trái phép. | Tài nguyên sẵn sàng khi người dùng hợp lệ cần sử dụng. |

### 🌐 Thách thức trong Cloud

**Bên thứ ba + truy cập qua mạng + tài nguyên dùng chung + cấu hình động**

→ Làm cho việc duy trì **Confidentiality – Integrity – Availability** trở nên phức tạp hơn.

---

### 🎯 THÔNG ĐIỆP CHÍNH

> **Cloud Security = Bảo vệ tài nguyên Cloud + xác định đúng trách nhiệm + duy trì CIA.**

Speaker Notes — Slide 3

> “Để bắt đầu, chúng ta cần trả lời một câu hỏi rất cơ bản: **Cloud Security thực chất là gì?**
>
> Hiểu đơn giản, Cloud Security là tập hợp các công nghệ, chính sách, quy trình và biện pháp kiểm soát nhằm bảo vệ **dữ liệu, ứng dụng, hạ tầng cũng như danh tính và quyền truy cập** trong môi trường Cloud.
>
> Tuy nhiên, có một điểm khiến Cloud Security khác với mô hình bảo mật truyền thống: **chúng ta không còn tự kiểm soát toàn bộ hạ tầng.**
>
> Một phần hạ tầng được vận hành bởi Cloud Service Provider, hay CSP. Và từ đây xuất hiện một khái niệm rất quan trọng: **Shared Responsibility Model – Mô hình trách nhiệm chia sẻ.**
>
> Có thể hiểu đơn giản thành hai phía.
>
> CSP chịu trách nhiệm về **Security of the Cloud** — tức là bảo vệ những thành phần thuộc về nền tảng Cloud mà họ cung cấp, chẳng hạn như trung tâm dữ liệu, phần cứng, mạng và hạ tầng nền tảng.
>
> Ngược lại, khách hàng chịu trách nhiệm về **Security in the Cloud** — chẳng hạn như cấu hình tài nguyên, quản lý danh tính, quyền truy cập, dữ liệu và ứng dụng của mình.
>
> Nhưng ranh giới này **không cố định**. Khi chuyển từ IaaS sang PaaS rồi SaaS, phần trách nhiệm của CSP tăng lên và phần khách hàng phải tự quản lý giảm xuống.
>
> Vì vậy, nếu dữ liệu bị rò rỉ, chúng ta không thể ngay lập tức kết luận rằng lỗi thuộc về CSP hay khách hàng. Trước tiên phải xác định **nguyên nhân sự cố và phần trách nhiệm tương ứng**.
>
> Vậy cuối cùng, dù ai chịu trách nhiệm, chúng ta đang cố gắng bảo vệ điều gì?
>
> Đó chính là **CIA Triad**.
>
> **Confidentiality** — chỉ người được phép mới có thể truy cập dữ liệu.
>
> **Integrity** — dữ liệu không bị thay đổi trái phép.
>
> Và **Availability** — hệ thống phải sẵn sàng khi người dùng hợp lệ cần sử dụng.
>
> Trong Cloud, ba mục tiêu này trở nên phức tạp hơn bởi chúng ta có sự tham gia của bên thứ ba, kết nối qua mạng, tài nguyên dùng chung và rất nhiều cấu hình có thể thay đổi.
>
> Vậy khi dữ liệu thực sự đi vào môi trường Cloud, nó sẽ phải đối mặt với những vấn đề cụ thể nào?
>
> Đó sẽ là nội dung của phần tiếp theo: **Bảo vệ dữ liệu trên Cloud**.”


# 📌 SLIDE 4: BẢO VỆ DỮ LIỆU TRÊN CLOUD

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Dữ liệu trên Cloud đi qua đâu?

**User → Network → Cloud Storage → Cloud Processing → User**

Trong quá trình này, dữ liệu tồn tại ở 3 trạng thái:

| 🌐 Data-in-Transit           | 💾 Data-at-Rest                          | ⚙️ Data-in-Use                            |
| ---------------------------- | ---------------------------------------- | ----------------------------------------- |
| Đang truyền qua mạng         | Đang được lưu trữ                        | Đang được xử lý                           |
| Internet / Private Network   | Database / Cloud Storage                 | RAM / CPU                                 |
| Nguy cơ: nghe lén, can thiệp | Nguy cơ: truy cập trái phép, mất dữ liệu | Nguy cơ: lộ dữ liệu trong quá trình xử lý |

> **Mỗi trạng thái → một nhóm cơ chế bảo vệ khác nhau.**

---

### 2. Data-in-Transit: Bảo vệ dữ liệu trên đường truyền

**Các nguy cơ chính:**

* 👂 **Eavesdropping** — nghe lén
* ✏️ **Tampering** — can thiệp/chỉnh sửa
* 🎭 **Impersonation** — giả mạo

**Nguyên tắc bảo vệ:**

> 🔐 **Sử dụng các giao thức và thuật toán mã hóa đã được kiểm chứng.**

**Defense in Depth:**

> **Private Network ≠ Automatically Trusted**

Dữ liệu cần được bảo vệ dù đi qua **Internet hay mạng riêng**.

---

### 3. Metadata: Không chỉ nội dung dữ liệu có giá trị

**Metadata = thông tin “xung quanh” dữ liệu**

Ví dụ:

* Ai truy cập?
* Khi nào truy cập?
* Tần suất truy cập?
* Dữ liệu nằm ở đâu?
* Có bao nhiêu dữ liệu?

### Khi sử dụng Cloud, cần biết:

**CSP thu thập metadata nào?**
↓
**Metadata được bảo vệ như thế nào?**
↓
**Khách hàng có quyền kiểm soát/truy cập đến đâu?**

---

### 4. Những vấn đề cần kiểm soát

| 🛡️ Integrity                      | 🔒 Privacy                    | 📍 Data Location        | ⚡ Availability                 |
| ---------------------------------- | ----------------------------- | ----------------------- | ------------------------------ |
| Dữ liệu có chính xác và nhất quán? | Ai được phép sử dụng/chia sẻ? | Dữ liệu được lưu ở đâu? | Dữ liệu có luôn truy cập được? |

---

### ❓ BÀI TOÁN TIẾP THEO

> **Nếu Cloud cần lưu trữ và tính toán trên dữ liệu của chúng ta, nhưng chúng ta không muốn Cloud nhìn thấy dữ liệu gốc — liệu có thể làm được không?**

### → Advanced Cryptography for Cloud

**ABE · FHE · Searchable Encryption**


Speaker Notes — Slide 4

> “Sau khi đã xác định Cloud Security là gì và trách nhiệm được phân chia như thế nào, chúng ta hãy thu hẹp phạm vi lại và nhìn vào đối tượng quan trọng nhất: **dữ liệu**.
>
> Dữ liệu trên Cloud không đứng yên ở một chỗ. Nó có thể bắt đầu từ người dùng, đi qua mạng, được lưu trữ trên Cloud, sau đó được đưa vào hệ thống để xử lý và cuối cùng trả kết quả về cho người dùng.
>
> Vì vậy, chúng ta có thể nhìn dữ liệu qua ba trạng thái chính: **Data-in-Transit, Data-at-Rest và Data-in-Use**.
>
> Khi dữ liệu đang truyền, chúng ta quan tâm đến việc nó có bị nghe lén, can thiệp hoặc giả mạo hay không. Khi dữ liệu được lưu trữ, vấn đề chuyển sang quyền truy cập, tính toàn vẹn và khả năng mất dữ liệu. Còn khi dữ liệu đang được xử lý, một vấn đề khó hơn xuất hiện: **Cloud cần sử dụng dữ liệu, nhưng để xử lý thì thông thường nó phải nhìn thấy dữ liệu.**
>
> Trước hết, với Data-in-Transit, một nguyên tắc quan trọng là **không nên mặc định rằng mạng riêng thì an toàn**. Dữ liệu đi qua Internet hay mạng nội bộ đều cần được bảo vệ bằng các giao thức và thuật toán mã hóa phù hợp, đã được kiểm chứng.
>
> Ngoài nội dung dữ liệu, chúng ta còn có một lớp thông tin khác thường bị bỏ qua, đó là **metadata**.
>
> Metadata có thể cho chúng ta biết ai truy cập dữ liệu, thời điểm truy cập, tần suất truy cập hoặc dữ liệu đang nằm ở đâu. Vì vậy, ngay cả khi nội dung đã được bảo vệ, metadata vẫn có thể tiết lộ những thông tin có giá trị.
>
> Khi đưa dữ liệu lên Cloud, chúng ta cần đặt ra bốn câu hỏi: **Dữ liệu có còn toàn vẹn không? Quyền riêng tư được bảo vệ thế nào? Dữ liệu đang nằm ở đâu? Và khi cần, chúng ta có thể truy cập nó hay không?**
>
> Tuy nhiên, ở đây xuất hiện một bài toán thú vị hơn.
>
> **Nếu tôi muốn tận dụng khả năng lưu trữ và tính toán rất mạnh của Cloud, nhưng lại không muốn Cloud nhìn thấy dữ liệu gốc của mình, thì tôi phải làm thế nào?**
>
> Đây chính là điểm mà các cơ chế mã hóa truyền thống bắt đầu gặp giới hạn, và cũng là lý do chúng ta cần đến **các kỹ thuật mật mã nâng cao cho Cloud**.
>
> Đó sẽ là nội dung của phần tiếp theo.”

# 📌 SLIDE 5: MẬT MÃ NÂNG CAO CHO CLOUD

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Từ bài toán bảo vệ dữ liệu đến bài toán “Cloud không được thấy dữ liệu”

Mã hóa truyền thống:

**Dữ liệu gốc → 🔐 Mã hóa → Cloud → 🔓 Giải mã → Xử lý**

→ Khi cần xử lý dữ liệu, bản rõ thường phải xuất hiện.

### ❓ Bài toán đặt ra

> **Làm thế nào để vẫn sử dụng được khả năng lưu trữ, tính toán và tìm kiếm của Cloud mà hạn chế việc Cloud nhìn thấy dữ liệu gốc?**

→ **Advanced Cryptography** mở rộng khả năng của mã hóa truyền thống.

---

### 2. Ba kỹ thuật — Ba bài toán khác nhau

| Kỹ thuật   | Bài toán cần giải quyết                           | Ý tưởng chính                                     |
| ---------- | ------------------------------------------------- | ------------------------------------------------- |
| 🔑 **ABE** | **Ai được phép truy cập?**                        | Kiểm soát quyền dựa trên thuộc tính               |
| 🧮 **FHE** | **Cloud có thể tính toán mà không thấy dữ liệu?** | Tính toán trực tiếp trên ciphertext               |
| 🔎 **SE**  | **Có thể tìm kiếm mà không giải mã toàn bộ?**     | Truy vấn dữ liệu mã hóa thông qua cơ chế tìm kiếm |

---

### 3. ABE — Attribute-Based Encryption

**Mục tiêu:** Kiểm soát truy cập dựa trên **thuộc tính** thay vì chỉ dựa trên danh tính cá nhân.

Ví dụ:

> **Doctor + Cardiology + Hospital A**
> → Có quyền truy cập hồ sơ phù hợp.

**Hai mô hình chính:**

* **CP-ABE:** Chính sách truy cập nằm trên **ciphertext**.
* **KP-ABE:** Chính sách truy cập nằm trong **user's secret key**.

> **Điều kiện giải mã:** Chính sách phải được **thỏa mãn**, không nhất thiết phải “khớp hoàn toàn”.

---

### 4. FHE — Fully Homomorphic Encryption

**Mục tiêu:** Cho phép thực hiện phép tính trên **dữ liệu đã mã hóa** mà không cần đưa dữ liệu về dạng rõ.

**Luồng cơ bản:**

**Plaintext → Encrypt → ☁️ Computation on Ciphertext → Encrypted Result → Decrypt**

### 🔑 Điểm đặc biệt

> **Cloud xử lý ciphertext → người dùng giữ quyền giải mã.**

**Ứng dụng:** Phân tích dữ liệu nhạy cảm, đặc biệt trong các lĩnh vực như y tế và tài chính.

---

### 5. SE — Searchable Encryption

**Mục tiêu:** Cho phép thực hiện **tìm kiếm trên dữ liệu mã hóa** mà không cần giải mã toàn bộ kho dữ liệu.

**Ví dụ:**

> 🔐 Kho email được mã hóa
> ↓
> 🔎 Truy vấn **“Urgent”**
> ↓
> 📩 Xác định các email phù hợp

---

## 🎯 TÓM TẮT

### **ABE → Access**

**Ai được phép truy cập?**

### **FHE → Compute**

**Cloud có thể tính toán mà không thấy dữ liệu?**

### **SE → Search**

**Cloud có thể tìm kiếm mà không cần đọc toàn bộ dữ liệu?**

> **Ba kỹ thuật này giải quyết ba nhu cầu khác nhau trong bài toán bảo vệ dữ liệu trên Cloud.**

Speaker Notes — Slide 5
> “Từ Slide 4, chúng ta đã thấy một vấn đề quan trọng: nếu dữ liệu được mã hóa, thì việc bảo vệ dữ liệu trở nên tốt hơn, nhưng chúng ta cũng gặp một bài toán mới — **Cloud phải làm gì với dữ liệu mà nó không được nhìn thấy?**
>
> Với mã hóa truyền thống, quy trình thường là: dữ liệu được mã hóa để lưu trữ hoặc truyền đi, nhưng khi cần xử lý thì dữ liệu phải được đưa về dạng mà hệ thống có thể sử dụng.
>
> Vì vậy, câu hỏi đặt ra là:
>
> **Liệu chúng ta có thể sử dụng khả năng của Cloud mà vẫn hạn chế việc Cloud nhìn thấy dữ liệu gốc hay không?**
>
> Đây chính là động lực cho các kỹ thuật **mật mã nâng cao**.
>
> Trong bài này, chúng ta tập trung vào ba kỹ thuật, và điều quan trọng là mỗi kỹ thuật giải quyết một bài toán khác nhau.
>
> **Thứ nhất là ABE — Attribute-Based Encryption.**
>
> ABE tập trung vào câu hỏi: **Ai được phép truy cập dữ liệu?**
>
> Thay vì chỉ nói rằng một người dùng cụ thể được phép đọc dữ liệu, chúng ta có thể xây dựng chính sách dựa trên các thuộc tính. Ví dụ, người dùng cần đồng thời có các thuộc tính như *Doctor, Cardiology và Hospital A* mới có thể truy cập một loại hồ sơ nhất định.
>
> ABE có hai mô hình nổi bật là **CP-ABE** và **KP-ABE**. Chúng khác nhau chủ yếu ở vị trí đặt chính sách truy cập: CP-ABE đặt chính sách trên ciphertext, còn KP-ABE đặt chính sách trong khóa của người dùng.
>
> **Thứ hai là FHE — Fully Homomorphic Encryption.**
>
> FHE giải quyết một câu hỏi khác:
>
> **Cloud có thể tính toán trên dữ liệu mà không cần biết dữ liệu gốc hay không?**
>
> Với FHE, dữ liệu được mã hóa trước khi gửi lên Cloud. Cloud có thể thực hiện các phép toán trực tiếp trên ciphertext và trả về kết quả cũng ở dạng mã hóa. Người sở hữu khóa mới có thể giải mã kết quả.
>
> Đây là lý do FHE đặc biệt đáng chú ý trong những bài toán như phân tích dữ liệu y tế, nơi dữ liệu vừa cần được xử lý vừa có yêu cầu cao về quyền riêng tư.
>
> **Cuối cùng là Searchable Encryption, hay SE.**
>
> SE giải quyết bài toán tìm kiếm. Nếu chúng ta có hàng nghìn tài liệu đã được mã hóa, làm thế nào để tìm được tài liệu chứa một từ khóa mà không phải giải mã toàn bộ kho dữ liệu?
>
> Searchable Encryption cung cấp các cơ chế để thực hiện truy vấn trên dữ liệu mã hóa, tùy thuộc vào lược đồ mà vẫn kiểm soát lượng thông tin bị tiết lộ.
>
> Vì vậy, chúng ta có thể ghi nhớ ba kỹ thuật này bằng ba từ:
>
> **ABE — Access.** Ai được truy cập?
>
> **FHE — Compute.** Có thể tính toán trên dữ liệu mã hóa không?
>
> **SE — Search.** Có thể tìm kiếm dữ liệu mã hóa không?
>
> Đây chính là ba hướng mà chúng ta sẽ lần lượt đi sâu trong các slide tiếp theo.”


# 📌 SLIDE 6: ABE — MÃ HÓA DỰA TRÊN THUỘC TÍNH

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. ABE giải quyết bài toán gì?

**Câu hỏi:**

> **Ai được phép giải mã dữ liệu trên Cloud?**

Thay vì cấp quyền chỉ dựa trên **danh tính cá nhân**, ABE sử dụng **thuộc tính** để xây dựng chính sách truy cập.

**Ví dụ:**

`Doctor` + `Cardiology` + `Hospital A`

→ Có thể thỏa mãn chính sách:

`Doctor AND Cardiology AND Hospital A`

### 🔑 Nguyên tắc

> **Giải mã thành công khi tập thuộc tính của người dùng thỏa mãn Access Policy.**

---

### 2. Hai mô hình chính: CP-ABE vs. KP-ABE

|                           | **CP-ABE**                         | **KP-ABE**                                 |
| ------------------------- | ---------------------------------- | ------------------------------------------ |
| **Policy nằm ở đâu?**     | 🔐 Ciphertext                      | 🔑 User Secret Key                         |
| **Attributes nằm ở đâu?** | 🔑 User Secret Key                 | 🔐 Ciphertext                              |
| **Ai quyết định Policy?** | Bên mã hóa dữ liệu                 | Cơ quan / hệ thống cấp khóa                |
| **Câu hỏi trực quan**     | “**Dữ liệu này cho ai?**”          | “**Người này được xem loại dữ liệu nào?**” |
| **Ví dụ**                 | Người gửi đặt quyền truy cập hồ sơ | Hệ thống cấp quyền theo nhóm dữ liệu       |

### 💡 Điểm khác biệt cốt lõi

**CP-ABE:**

> **Policy → Ciphertext**

**KP-ABE:**

> **Policy → Key**

---

### 3. Cơ chế ABE — Từ thuộc tính đến giải mã

**① Setup**
Tạo tham số hệ thống và khóa công khai.

↓

**② Key Generation**
Cấp cho người dùng một **Secret Key** gắn với thuộc tính hoặc Policy.

↓

**③ Encryption**
Mã hóa dữ liệu và gắn **Access Policy / Attributes** tùy mô hình.

↓

**④ Decryption**
Hệ thống kiểm tra:

**User Attributes ⟹ Access Policy?**

* ✅ **Thỏa mãn** → Giải mã thành công
* ❌ **Không thỏa mãn** → Giải mã thất bại

---

### 🎯 THÔNG ĐIỆP CẦN NHỚ

> **ABE biến quyền truy cập thành một bài toán về thuộc tính và chính sách.**

**CP-ABE:** Người mã hóa quyết định **ai có thể đọc dữ liệu**.
**KP-ABE:** Chính sách trong khóa quyết định **người dùng có thể đọc loại dữ liệu nào**.



Speaker Notes — Slide 6

> “Ở Slide 5, chúng ta đã nhìn thấy ABE như một trong ba kỹ thuật mật mã nâng cao, với nhiệm vụ chính là giải quyết bài toán **Access — ai được phép truy cập dữ liệu**.
>
> Bây giờ chúng ta đi sâu hơn một bước: **ABE thực sự làm điều đó như thế nào?**
>
> Điểm quan trọng của ABE là quyền truy cập không nhất thiết phải gắn với một cá nhân cụ thể. Thay vào đó, hệ thống sử dụng các **thuộc tính** để xây dựng chính sách.
>
> Ví dụ, chúng ta có một hồ sơ bệnh án và quy định rằng người muốn truy cập phải có ba thuộc tính: **Doctor, Cardiology và Hospital A**.
>
> Như vậy, hệ thống không chỉ hỏi 'Bạn là ai?', mà hỏi thêm: **Bạn có những thuộc tính nào, và những thuộc tính đó có thỏa mãn chính sách truy cập hay không?**
>
> Đây chính là nguyên tắc cốt lõi của ABE:
>
> **Nếu tập thuộc tính của người dùng thỏa mãn Access Policy thì quá trình giải mã có thể thành công. Nếu không thỏa mãn thì không thể giải mã.**
>
> Từ đây, ABE được chia thành hai mô hình rất quan trọng: **CP-ABE và KP-ABE**.
>
> Với **CP-ABE — Ciphertext-Policy ABE**, chính sách truy cập nằm trên bản mã. Người mã hóa dữ liệu quyết định chính sách.
>
> Ví dụ, khi tôi đưa một hồ sơ bệnh án lên Cloud, tôi có thể đặt chính sách rằng:
>
> *'Chỉ người có thuộc tính Doctor AND Cardiology AND Hospital A mới được giải mã.'*
>
> Còn khóa của người dùng chỉ chứa các thuộc tính mà người đó được cấp.
>
> Vì vậy, có thể nhớ CP-ABE bằng câu:
>
> **'Dữ liệu này cho ai?'**
>
> Ngược lại, với **KP-ABE — Key-Policy ABE**, chính sách truy cập nằm trong khóa của người dùng. Bản mã chỉ mang các thuộc tính mô tả loại dữ liệu.
>
> Khi đó, cơ quan cấp khóa quyết định một người dùng có thể truy cập những loại dữ liệu nào thông qua chính sách được nhúng trong khóa của họ.
>
> Vì vậy, KP-ABE có thể ghi nhớ bằng câu:
>
> **'Người này được xem loại dữ liệu nào?'**
>
> Đây là khác biệt quan trọng nhất giữa hai mô hình:
>
> **CP-ABE: Policy nằm ở Ciphertext.**
>
> **KP-ABE: Policy nằm ở Key.**
>
> Về mặt quy trình, chúng ta có thể hình dung ABE qua bốn bước.
>
> Đầu tiên là **Setup**, hệ thống tạo các tham số cần thiết.
>
> Tiếp theo là **Key Generation**, người dùng được cấp Secret Key tương ứng với thuộc tính hoặc chính sách của họ.
>
> Sau đó là **Encryption**, dữ liệu được mã hóa và gắn với Policy hoặc Attributes tùy vào mô hình.
>
> Cuối cùng là **Decryption**. Hệ thống kiểm tra xem thông tin trong khóa có thỏa mãn chính sách hay không. Nếu có, người dùng giải mã được; nếu không, bản mã vẫn được bảo vệ.
>
> Như vậy, điều quan trọng nhất cần nhớ ở slide này là:
>
> **ABE biến bài toán kiểm soát truy cập thành bài toán thuộc tính và chính sách.**
>
> Nhưng đến đây chúng ta mới đang nói về mô hình ABE cơ bản. Một câu hỏi khó hơn sẽ xuất hiện:
>
> **Nếu hệ thống có nhiều cơ quan cấp khóa, nhiều người dùng và nhiều miền quản trị khác nhau thì chúng ta tổ chức ABE như thế nào? Và làm sao chứng minh rằng hệ thống thực sự an toàn trước một đối thủ?**
>
> Đó chính là nội dung của phần tiếp theo: **KP-ABE phi tập trung và Security Game.**”



# 📌 SLIDE 7: KP-ABE PHI TẬP TRUNG & CHỨNG MINH BẢO MẬT

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Từ KP-ABE cơ bản → KP-ABE phi tập trung

**Bài toán đặt ra:**

> Nếu hệ thống có nhiều **Attribute Authority (AA)** thuộc các tổ chức / miền quản trị khác nhau, làm thế nào để quản lý khóa mà không phụ thuộc vào một cơ quan trung tâm duy nhất?

**KP-ABE phi tập trung** cho phép:

* Nhiều **Attribute Authority** cùng tồn tại.
* Mỗi AA quản lý một tập thuộc tính riêng.
* Các AA có thể tham gia hoặc rời hệ thống mà không cần tái thiết lập toàn bộ hệ thống.
* Người dùng nhận các thành phần khóa từ nhiều AA khác nhau.

---

### 2. 5 thành phần chính của lược đồ

**① Global Setup**
→ Tạo các tham số hệ thống dùng chung.

**② Authority Setup**
→ Mỗi AA tạo khóa cho các thuộc tính mình quản lý.

**③ Key Issuing**
→ Người dùng tương tác với các AA để nhận thành phần khóa tương ứng.

**④ Encryption**
→ Dữ liệu được mã hóa cùng tập thuộc tính mô tả dữ liệu.

**⑤ Decryption**
→ Người dùng kết hợp các thành phần khóa; giải mã thành công khi **các thuộc tính thỏa mãn Access Policy**.

### 🎯 Ý tưởng cốt lõi

> **Không còn một “Authority” duy nhất quyết định toàn bộ quyền truy cập.**

---

### 3. Security Game — Chứng minh lược đồ có an toàn không?

Độ an toàn được mô hình hóa bằng một **trò chơi giữa:**

**Adversary** 🆚 **Challenger**

#### ① Key Queries

Adversary yêu cầu các khóa bí mật theo những truy vấn được phép.

↓

#### ② Challenge

Adversary chọn hai bản rõ:

$$
m_0,\;m_1
$$

Challenger chọn ngẫu nhiên \(b \in \{0,1\}\), rồi mã hóa \(m_b\).

↓

#### ③ More Queries

Adversary tiếp tục thực hiện các truy vấn khóa nhưng **không được vi phạm điều kiện truy cập của Challenge**.

↓

#### ④ Guess

Adversary đoán:

$$
b' = 0 \quad \text{hay} \quad b' = 1
$$

### 🔐 Tiêu chí an toàn

Nếu Adversary **không thể đạt lợi thế đáng kể so với đoán ngẫu nhiên**:

$$
Pr[b'=b] \approx \frac{1}{2}
$$

→ Lược đồ đạt **Selective-ID Security** trong mô hình đang xét.

---

### 💡 THÔNG ĐIỆP CẦN NHỚ

> **KP-ABE phi tập trung giải quyết bài toán quản lý nhiều Authority; Security Game cho chúng ta một cách hình thức để kiểm tra mức độ an toàn của lược đồ.**


Speaker Notes — Slide 7

> “Ở Slide 6, chúng ta đã thấy KP-ABE có một đặc điểm quan trọng: **chính sách truy cập nằm trong khóa của người dùng**.
>
> Nhưng nếu triển khai trong một hệ thống Cloud lớn thì sẽ xuất hiện một vấn đề mới:
>
> **Chúng ta có nhất thiết phải có một cơ quan duy nhất quản lý tất cả thuộc tính của tất cả người dùng hay không?**
>
> Ví dụ, một hệ thống có thể có một cơ quan quản lý thuộc tính về chức vụ, một cơ quan quản lý thuộc tính về bệnh viện, và một cơ quan khác quản lý thuộc tính về chuyên môn.
>
> Đây là lúc chúng ta cần đến **KP-ABE phi tập trung — Decentralized KP-ABE**.
>
> Điểm quan trọng ở đây là hệ thống có thể có **nhiều Attribute Authority**, và mỗi Authority chỉ quản lý những thuộc tính thuộc phạm vi của mình. Người dùng có thể nhận các thành phần khóa từ nhiều Authority khác nhau.
>
> Toàn bộ quá trình có thể được hình dung qua 5 bước.
>
> Đầu tiên là **Global Setup**, hệ thống tạo các tham số chung.
>
> Tiếp theo là **Authority Setup**, mỗi Authority thiết lập các khóa cần thiết cho những thuộc tính mà mình quản lý.
>
> Sau đó là **Key Issuing**, người dùng tương tác với các Authority để nhận các thành phần khóa tương ứng.
>
> Bước thứ tư là **Encryption**. Dữ liệu được mã hóa cùng các thuộc tính mô tả loại dữ liệu đó.
>
> Cuối cùng là **Decryption**. Người dùng kết hợp các thành phần khóa của mình và chỉ có thể giải mã nếu các thuộc tính mà họ sở hữu thỏa mãn chính sách truy cập.
>
> Như vậy, điểm quan trọng nhất của mô hình phi tập trung là:
>
> **Chúng ta không còn phụ thuộc vào một Authority duy nhất để quản lý toàn bộ hệ thống.**
>
> Nhưng đến đây lại xuất hiện một câu hỏi khác:
>
> **Làm thế nào chúng ta biết được một lược đồ mật mã như vậy thực sự an toàn?**
>
> Trong mật mã học, người ta không chỉ nói rằng một thuật toán 'có vẻ an toàn'. Độ an toàn thường được mô hình hóa bằng một **Security Game**.
>
> Hãy hình dung đây là một cuộc chơi giữa hai bên: **Adversary**, đại diện cho đối thủ, và **Challenger**, đại diện cho hệ thống.
>
> Đầu tiên, Adversary được phép thực hiện các truy vấn khóa theo những điều kiện mà mô hình cho phép.
>
> Sau đó đến bước **Challenge**. Adversary đưa ra hai bản rõ \(m_0\) và \(m_1\). Challenger chọn ngẫu nhiên một trong hai bản rõ, mã hóa nó và gửi bản mã cho Adversary.
>
> Sau khi nhận bản mã, Adversary vẫn có thể thực hiện thêm các truy vấn hợp lệ. Cuối cùng, Adversary phải đoán xem bản mã đó được tạo từ \(m_0\) hay \(m_1\).
>
> Nếu chỉ đoán ngẫu nhiên thì xác suất đúng là:
>
> $$
> \frac{1}{2}
> $$
>
> Vì vậy, mục tiêu của một lược đồ an toàn là làm cho Adversary **không thể đạt được một lợi thế đáng kể so với xác suất đoán ngẫu nhiên**, trong những giới hạn mà mô hình bảo mật đặt ra.
>
> Đây chính là ý tưởng đằng sau **Selective-ID Security** mà chúng ta đang xét.
>
> Như vậy, ở phần ABE, chúng ta đã đi từ một câu hỏi rất thực tế là **'Ai được phép truy cập dữ liệu?'**, đến một mô hình mật mã có thể quản lý nhiều Authority và có cơ chế hình thức để phân tích độ an toàn.
>
> Nhưng ABE mới giải quyết bài toán **kiểm soát quyền truy cập**.
>
> Vậy nếu chúng ta muốn Cloud **thực sự xử lý dữ liệu trong khi dữ liệu vẫn ở dạng mã hóa**, thì sao?
>
> Đó là một bài toán hoàn toàn khác, và nó dẫn chúng ta đến kỹ thuật tiếp theo:
>
> **Fully Homomorphic Encryption — FHE.**”


# 📌 SLIDE 8: FHE — TÍNH TOÁN TRÊN DỮ LIỆU MÃ HÓA

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. FHE giải quyết bài toán gì?

**Câu hỏi:**

> **Làm thế nào để Cloud xử lý dữ liệu mà không cần nhìn thấy dữ liệu gốc?**

Với mã hóa thông thường:

**Plaintext → Encryption → Cloud → Decryption → Computation**

→ Muốn tính toán thường phải **giải mã dữ liệu**.

Với **FHE**:

**Plaintext → Encryption → Computation on Ciphertext → Decryption**

→ Cloud có thể thực hiện phép toán **trực tiếp trên bản mã**.

### 🎯 Nguyên lý cốt lõi

$$
Dec(Eval(E(m),f)) = f(m)
$$

**Tính toán trên bản mã → kết quả tương ứng với tính toán trên bản rõ.**

---

### 2. Kiến trúc triển khai: 3 thành phần

| Thành phần                 | Vai trò                                              |
| -------------------------- | ---------------------------------------------------- |
| 👤 **User**                | Sở hữu dữ liệu, mã hóa dữ liệu và giải mã kết quả    |
| 💻 **HC Node**             | Thực hiện các phép toán đồng cấu trên **ciphertext** |
| 🛡️ **Bootstrapping Node** | Làm mới ciphertext khi nhiễu tăng cao                |

> **Lưu ý:** Secure Enclave và Remote Attestation là các cơ chế bảo vệ của **kiến trúc triển khai cụ thể**, không phải điều kiện bắt buộc của mọi hệ thống FHE.

---

### 3. Luồng xử lý FHE

**① User**

Dữ liệu gốc
↓
🔐 **Encrypt**
↓

**② HC Node**

`Ciphertext`
↓
⚙️ **Homomorphic Computation**
`+ , × , ...`
↓
`Ciphertext + Noise`

↓ *(Noise tăng cao)*

**③ Bootstrapping Node**

🔄 **Bootstrapping**
→ Làm mới ciphertext
→ Giảm ảnh hưởng của noise

↓

**④ HC Node**

Tiếp tục tính toán

↓

**⑤ User**

🔓 **Decrypt**

→ **Kết quả cuối cùng**

---

### ⚠️ 4. Bài toán Noise

Mỗi phép toán đồng cấu làm **nhiễu trong ciphertext tăng lên**.

**Noise thấp**
→ Có thể tiếp tục tính toán

**Noise vượt ngưỡng**
→ Không thể giải mã chính xác

### 🔄 Bootstrapping

> **Bootstrapping = làm mới ciphertext để tiếp tục tính toán.**

Trong kiến trúc đang xét:

**Ciphertext có nhiều Noise**
→ Secure Enclave xử lý Bootstrapping
→ **Refreshed Ciphertext**
→ HC Node tiếp tục tính toán

---

### 💡 THÔNG ĐIỆP CẦN NHỚ

> **FHE cho phép Cloud tính toán trên dữ liệu mà dữ liệu vẫn ở dạng mã hóa.**

**ABE:** Ai được truy cập?
**FHE:** Cloud có thể tính toán trên dữ liệu mà không thấy dữ liệu không?




Speaker Notes — Slide 8


> “Ở Slide 6 và Slide 7, chúng ta đã giải quyết bài toán **kiểm soát truy cập** bằng ABE: ai được phép đọc dữ liệu và hệ thống có thể quản lý quyền đó như thế nào.
>
> Nhưng bây giờ chúng ta chuyển sang một bài toán khác.
>
> **Nếu Cloud được phép xử lý dữ liệu của chúng ta, liệu chúng ta có thể giữ dữ liệu đó ở trạng thái mã hóa trong suốt quá trình xử lý hay không?**
>
> Đây chính là vấn đề mà **Fully Homomorphic Encryption — FHE** hướng tới.
>
> Với mã hóa thông thường, chúng ta thường có một quy trình là: dữ liệu được mã hóa để bảo vệ, nhưng khi cần tính toán thì dữ liệu phải được giải mã. Chính thời điểm đó, dữ liệu gốc có thể xuất hiện trên môi trường Cloud.
>
> FHE thay đổi cách tiếp cận này.
>
> Dữ liệu được mã hóa trước khi gửi lên Cloud. Sau đó, Cloud thực hiện phép tính trực tiếp trên **ciphertext**. Cuối cùng, người sở hữu khóa mới giải mã kết quả.
>
> Có thể hiểu đơn giản:
>
> **Cloud nhìn thấy bản mã, thực hiện phép tính trên bản mã, nhưng không cần biết bản rõ ban đầu.**
>
> Về mặt toán học, ý tưởng có thể biểu diễn đơn giản bằng công thức:
>
> $$
> Dec(Eval(E(m),f)) = f(m)
> $$
>
> Nghĩa là nếu chúng ta mã hóa dữ liệu \(m\), sau đó để Cloud thực hiện hàm \(f\) trên bản mã, khi giải mã kết quả chúng ta thu được chính kết quả của việc áp dụng \(f\) lên dữ liệu gốc.
>
> Trong kiến trúc mà chúng ta đang xét, có ba thành phần chính.
>
> **Thứ nhất là User** — chủ sở hữu dữ liệu. User chịu trách nhiệm mã hóa dữ liệu ban đầu và cuối cùng giải mã kết quả.
>
> **Thứ hai là HC Node**, tức nút tính toán đồng cấu. Đây là nơi Cloud thực hiện các phép toán như cộng, nhân và các phép toán được hỗ trợ trên ciphertext.
>
> **Thứ ba là Bootstrapping Node.** Thành phần này có nhiệm vụ xử lý một vấn đề kỹ thuật rất quan trọng của FHE: **Noise**.
>
> Mỗi phép toán trên ciphertext đều làm nhiễu trong bản mã tăng lên. Nếu thực hiện càng nhiều phép toán, noise càng tích tụ. Khi vượt quá một ngưỡng nhất định, bản mã có thể không còn giải mã chính xác được nữa.
>
> Vì vậy chúng ta cần đến **Bootstrapping**.
>
> Có thể hình dung Bootstrapping giống như việc 'làm mới' một bản mã đã tích tụ quá nhiều nhiễu. Sau khi được làm mới, ciphertext có thể tiếp tục được đưa trở lại HC Node để thực hiện các phép tính tiếp theo.
>
> Trong kiến trúc cụ thể mà chúng ta đang trình bày, Bootstrapping Node được đặt trong **Secure Enclave**. Enclave tạo ra một môi trường thực thi được bảo vệ cho thành phần này.
>
> Ngoài ra, kiến trúc có thể sử dụng **Remote Attestation** để User xác minh trạng thái hoặc cấu hình của môi trường trước khi thiết lập kênh an toàn.
>
> Tuy nhiên, có một điểm cần phân biệt: **FHE không đồng nghĩa với Secure Enclave.** FHE là cơ chế mật mã cho phép tính toán trên ciphertext; Secure Enclave và Remote Attestation là những cơ chế bảo vệ bổ sung trong kiến trúc triển khai cụ thể này.
>
> Toàn bộ luồng có thể tóm tắt như sau:
>
> **User mã hóa dữ liệu → HC Node tính toán trên ciphertext → Bootstrapping khi noise tăng cao → HC Node tiếp tục tính toán → User giải mã kết quả.**
>
> Đây chính là điểm khác biệt lớn mà FHE mang lại: **Cloud có thể cung cấp năng lực tính toán mà không nhất thiết phải được nhìn thấy dữ liệu gốc.**
>
> Nhưng FHE giải quyết bài toán **tính toán**. Còn một nhu cầu rất phổ biến khác là:
>
> **Nếu hàng nghìn tài liệu đều đã được mã hóa, làm thế nào để Cloud tìm được tài liệu chứa một từ khóa mà không cần giải mã toàn bộ kho dữ liệu?**
>
> Đó chính là bài toán tiếp theo, và chúng ta sẽ chuyển sang **Searchable Encryption — SE**.”


# 📌 SLIDE 9: FHE — TÍNH TOÁN THUÊ NGOÀI & ỨNG DỤNG TRONG Y TẾ

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Từ lý thuyết → Tính toán thuê ngoài

**Tình huống:**

> Doanh nghiệp B có dữ liệu nhạy cảm và muốn **thuê Cloud thực hiện phép tính**, nhưng không muốn Cloud biết dữ liệu gốc.

### Luồng xử lý

```text
        DOANH NGHIỆP B                         CLOUD

Dữ liệu gốc: 5 , 10
       │
       │ ① Encrypt
       ▼
Ciphertext: Enc(5), Enc(10)
       │
       └──────────────────────────────►
                                      │
                                      │ ② Homomorphic
                                      │    Computation
                                      │
                                      ▼
                               Enc(5 + 10)
                                      │
       ◄──────────────────────────────┘
       │
       │ ③ Decrypt
       ▼
     Kết quả: 15
```

### 🔑 Điều quan trọng

**Cloud biết:**
→ Ciphertext + phép tính cần thực hiện

**Cloud không cần biết:**
→ Dữ liệu gốc \(5,10\)

**User biết:**
→ Dữ liệu gốc + kết quả sau khi giải mã

---

### 2. Ví dụ trực quan về tính chất đồng cấu

Với một lược đồ đồng cấu phù hợp:

$$
Enc(5) \oplus Enc(10)
$$

→ Cloud thực hiện phép toán trên ciphertext

$$
\Downarrow
$$

$$
Enc(15)
$$

→ User giải mã:

$$
Dec(Enc(15)) = 15
$$

> **Điểm mấu chốt:** phép tính được thực hiện **trước khi giải mã**.

---

### 3. Ứng dụng: Phân tích dữ liệu y tế

🏥 **Bài toán**

Bệnh viện sở hữu dữ liệu bệnh nhân nhưng muốn tận dụng năng lực tính toán / AI của Cloud.

**Mâu thuẫn:**

`Dữ liệu càng chi tiết → phân tích càng hữu ích`

nhưng

`Dữ liệu càng nhạy cảm → yêu cầu bảo vệ càng cao`

### Với FHE

**Bệnh viện**

Dữ liệu y tế
↓
🔐 **Mã hóa**
↓

**Cloud**

⚙️ Phân tích / tính toán trên ciphertext
↓

**Kết quả mã hóa**

↓

**Bệnh viện**

🔓 **Giải mã**

→ Kết quả phân tích

### 🎯 Giá trị bảo mật

Cloud có thể cung cấp **năng lực tính toán**, trong khi dữ liệu bệnh nhân được duy trì ở dạng mã hóa trong quá trình xử lý.

> **FHE mở ra khả năng thuê ngoài phân tích dữ liệu nhạy cảm mà không cần giao dữ liệu gốc cho Cloud.**

---

### 💡 THÔNG ĐIỆP CẦN NHỚ

> **FHE tách “quyền tính toán” khỏi “quyền nhìn thấy dữ liệu”.**

**Cloud:** có thể tính toán.
**User:** giữ quyền giải mã.

---

### ❓ CÂU HỎI CHUYỂN TIẾP

> **Nếu Cloud không được nhìn thấy nội dung dữ liệu, vậy làm thế nào để Cloud tìm đúng tài liệu chứa một từ khóa?**

→ **Searchable Encryption (SE)**



Speaker Notes — Slide 9

> “Ở Slide 8, chúng ta đã nhìn FHE từ góc độ kỹ thuật: ciphertext, homomorphic computation, noise và bootstrapping.
>
> Bây giờ chúng ta tạm rời phần kỹ thuật để trả lời một câu hỏi đơn giản hơn:
>
> **FHE thực sự giúp ích gì khi doanh nghiệp sử dụng Cloud?**
>
> Hãy tưởng tượng Doanh nghiệp B có một tập dữ liệu nhạy cảm gồm hai giá trị là 5 và 10. Doanh nghiệp muốn thuê Cloud thực hiện phép tính tổng nhưng không muốn gửi dữ liệu dưới dạng rõ.
>
> Trước tiên, doanh nghiệp mã hóa hai giá trị đó. Cloud chỉ nhận được hai ciphertext.
>
> Sau đó, doanh nghiệp yêu cầu Cloud thực hiện phép cộng.
>
> Điểm đặc biệt ở đây là Cloud **không cần giải mã hai ciphertext**. Nó thực hiện phép toán đồng cấu trực tiếp trên chúng và tạo ra một ciphertext mới tương ứng với kết quả.
>
> Khi nhận kết quả, chỉ doanh nghiệp sở hữu khóa giải mã mới có thể lấy ra giá trị cuối cùng là 15.
>
> Vì vậy, chúng ta có một sự thay đổi rất quan trọng trong mô hình thuê ngoài:
>
> **Cloud có quyền thực hiện phép tính, nhưng không nhất thiết có quyền nhìn thấy dữ liệu.**
>
> Đây chính là ý nghĩa lớn nhất của FHE.
>
> Có một điểm mình muốn làm rõ để tránh hiểu nhầm: ví dụ 5 và 10 ở đây chỉ nhằm minh họa **tính chất đồng cấu**. Trong một hệ FHE thực tế, ciphertext không đơn giản là 'nhân đôi số 5 thành 10 rồi chia 2 để giải mã'. Quy trình mã hóa, tính toán và giải mã được thực hiện bằng một lược đồ mật mã với khóa và các phép toán tương ứng.
>
> Bây giờ chúng ta thử đưa ý tưởng này vào một lĩnh vực nhạy cảm hơn: **y tế**.
>
> Bệnh viện có một lượng lớn dữ liệu bệnh nhân và muốn sử dụng năng lực tính toán của Cloud để thực hiện các phân tích, chẳng hạn như phân tích thống kê hoặc các mô hình dự báo.
>
> Nhưng dữ liệu y tế chứa rất nhiều thông tin nhạy cảm. Nếu bệnh viện gửi dữ liệu dạng rõ cho Cloud, chúng ta lại quay về đúng vấn đề mà FHE muốn giải quyết.
>
> Với FHE, dữ liệu có thể được mã hóa trước khi gửi lên môi trường tính toán. Cloud thực hiện các phép toán trên ciphertext và trả về kết quả đã mã hóa. Bệnh viện sau đó sử dụng khóa của mình để giải mã kết quả.
>
> Như vậy, FHE tạo ra một mô hình rất thú vị:
>
> **Cloud cung cấp năng lực tính toán, nhưng quyền giải mã vẫn nằm ở chủ sở hữu dữ liệu.**
>
> Đây cũng là lý do FHE được nghiên cứu cho các bài toán xử lý dữ liệu nhạy cảm, trong đó có dữ liệu y tế.
>
> Và đến đây, chúng ta đã giải quyết một nhu cầu rất cụ thể:
>
> **Muốn tính toán trên dữ liệu mã hóa → dùng FHE.**
>
> Nhưng Cloud không chỉ được thuê để tính toán. Một thao tác rất phổ biến khác là **tìm kiếm**.
>
> Ví dụ, chúng ta có hàng nghìn email hoặc tài liệu đã được mã hóa. Người dùng muốn tìm tất cả tài liệu chứa từ khóa 'Urgent'.
>
> Nếu giải mã toàn bộ dữ liệu trước khi tìm kiếm thì chúng ta lại tạo ra một điểm phơi nhiễm mới.
>
> Vậy câu hỏi tiếp theo là:
>
> **Có thể tìm kiếm trên dữ liệu đã mã hóa mà không cần tiết lộ nội dung hay không?**
>
> Đây chính là bài toán mà **Searchable Encryption — SE** giải quyết.
>
> Mời thầy cô và các bạn cùng chuyển sang **Slide 10: Searchable Encryption — Tìm kiếm trên dữ liệu mã hóa.**”

# 📌 SLIDE 10: SEARCHABLE ENCRYPTION (SE) — TÌM KIẾM TRÊN DỮ LIỆU MÃ HÓA

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Bài toán: Mã hóa rồi thì tìm kiếm thế nào?

Khi dữ liệu được mã hóa và lưu trên Cloud:

> **Làm sao tìm đúng tài liệu cần thiết mà không phải giải mã toàn bộ kho dữ liệu?**

* 🔒 **Mã hóa thông thường:** Cloud không đọc được nội dung → bảo vệ quyền riêng tư.
* 🔎 **Nhưng:** Cloud cũng không thể thực hiện tìm kiếm trực tiếp trên nội dung đã mã hóa.
* 💡 **Searchable Encryption (SE):** Cho phép thực hiện truy vấn dựa trên **từ khóa** mà không cần công khai nội dung gốc.

**Ý tưởng cốt lõi:**

`Dữ liệu mã hóa + Keyword Index / Trapdoor → Tìm kiếm → Kết quả`

---

### 2. Cơ chế Searchable Encryption

**Luồng xử lý cơ bản:**

**① Mã hóa**
Chủ sở hữu mã hóa tài liệu và xây dựng thông tin tìm kiếm tương ứng.

↓

**② Tạo truy vấn**
Người dùng tạo **Trapdoor** cho từ khóa cần tìm.

↓

**③ Đối sánh**
Cloud kiểm tra sự phù hợp giữa Trapdoor và **chỉ mục từ khóa**, thay vì đọc nội dung tài liệu.

↓

**④ Trả kết quả**
Cloud trả về các tài liệu phù hợp để người dùng tiếp tục truy cập/giải mã theo quyền được cấp.

### Hai hướng triển khai phổ biến

* 🔑 **Symmetric-key SE:** Sử dụng khóa đối xứng và chỉ mục từ khóa, thường hướng tới hiệu năng tìm kiếm cao.
* 🌐 **PEKS:** *Public Key Encryption with Keyword Search* — hỗ trợ tìm kiếm từ khóa trên dữ liệu mã hóa bằng cơ chế khóa công khai.

---

### 3. Ví dụ: Tìm kiếm mà không đọc nội dung

#### 📬 Email — từ khóa `"Urgent"`

```text
Email đã mã hóa
       ↓
  Keyword Index
       ↓
Trapdoor: "Urgent"
       ↓
Cloud đối sánh
       ↓
Tìm thấy email phù hợp
       ↓
Chuyển kết quả cho người có quyền
```

**Điểm quan trọng:** Cloud có thể xác định **email nào phù hợp với truy vấn** mà không cần biết nội dung đầy đủ của email.

#### 🎙️ Kho văn bản lớn

Các tài liệu được gắn chỉ mục như:

`"electoral debate"` · `"BBC"` · `"date"`

→ Người dùng có thể tìm đúng tài liệu cần thiết trong một kho lớn mà không phải giải mã toàn bộ dữ liệu.

---

### 4. Kết thúc Phần 3 — Ba kỹ thuật, Ba bài toán

| Kỹ thuật   | Giải quyết bài toán                                  |
| ---------- | ---------------------------------------------------- |
| 🔐 **ABE** | **Ai được phép truy cập?**                           |
| ⚙️ **FHE** | **Cloud có thể tính toán gì mà không thấy dữ liệu?** |
| 🔎 **SE**  | **Cloud có thể tìm kiếm gì mà không đọc dữ liệu?**   |

> **ABE → Kiểm soát truy cập**
> **FHE → Tính toán trên dữ liệu mã hóa**
> **SE → Tìm kiếm trên dữ liệu mã hóa**

---

# 🎙️ Speaker Notes — Slide 10: Searchable Encryption

> “Sau khi đã tìm hiểu ABE để kiểm soát quyền truy cập và FHE để thực hiện tính toán trên dữ liệu mã hóa, chúng ta còn một bài toán rất thực tế:
>
> **Nếu hàng nghìn, thậm chí hàng triệu tài liệu trên Cloud đều đã được mã hóa, thì làm thế nào để tìm đúng tài liệu mình cần?**
>
> Nếu giải mã toàn bộ dữ liệu rồi mới tìm kiếm thì vừa tốn thời gian, vừa làm mất đi lợi ích của việc mã hóa. Đây chính là bài toán mà **Searchable Encryption — SE**, hay mã hóa có thể tìm kiếm, hướng tới giải quyết.
>
> Ý tưởng của SE khá trực quan. Thay vì yêu cầu Cloud đọc nội dung tài liệu, hệ thống xây dựng các **thông tin tìm kiếm**, chẳng hạn như chỉ mục từ khóa. Khi người dùng muốn tìm một từ khóa, họ tạo ra một **Trapdoor**, có thể hiểu đơn giản là một dạng truy vấn được mã hóa.
>
> Cloud nhận Trapdoor và thực hiện đối sánh với các chỉ mục mà không cần đọc nội dung đầy đủ của tài liệu.
>
> Có hai hướng triển khai phổ biến. Thứ nhất là **Searchable Encryption sử dụng khóa đối xứng**, thường tập trung vào hiệu quả tìm kiếm. Thứ hai là **PEKS — Public Key Encryption with Keyword Search**, cho phép xây dựng cơ chế tìm kiếm từ khóa dựa trên mật mã khóa công khai.
>
> Để hình dung rõ hơn, hãy lấy ví dụ về **email khẩn cấp**.
>
> Giả sử Alice đang đi nghỉ và muốn những email có từ khóa *‘Urgent’* được tự động chuyển cho John. Các email được lưu dưới dạng mã hóa nên máy chủ trung gian không thể đọc nội dung. John tạo một **Trapdoor cho từ khóa ‘Urgent’** và gửi truy vấn đó cho hệ thống. Cloud thực hiện đối sánh với thông tin tìm kiếm và xác định những email phù hợp để xử lý tiếp theo.
>
> Điểm quan trọng ở đây là: **Cloud có thể thực hiện chức năng tìm kiếm mà không cần đọc toàn bộ nội dung tài liệu.**
>
> Từ ví dụ này, chúng ta có thể nhìn lại toàn bộ Phần 3 dưới một góc rất đơn giản:
>
> **ABE trả lời câu hỏi: Ai được phép truy cập?**
>
> **FHE trả lời câu hỏi: Làm thế nào Cloud có thể tính toán mà không thấy dữ liệu?**
>
> Và **SE trả lời câu hỏi: Làm thế nào Cloud có thể tìm kiếm mà không cần đọc dữ liệu?**
>
> Như vậy, ba kỹ thuật này bảo vệ dữ liệu ở ba khía cạnh khác nhau: **truy cập, tính toán và tìm kiếm**.
>
> Tuy nhiên, bảo mật Cloud không chỉ dừng lại ở dữ liệu. Ngay cả khi dữ liệu đã được bảo vệ bằng những cơ chế mật mã mạnh, **hạ tầng mạng, máy chủ, vùng tin cậy và cấu hình hệ thống** vẫn có thể trở thành điểm yếu.
>
> Vì vậy, từ đây chúng ta sẽ **zoom out một lần nữa — từ bảo vệ dữ liệu sang bảo vệ toàn bộ hạ tầng Cloud**.
>
> Xin mời thầy cô và các bạn cùng bước sang **Phần 4: Bảo vệ hạ tầng và Vùng tin cậy — Trust Zones**.”

# 📌 SLIDE 11: BẢO VỆ HẠ TẦNG & VÙNG TIN CẬY

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Zoom Out: Từ Dữ liệu đến Hạ tầng

Sau khi bảo vệ **dữ liệu bằng mật mã**, chúng ta mở rộng phạm vi bảo vệ:

**DATA**
↓
**NETWORK**
↓
**IDENTITY & ACCESS**
↓
**HOST / VM**

> **Bảo mật Cloud không chỉ bảo vệ dữ liệu, mà còn phải bảo vệ môi trường đang lưu trữ và xử lý dữ liệu.**

---

### 2. Network Security: Private Cloud vs. Public Cloud

| 🏢 Private Cloud                                                             | 🌐 Public Cloud                                                         |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Môi trường mạng được tổ chức và kiểm soát tập trung hơn                      | Tài nguyên được cung cấp qua hạ tầng Cloud của CSP                      |
| Có thể áp dụng các cơ chế kiểm soát mạng nội bộ quen thuộc                   | Phụ thuộc nhiều hơn vào cấu hình, dịch vụ và khả năng kiểm soát của CSP |
| Vẫn phải đối phó với misconfiguration, unauthorized access và insider threat | Tăng mức độ phụ thuộc vào kết nối mạng và cấu hình tài nguyên           |

### Các rủi ro cần chú ý trong Cloud

* 🌐 **Network Exposure:** tài nguyên có thể được truy cập qua Internet.
* ⚙️ **Misconfiguration:** cấu hình sai có thể mở rộng phạm vi truy cập ngoài dự kiến.
* 📊 **Visibility & Monitoring:** khả năng quan sát phụ thuộc vào dịch vụ và công cụ mà CSP cung cấp.
* ⚡ **Availability:** dịch vụ có thể phụ thuộc vào kết nối mạng và hạ tầng bên ngoài tổ chức.

> **Public Cloud không đồng nghĩa với “không an toàn” — vấn đề nằm ở cách thiết kế, cấu hình và kiểm soát.**

---

### 3. Trust Zones: Giới hạn phạm vi của một sự cố

### 🎯 Ý tưởng cốt lõi

**Trust Zone = Network Segmentation + Access Control / IAM**

Thay vì coi toàn bộ hệ thống là một vùng tin cậy:

**Users → Zone A → Zone B → Zone C → Critical Resources**

Mỗi vùng có:

* Quyền truy cập riêng
* Chính sách mạng riêng
* Cơ chế giám sát riêng
* Ranh giới rõ ràng với các vùng khác

### 🛡️ Mục tiêu

**Ngăn chặn:**

**Initial Access → Lateral Movement → Critical Resources**

Đặc biệt trong các tình huống:

* APT
* Compromised account
* Insider threat
* Compromised VM / workload

---

### 🔑 Tư duy bảo mật

> **“Không mặc nhiên tin tưởng chỉ vì một thành phần đang nằm bên trong mạng.”**

→ Xác thực danh tính
→ Kiểm tra quyền
→ Phân đoạn tài nguyên
→ Giám sát hoạt động

---

### 🎯 THÔNG ĐIỆP CHÍNH

> **Bảo vệ Cloud không dừng ở việc mã hóa dữ liệu — cần giới hạn cả nơi dữ liệu được lưu trữ, xử lý và ai có thể tiếp cận nó.**

Speaker Notes — Slide 11
> “Sau khi đã tìm hiểu các kỹ thuật mật mã giúp bảo vệ dữ liệu, bây giờ chúng ta sẽ **zoom out** một lần nữa.
>
> Bởi vì bảo mật Cloud không chỉ là bảo vệ bản thân dữ liệu. Chúng ta còn phải bảo vệ **hạ tầng đang lưu trữ, truyền tải và xử lý dữ liệu đó**.
>
> Có thể hình dung các lớp bảo vệ theo thứ tự: **Data → Network → Identity & Access → Host và VM**.
>
> Ở cấp độ mạng, một câu hỏi thường được đặt ra là: **Private Cloud có an toàn hơn Public Cloud không?**
>
> Thay vì xem đây là câu hỏi có một câu trả lời tuyệt đối, chúng ta nên nhìn vào **mô hình kiểm soát và bề mặt tấn công**.
>
> Private Cloud thường cho tổ chức mức độ kiểm soát trực tiếp hơn đối với môi trường mạng. Tuy nhiên, nó vẫn phải đối phó với những vấn đề quen thuộc như cấu hình sai, tài khoản bị xâm phạm hoặc mối đe dọa từ người bên trong.
>
> Với Public Cloud, một phần hạ tầng nằm dưới sự vận hành của CSP và tài nguyên có thể được truy cập qua mạng Internet. Vì vậy, các vấn đề như **network exposure, misconfiguration, monitoring và availability** trở nên đặc biệt quan trọng.
>
> Trong số đó, **misconfiguration — cấu hình sai** là một vấn đề rất đáng chú ý. Chỉ một thiết lập sai về quyền truy cập hoặc cấu hình mạng cũng có thể khiến tài nguyên vốn chỉ dành cho một phạm vi nhỏ trở nên có thể truy cập từ bên ngoài.
>
> Nhưng ngay cả khi chúng ta đã cấu hình mạng tốt, vẫn còn một câu hỏi khác:
>
> **Nếu một tài khoản hoặc một máy ảo đã bị xâm nhập thì chuyện gì xảy ra tiếp theo?**
>
> Đây là lúc chúng ta cần đến ý tưởng **Trust Zones**.
>
> Thay vì coi toàn bộ hệ thống là một vùng tin cậy duy nhất, chúng ta chia hạ tầng thành nhiều vùng và đặt các ranh giới kiểm soát giữa chúng.
>
> Ví dụ, một tài khoản hoặc máy ảo ở Zone A không mặc nhiên được truy cập Zone B. Muốn đi qua ranh giới đó, hệ thống phải kiểm tra quyền truy cập và áp dụng chính sách tương ứng.
>
> Mục tiêu rất quan trọng ở đây là hạn chế **lateral movement — di chuyển ngang**. Nếu một thành phần bị xâm nhập, kẻ tấn công không nên có khả năng dễ dàng di chuyển từ tài nguyên này sang toàn bộ hệ thống.
>
> Vì vậy, Trust Zone có thể được hiểu đơn giản là sự kết hợp giữa **phân đoạn mạng và kiểm soát truy cập**, với tư duy rằng không nên mặc nhiên tin tưởng một thành phần chỉ vì nó đang nằm bên trong mạng.
>
> Như vậy, đến đây chúng ta đã đi từ **bảo vệ dữ liệu bằng mật mã** sang **bảo vệ hạ tầng bằng network segmentation và access control**.
>
> Nhưng vẫn còn một vấn đề: **trách nhiệm bảo mật thay đổi như thế nào khi chúng ta chuyển từ IaaS sang PaaS và SaaS? Và ở từng mô hình, khách hàng thực sự phải bảo vệ những gì?**
>
> Đó sẽ là nội dung chúng ta tìm hiểu tiếp theo.”

# 📌 SLIDE 12: IaaS / PaaS / SaaS — RANH GIỚI TRÁCH NHIỆM THAY ĐỔI THẾ NÀO?

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Cùng là Cloud — nhưng trách nhiệm bảo mật không giống nhau

|                                  | **IaaS**                                  | **PaaS**                                   | **SaaS**                                    |
| -------------------------------- | ----------------------------------------- | ------------------------------------------ | ------------------------------------------- |
| **CSP chịu trách nhiệm**         | Data Center, phần cứng, mạng, Hypervisor  | IaaS + OS/Runtime/Middleware của nền tảng  | Hạ tầng + nền tảng + ứng dụng               |
| **Khách hàng chịu trách nhiệm**  | OS, cấu hình mạng, ứng dụng, dữ liệu, IAM | Mã nguồn, dữ liệu, IAM & cấu hình ứng dụng | Dữ liệu, người dùng, IAM & cấu hình dịch vụ |
| **Mức kiểm soát của khách hàng** | 🟢 Cao                                    | 🟡 Trung bình                              | 🔵 Thấp hơn                                 |
| **Điểm cần chú ý**               | VM & OS Security                          | Application Security                       | Identity & Access Control                   |

> **Nguyên tắc:** Càng sử dụng dịch vụ ở tầng cao hơn, CSP càng đảm nhận nhiều thành phần hơn — nhưng khách hàng vẫn phải quản lý phần trách nhiệm nằm trong phạm vi của mình.

---

### 2. Hai thay đổi quan trọng khi lên Cloud

#### 🔄 Từ **Network-centric** → **Identity-centric**

Trong môi trường truyền thống:

**“Bạn đang kết nối từ đâu?”**
→ IP, Firewall, Network perimeter

Trong Cloud:

**“Bạn là ai và được phép làm gì?”**
→ Identity, Authentication, Authorization, IAM

**📌 Vì vậy:** IAM trở thành một lớp kiểm soát trung tâm khi người dùng, thiết bị và dịch vụ có thể truy cập tài nguyên từ nhiều vị trí khác nhau.

---

#### ⚠️ Quyền truy cập cần đủ **fine-grained**

Một tài khoản có quyền truy cập không đồng nghĩa với việc tài khoản đó nên được phép truy cập **mọi tài nguyên**.

Cần kiểm soát:

* **Ai?** → Identity
* **Được làm gì?** → Permission
* **Trên tài nguyên nào?** → Resource
* **Trong điều kiện nào?** → Context / Policy

> **Mục tiêu:** Cấp **đúng quyền — đúng tài nguyên — đúng thời điểm**.

---

### 3. Ví dụ: Rủi ro khi kiểm soát quyền chưa đủ chi tiết

**SaaS / Document Sharing**

```text
Người dùng A
     │
     ├── Có quyền xem tài liệu
     │
     ▼
  Tài liệu
     │
     └── Tài nguyên liên quan / nội dung nhúng
                    │
                    ▼
          Có thể có cơ chế truy cập riêng
```

📌 **Bài học:** Thu hồi quyền đối với một tài nguyên không phải lúc nào cũng đồng nghĩa với việc **mọi tài nguyên liên quan** đều bị thu hồi quyền.

→ Vì vậy cần kiểm tra **toàn bộ chuỗi quyền truy cập**, không chỉ quyền ở giao diện chính của ứng dụng.

---

### 4. Cầu nối sang phần tiếp theo

> **IaaS → nhiều quyền kiểm soát hơn → nhiều trách nhiệm hơn**

Đặc biệt với **Virtual Server / VM**, khách hàng phải chủ động:

**Cấu hình → Gia cố → Bảo vệ khóa → Firewall → Logging → Audit**

➡️ **Tiếp theo: 6 khuyến nghị bảo mật máy chủ ảo**

---

# 🎙️ Speaker Notes — Slide 12: IaaS / PaaS / SaaS

> “Sau khi đã nhìn vấn đề ở cấp độ mạng và Trust Zone, chúng ta tiếp tục **đi vào bên trong kiến trúc Cloud** để xem một câu hỏi rất quan trọng:
>
> **Khi sử dụng IaaS, PaaS hay SaaS, trách nhiệm bảo mật của khách hàng thay đổi như thế nào?**
>
> Điểm cần nhớ đầu tiên là: **Cloud không có nghĩa là CSP chịu trách nhiệm cho mọi thứ.** Ranh giới trách nhiệm được phân chia giữa nhà cung cấp và khách hàng, và ranh giới đó thay đổi theo mô hình dịch vụ.
>
> Với **IaaS**, CSP chủ yếu bảo vệ phần hạ tầng bên dưới như trung tâm dữ liệu, phần cứng, mạng và Hypervisor. Khách hàng vẫn phải quản lý hệ điều hành, cấu hình mạng, ứng dụng, dữ liệu và quyền truy cập.
>
> Vì vậy, IaaS cho khách hàng mức độ kiểm soát rất lớn, nhưng đi kèm với đó là trách nhiệm bảo mật cũng lớn hơn. Một cấu hình sai trên máy chủ ảo, một dịch vụ không cần thiết được mở, hay một hệ điều hành không được cập nhật đều có thể trở thành điểm yếu.
>
> Khi chuyển lên **PaaS**, CSP tiếp quản thêm nhiều thành phần của nền tảng như hệ điều hành, runtime hoặc middleware. Khách hàng có thể tập trung nhiều hơn vào mã nguồn, dữ liệu và cấu hình ứng dụng.
>
> Còn với **SaaS**, phần lớn hạ tầng và ứng dụng đã được nhà cung cấp quản lý. Tuy nhiên, khách hàng vẫn phải chịu trách nhiệm đối với những thứ thuộc về mình, đặc biệt là **người dùng, danh tính, quyền truy cập, dữ liệu và cấu hình dịch vụ**.
>
> Vì vậy, chúng ta có thể hình dung một quy luật rất đơn giản:
>
> **Càng đi từ IaaS lên PaaS rồi SaaS, CSP quản lý càng nhiều thành phần hơn; nhưng khách hàng không bao giờ được phép bỏ qua phần trách nhiệm của mình.**
>
> Điều này dẫn chúng ta đến một thay đổi rất quan trọng trong tư duy bảo mật.
>
> Trong mô hình mạng truyền thống, chúng ta thường đặt câu hỏi: **‘Người dùng đang ở đâu?’** Chúng ta dựa nhiều vào IP, firewall và vành đai mạng để quyết định quyền truy cập.
>
> Nhưng trong Cloud, người dùng và dịch vụ có thể truy cập tài nguyên từ rất nhiều vị trí khác nhau. Vì vậy, câu hỏi ngày càng chuyển thành:
>
> **‘Người này là ai, đang yêu cầu quyền gì và có được phép thực hiện hành động đó hay không?’**
>
> Đây chính là lý do **Identity và IAM — Identity and Access Management** trở thành một lớp bảo mật rất quan trọng.
>
> Đồng thời, quyền truy cập cũng cần đủ **fine-grained**, tức là đủ chi tiết. Chúng ta không chỉ hỏi ‘người dùng này có quyền truy cập hay không’, mà phải hỏi: **họ có quyền gì, trên tài nguyên nào, trong điều kiện nào và trong bao lâu?**
>
> Điều này đặc biệt quan trọng với SaaS. Một ứng dụng có thể cung cấp tính năng chia sẻ tài liệu rất tiện lợi nhưng những tài nguyên liên quan, chẳng hạn nội dung nhúng hoặc liên kết phụ thuộc, có thể có cơ chế quyền riêng. Vì vậy, việc thu hồi một quyền ở lớp bên ngoài không nhất thiết có nghĩa là mọi tài nguyên liên quan đều tự động mất quyền truy cập.
>
> Và đây chính là điểm chúng ta cần ghi nhớ:
>
> **Bảo mật Cloud không chỉ là bảo vệ hạ tầng; đó còn là bài toán quản lý chính xác ai được làm gì trên tài nguyên nào.**
>
> Trong ba mô hình, **IaaS** đặt nhiều trách nhiệm trực tiếp lên khách hàng nhất ở tầng máy chủ. Vì vậy, ngay sau đây chúng ta sẽ tập trung vào câu hỏi:
>
> **Nếu chúng ta tự quản lý máy chủ ảo, cần làm gì để gia cố nó trước các rủi ro bảo mật?**
>
> Xin mời thầy cô và các bạn chuyển sang **Slide 13: 6 khuyến nghị bảo mật máy chủ ảo — VM Security Checklist**.”



# 📌 SLIDE 13: BẢO MẬT ỨNG DỤNG PAAS (PAAS APPLICATION SECURITY)

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. PaaS: Ai chịu trách nhiệm bảo mật?

**PaaS không loại bỏ trách nhiệm bảo mật — mà phân chia lại trách nhiệm.**

| CSP quản lý                        | Khách hàng quản lý                  |
| :--------------------------------- | :---------------------------------- |
| Hạ tầng & nền tảng dịch vụ         | Mã nguồn ứng dụng                   |
| Runtime thuộc phạm vi dịch vụ      | Dữ liệu & cấu hình ứng dụng         |
| Vá lỗi / bảo vệ nền tảng           | Dependency & thư viện ứng dụng      |
| Tính sẵn sàng của dịch vụ theo SLA | Quyền truy cập & tài khoản ứng dụng |

> ⚠️ **Ranh giới trách nhiệm phụ thuộc vào dịch vụ PaaS cụ thể và cấu hình triển khai.**

---

### 2. Ba vùng cần kiểm soát

#### 🏢 CSP — Platform Security

* Bảo vệ **hạ tầng, nền tảng và runtime** thuộc phạm vi dịch vụ.
* Quản lý các thành phần nền tảng, bản vá và cô lập workload theo kiến trúc dịch vụ.

#### 👨‍💻 Customer — Application Security

* Bảo vệ **mã nguồn, dữ liệu và cấu hình ứng dụng**.
* Kiểm soát dependency, secret, cấu hình bảo mật và quyền truy cập.

#### 🔗 Third-party Dependencies

* Ứng dụng có thể phụ thuộc vào **API, thư viện hoặc dịch vụ bên ngoài**.
* Một thành phần yếu có thể trở thành **điểm xâm nhập vào chuỗi ứng dụng**.
* Cần kiểm kê, đánh giá và cập nhật dependency định kỳ.

---

### 3. Secure PaaS = Kiểm soát đúng ranh giới

```text
       CSP
        ↓
Infrastructure → Platform → Runtime
                         ↓
                    Application
                         ↓
                 Data & Identity
                         ↓
              3rd-party Dependencies
```

**Khách hàng cần xác định rõ:**

> **“Thành phần nào do CSP quản lý — thành phần nào do mình quản lý — thành phần nào phụ thuộc bên thứ ba?”**

### 🎯 KEY TAKEAWAY

> **PaaS giảm gánh nặng quản trị hạ tầng, nhưng không làm ứng dụng tự động an toàn.**

**CSP bảo vệ nền tảng → Khách hàng bảo vệ ứng dụng & dữ liệu → Các dependency phải được kiểm soát.**

---

## 🎙️ SPEAKER NOTES

> “Ở các slide trước, chúng ta đã thấy một nguyên tắc quan trọng của Cloud Security: **trách nhiệm bảo mật không giống nhau ở mọi mô hình dịch vụ**.
>
> Với PaaS, nhà cung cấp đã quản lý một phần rất lớn bên dưới ứng dụng. Chúng ta không còn phải trực tiếp quản lý toàn bộ máy chủ vật lý hay nhiều thành phần nền tảng như trong IaaS.
>
> Tuy nhiên, điều đó không có nghĩa là ứng dụng được bảo vệ hoàn toàn bởi CSP.
>
> Có thể hình dung trách nhiệm thành hai phía.
>
> **Phía thứ nhất là CSP.** Nhà cung cấp chịu trách nhiệm đối với hạ tầng, nền tảng và các thành phần runtime thuộc phạm vi của dịch vụ PaaS.
>
> **Phía thứ hai là khách hàng.** Chúng ta vẫn phải bảo vệ mã nguồn, dữ liệu, cấu hình ứng dụng và những thành phần mà mình trực tiếp đưa vào hoặc kiểm soát.
>
> Ranh giới chính xác sẽ phụ thuộc vào dịch vụ PaaS cụ thể. Vì vậy, khi đánh giá một nền tảng, không nên chỉ hỏi ‘CSP có bảo mật hay không’, mà phải hỏi cụ thể hơn: **CSP bảo vệ đến lớp nào và khách hàng còn phải bảo vệ những gì?**
>
> Một điểm rất đáng chú ý là **third-party dependencies**.
>
> Một ứng dụng PaaS hiếm khi hoạt động hoàn toàn độc lập. Nó có thể sử dụng thư viện mã nguồn mở, gọi API của bên thứ ba hoặc phụ thuộc vào một dịch vụ bên ngoài.
>
> Vì vậy, nếu chỉ kiểm tra mã nguồn của ứng dụng mà bỏ qua dependency, chúng ta vẫn có thể bỏ sót một nguồn rủi ro quan trọng.
>
> Do đó, khi xây dựng ứng dụng trên PaaS, chúng ta cần nhìn toàn bộ chuỗi:
>
> **CSP bảo vệ nền tảng → khách hàng bảo vệ ứng dụng và dữ liệu → các dependency bên ngoài cũng phải được kiểm soát.**
>
> Đây chính là ý nghĩa của việc xác định rõ **security boundary** — ranh giới trách nhiệm bảo mật.
>
> Và từ đây, chúng ta sẽ đi đến một câu hỏi cụ thể hơn:
>
> **Nếu ứng dụng đã nằm trên nền tảng Cloud, vậy ai được phép truy cập ứng dụng và chúng ta kiểm soát quyền đó như thế nào?**
>
> Đó chính là nội dung của slide tiếp theo: **IAM và SSO — quản lý danh tính và kiểm soát truy cập.**”





# 📌 SLIDE 14: ĐỊNH DANH VÀ QUẢN LÝ TRUY CẬP (IAM & SSO)

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Từ “Vị trí mạng” → “Định danh”

🌐 **Cloud phân tán**

* Người dùng, thiết bị và ứng dụng có thể truy cập tài nguyên từ nhiều mạng và vị trí.
* IP, Port và Firewall vẫn quan trọng nhưng **không đủ để xác định quyền truy cập**.

🎯 **Identity-first Security**

> **“Bạn đang ở đâu?” → “Bạn là ai, được phép làm gì?”**

---

### 2. IAM — Nền tảng Kiểm soát Truy cập

**IAM (Identity & Access Management)** liên kết:

**Identity → Authentication → Authorization → Resource → Action**

| Thành phần            | Câu hỏi cần trả lời                  |
| :-------------------- | :----------------------------------- |
| 🔑 **Authentication** | Bạn là ai?                           |
| 🛡️ **Authorization** | Bạn được phép làm gì?                |
| 🎯 **Resource**       | Bạn được truy cập tài nguyên nào?    |
| 📋 **Logging**        | Hoạt động đó có được ghi nhận không? |

### Nguyên tắc cốt lõi

**MFA + Least Privilege + Role-based Access + Logging**

> **Xác thực thành công ≠ được phép làm mọi thứ.**

---

### 3. SSO — Xác thực tập trung

```text
User
  ↓
Identity Provider (IdP)
  ↓
Authentication + MFA
  ↓
Token / Session
  ↓
Ứng dụng liên kết
```

🟩 **Lợi ích**

* Giảm số lượng mật khẩu cần quản lý.
* Tập trung quản lý vòng đời tài khoản.
* Thu hồi quyền nhanh và nhất quán hơn.
* Có thể áp dụng chính sách xác thực và giám sát tập trung.

🟥 **Rủi ro cần kiểm soát**

* **Compromised Identity:** Tài khoản trung tâm bị chiếm quyền → nhiều dịch vụ có thể bị ảnh hưởng.
* **Stolen Session / Token:** Phiên hợp lệ bị đánh cắp → có thể truy cập mà không cần biết mật khẩu.
* **Over-privilege:** SSO không tự động đảm bảo quyền tối thiểu.

### 🎯 Kiểm soát

**MFA → Least Privilege → Session Control → Monitoring**

---

## 🔑 KEY TAKEAWAY

> **IAM không chỉ trả lời “Ai đăng nhập?” mà còn phải trả lời:**
>
> **“Được làm gì, trên tài nguyên nào và hoạt động đó có được ghi nhận hay không?”**

---

## 🎙️ SPEAKER NOTES

> “Ở Slide 13, chúng ta đã xác định được một nguyên tắc: trong PaaS, CSP bảo vệ phần nền tảng thuộc phạm vi dịch vụ, còn khách hàng vẫn phải bảo vệ ứng dụng, dữ liệu và các thành phần mình kiểm soát.
>
> Nhưng khi đã có một ứng dụng và dữ liệu cần bảo vệ, chúng ta gặp một câu hỏi tiếp theo:
>
> **Ai được phép truy cập và họ được phép làm gì?**
>
> Đây chính là vấn đề của **Identity và Access Management — IAM**.
>
> Trong môi trường truyền thống, kiểm soát truy cập thường dựa khá nhiều vào vị trí mạng. Chúng ta có thể hỏi một thiết bị đang ở mạng nào, địa chỉ IP nào hoặc kết nối qua cổng nào.
>
> Tuy nhiên, Cloud làm cho ranh giới mạng trở nên linh hoạt hơn. Người dùng có thể truy cập tài nguyên từ nhiều địa điểm, thiết bị và mạng khác nhau.
>
> Điều đó không có nghĩa là firewall hay network security không còn quan trọng. Chúng vẫn là một lớp phòng thủ cần thiết. Nhưng chúng không thể tự mình trả lời câu hỏi: **người này có được phép thực hiện hành động này trên tài nguyên này hay không?**
>
> Vì vậy, chúng ta chuyển trọng tâm sang **Identity**.
>
> IAM có thể được nhìn như một chuỗi:
>
> **Identity → Authentication → Authorization → Resource → Action.**
>
> Đầu tiên, hệ thống phải xác minh người dùng là ai. Đây là **Authentication**.
>
> Sau đó, hệ thống phải xác định người đó được phép làm gì. Đây là **Authorization**.
>
> Và quan trọng hơn, quyền đó phải gắn với **tài nguyên cụ thể và hành động cụ thể**.
>
> Ví dụ, một người dùng có thể được phép đọc một tài liệu nhưng không được phép xóa tài liệu đó. Việc đăng nhập thành công không đồng nghĩa với việc người dùng có toàn quyền trên hệ thống.
>
> Đây chính là lý do chúng ta áp dụng **Least Privilege** — mỗi danh tính chỉ nên có những quyền cần thiết cho công việc.
>
> Bên cạnh đó, các hoạt động truy cập cần được ghi log để có thể kiểm toán và phát hiện hành vi bất thường.
>
> Một cơ chế thường được sử dụng để đơn giản hóa việc xác thực là **SSO — Single Sign-On**.
>
> Quy trình có thể hình dung rất đơn giản:
>
> **User → Identity Provider → Authentication và MFA → Token hoặc Session → Ứng dụng.**
>
> Người dùng xác thực với một hệ thống định danh trung tâm. Sau khi xác thực thành công, thông tin xác thực phù hợp được sử dụng để truy cập các ứng dụng đã liên kết.
>
> Điểm quan trọng là **SSO không có nghĩa tất cả ứng dụng phải lưu mật khẩu của người dùng**. Việc xác thực có thể được tập trung tại Identity Provider.
>
> SSO đem lại nhiều lợi ích: giảm số lượng mật khẩu, đơn giản hóa quản lý tài khoản và hỗ trợ thu hồi quyền tập trung.
>
> Nhưng SSO cũng tạo ra một vấn đề gọi là **blast radius**.
>
> Nếu một danh tính trung tâm bị chiếm quyền, nhiều ứng dụng liên kết có thể cùng bị ảnh hưởng. Ngoài ra, nếu session hoặc token hợp lệ bị đánh cắp, kẻ tấn công có thể sử dụng phiên đó mà không nhất thiết phải biết mật khẩu.
>
> Vì vậy, SSO không nên được hiểu là ‘đăng nhập một lần rồi tin tưởng tất cả’.
>
> Chúng ta cần kết hợp **MFA, Least Privilege, kiểm soát session và monitoring**.
>
> Như vậy, nếu Slide 13 trả lời câu hỏi:
>
> **‘PaaS: CSP và khách hàng chịu trách nhiệm bảo mật đến đâu?’**
>
> thì Slide 14 trả lời:
>
> **‘Ai được phép truy cập và chúng ta kiểm soát danh tính đó như thế nào?’**
>
> Nhưng IAM ở mức cơ bản vẫn chưa trả lời đầy đủ một câu hỏi rất quan trọng:
>
> **Một người đã được xác thực thì cụ thể họ được làm gì trên từng tài nguyên?**
>
> Đây chính là vấn đề của **Fine-grained Access Control**, và đó sẽ là nội dung trọng tâm của Slide 15.”




# 📌 SLIDE 15: BẢO MẬT SaaS & KIỂM SOÁT TRUY CẬP CHI TIẾT

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. SaaS thay đổi trách nhiệm bảo mật như thế nào?

| CSP / SaaS Provider       | Khách hàng            |
| ------------------------- | --------------------- |
| Ứng dụng & nền tảng       | 👤 User / Identity    |
| Hạ tầng & Database        | 🔐 Quyền truy cập     |
| Vá lỗi & vận hành dịch vụ | 📄 Dữ liệu & cấu hình |
| Bảo mật dịch vụ           | 📋 Kiểm soát sử dụng  |

> **CSP quản lý nhiều hơn → khách hàng ít kiểm soát hạ tầng hơn → IAM, dữ liệu và quyền truy cập trở nên đặc biệt quan trọng.**

**Khi đánh giá SaaS, cần xem xét:**
**Architecture → Secure Development → Security Testing → Release Management → Access Control**

---

### 2. Thách thức: Fine-grained Access Control

**Không chỉ hỏi:**

> “Ai được truy cập ứng dụng?”

**Mà phải hỏi:**

> **“Ai được làm gì, trên tài nguyên nào và trong điều kiện nào?”**

```text
IDENTITY
   ↓
RESOURCE
   ↓
ACTION
   ↓
CONDITION
```

Ví dụ:

* 👤 **Identity:** Nhân viên phòng Kế toán
* 📄 **Resource:** Báo cáo tài chính
* ✏️ **Action:** Xem / sửa / chia sẻ
* 🌐 **Condition:** Thiết bị hợp lệ / vị trí phù hợp / thời gian cho phép

→ Mục tiêu: **Least Privilege ở mức tài nguyên và hành động.**

---

### 3. Rủi ro khi quyền truy cập quá thô

⚠️ **Coarse-grained Access Control**

* Chỉ có các mức quyền đơn giản như **View / Edit / Share**.
* Khó giới hạn quyền theo **người dùng → tài nguyên → hành động → điều kiện**.
* Dễ phát sinh **over-privilege** và khó đáp ứng yêu cầu kiểm toán.

### 🔎 Ví dụ: Tài nguyên được chia sẻ / nhúng

Một tài liệu có thể tham chiếu hoặc nhúng các tài nguyên khác.

**Thu hồi quyền trên tài liệu chính**
≠
**Đảm bảo mọi quyền đối với tài nguyên liên quan đều đã bị thu hồi**

→ Cần kiểm tra **quyền của từng tài nguyên và quan hệ giữa các tài nguyên**.

---

### 🎯 KEY TAKEAWAY

> **Trong SaaS, kiểm soát truy cập không dừng ở “ai được vào”, mà phải xác định “ai được làm gì trên tài nguyên nào”.**

**Identity → Resource → Action → Condition**

→ **Least Privilege + Logging + Monitoring + Access Review**

---

## 🎙️ SPEAKER NOTES — SLIDE 15

“Sau khi đã tìm hiểu IAM và SSO ở slide trước, chúng ta chuyển sang mô hình có mức độ trừu tượng cao hơn: **SaaS — Software as a Service**.

Điểm quan trọng đầu tiên là trách nhiệm bảo mật đã thay đổi.

Trong SaaS, nhà cung cấp quản lý phần lớn hạ tầng phía dưới, nền tảng và bản thân ứng dụng. Vì vậy, khách hàng không còn trực tiếp quản lý máy chủ hay hệ điều hành như trong IaaS.

Điều đó không có nghĩa là khách hàng không còn trách nhiệm bảo mật.

Trọng tâm chuyển sang **danh tính người dùng, quyền truy cập, dữ liệu và cách dịch vụ được sử dụng**.

Vì vậy, khi đánh giá một dịch vụ SaaS, chúng ta không nên chỉ nhìn vào chức năng của sản phẩm. Cần quan tâm đến kiến trúc, quy trình phát triển an toàn, kiểm thử bảo mật và cách nhà cung cấp quản lý các bản phát hành.

Nhưng ở đây có một vấn đề quan trọng hơn liên quan trực tiếp đến những gì chúng ta vừa học ở Slide 14:

**IAM xác định người dùng là ai và họ có quyền gì. Nhưng trong SaaS, quyền đó có thể cần được kiểm soát đến mức rất chi tiết.**

Ví dụ, không chỉ hỏi một nhân viên có được sử dụng ứng dụng hay không.

Chúng ta cần hỏi:

**Người đó được truy cập tài nguyên nào? Được thực hiện hành động gì? Và trong điều kiện nào?**

Đó chính là tư duy **Fine-grained Access Control**.

Có thể mô hình hóa rất đơn giản:

**Identity → Resource → Action → Condition.**

Ví dụ, một nhân viên phòng Kế toán có thể được phép xem báo cáo tài chính, nhưng không nhất thiết được sửa hoặc chia sẻ báo cáo đó.

Thậm chí quyền này có thể còn phụ thuộc vào điều kiện như thiết bị, vị trí hoặc trạng thái xác thực.

Vấn đề là không phải dịch vụ SaaS nào cũng cung cấp mức độ kiểm soát chi tiết như vậy.

Một số hệ thống chỉ cung cấp những quyền tương đối thô như **View, Edit hoặc Share**. Khi đó, doanh nghiệp có thể gặp khó khăn trong việc áp dụng đầy đủ nguyên tắc **Least Privilege**.

Một tình huống khác cần chú ý là **tài nguyên được tham chiếu hoặc nhúng**.

Một tài liệu có thể sử dụng hoặc liên kết đến những tài nguyên khác. Khi đó, việc thu hồi quyền trên tài liệu chính không nên mặc định được hiểu là mọi quyền đối với các tài nguyên liên quan cũng đã được thu hồi.

Vì vậy, khi đánh giá quyền truy cập trong SaaS, chúng ta phải nhìn vào **từng tài nguyên và mối quan hệ giữa chúng**, thay vì chỉ kiểm tra quyền của ứng dụng ở mức tổng thể.

Điểm này nối trực tiếp với Slide 14.

Slide 14 tập trung vào câu hỏi:

**Ai là người dùng và họ được cấp quyền như thế nào?**

Còn Slide 15 đi thêm một bước:

**Quyền đó áp dụng lên tài nguyên nào và cho phép thực hiện hành động gì?**

Đó chính là sự chuyển từ **Identity Management** sang **Fine-grained Access Control**.

Và khi quyền truy cập đã được kiểm soát đến mức tài nguyên và hành động, chúng ta vẫn cần logging, monitoring và access review để phát hiện những quyền được cấp sai hoặc không còn cần thiết.

Như vậy, với SaaS, chúng ta không trực tiếp hardening máy chủ như IaaS. Nhưng chúng ta phải kiểm soát rất chặt **ai có quyền truy cập dữ liệu và họ có thể làm gì với dữ liệu đó**.

Đây cũng là điểm chúng ta sẽ chuyển sang lớp tiếp theo.

Nếu trong SaaS, phần lớn hạ tầng đã do nhà cung cấp quản lý, thì trong **IaaS**, khách hàng lại có quyền kiểm soát trực tiếp máy chủ ảo và hệ điều hành.

Vì vậy, câu hỏi tiếp theo sẽ là:

**Khi tự quản lý một Virtual Machine, chúng ta phải bảo mật nó từ đâu?**

Ở Slide 16, chúng ta sẽ đi vào **Virtual Machine Security Checklist — từ VM Image, credentials, firewall cho đến logging và auditing.**”




# 📌 SLIDE 16: BẢO MẬT MÁY CHỦ ẢO (VIRTUAL MACHINE SECURITY)

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. IaaS: Khi khách hàng trực tiếp quản lý VM

Trong IaaS, khách hàng thường chịu trách nhiệm đối với:

**VM → OS → Services → Accounts → Network Rules → Application**

⚠️ **Self-Provisioning** giúp tạo VM nhanh nhưng cũng dễ tạo ra:

* OS / Image chưa được gia cố
* Dịch vụ và cổng không cần thiết
* Credentials được lưu sai cách
* Quyền truy cập quá rộng
* Log không được thu thập tập trung

> 🎯 **Nguyên tắc:**
> **Secure-by-Default — VM phải bắt đầu từ một cấu hình an toàn, thay vì tạo trước rồi mới gia cố sau.**

---

### 2. VM Security Checklist — 6 lớp kiểm soát

|   #   | Kiểm soát                      | Cần làm gì?                                                                    |
| :---: | ------------------------------ | ------------------------------------------------------------------------------ |
| **1** | 🧱 **Hardened Image**          | Dùng **golden image** đã được kiểm tra; chỉ cài thành phần cần thiết           |
| **2** | 🔄 **Patch & Configuration**   | Vá OS / package; chuẩn hóa cấu hình và kiểm tra drift                          |
| **3** | 🔑 **Identity & Credentials**  | Không lưu secret trong image; MFA/SSH Key; **Least Privilege**; kiểm soát sudo |
| **4** | 🛡️ **Host Firewall**          | Chỉ mở **port cần thiết**; giới hạn nguồn truy cập; tắt dịch vụ không dùng     |
| **5** | 📋 **Logging & Auditing**      | Thu thập authentication, privilege, system events; gửi log về nơi tập trung    |
| **6** | 🔍 **Continuous Verification** | Vulnerability scanning, configuration assessment và kiểm tra định kỳ           |

---

### 3. Secure VM Lifecycle

```text
GOLDEN IMAGE
     ↓
SECURE CONFIGURATION
     ↓
CONTROLLED PROVISIONING
     ↓
LEAST-PRIVILEGE ACCESS
     ↓
MINIMAL ATTACK SURFACE
     ↓
CENTRALIZED LOGGING
     ↓
SCAN • PATCH • REVIEW
     ↺
```

> **VM Security ≠ một lần hardening**
> → Đây là **một quy trình liên tục từ tạo → vận hành → kiểm tra → gia cố**.

---

### 🎯 KEY TAKEAWAY

**Một VM an toàn cần đồng thời:**

**Hardened Image + Least Privilege + Minimal Ports + Patch + Logging + Continuous Verification**

> **Bảo mật VM bắt đầu trước khi VM được tạo và tiếp tục trong suốt vòng đời của nó.**

---

## 🎙️ SPEAKER NOTES — SLIDE 16

“Sau khi đã đi qua SaaS và vấn đề kiểm soát truy cập ở mức tài nguyên, chúng ta chuyển xuống lớp **IaaS — nơi khách hàng có quyền kiểm soát trực tiếp máy chủ ảo**.

Đây là điểm khác biệt rất quan trọng.

Trong SaaS, phần lớn hạ tầng được nhà cung cấp quản lý. Nhưng trong IaaS, khách hàng thường phải tự chịu trách nhiệm đối với **hệ điều hành, các dịch vụ chạy trên máy, tài khoản, cấu hình mạng và nhiều thiết lập bảo mật khác**.

Điều này tạo ra một vấn đề đặc trưng của Cloud: **Self-Provisioning**.

Một VM có thể được tạo ra rất nhanh. Nhưng nếu mỗi VM được tạo theo một cách khác nhau, chúng ta rất dễ có những máy chủ với cấu hình không đồng nhất: máy chưa được cập nhật, có dịch vụ không cần thiết, mở quá nhiều cổng hoặc chứa sẵn thông tin xác thực.

Vì vậy, nguyên tắc đầu tiên của Slide 16 là:

**Secure-by-Default.**

Thay vì tạo một VM rồi mới tìm cách bảo mật, chúng ta bắt đầu bằng một **Golden Image** hoặc một image chuẩn đã được kiểm tra và gia cố.

Từ đó, chúng ta có sáu nhóm kiểm soát.

**Thứ nhất là Hardened Image.**

Image nên chứa phiên bản OS và các thành phần cần thiết, đồng thời loại bỏ những dịch vụ không sử dụng. Việc chuẩn hóa image giúp các VM được tạo ra có cấu hình bảo mật nhất quán.

**Thứ hai là Patch và Configuration Management.**

Một image an toàn tại thời điểm triển khai không có nghĩa là nó sẽ luôn an toàn. OS và package tiếp tục xuất hiện lỗ hổng, trong khi cấu hình có thể thay đổi theo thời gian.

Vì vậy cần có quy trình cập nhật bản vá và kiểm tra **configuration drift** — tức là phát hiện khi cấu hình thực tế lệch khỏi baseline đã được phê duyệt.

**Thứ ba là Identity và Credentials.**

Không nên nhúng mật khẩu, private key hoặc các secret cố định vào VM image.

Thay vào đó, sử dụng các cơ chế quản lý định danh và secret phù hợp, cấp quyền theo nguyên tắc **Least Privilege**, đồng thời kiểm soát các tài khoản có quyền đặc biệt như sudo hoặc administrator.

Điểm quan trọng là: nếu một image được dùng để tạo hàng trăm VM, một credential bị nhúng trong image có thể trở thành một bí mật dùng chung trên rất nhiều máy.

**Thứ tư là Host Firewall.**

Mỗi VM không nên mặc định mở tất cả các cổng.

Chúng ta chỉ mở những port thực sự cần thiết cho dịch vụ và giới hạn nguồn truy cập nếu có thể.

Đồng thời, những service không sử dụng nên được tắt.

Mục tiêu là giảm **Attack Surface** — càng ít cửa vào không cần thiết thì càng giảm số điểm có thể bị khai thác.

**Thứ năm là Logging và Auditing.**

Chúng ta cần biết ai đã đăng nhập, có hoạt động nâng quyền hay không, hệ thống đã thay đổi những gì và có sự kiện bất thường nào xảy ra.

Quan trọng hơn, log không nên chỉ nằm trên chính VM.

Nếu VM bị xâm nhập và log chỉ được lưu cục bộ, kẻ tấn công có thể tìm cách sửa hoặc xóa log.

Vì vậy, các sự kiện quan trọng nên được chuyển tới hệ thống logging tập trung và được bảo vệ phù hợp.

**Thứ sáu là Continuous Verification.**

Đây là điểm giúp chúng ta tránh suy nghĩ rằng hardening chỉ là một thao tác thực hiện một lần.

VM cần được kiểm tra định kỳ bằng vulnerability scanning, configuration assessment và các cơ chế giám sát phù hợp.

Nếu phát hiện cấu hình lệch chuẩn hoặc lỗ hổng mới, chúng ta phải quay lại quá trình **patch và hardening**.

Vì vậy, toàn bộ vòng đời của VM có thể được nhìn như sau:

**Golden Image → Secure Configuration → Controlled Provisioning → Least Privilege → Minimal Attack Surface → Centralized Logging → Scan, Patch và Review.**

Điều quan trọng là chu trình này có tính lặp lại.

Một VM có thể an toàn khi được triển khai nhưng trở nên dễ bị tổn thương sau một thời gian nếu không được cập nhật và kiểm tra.

Do đó, thông điệp chính của Slide 16 là:

> **Bảo mật VM không phải là một thao tác hardening sau triển khai. Đó là một quy trình liên tục bắt đầu từ image và kéo dài trong toàn bộ vòng đời của VM.**

Như vậy, chúng ta đã đi qua các lớp từ **PaaS, IAM, SaaS đến IaaS và Virtual Machine Security**.

Ở slide cuối, chúng ta sẽ không tiếp tục đi sâu vào một công nghệ riêng lẻ nữa, mà sẽ **ghép các lớp này thành một mô hình bảo vệ thống nhất**.

Đó là **Security Controls và Defense-in-Depth** — từ phòng ngừa, phát hiện cho đến khắc phục và khôi phục.

Mời thầy cô và các bạn c




# 📌 SLIDE 17: SECURITY CONTROLS — PHÒNG NGỪA, PHÁT HIỆN & KHẮC PHỤC

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Security Controls là gì?

**Security Control** = biện pháp bảo vệ được thiết kế để:

> **Giảm khả năng xảy ra sự cố → Phát hiện khi sự cố xảy ra → Giảm tác động → Khôi phục an toàn**

Các control không hoạt động độc lập mà **bổ trợ cho nhau trong toàn bộ vòng đời sự cố**.

---

### 2. Bốn Nhóm Security Controls

|        Nhóm        | Mục tiêu                               | Ví dụ trong Cloud                              |
| :----------------: | -------------------------------------- | ---------------------------------------------- |
|  🛑 **Deterrent**  | Giảm ý định / hành vi vi phạm          | Security Policy, Warning, Legal Notice         |
| 🛡️ **Preventive** | Ngăn hoặc giảm khả năng xảy ra sự cố   | MFA, IAM, Encryption, Firewall, Hardening      |
|  🔍 **Detective**  | Phát hiện sự kiện / hành vi bất thường | Logging, Monitoring, IDS/IPS, Alerting         |
|  🔄 **Corrective** | Giảm tác động & khôi phục              | Incident Response, Isolation, Backup, Recovery |

> **Một hệ thống không chỉ cần “ngăn chặn” — mà phải có khả năng phát hiện và phục hồi khi phòng ngừa không đủ.**

---

### 3. Các Control phối hợp như thế nào?

```text
              SECURITY EVENT
                    │
                    ▼
🛑 DETERRENT ──► 🛡️ PREVENTIVE
                       │
                 Nếu sự cố xảy ra
                       ▼
                  🔍 DETECTIVE
                       │
                 Xác định / cảnh báo
                       ▼
                  🔄 CORRECTIVE
                       │
                Cô lập → Khắc phục
                       │
                       ▼
                   RECOVERY
```

### Ví dụ: Tài khoản Cloud bị chiếm quyền

**Preventive**
→ MFA + Least Privilege

**Detective**
→ Phát hiện đăng nhập bất thường + Logging

**Corrective**
→ Thu hồi session/token → Khóa tài khoản → Reset credential

**Recovery**
→ Khôi phục cấu hình / dữ liệu nếu bị thay đổi

---

### 🎯 KEY TAKEAWAY

> **Security Controls không chỉ nhằm ngăn tấn công.**
>
> **Mục tiêu là xây dựng một chuỗi kiểm soát liên tục:**
>
> **Deterrent → Preventive → Detective → Corrective**

**Không có control đơn lẻ nào bảo vệ toàn bộ hệ thống.**

---

## 🎙️ SPEAKER NOTES — SLIDE 17

“Kính thưa thầy cô và các bạn,

Sau khi đã đi qua các lớp bảo mật cụ thể — từ dữ liệu, IAM, mạng, ứng dụng cho đến máy chủ ảo — chúng ta cần một cách để **phân loại và nhìn nhận các biện pháp bảo mật này một cách có hệ thống**.

Đó là vai trò của **Security Controls**.

Security Control có thể hiểu đơn giản là một biện pháp được thiết kế để giảm rủi ro bảo mật.

Điểm quan trọng là một hệ thống không thể chỉ dựa vào các cơ chế phòng ngừa.

Chúng ta có thể triển khai MFA, firewall, encryption, hardening và rất nhiều biện pháp khác. Nhưng không có biện pháp nào đảm bảo rằng mọi sự cố đều bị ngăn chặn tuyệt đối.

Vì vậy, chúng ta cần nhìn Security Controls theo cả **trước, trong và sau sự cố**.

Ở đây chúng ta sử dụng bốn nhóm chính.

**Nhóm thứ nhất là Deterrent Controls — kiểm soát răn đe.**

Mục tiêu là làm giảm ý định hoặc hành vi vi phạm.

Ví dụ có thể là chính sách bảo mật, cảnh báo, quy định sử dụng hệ thống hoặc thông báo về các hậu quả khi vi phạm.

Nhóm này không trực tiếp ngăn một cuộc tấn công bằng kỹ thuật, nhưng nó tạo ra một lớp kiểm soát về mặt tổ chức và hành vi.

**Nhóm thứ hai là Preventive Controls — kiểm soát phòng ngừa.**

Đây là những cơ chế chúng ta đã gặp rất nhiều trong các slide trước.

Ví dụ như **MFA, IAM, mã hóa, firewall, network segmentation và hardening**.

Mục tiêu là ngăn sự cố xảy ra hoặc giảm khả năng một hành vi tấn công thành công.

Tuy nhiên, nếu một tài khoản vẫn bị chiếm quyền hoặc một lỗ hổng vẫn bị khai thác, chúng ta cần nhóm control tiếp theo.

**Nhóm thứ ba là Detective Controls — kiểm soát phát hiện.**

Ở đây chúng ta cần biết chuyện gì đang xảy ra.

Logging ghi lại sự kiện. Monitoring theo dõi hoạt động. IDS/IPS và các cơ chế cảnh báo có thể giúp nhận diện hành vi bất thường.

Ví dụ, nếu một tài khoản đột nhiên đăng nhập từ một vị trí bất thường hoặc thực hiện hàng loạt thao tác nhạy cảm, hệ thống có thể tạo cảnh báo để đội ngũ bảo mật điều tra.

Nhưng phát hiện thôi vẫn chưa đủ.

Sau khi xác định có sự cố, chúng ta cần **Corrective Controls — kiểm soát khắc phục**.

Ví dụ, chúng ta có thể cô lập máy chủ, thu hồi session hoặc token, khóa tài khoản, thay đổi credential, khôi phục cấu hình hoặc phục hồi dữ liệu từ backup.

Hãy lấy một tình huống đơn giản:

**Một tài khoản Cloud bị chiếm quyền.**

Preventive Control có thể đã yêu cầu **MFA và Least Privilege**.

Nhưng giả sử kẻ tấn công vẫn vượt qua được lớp này.

Detective Control sẽ giúp phát hiện những dấu hiệu như đăng nhập bất thường hoặc hành vi sử dụng tài nguyên khác thường.

Sau đó, Corrective Control có thể được kích hoạt: **thu hồi session, khóa tài khoản và reset credential**.

Nếu dữ liệu hoặc cấu hình đã bị thay đổi, chúng ta tiếp tục sử dụng các cơ chế **Recovery** để đưa hệ thống trở lại trạng thái an toàn.

Qua ví dụ này có thể thấy bốn nhóm control không thay thế nhau.

Chúng tạo thành một chuỗi:

**Deterrent → Preventive → Detective → Corrective.**

Và đây là điểm quan trọng nhất của Slide 17:

**Bảo mật không chỉ là ngăn tấn công.**

Một kiến trúc bảo mật trưởng thành phải giả định rằng một số biện pháp có thể bị vượt qua, từ đó chuẩn bị sẵn khả năng **phát hiện, giới hạn tác động và khôi phục**.

Đến đây, chúng ta đã có các loại Security Controls.

Nhưng vẫn còn một câu hỏi:

**Làm thế nào để kết hợp các control này với toàn bộ những lớp kỹ thuật mà chúng ta đã học — Cryptography, IAM, Network, Application, VM, Monitoring và Recovery?**

Đó sẽ là nội dung của **Slide 18**.

Ở slide cuối, chúng ta sẽ ghép tất cả thành một bức tranh thống nhất về **Defense-in-Depth — phòng thủ đa lớp**, đồng thời tổng kết lại những nguyên tắc quan trọng nhất của toàn bộ bài trình bày.

Mời thầy cô và các bạn cùng chuyển sang **Slide 18: Tổng kết — Kiến trúc Bảo mật Cloud & Defense-in-Depth**.”


# 📌 SLIDE 18: TỔNG KẾT — CLOUD SECURITY ARCHITECTURE & DEFENSE-IN-DEPTH

## 🖥️ NỘI DUNG HIỂN THỊ TRÊN SLIDE

### 1. Ghép các lớp thành một kiến trúc bảo mật

```text
                 CLOUD SECURITY
                       │
        ┌──────────────┴──────────────┐
        │                             │
 SHARED RESPONSIBILITY           RISK & CIA
        │                             │
        └──────────────┬──────────────┘
                       ↓
              ┌─────────────────┐
              │  DATA SECURITY  │
              │  Crypto + Access│
              └────────┬────────┘
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   🔐 CRYPTOGRAPHY    👤 IAM       🌐 NETWORK
   ABE · FHE · SE    Identity      Zones / FW
        │              │              │
        └──────────────┼──────────────┘
                       ↓
             APPLICATION & VM
              SaaS · PaaS · IaaS
                       ↓
              MONITORING & LOGGING
                       ↓
               RESPONSE & RECOVERY
                       ↓
              🛡️ DEFENSE-IN-DEPTH
```

> **Mỗi lớp giải quyết một nhóm rủi ro khác nhau; các lớp phối hợp để giảm khả năng một điểm yếu đơn lẻ dẫn đến sự cố trên toàn hệ thống.**

---

### 2. Ba nguyên tắc cần nhớ

#### 🤝 1. SHARED RESPONSIBILITY

**Cloud không loại bỏ trách nhiệm bảo mật — Cloud phân chia lại trách nhiệm.**

| Mô hình  | Khách hàng tập trung vào                   |
| -------- | ------------------------------------------ |
| **IaaS** | OS, VM, Network, Application, Data         |
| **PaaS** | Application, Data, Identity, Configuration |
| **SaaS** | Identity, Data, Access, Usage              |

> **Luôn xác định rõ: “Ai chịu trách nhiệm cho lớp nào?”**

---

#### 🔐 2. DATA SECURITY ≠ ENCRYPTION ONLY

Bảo vệ dữ liệu cần kết hợp:

**Confidentiality + Integrity + Availability**

với:

**Access Control + Privacy + Data Lifecycle + Metadata**

> **Mã hóa bảo vệ dữ liệu, nhưng quyền truy cập quyết định ai có thể sử dụng dữ liệu.**

---

#### 🛡️ 3. DEFENSE-IN-DEPTH

Không phụ thuộc vào một cơ chế duy nhất:

**Cryptography**
↓
**IAM & Least Privilege**
↓
**Network Segmentation**
↓
**Application / VM Security**
↓
**Monitoring & Detection**
↓
**Response & Recovery**

> **Một lớp bị vượt qua → các lớp còn lại tiếp tục giới hạn tác động.**

---

### 3. Điểm cần đặc biệt bảo vệ: CREDENTIALS & SECRETS

Cloud/DevOps tạo ra nhiều loại secret:

**API Keys · Passwords · Tokens · Certificates · SSH Keys · Service Accounts**

⚠️ Nếu quản lý kém:

**Leaked Secret**
→ **Unauthorized Access**
→ **Privilege Escalation**
→ **Lateral Movement**

### Nguyên tắc:

**Least Privilege → Secure Storage → Rotation → Monitoring → Revocation**

> 🔑 **Không chỉ bảo vệ tài nguyên Cloud — hãy bảo vệ cả những “chìa khóa” có quyền truy cập vào chúng.**

---

## 🎙️ SPEAKER NOTES — SLIDE 18

“Kính thưa thầy cô và các bạn,

Đến slide cuối cùng, chúng ta sẽ không nhìn từng công nghệ một cách riêng lẻ nữa, mà ghép tất cả những nội dung đã học thành **một kiến trúc bảo mật Cloud thống nhất**.

Nếu nhìn từ trên xuống, điểm đầu tiên là **Shared Responsibility**.

Đây là nền tảng để xác định trách nhiệm giữa Cloud Service Provider và khách hàng.

Khi sử dụng Cloud, chúng ta không thể chỉ hỏi:

**‘CSP có bảo mật hệ thống hay không?’**

Mà phải hỏi chính xác hơn:

**‘CSP chịu trách nhiệm đến lớp nào, và từ lớp nào trở đi khách hàng phải tự kiểm soát?’**

Với **IaaS**, khách hàng có quyền kiểm soát nhiều hơn đối với VM, hệ điều hành, network và application.

Với **PaaS**, CSP quản lý nhiều thành phần nền tảng hơn, còn khách hàng tập trung nhiều hơn vào application, data, identity và configuration.

Với **SaaS**, nhà cung cấp quản lý phần lớn stack phía dưới, nên trọng tâm của khách hàng chuyển mạnh sang identity, dữ liệu, quyền truy cập và cách dịch vụ được sử dụng.

Sau Shared Responsibility là mục tiêu bảo mật **CIA**:

**Confidentiality — Integrity — Availability.**

Đây là ba mục tiêu xuyên suốt toàn bộ kiến trúc.

Để bảo vệ dữ liệu, chúng ta sử dụng nhiều lớp khác nhau.

**Cryptography** cung cấp các cơ chế bảo vệ dữ liệu, trong đó chúng ta đã tìm hiểu những kỹ thuật như **ABE, FHE và Searchable Encryption**.

Nhưng cryptography không thể tự giải quyết toàn bộ bài toán.

Chúng ta còn cần **IAM** để xác định ai được truy cập và được phép thực hiện hành động gì.

**Network Security** giúp phân đoạn môi trường, giới hạn luồng truy cập và giảm phạm vi ảnh hưởng khi xảy ra sự cố.

Tiếp theo là **Application và VM Security**.

Ở lớp ứng dụng, chúng ta đã thấy sự khác nhau giữa SaaS, PaaS và IaaS, cũng như tầm quan trọng của fine-grained access control.

Ở lớp VM, chúng ta có secure image, patching, firewall, least privilege và centralized logging.

Nhưng ngay cả những lớp phòng ngừa này cũng không thể đảm bảo rằng mọi sự cố đều được ngăn chặn.

Vì vậy, chúng ta cần **Monitoring, Detection, Response và Recovery**.

Đây chính là tư tưởng của **Defense-in-Depth — phòng thủ đa lớp**.

Mỗi lớp giải quyết một nhóm rủi ro khác nhau.

Nếu một lớp bị vượt qua, các lớp còn lại vẫn phải tiếp tục hoạt động để **giới hạn quyền truy cập, giảm phạm vi ảnh hưởng, phát hiện hành vi bất thường và hỗ trợ khôi phục hệ thống**.

Từ toàn bộ bài trình bày, chúng ta có thể giữ lại ba nguyên tắc lớn.

**Thứ nhất: Shared Responsibility.**

Cloud không loại bỏ trách nhiệm bảo mật. Cloud **phân chia lại trách nhiệm**.

Vì vậy, trước khi triển khai một dịch vụ, chúng ta cần xác định rõ:

**CSP chịu trách nhiệm gì? Khách hàng chịu trách nhiệm gì?**

**Thứ hai: Data Security không chỉ là Encryption.**

Mã hóa rất quan trọng, nhưng bảo vệ dữ liệu còn bao gồm quyền truy cập, tính toàn vẹn, tính sẵn sàng, quyền riêng tư, vòng đời dữ liệu và cả metadata.

**Thứ ba: Security phải được xây dựng theo nhiều lớp.**

Cryptography, IAM, Network, Application, VM, Monitoring và Recovery không thay thế nhau.

Chúng bổ sung cho nhau để giảm khả năng một điểm yếu đơn lẻ dẫn đến việc toàn bộ hệ thống bị ảnh hưởng.

Và trước khi kết thúc, có một vấn đề đặc biệt đáng chú ý trong môi trường Cloud hiện đại:

**Credentials và Secrets.**

Một hệ thống Cloud không chỉ có tài khoản người dùng.

Chúng ta còn có **API key, password, access token, certificate, SSH key và service account**.

Số lượng secret có thể tăng rất nhanh khi doanh nghiệp sử dụng Cloud và DevOps.

Nếu một secret bị lộ và được cấp quá nhiều quyền, nó có thể trở thành điểm khởi đầu cho việc truy cập trái phép, leo thang đặc quyền và di chuyển ngang giữa các hệ thống.

Vì vậy, secrets cần được quản lý theo vòng đời:

**Least Privilege → Secure Storage → Rotation → Monitoring → Revocation.**

Và đây cũng là thông điệp cuối cùng của toàn bộ bài trình bày:

> **Đừng chỉ bảo vệ hạ tầng Cloud — hãy bảo vệ cả những “chìa khóa” có quyền truy cập vào nó.**

Nếu chúng ta phải tóm tắt toàn bộ bài học trong một chuỗi, có thể nhớ:

**Xác định trách nhiệm → Bảo vệ dữ liệu → Kiểm soát danh tính → Phân đoạn mạng → Gia cố ứng dụng và hạ tầng → Giám sát → Phản ứng → Khôi phục.**

Đó chính là tư duy **Defense-in-Depth**.

Em xin chân thành cảm ơn thầy cô và các bạn đã lắng nghe.

**Sau đây, em xin mời thầy cô và các bạn đặt câu hỏi và cùng thảo luận.**”
