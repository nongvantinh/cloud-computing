# BẢO MẬT ĐÁM MÂY — BẢN RÚT GỌN 12 SLIDE (20–30 phút)

> Kịch bản nói giữ mạch dẫn dắt như `presentation.md` nhưng đã lược phần đi sâu và ví dụ dài.
> Bản đầy đủ 18 slide vẫn ở `presentation.md` + `Chapter11_Vietnamese_Presentation.pptx`.
> File trình chiếu: `Chapter11_Vietnamese_Presentation_Short.pptx` (build: `tools/build_short.py`, notes: `tools/short_notes.py`).
> File này được sinh tự động: `tools/export_short_md.py`.

| # | Slide | Số từ | Thời lượng |
|---|-------|-------|-----------|
| 1 | TIÊU ĐỀ | 121 | ~0:56 |
| 2 | MỤC LỤC | 170 | ~1:18 |
| 3 | NỀN TẢNG: TRÁCH NHIỆM & MỤC TIÊU BẢO MẬT | 317 | ~2:26 |
| 4 | BẢO VỆ DỮ LIỆU TRÊN CLOUD | 366 | ~2:49 |
| 5 | BA BÀI TOÁN — BA KỸ THUẬT | 221 | ~1:42 |
| 6 | ABE — MÃ HÓA DỰA TRÊN THUỘC TÍNH | 292 | ~2:15 |
| 7 | FHE — TÍNH TOÁN TRÊN DỮ LIỆU MÃ HÓA | 307 | ~2:22 |
| 8 | SE — TÌM KIẾM TRÊN DỮ LIỆU MÃ HÓA | 316 | ~2:26 |
| 9 | BẢO VỆ HẠ TẦNG & VÙNG TIN CẬY | 264 | ~2:02 |
| 10 | IaaS / PaaS / SaaS & QUẢN LÝ TRUY CẬP | 337 | ~2:36 |
| 11 | MÁY CHỦ ẢO & CÁC LỚP KIỂM SOÁT | 298 | ~2:18 |
| 12 | TỔNG KẾT | 241 | ~1:51 |

**Tổng: 3250 từ ≈ 25 phút nói** (nhịp 130 từ/phút) — cộng thời gian chuyển slide khoảng 25–27 phút.

---

## SLIDE 1 — TIÊU ĐỀ

**Trên slide:** Chương 11 · BẢO MẬT ĐÁM MÂY · Cloud Security — Trách nhiệm · Dữ liệu · Mật mã · Hạ tầng · Ứng dụng · Kiểm soát.

**Nói** (~0:56):

Em xin chào thầy cô và các bạn.

Bài trình bày hôm nay của em là Chương 11 — Bảo mật đám mây.

Khi đưa một hệ thống lên Cloud, chúng ta thường nghĩ ngay đến lợi ích: triển
khai nhanh, mở rộng linh hoạt, không phải đầu tư hạ tầng. Nhưng cùng với đó,
mô hình bảo mật cũng thay đổi — và đó là điều em muốn trình bày hôm nay.

Vì thời gian có hạn, em xin đi nhanh qua bức tranh tổng thể, tập trung vào ý
tưởng và cách tư duy; phần chi tiết kỹ thuật em xin trao đổi thêm ở phần hỏi
đáp.

Trước hết, em xin giới thiệu nội dung bài trình bày.

---

## SLIDE 2 — MỤC LỤC

**Trên slide:** 6 phần trong 2 hàng thẻ, mỗi phần 2 dòng ý.

**Nói** (~1:18):

Bài của em gồm sáu phần, đi theo một mạch từ khái quát đến cụ thể.

Phần một là nền tảng: bảo mật đám mây khác gì bảo mật truyền thống, ai chịu
trách nhiệm, và rốt cuộc chúng ta đang bảo vệ điều gì.

Phần hai thu hẹp lại vào đối tượng quan trọng nhất — dữ liệu.

