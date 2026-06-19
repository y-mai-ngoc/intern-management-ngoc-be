import os
import django
from datetime import date
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from interns.models import Intern, LearningRecord, WeeklyTask

def seed_data():
    print("🧹 Đang làm sạch database (Xóa dữ liệu cũ)...")
    WeeklyTask.objects.all().delete()
    LearningRecord.objects.all().delete()
    Intern.objects.all().delete()

    print("Đang khởi tạo dữ liệu mẫu cho Thực tập sinh...")

    # ==========================================
    # DATA TEST 1: ALEX DONOVAN
    # ==========================================
    alex = Intern.objects.create(
        name="Alex Donovan",
        email="alex.d@example.com",
        university="Stanford University",
        major="Computer Science",
        company="Meta Platforms",
        photo="https://api.dicebear.com/7.x/avataaars/svg?seed=Alex",
        start_date=date(2025, 6, 22),
        mentor="Lead Mentor",
        status="Active"
    )
    LearningRecord.objects.create(
        intern=alex, 
        topic="UI Refactoring", 
        desc="Sửa giao diện Dashboard cho sạch đẹp và responsive theo chuẩn Figma.", 
        status="completed",
        date=date(2026, 6, 15)
    )
    LearningRecord.objects.create(
        intern=alex, 
        topic="State Management", 
        desc="Tìm hiểu và áp dụng Redux Toolkit hoặc Context API vào quản lý giỏ hàng.", 
        status="in_progress",
        date=date(2026, 6, 17)
    )
    WeeklyTask.objects.create(
        intern=alex, 
        name="Week 1: Setup project & UI Layout", 
        desc="Tạo cấu trúc thư mục Front-End và thiết kế Sidebar", 
        mon="8h", tue="8h", wed="7h", thu="8h", fri="6h",
        result="Đã hoàn thành layout cơ bản của Dashboard"
    )
    WeeklyTask.objects.create(
        intern=alex, 
        name="Week 1: Fix Bug Sidebar & Navbar", 
        desc="Sửa lỗi lệch icon và không hiển thị avatar", 
        mon="2h", tue="4h", wed="", thu="2h", fri="4h",
        result="Giao diện đã hiển thị chuẩn chỉnh"
    )
    ngoc = Intern.objects.create(
        name="Y Mai Ngoc",
        email="ngoc.ym@pnv.edu.vn",
        university="Passerelles Numériques Vietnam",
        major="Front-End Developer",
        company="Stitch Corporation",
        photo="https://api.dicebear.com/7.x/avataaars/svg?seed=Ngoc",
        start_date=date(2026, 4, 6),
        mentor="Lead Mentor",
        status="Active"
    )

    # Thêm Learning Records cho Ngoc
    LearningRecord.objects.create(
        intern=ngoc, 
        topic="React Native Fundamentals", 
        desc="Học cấu trúc thư mục, các component cơ bản View, Text, Image và StyleSheet.", 
        status="completed",
        date=date(2026, 4, 10)
    )
    LearningRecord.objects.create(
        intern=ngoc, 
        topic="Django REST Framework API", 
        desc="Kết nối ứng dụng React với Back-end Django qua API Axios.", 
        status="in_progress",
        date=date(2026, 6, 19)
    )
    WeeklyTask.objects.create(
        intern=ngoc, 
        name="Week 1: Phân tích thiết kế Database đồ án", 
        desc="Xác định các bảng cần thiết cho hệ thống FoodLink", 
        mon="8h", tue="8h", wed="8h", thu="8h", fri="8h",
        result="Đã chốt cấu trúc database 4 bảng với Mentor"
    )
    WeeklyTask.objects.create(
        intern=ngoc, 
        name="Week 2: Code giao diện trang chủ & Login", 
        desc="Thiết kế UI cho Mobile App", 
        mon="8h", tue="6h", wed="7h", thu="8h", fri="5h",
        result="Hoàn thành xong UI form Login"
    )

    print("Đã bơm dữ liệu mẫu khớp 100% với Model của bạn vào Database!")

if __name__ == '__main__':
    seed_data()