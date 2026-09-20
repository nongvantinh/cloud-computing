# CLOUD SECURITY

## Từ mô hình trách nhiệm đến các kỹ thuật bảo vệ dữ liệu, hạ tầng và ứng dụng

---

# PHẦN I — TẠI SAO CLOUD SECURITY LÀ MỘT BÀI TOÁN KHÁC?

### Slide 1 — Cloud Security là gì?

* Cloud Security là tập hợp công nghệ, chính sách và quy trình nhằm bảo vệ:

  * Dữ liệu
  * Ứng dụng
  * Hạ tầng
  * Danh tính người dùng
* Điểm khác biệt của cloud:

  * Tài nguyên được thuê ngoài
  * Hạ tầng có tính chia sẻ
  * Truy cập qua mạng
  * Quy mô thay đổi linh hoạt
* Vì vậy, bảo mật cloud không chỉ là “bảo mật máy chủ”.

**Thông điệp:** Khi đưa hệ thống lên cloud, mô hình bảo mật cũng thay đổi.

---

### Slide 2 — Ai chịu trách nhiệm bảo mật?

## Shared Responsibility Model

* CSP chịu trách nhiệm đối với phần hạ tầng/dịch vụ mà họ cung cấp.
* Khách hàng chịu trách nhiệm đối với những gì họ triển khai và cấu hình.
* Trách nhiệm thay đổi tùy IaaS, PaaS và SaaS.

**Đặt câu hỏi cho người nghe:**

> Nếu dữ liệu trên cloud bị lộ, lỗi thuộc về nhà cung cấp hay khách hàng?

→ Câu trả lời: **phụ thuộc vào lớp dịch vụ và phần trách nhiệm tương ứng.**

---

### Slide 3 — Bảo mật thực sự cần bảo vệ điều gì?

## CIA Triad

### Confidentiality

Ai được phép xem dữ liệu?

### Integrity

Dữ liệu có bị thay đổi trái phép không?

### Availability

Khi cần, hệ thống có hoạt động không?

Sau đó liên hệ với cloud:

> Cloud càng linh hoạt và phụ thuộc vào bên thứ ba, bài toán CIA càng trở nên phức tạp.

---

# PHẦN II — BẢO VỆ DỮ LIỆU TRÊN CLOUD

### Slide 4 — Dữ liệu trên Cloud đang ở đâu và đi đâu?

Đưa người nghe theo vòng đời dữ liệu:

**User → Network → Cloud Storage → Cloud Processing → User**

Từ đó xác định 3 trạng thái:

* **Data-in-transit** — dữ liệu đang truyền
* **Data-at-rest** — dữ liệu đang lưu trữ
* **Data-in-use** — dữ liệu đang được xử lý

Sau đó đặt vấn đề:

> Mỗi trạng thái cần một cách bảo vệ khác nhau.

---

### Slide 5 — Những vấn đề khi dữ liệu nằm trong tay CSP

Tập trung vào 4 vấn đề:

1. **Integrity** — dữ liệu có chính xác và nhất quán?
2. **Privacy** — ai có thể truy cập/chia sẻ dữ liệu?
3. **Data location** — dữ liệu thực sự được lưu ở đâu?
4. **Availability** — dữ liệu có luôn sẵn sàng không?

Bổ sung:

* Metadata cũng có thể tiết lộ thông tin.
* Dữ liệu có thể được lưu trên nhiều máy chủ/vị trí khác nhau.

**Thông điệp:**

> Không chỉ nội dung dữ liệu cần được bảo vệ; thông tin “xung quanh dữ liệu” cũng có giá trị.

---

### Slide 6 — Bảo vệ dữ liệu đang truyền

## Data-in-Transit Security

* Dữ liệu có thể đi qua:

  * Internet
  * Mạng riêng
  * Các kết nối giữa người dùng và cloud
* Các nguy cơ:

  * Nghe lén
  * Can thiệp
  * Giả mạo
* Giải pháp:

  * Mã hóa
  * Giao thức bảo mật đã được kiểm chứng
  * Xác thực đầu cuối

**Điểm nhấn:**

> Không phải “có mã hóa” là đủ; phải sử dụng cơ chế mã hóa phù hợp và đã được kiểm chứng.

---