Từ phần hai sẽ nảy ra một bài toán: làm sao để Cloud xử lý dữ liệu mà không
nhìn thấy dữ liệu. Đó là lý do có phần ba — ba kỹ thuật mật mã nâng cao: ABE,
FHE và Searchable Encryption. Đây là phần trọng tâm.

Phần bốn lùi lại một bước để nhìn rộng hơn: hạ tầng và vùng tin cậy.

Phần năm đi vào ứng dụng, danh tính và máy chủ ảo — những gì khách hàng trực
tiếp quản lý.

Và phần sáu tổng hợp thành các lớp kiểm soát, khép bài bằng tư duy phòng thủ
nhiều lớp.

Chúng ta bắt đầu với phần một.

---

## SLIDE 3 — NỀN TẢNG: TRÁCH NHIỆM & MỤC TIÊU BẢO MẬT

**Trên slide:** Shared Responsibility (CSP / Khách hàng / Dịch chuyển IaaS→PaaS→SaaS) + bộ ba CIA.

**Nói** (~2:26):

Để bắt đầu, chúng ta cần trả lời một câu hỏi rất cơ bản: bảo mật đám mây thực
chất là gì?

Hiểu đơn giản, đó là tập hợp các công nghệ, chính sách và quy trình nhằm bảo
vệ bốn thứ: dữ liệu, ứng dụng, hạ tầng, và danh tính cùng quyền truy cập.

Nhưng có một điểm khiến bài toán này khác hẳn mô hình truyền thống: chúng ta
không còn tự kiểm soát toàn bộ hạ tầng. Tài nguyên đi thuê, hạ tầng dùng
chung, và mọi truy cập đều qua mạng.

Từ đó xuất hiện khái niệm quan trọng nhất của Cloud: Shared Responsibility
Model — mô hình trách nhiệm chung. Có thể hiểu thành hai phía. Nhà cung cấp
chịu trách nhiệm với nền tảng họ cung cấp: trung tâm dữ liệu, phần cứng, mạng
lõi, lớp ảo hóa. Khách hàng chịu trách nhiệm với những gì mình triển khai lên
đó: dữ liệu, danh tính, quyền truy cập và cấu hình dịch vụ.

Ranh giới này không cố định: chuyển từ IaaS sang PaaS rồi SaaS, phần nhà cung
cấp lo tăng dần, phần khách hàng giảm đi — nhưng không bao giờ bằng không. Vì
vậy khi có sự cố, trước hết phải xác định nó nằm ở lớp nào.

Vậy dù ai chịu trách nhiệm, rốt cuộc chúng ta đang bảo vệ điều gì? Đó là bộ
ba CIA. Confidentiality — chỉ người được phép mới xem được dữ liệu. Integrity
— dữ liệu không bị thay đổi trái phép. Availability — khi người dùng hợp lệ
cần thì hệ thống phải sẵn sàng.

Ý cần nhớ ở phần này: Cloud không xóa bỏ trách nhiệm bảo mật, nó phân chia
lại trách nhiệm.

Vậy khi dữ liệu thực sự đi vào Cloud, nó phải đối mặt với những vấn đề gì?
Đó là nội dung phần tiếp theo.

---

## SLIDE 4 — BẢO VỆ DỮ LIỆU TRÊN CLOUD

**Trên slide:** Vòng đời dữ liệu (Người dùng → Đường truyền → Lưu trữ → Xử lý → Trả kết quả) + 3 trạng thái + 4 vấn đề cần kiểm soát.

**Nói** (~2:49):

Sau khi đã xác định trách nhiệm và mục tiêu, chúng ta nhìn vào đối tượng quan
trọng nhất: dữ liệu.

Dữ liệu trên Cloud không nằm yên một chỗ. Nó bắt đầu từ người dùng, đi qua
mạng, được lưu trữ, rồi được đưa vào xử lý và trả kết quả về. Nhìn theo vòng
đời đó, dữ liệu tồn tại ở ba trạng thái, mỗi trạng thái cần một cách bảo vệ
khác nhau.

