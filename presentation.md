### KỊCH BẢN THUYẾT TRÌNH: BẢO MẬT ĐÁM MÂY (CLOUD SECURITY)

---

#### 📌 **[Slide 1: Tổng quan về Bảo mật Đám mây]**

Xin chào thầy và các anh chị học viên, tiếp theo em xin trình bày về  đề tài **Bảo mật điện toán đám mây**. Đây là một lĩnh vực chuyên sâu thuộc bảo mật máy tính, bảo mật mạng và bảo mật dữ liệu.


Mục tiêu cốt lõi của bảo mật điện toán đám mây là duy trì và bảo vệ bộ ba thuộc tính **CIA: Tính bí mật (Confidentiality), Tính toàn vẹn (Integrity) và Tính sẵn sàng (Availability)** của dữ liệu cũng như hệ thống. 

Một điểm vô cùng quan trọng cần lưu ý là trong môi trường đám mây, trách nhiệm bảo mật luôn được **chia sẻ giữa nhà cung cấp dịch vụ (CSP) và khách hàng**. Nhà cung cấp có nhiệm vụ bảo đảm an toàn cho hạ tầng và dịch vụ cung cấp, trong khi khách hàng chịu trách nhiệm quản lý người dùng, dữ liệu và áp dụng các biện pháp kiểm soát vận hành phù hợp.

---

#### 📌 **[Slide 2: Bảo mật dữ liệu & Siêu dữ liệu]**
**Lời nói:**
"Chuyển sang phần bảo mật dữ liệu, yếu tố đầu tiên chúng ta cần quan tâm là **dữ liệu đang truyền (data-in-transit)** qua mạng công cộng như Internet hoặc qua các mạng riêng nội bộ. Rủi ro lớn nhất đối với dữ liệu đang truyền không phải là việc có mã hóa hay không, mà là **không sử dụng thuật toán mã hóa đã được kiểm chứng**.

Bên cạnh bản thân dữ liệu, người dùng cần chú ý đặc biệt đến **siêu dữ liệu (metadata)** mà nhà cung cấp thu thập. Chúng ta phải đòi hỏi sự rõ ràng từ nhà cung cấp về **tính toàn vẹn, quyền riêng tư, vị trí lưu trữ vật lý và tính sẵn sàng của dữ liệu** kể cả khi xảy ra thảm họa."

---

#### 📌 **[Slide 3: Các kỹ thuật mã hóa nâng cao: ABE & SE]**
**Lời nói:**
"Để giải quyết các bài toán bảo mật phức tạp trên đám mây, các kỹ thuật mật mã hiện đại đã ra đời.

Đầu tiên là **Mã hóa dựa trên thuộc tính (ABE)**, gồm **CP-ABE** nơi bên mã hóa kiểm soát chính sách truy cập, và **KP-ABE** nơi khóa riêng được gắn với chính sách của người dùng. Trong mô hình ABE phi tập trung, các cơ quan thuộc tính có thể tham gia hoặc rời hệ thống linh hoạt mà không cần khởi động lại toàn bộ mạng.

Kỹ thuật tiếp theo là **Mã hóa có thể tìm kiếm (SE)**. Giải pháp này giúp người dùng thực hiện truy vấn an toàn trên dữ liệu đã mã hóa thông qua các chỉ mục từ khóa mà không làm phơi bày nội dung gốc."

---

#### 📌 **[Slide 4: Mã hóa đồng cấu toàn phần (FHE)]**
**Lời nói:**
"Một bước tiến đột phá khác chính là **Mã hóa đồng cấu toàn phần (FHE)** — công nghệ cho phép thực hiện các phép tính trực tiếp trên bản mã mà không cần giải mã dữ liệu.

Hệ thống FHE hoạt động nhờ sự phối hợp giữa ba bên: **Người dùng** giữ dữ liệu riêng tư, **Nút tính toán đồng cấu (HC)** chạy trên CPU/GPU để xử lý phép tính, và **Nút khởi tạo (Bootstrapping)** chạy trong vùng bao an toàn để giải mã trung gian và làm mới bản mã nhằm loại bỏ nhiễu. 

Ứng dụng thực tế tuyệt vời của FHE là cho phép thuê ngoài lưu trữ và tính toán dữ liệu nhạy cảm trong các ngành đòi hỏi bảo mật cao như **phân tích dự báo y tế**. Ví dụ: Doanh nghiệp B mã hóa tập dữ liệu VIDS gồm hai số 5 và 10 thành 10 và 20 rồi gửi lên đám mây; khi cần tính tổng, đám mây cộng ra 30 và gửi về, doanh nghiệp giải mã thu được kết quả 15 mà nhà cung cấp đám mây không hề biết dữ liệu gốc."