# PHẦN III — KHI MÃ HÓA THÔNG THƯỜNG CHƯA ĐỦ

### Slide 7 — Bài toán lớn: Muốn Cloud xử lý dữ liệu nhưng không muốn Cloud biết dữ liệu

Đây là **slide chuyển tiếp quan trọng nhất của bài**.

Đặt tình huống:

> Tôi muốn thuê Cloud lưu trữ và tính toán trên dữ liệu của mình.
> Nhưng tôi không muốn CSP nhìn thấy dữ liệu gốc.

Nếu giải pháp truyền thống là:

**Encrypt → Upload → Decrypt → Process**

thì lúc xử lý dữ liệu phải xuất hiện dạng rõ.

→ Từ đây xuất hiện nhu cầu về **Advanced Cryptography**.

---

### Slide 8 — Ba kỹ thuật mật mã cho Cloud

Giới thiệu 3 kỹ thuật như 3 câu trả lời cho 3 nhu cầu khác nhau:

| Nhu cầu                                       | Kỹ thuật                  |
| --------------------------------------------- | ------------------------- |
| Ai được phép giải mã?                         | **ABE**                   |
| Có thể tính toán trên dữ liệu mã hóa?         | **FHE**                   |
| Có thể tìm kiếm dữ liệu mà không cần giải mã? | **Searchable Encryption** |

Đây là slide “bản đồ” cho toàn bộ phần mật mã.

---

### Slide 9 — ABE: Kiểm soát quyền truy cập bằng thuộc tính

## Attribute-Based Encryption

Ví dụ:

> Chỉ người có thuộc tính
> **“Doctor” + “Cardiology” + “Hospital A”**
> mới được đọc dữ liệu.

Giới thiệu:

* CP-ABE
* KP-ABE
* Cơ chế khớp thuộc tính
* Khi nào giải mã thành công?

Không cần quá sâu về toán học ở slide này.

---

### Slide 10 — KP-ABE phi tập trung: Khi hệ thống có nhiều cơ quan

Đi sâu hơn từ ABE:

* Global Setup
* Authority Setup
* Key Generation
* Encryption
* Decryption

Sau đó giới thiệu:

**Security Game / Selective-ID**

Mục đích:

> Làm thế nào chứng minh rằng một đối thủ không thể lấy được dữ liệu nếu không thỏa chính sách?

Đây là slide kỹ thuật nhất của ABE.

---

### Slide 11 — FHE: Tính toán mà không cần nhìn thấy dữ liệu

## Fully Homomorphic Encryption

Đây có thể là **slide “wow” của bài**.

Luồng:

**Dữ liệu gốc → Mã hóa → Cloud tính toán trên bản mã → Kết quả mã hóa → Giải mã**

Ví dụ đơn giản:

**5 × 2 = 10**

Thay vì gửi 5 và 2 cho Cloud:

**Enc(5), Enc(2)**

Cloud thực hiện phép toán trên bản mã.

→ Người dùng nhận kết quả mã hóa và giải mã.

---

### Slide 12 — FHE trong thực tế: Tính toán thuê ngoài

Dùng ví dụ của bạn:

**Dữ liệu:** 5, 10
↓
**Mã hóa**
↓
**Cloud xử lý**
↓
**Kết quả mã hóa tương ứng với 15**
↓
**Doanh nghiệp giải mã → 15**

Sau đó đưa ứng dụng:

### Healthcare

Bệnh viện/doanh nghiệp có thể thuê Cloud phân tích dữ liệu nhạy cảm mà hạn chế việc Cloud nhìn thấy dữ liệu gốc.

**Thông điệp:**

> FHE chuyển Cloud từ “nơi nhìn thấy dữ liệu” thành “nơi thực hiện phép tính trên dữ liệu”.

---

### Slide 13 — Searchable Encryption: Tìm kiếm mà không cần giải mã

Bài toán:

> Nếu toàn bộ dữ liệu đã mã hóa, làm sao Cloud tìm được tài liệu chứa từ khóa **“Urgent”**?

Searchable Encryption giải quyết vấn đề này thông qua:

* Searchable index
* Keyword
* Trapdoor/query
* Encrypted data

Ví dụ:

**Email chứa “Urgent” → hệ thống xác định tài liệu phù hợp → không cần công khai toàn bộ nội dung.**