Khi dữ liệu đang truyền, điều chúng ta quan tâm là nó có bị nghe lén hay giả
mạo không; cách xử lý là mã hóa đường truyền kết hợp xác thực hai đầu — và
một nguyên tắc đáng nhớ là không nên mặc định cứ mạng riêng là an toàn.

Khi dữ liệu đang được lưu trữ, vấn đề chuyển sang quyền truy cập và khả năng
mất dữ liệu — xử lý bằng mã hóa lưu trữ và quản lý khóa cho tốt.

Còn khi dữ liệu đang được xử lý, một vấn đề khó hơn xuất hiện: để xử lý thì
thông thường Cloud phải nhìn thấy dữ liệu. Em xin quay lại điểm này ngay sau
đây.

Ngoài ba trạng thái, khi dữ liệu nằm trong tay nhà cung cấp còn bốn vấn đề
cần kiểm soát: dữ liệu có còn toàn vẹn không, quyền riêng tư được bảo vệ thế
nào, dữ liệu thực sự đang được lưu ở đâu — điều này còn liên quan đến quy
định pháp lý của từng quốc gia — và khi cần thì có truy cập được không.

Một lớp thông tin nữa thường bị bỏ qua là metadata: ai truy cập, khi nào, tần
suất ra sao. Nghĩa là ngay cả khi nội dung đã mã hóa, thông tin xung quanh dữ
liệu vẫn có thể tiết lộ những điều có giá trị.

Đến đây, một bài toán thú vị hơn xuất hiện: nếu em muốn tận dụng khả năng
tính toán của Cloud, nhưng không muốn Cloud nhìn thấy dữ liệu gốc, thì phải
làm thế nào?

Đây chính là chỗ mã hóa truyền thống gặp giới hạn — và là nội dung phần ba.

---

## SLIDE 5 — BA BÀI TOÁN — BA KỸ THUẬT

**Trên slide:** Luồng “Mã hóa → Tải lên → Giải mã để xử lý → Cloud thấy dữ liệu gốc” + bảng ánh xạ câu hỏi ↔ kỹ thuật.

**Nói** (~1:42):

Chúng ta thử đặt lại bài toán vừa nêu cho thật rõ.

Cách làm truyền thống là: mã hóa dữ liệu ở máy mình, tải bản mã lên Cloud, và
khi cần xử lý thì giải mã ra rồi tính toán. Nhìn vào luồng này ta thấy ngay
điểm yếu: đến bước xử lý, dữ liệu vẫn phải hiện ra ở dạng rõ trên hệ thống
của nhà cung cấp. Mã hóa chỉ bảo vệ được lúc truyền và lúc lưu, còn lúc dùng
thì không.

Vậy bài toán đặt ra là: muốn Cloud xử lý dữ liệu, nhưng không muốn Cloud biết
dữ liệu.

Từ nhu cầu đó xuất hiện các kỹ thuật mật mã nâng cao. Em xin giới thiệu ba kỹ
thuật, và cách dễ nhớ nhất là xem chúng như ba câu trả lời cho ba câu hỏi
khác nhau.

Ai được phép giải mã? Trả lời bằng ABE — mã hóa dựa trên thuộc tính.

Có thể tính toán ngay trên dữ liệu đã mã hóa không? Trả lời bằng FHE — mã hóa
đồng cấu toàn phần.

Có thể tìm kiếm mà không cần giải mã không? Trả lời bằng Searchable
Encryption.

Slide này giống như một bản đồ. Ba slide tiếp theo em xin đi nhanh vào từng
kỹ thuật, bắt đầu với ABE.

---

## SLIDE 6 — ABE — MÃ HÓA DỰA TRÊN THUỘC TÍNH

**Trên slide:** 3 bước (Thuộc tính người dùng → Chính sách trên dữ liệu → Khớp thì giải mã) + CP-ABE / KP-ABE.

**Nói** (~2:15):

Kỹ thuật thứ nhất trả lời câu hỏi: ai được phép giải mã.

