# cn331-as2

## สมาชิก 
## 1.ชุติกาญจน์ กีดคำ 6610625011
## 2.ธนวรรณ ผ่องแผ้ว 6610685171
## ความสามารถของระบบ
- ระบบรับรองการเข้าสู่ระบบโดยแยกเป็น admin และ students
- admin สามารถจักการกับรายวิชาได้ผ่าน admin interface ของ django โดยรายวิชาประกอบด้วย รหัส ชื่อ ภาคการศึกษา ปีการศึกษา จำนวนที่นั่งที่รับได้ และสามารถกำหนดสถานะว่าเปิดหรือปิดรับการขอโควต้า นอกจากนี้ยังสามารถดูรายชื่อนักเรียนที่ขอโควต้าในแต่ละรายวิชาได้ สามารถให้สิทธิโควต้าได้โดยที่ student ไม่ได้ขอ สามารถลบคำขอโควต้าได้ อีกทั้งยังสามารถเพิ่มหรือลบ user ได้อีกด้วย
- student(userทั่วไป) สามารถเลือกดูรายวิชาที่เปิดให้ขอโควต้า และกดขอโควต้าได้หากยังมีที่ว่าง สามารถดูรายชื่อวิชาที่ขอได้สำเร็จ และสามารถยกเลิกการขอโควต้าได้ โดยในกรณีนี้จะมีที่ว่างให้คนอื่นสามารถลงเพิ่มได้
- ในหน้าcourses แสดงรายวิชาทั้งหมดที่มี สามารถเลือกดูเฉพาะภาคการศึกษาที่ต้องการได้ กดปุ่มenrollเพื่อขอโควต้ารายวิชานั้น ๆ เมื่อกดแล้ว ระบบจะถามว่าต้องการขอโควต้าวิชานั้น ๆ ใช่หรือไม่ เมื่อกดตกลง หน้าเว็บจะอยู่หน้าเดิม และจำนวนที่นั่งที่เปิดรับจะลดลง ส่วนในรายวิชาที่ทำการขอโควต้าไปแล้ว ปุ่มenrollจะเปลี่ยนเป็นข้อความว่า"ขอโควต้าแล้ว" และมีข้อความว่าขอโควต้าสำเร็จแสดงขึ้นมา ในกรณีที่จำนวนที่นั่ง=0 ปุ่มenrollจะเปลี่ยนเป็นข้อความว่า"เต็ม" และไม่สามารถกดได้ และหากในรายวิชานั้นไม่เปิดให้ขอโควต้า ปุ่มenrollจะเปลี่ยนเป็นข้อความว่า "รายวิชานี้ไม่เปิดให้ขอโควต้า" โดยผู้ใช้สามารถคลิกที่วิชาเพื่อดูรายละเอียดของแต่ละวิชาได้
- ในหน้าmycourse แสดงรายวิชาที่ลงทะเบียนเสร็จแล้วทั้งหมด โดยสามารถลบวิชานั้น ๆ ออกได้ โดยหลังจากกดลบ ระบบจะถามยืนยันว่าต้องการลบรายวิชานี้ใช่หรือไม่ หากกดตกลง วิชานั้นจะหายไปจากหน้า mycourse มีข้อความว่าลบสำเร็จแล้วโชว์ขึ้นมา และจำนวนที่นั่งที่เหลือจะเพิ่มขึ้น ส่วนในกรณีที่ยังไม่ได้ขอโควต้าวิชาใด ตารางจะแสดง "คุณยังไม่ได้ขอโควต้าในรายวิชาใด"
## คลิปการใช้งาน
> [Youtube](https://youtu.be/lWujDl7PQKg?si=AtTPa_kwv-FdTpGg)