---

# PHẦN IV — BẢO VỆ HẠ TẦNG CLOUD

### Slide 14 — Từ dữ liệu đến hạ tầng: Cloud được bảo vệ như thế nào?

Đưa người nghe “zoom out”:

**Data Security**
↓
**Network Security**
↓
**Identity & Access Management**
↓
**Host / VM Security**

Giới thiệu sự khác biệt:

### Private Cloud

* Môi trường kiểm soát chặt hơn
* Tô-pô mạng gần với mô hình mạng riêng/extranet

### Public Cloud

* Kết nối Internet
* Multi-tenancy
* Phụ thuộc nhiều hơn vào cấu hình và dịch vụ CSP

---

### Slide 15 — Trust Zones: Không tin tưởng mọi thứ mặc định

Các nguy cơ:

* APT
* Insider threat
* Truy cập trái phép
* Lateral movement

Giải pháp:

### Network Segmentation

Chia hệ thống thành các vùng.

### IAM

Xác định:

> **Ai được phép làm gì?**

### Trust Zone

Thiết lập ranh giới bảo vệ quanh tài nguyên quan trọng.

Có thể liên hệ sang tư duy:

> Không phải cứ ở “bên trong mạng” thì mặc nhiên đáng tin cậy.

---

# PHẦN V — BẢO MẬT ỨNG DỤNG VÀ MÁY CHỦ

### Slide 16 — IaaS, PaaS, SaaS: Trách nhiệm thay đổi như thế nào?

Làm một bảng duy nhất:

|                          | IaaS             | PaaS               | SaaS                        |
| ------------------------ | ---------------- | ------------------ | --------------------------- |
| CSP quản lý              | Hạ tầng          | Hạ tầng + nền tảng | Gần như toàn bộ ứng dụng    |
| Khách hàng tập trung vào | OS, network, app | App, data, access  | User, data, access          |
| Rủi ro tiêu biểu         | VM/configuration | Platform/access    | Permission/misconfiguration |

Đưa **WPS** vào đây như một **case study PaaS**, thay vì dành riêng một slide.

---

### Slide 17 — Từ Identity đến VM: Những điểm kiểm soát quan trọng

Chia thành 3 nhóm:

### Identity

* SSO
* Strong authentication
* Least privilege

### Application

* Access control
* Fine-grained permissions
* Host OS hardening

### Virtual Server

* Secure-by-default
* Kiểm tra VM images
* Không lưu private key trong cloud image
* Không để certificate/credential trong image
* Host firewall
* Centralized logging

Có thể trình bày 6 khuyến nghị VM dưới dạng **checklist** thay vì đọc từng dòng.

---

# PHẦN VI — TỔNG HỢP: BẢO MẬT CLOUD LÀ MỘT HỆ THỐNG NHIỀU LỚP

### Slide 18 — Defense in Depth: Từ phòng ngừa đến khắc phục

Kết hợp toàn bộ bài vào 4 nhóm controls:

**1. Deterrent**
↓
Cảnh báo, chính sách

**2. Preventive**
↓
Mã hóa, IAM, firewall, hardening

**3. Detective**
↓
Monitoring, logging, intrusion detection

**4. Corrective**
↓
Backup, recovery, incident response

---

### Slide 19 — Kết luận: Cloud Security không phải một công nghệ

Tổng kết bài bằng một sơ đồ:

**SHARED RESPONSIBILITY**
↓
**CIA**
↓
**DATA PROTECTION**
↓
**ADVANCED CRYPTOGRAPHY**
↓
**NETWORK & TRUST ZONES**
↓
**IAM & APPLICATION SECURITY**
↓
**VM & INFRASTRUCTURE SECURITY**
↓
**SECURITY CONTROLS**

### 3 thông điệp cuối cùng

**1.** Cloud không loại bỏ trách nhiệm bảo mật — nó **phân chia lại trách nhiệm**.

**2.** Bảo vệ dữ liệu không chỉ là mã hóa; cần kiểm soát **quyền truy cập, tính toàn vẹn, vị trí, tính riêng tư và khả năng xử lý an toàn**.

**3.** Cloud Security hiệu quả cần **nhiều lớp bảo vệ kết hợp**, từ cryptography và IAM đến network, application, monitoring và recovery.