Với mã hóa thông thường, muốn cho ai đọc thì phải mã hóa riêng cho người đó.
Cách này ổn khi có vài người dùng, nhưng trong một tổ chức lớn, liên tục có
người vào người ra, thì quản lý khóa trở thành gánh nặng.

ABE tiếp cận theo hướng khác. Thay vì hỏi "mã hóa cho ai", nó hỏi "ai đủ điều
kiện thì được đọc". Dữ liệu được mã hóa kèm một chính sách truy cập — tức là
điều kiện phải thỏa mới đọc được. Mỗi người dùng được cấp một khóa gắn với
tập thuộc tính của mình, chẳng hạn vai trò, phòng ban, tổ chức. Khi giải mã,
hệ thống đối chiếu thuộc tính trong khóa với chính sách trong bản mã: thỏa
thì giải mã thành công, không thỏa thì không ra được gì.

Có hai mô hình chính. CP-ABE đặt chính sách ở bản mã, nghĩa là người mã hóa
quyết định ai được đọc dữ liệu của mình. KP-ABE thì ngược lại, đặt chính sách
ở khóa, nghĩa là cơ quan cấp khóa quyết định một người được đọc những loại dữ
liệu nào.

Điểm đáng giá nhất của ABE là quyền truy cập nằm ngay trong bản mã, chứ không
nằm ở phần mềm kiểm soát truy cập của máy chủ. Kể cả khi kẻ tấn công lấy được
bản mã, không có thuộc tính phù hợp thì vẫn không đọc được.

ABE đã giải quyết câu hỏi ai được đọc, nhưng chưa trả lời được câu hỏi khó
hơn: làm sao tính toán trên dữ liệu mà không cần nhìn thấy nó. Đó là kỹ thuật
tiếp theo.

---

## SLIDE 7 — FHE — TÍNH TOÁN TRÊN DỮ LIỆU MÃ HÓA

**Trên slide:** Luồng Mã hóa → Gửi lên Cloud → Tính trên bản mã → Kết quả mã hóa → Giải mã + Điểm đặc biệt / Đánh đổi.

**Nói** (~2:22):

Kỹ thuật thứ hai, theo em, là ý tưởng thú vị nhất của chương: FHE — mã hóa
đồng cấu toàn phần.

Ý tưởng như sau. Người dùng mã hóa dữ liệu ngay tại máy mình rồi gửi bản mã
lên Cloud. Cloud thực hiện phép toán trực tiếp trên bản mã — không giải mã,
và cũng không có khóa để giải mã. Kết quả tính ra vẫn đang ở dạng mã hóa; chỉ
người giữ khóa mới giải mã để lấy kết quả thật.

Điều đặc biệt là trong suốt quá trình đó, dữ liệu gốc không một lần nào xuất
hiện ở phía nhà cung cấp. Nói cách khác, FHE biến Cloud từ "nơi nhìn thấy dữ
liệu" thành "nơi chỉ thực hiện phép tính trên dữ liệu". Đây chính là lời giải
cho bài toán dữ liệu đang được xử lý mà em nêu ở phần hai.

Tất nhiên là có cái giá phải trả, ở hai điểm.

Thứ nhất là chi phí: tính toán trên bản mã chậm hơn rất nhiều so với tính
toán thông thường, nên chưa thể áp dụng đại trà.

Thứ hai là nhiễu. Mỗi bản mã mang theo một lượng nhiễu nhỏ, và mỗi phép toán
lại làm nhiễu tích lũy thêm; đến một ngưỡng nào đó thì không còn giải mã đúng
được nữa. Kỹ thuật xử lý việc này gọi là bootstrapping — hiểu đơn giản là làm
sạch bớt nhiễu để có thể tiếp tục tính.

Vì vậy hiện nay FHE phù hợp nhất với những bài toán mà dữ liệu rất nhạy cảm
và việc giữ bí mật quan trọng hơn tốc độ.

Như vậy chúng ta đã có câu trả lời cho việc đọc và việc tính toán. Còn một
nhu cầu rất đời thường nữa chưa được giải quyết: tìm kiếm.