---

#### 📌 **[Slide 5: Bảo mật hạ tầng mạng & Vùng tin cậy]**
**Lời nói:**
"Về bảo mật hạ tầng, đối với **Đám mây riêng**, tô-pô mạng có nhiều điểm tương đồng với một **mạng Extranet an toàn**. Tuy nhiên, với **Đám mây công cộng**, tổ chức phải đối mặt với ba yếu tố rủi ro chính: dữ liệu bị phơi bày ra Internet, sự thiếu hụt khả năng kiểm toán thời gian thực, và sự phụ thuộc vào tính sẵn sàng của đường truyền.

Đặc biệt, **lỗi cấu hình sai (misconfiguration)** là rủi ro rất dễ xảy ra, điển hình như sự cố năm 2008 khi Pakistan Telecom công bố tuyến giả khiến YouTube bị ngắt kết nối trên toàn cầu trong hai giờ. 

Để bảo vệ hạ tầng trước các mối đe dọa dai dẳng (APT) hoặc kẻ nội gián, giải pháp **Vùng tin cậy (Trust Zones - TZ)** được triển khai bằng cách kết hợp phân đoạn mạng và quản lý danh tính truy cập (IAM)."

---

#### 📌 **[Slide 6: Bảo mật ứng dụng PaaS & SaaS]**
**Lời nói:**
"Đối với dịch vụ PaaS, công tác bảo mật tập trung vào **gia cố hệ điều hành máy chủ (host OS hardening)** — bao gồm dùng mật khẩu mạnh, tắt dịch vụ không cần thiết, bật tường lửa riêng và vá lỗi thường xuyên nhằm ngăn lỗ hổng từ máy chủ lan sang các máy ảo.

Cơ chế **Đăng nhập một lần (SSO)** giúp trải nghiệm thuận tiện và dùng được mật khẩu mạnh hơn, nhưng cũng có rủi ro là một khi kẻ tấn công vượt qua bước đăng nhập ban đầu, họ có thể tự do di chuyển trong tài nguyên mạng.

Đối với **SaaS**, nhà cung cấp quản lý toàn bộ ứng dụng nhưng khách hàng vẫn phải chịu trách nhiệm phân quyền người dùng. Lưu ý rằng trên đám mây, kiểm soát truy cập dựa trên mạng truyền thống đang suy giảm vai trò, nhường chỗ cho kiểm soát truy cập dựa trên người dùng và định danh."

---

#### 📌 **[Slide 7: An toàn máy chủ ảo & Các biện pháp kiểm soát]**
**Lời nói:**
"Khi quản lý các máy chủ ảo (VM), nguyên tắc bắt buộc là áp dụng **cấu hình an toàn theo mặc định**, cô lập khóa giải mã khỏi đám mây, chỉ mở các cổng tối thiểu và ghi nhật ký kiểm toán ra một máy chủ riêng biệt.

Để bảo vệ toàn diện, kiến trúc Bảo mật điện toán đám mây vận hành dựa trên **bốn biện pháp kiểm soát**:
1. **Răn đe (Deterrent controls):** Thông báo và cảnh báo nhằm làm giảm ý định tấn công.
2. **Phòng ngừa (Preventive controls):** Tăng cường xác thực mạnh để loại bỏ lỗ hổng.
3. **Phát hiện (Detective controls):** Giám sát mạng và phát hiện xâm nhập kịp thời.
4. **Khắc phục (Corrective controls):** Khôi phục bản sao lưu nhằm hạn chế thiệt hại sau sự cố."

---

#### 📌 **[Slide 8: Tổng kết & Thông điệp kết luận]**
**Lời nói:**
"Tóm lại, Bảo mật điện toán đám mây là sự kết hợp giữa **mô hình trách nhiệm chia sẻ** và việc duy trì bộ ba **CIA**. Các tổ chức không nên ỷ ỉa hoàn toàn vào bảo mật có sẵn của nhà cung cấp, bởi vì sự bùng nổ của các chứng thư và mật khẩu không được quản lý tốt có thể tạo điểm tựa cho kẻ tấn công xâm nhập theo chiều ngang vào các tài sản quan trọng nhất.

Cảm ơn thầy cô và các bạn đã chú ý lắng nghe! Sau đây xin mời thầy cô và các bạn cùng đặt câu hỏi và thảo luận."

---

📝 *Nếu bạn muốn mình hỗ trợ tạo một bài thuyết trình Slide Deck hoàn chỉnh hoặc bộ câu hỏi trắc nghiệm ôn tập từ nội dung này, hãy cho mình biết nhé!*