---

## SLIDE 8 — SE — TÌM KIẾM TRÊN DỮ LIỆU MÃ HÓA

**Trên slide:** Hai luồng song song — Khi tải lên (từ khóa → chỉ mục mã hóa) và Khi tìm kiếm (trapdoor → đối chiếu → trả tài liệu).

**Nói** (~2:26):

Kỹ thuật thứ ba xuất phát từ một tình huống rất thực tế.

Giả sử em đã mã hóa toàn bộ dữ liệu trước khi đưa lên Cloud. Về bảo mật thì
rất tốt, nhưng Cloud không tìm kiếm được nữa, vì với nó tất cả chỉ là dữ liệu
vô nghĩa; muốn tìm một tài liệu thì phải tải cả kho về giải mã hết — không
khả thi.

Searchable Encryption giải quyết bằng cách tách việc tìm kiếm ra khỏi việc
đọc nội dung, chia thành hai giai đoạn.

Giai đoạn thứ nhất là khi tải dữ liệu lên. Ngoài việc mã hóa tài liệu, hệ
thống còn rút ra các từ khóa và xây dựng một chỉ mục tìm kiếm — bản thân chỉ
mục này cũng được mã hóa. Cả hai cùng được lưu trên Cloud.

Giai đoạn thứ hai là khi tìm kiếm. Người dùng không gửi từ khóa ở dạng rõ, mà
sinh ra một trapdoor — có thể hiểu là truy vấn đã được mã hóa. Cloud dùng
trapdoor đối chiếu với chỉ mục, xác định tài liệu nào khớp và trả về đúng
những tài liệu đó, mà không đọc được nội dung và cũng không biết từ khóa thực
sự là gì.

Em xin lưu ý một điểm: kỹ thuật này vẫn để lộ thông tin gián tiếp — chẳng hạn
những tài liệu nào hay được trả về cùng nhau. Người ta gọi đó là rò rỉ mẫu
truy cập, và đây vẫn là hướng đang được nghiên cứu cải tiến.

Tóm lại phần ba: ba kỹ thuật trả lời ba câu hỏi — ABE là ai được đọc, FHE là
tính toán thế nào, SE là tìm kiếm ra sao.

Nhưng bảo vệ tốt dữ liệu thôi thì chưa đủ. Chúng ta hãy lùi lại một bước để
nhìn vào lớp bên dưới: hạ tầng.

---

## SLIDE 9 — BẢO VỆ HẠ TẦNG & VÙNG TIN CẬY

**Trên slide:** 4 lớp (Dữ liệu → Mạng → Danh tính → Máy chủ/VM) + Private vs Public Cloud + nguy cơ điển hình.

**Nói** (~2:02):

Đến đây em xin chuyển từ dữ liệu sang hạ tầng.

Nhìn tổng thể, bảo mật Cloud xếp thành nhiều lớp đồng tâm. Trong cùng là dữ
liệu, bao quanh là mạng, tiếp đến là quản lý danh tính và truy cập, ngoài
cùng là máy chủ và máy ảo. Cách nhìn này có ích, vì mỗi lớp là một cơ hội để
phát hiện và chặn kẻ tấn công: vượt qua được lớp này chưa có nghĩa là vào
được lớp trong.

Bối cảnh triển khai cũng ảnh hưởng nhiều. Private Cloud là môi trường kiểm
soát chặt hơn, gần với mô hình mạng nội bộ quen thuộc. Còn Public Cloud thì
kết nối Internet, nhiều khách hàng dùng chung hạ tầng, và phụ thuộc rất nhiều
vào việc chúng ta cấu hình có đúng hay không.

Những nguy cơ điển hình ở lớp này gồm: tấn công có chủ đích kéo dài; mối đe
dọa từ chính người bên trong; truy cập trái phép; và di chuyển ngang — tức là
chiếm được một máy rồi lần sang các máy khác trong cùng mạng.

Cách xử lý gồm ba việc đi cùng nhau: chia mạng thành các phân đoạn để giới
hạn phạm vi thiệt hại; thiết lập vùng tin cậy quanh những tài nguyên quan
trọng nhất; và dùng IAM để quy định rõ ai được làm gì.

Tư duy cần nhớ: không phải cứ nằm bên trong mạng thì mặc nhiên đáng tin cậy.

Nói đến IAM, chúng ta sang phần năm: những gì khách hàng trực tiếp quản lý.

---

## SLIDE 10 — IaaS / PaaS / SaaS & QUẢN LÝ TRUY CẬP

**Trên slide:** Bảng 3 mô hình (CSP quản lý / Khách hàng lo / Rủi ro tiêu biểu) + 4 thẻ IAM.

**Nói** (~2:36):

Phần năm nói về ứng dụng và danh tính — và bảng này, theo em, là ý quan trọng
nhất của cả phần.

Ở phần một em có nói ranh giới trách nhiệm dịch chuyển theo mô hình dịch vụ.
Bảng này cho thấy cụ thể nó dịch chuyển như thế nào.

Với IaaS, nhà cung cấp chỉ lo hạ tầng; khách hàng tự lo hệ điều hành, mạng và
ứng dụng — rủi ro nằm ở cấu hình máy ảo. Với PaaS, nhà cung cấp lo thêm nền
tảng; khách hàng tập trung vào ứng dụng, dữ liệu và quyền truy cập.

Với SaaS, nhà cung cấp lo gần như toàn bộ; phần còn lại của khách hàng chủ
yếu là quản lý người dùng và phân quyền. Nghe thì ít việc nhất, nhưng thực tế
lại là nơi hay xảy ra sự cố nhất: chia sẻ dữ liệu nhầm ra bên ngoài, hoặc cấp
quyền rộng hơn mức cần thiết.

Nhìn ngang cả ba cột, ta thấy một điểm chung xuyên suốt: quản lý danh tính và
truy cập. Có bốn việc cần làm. Thứ nhất là SSO — đăng nhập một lần — để tập
trung việc xác thực, dễ kiểm soát và dễ thu hồi. Thứ hai là xác thực mạnh,
tức đa yếu tố, để một mật khẩu bị lộ không đủ để vào hệ thống. Thứ ba là đặc
quyền tối thiểu: chỉ cấp đúng quyền cần dùng và rà soát định kỳ. Thứ tư là
phân quyền chi tiết theo vai trò và theo tài nguyên.

Đi kèm là quản lý secrets — API key, token, chứng chỉ, khóa SSH: lưu trữ an
toàn, xoay vòng định kỳ và thu hồi được ngay khi nghi ngờ bị lộ.

Ý cần nhớ: trên Cloud, phần lớn sự cố không đến từ việc phá vỡ mã hóa, mà từ
cấu hình sai và quyền cấp thừa.

Còn một thành phần nữa khách hàng trực tiếp quản lý, đó là máy chủ ảo.

---

## SLIDE 11 — MÁY CHỦ ẢO & CÁC LỚP KIỂM SOÁT

**Trên slide:** 5 việc tối thiểu cho máy ảo + 4 nhóm kiểm soát.

**Nói** (~2:18):

Em xin nói nhanh hai nội dung cuối trước khi tổng kết.

Thứ nhất là máy chủ ảo. Đặc điểm của Cloud là máy ảo được tạo ra rất nhanh và
rất nhiều, nên một cấu hình sai cũng được nhân bản rất nhanh. Có năm việc tối
thiểu cần làm.

Một, cấu hình an toàn ngay từ mặc định, vì nhiều máy ảo tạo ra rồi để đó
không ai quay lại chỉnh. Hai, chỉ dùng image đã được kiểm tra, có nguồn gốc
rõ ràng. Ba, tuyệt đối không nhúng khóa riêng hay chứng chỉ vào image, vì
image có thể bị sao chép và khi đó khóa cũng đi theo. Bốn, bật firewall ngay
trên máy ảo chứ không chỉ dựa vào firewall lớp mạng — đúng tinh thần phòng
thủ nhiều lớp. Năm, đẩy log tập trung ra ngoài, để khi máy ảo bị xóa thì bằng
chứng vẫn còn.

Thứ hai là bức tranh tổng thể về kiểm soát bảo mật, gồm bốn nhóm, sắp theo
trình tự một sự cố diễn ra. Nhóm răn đe làm kẻ tấn công nản lòng ngay từ đầu.
Nhóm ngăn ngừa chặn tấn công xảy ra: mã hóa, IAM, firewall, hardening — phần
lớn những gì em trình bày nãy giờ nằm ở nhóm này. Nhóm phát hiện cho ta biết
có chuyện đang xảy ra: giám sát, log, phát hiện xâm nhập. Và nhóm khắc phục
đưa hệ thống trở lại bình thường: sao lưu, khôi phục, ứng phó sự cố.

Ý cần nhớ: không nhóm nào đủ một mình. Ngăn ngừa có thể bị vượt qua nên phải
có phát hiện; phát hiện rồi thì phải có khả năng khắc phục.

Và đó cũng là tinh thần để em khép lại bài trình bày.

---

## SLIDE 12 — TỔNG KẾT

**Trên slide:** Chuỗi Trách nhiệm → Dữ liệu → Mật mã → Mạng & Trust zone → IAM & Ứng dụng → Giám sát & Khôi phục + 3 thông điệp.

**Nói** (~1:51):

Em xin tổng kết lại toàn bộ bài.

Nếu phải gói tất cả vào một chuỗi, em xin đề xuất chuỗi này: xác định trách
nhiệm, bảo vệ dữ liệu, kiểm soát danh tính, phân đoạn mạng, gia cố ứng dụng
và hạ tầng, giám sát, rồi khôi phục. Đó chính là tư duy Defense in Depth —
phòng thủ nhiều lớp.

Và em xin nhấn mạnh ba thông điệp cuối cùng.

Thứ nhất, Cloud không loại bỏ trách nhiệm bảo mật, mà phân chia lại trách
nhiệm. Dù dùng IaaS, PaaS hay SaaS, phần của khách hàng luôn còn đó — chỉ là
nó nằm ở chỗ khác nhau.

Thứ hai, bảo vệ dữ liệu không chỉ là mã hóa. Còn phải kiểm soát ai được đọc,
dữ liệu có toàn vẹn không, đang lưu ở đâu, và có thể xử lý an toàn hay không.
Chính những câu hỏi đó dẫn tới ABE, FHE và Searchable Encryption ở phần ba.

Thứ ba, bảo mật Cloud hiệu quả không nằm ở một công nghệ duy nhất, mà ở nhiều
lớp kết hợp với nhau: từ mật mã và IAM đến mạng, ứng dụng, giám sát và khôi
phục.

Bài trình bày của em đến đây là kết thúc. Em xin chân thành cảm ơn thầy cô và
các bạn đã lắng nghe.

Sau đây em xin mời thầy cô và các bạn đặt câu hỏi và cùng thảo luận ạ.

---

## NỘI DUNG ĐÃ LƯỢC BỎ (giữ lại để phòng khi bị hỏi)

| Nội dung | Ở đâu trong bản đầy đủ |
|---|---|
| KP-ABE phi tập trung, 5 thành phần lược đồ, Security Game / Selective-ID | `presentation.md` — Slide 7 |
| FHE: kiến trúc 3 thành phần, chi tiết noise & bootstrapping | `presentation.md` — Slide 8 |
| FHE: ví dụ 5+10, ứng dụng phân tích dữ liệu y tế | `presentation.md` — Slide 9 |
| SE: hai hướng triển khai, ví dụ email “Urgent” | `presentation.md` — Slide 10 |
| Bảo mật ứng dụng PaaS chi tiết (WPS) | `presentation.md` — Slide 13 |
| SaaS & fine-grained access control chi tiết | `presentation.md` — Slide 15 |
| Vòng đời secrets đầy đủ | `presentation.md` — Slide 18 |
