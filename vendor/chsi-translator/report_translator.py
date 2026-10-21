import io

import PyPDF2
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from pathlib import Path

import model


# verify whether the value has Chinese
def is_contains_chinese(value: str):
    for _char in value:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


# Confirmed English fields only; no network translation
def translate_to_english(value: str) -> str:
    # Private fields never go to a remote translator or console logs.
    if is_contains_chinese(value):
        raise ValueError("请先在本地配置中填写确认过的英文内容。")
    return value


def save_english_report(output_file_path: str,
                        pdf_template: model.PdfTemplate,
                        personal_information: model.PersonalInformation) -> None:
    """
    生成英文版在线学籍验证报告 PDF
    :param output_file_path: 输出 PDF 文件路径
    :param pdf_template: 模板信息对象（包含模板路径、二维码、照片等）
    :param personal_information: 个人信息对象（已按顺序包含13个字段，无 id_number）
    """
    # ========== PDF 页面元素坐标（与原始模板匹配）==========
    time_x = 180
    time_y = 745.2
    personal_info_x = 180
    personal_info_y = 710.8
    line_height = 28          # 每行信息的垂直间距
    verification_code_x = 252
    verification_code_y = 203.5
    qr_code_x = 75
    qr_code_y = 156
    certificate_photo_x = 460
    certificate_photo_y = 615

    # ========== 注册字体（确保中英文显示正常）==========
    pdfmetrics.registerFont(TTFont("Roboto-Regular", str(Path(__file__).resolve().parent / "font" / "Roboto-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("Roboto-Medium", str(Path(__file__).resolve().parent / "font" / "Roboto-Medium.ttf")))

    # ========== 创建内存画布 ==========
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    # ---------- 1. 绘制日期行 ----------
    can.setFont("Roboto-Regular", 8.6)
    can.setFillColor("rgb(153, 153, 153)")
    time_str = f"Date of Renewal: {pdf_template.date_of_renewal}    Date of Expiry: {pdf_template.date_of_expiry}"
    can.drawString(time_x, time_y, time_str)

    # ---------- 2. 绘制个人信息（严格按照指定顺序）----------
    can.setFont("Roboto-Regular", 8.6)
    can.setFillColor("rgb(0, 0, 0)")

    # 定义字段的绘制顺序（与 PersonalInformation 类的初始化顺序完全一致）
    fields_order = [
        "name",                     # Name
        "sex",                      # Sex
        "date_of_birth",            # Date of Birth
        "ethnic_background",        # Ethnic Background
        "higher_education_institution",  # Higher Education Institution
        "education_level",          # Education Level
        "major",                    # Major
        "length_of_program",        # Length of Program
        "type_of_education",        # Type of Education
        "form_of_learning",         # Form of Learning
        "start_date",               # Start Date
        "status_of_student_record", # Status of Student Record
        "anticipated_graduation_date"  # Anticipated Graduation Date
    ]

    current_y = personal_info_y
    for field in fields_order:
        value = getattr(personal_information, field, "")
        # 如果值仍为中文，可在此调用翻译函数（通常已在外部预处理，此处直接绘制）
        can.drawString(personal_info_x, current_y, value)
        current_y -= line_height

    # ---------- 3. 绘制验证码 ----------
    can.setFont("Roboto-Medium", 10)
    can.setFillColor("rgb(0, 186, 199)")
    can.drawString(verification_code_x, verification_code_y, pdf_template.verification_code)

    # ---------- 4. 绘制二维码和学生照片 ----------
    can.drawImage(pdf_template.qr_code, qr_code_x, qr_code_y, 68, 68)
    can.drawImage(pdf_template.certificate_photo, certificate_photo_x, certificate_photo_y, 75.6, 100.8)

    can.save()

    # ========== 将画布内容合并到模板 PDF ==========
    # Remove covered sample records in memory; keep the source asset untouched.
    from template_cleaning import load_clean_template
    page = load_clean_template(pdf_template.template_path)
    packet.seek(0)
    page.merge_page(PyPDF2.PdfReader(packet).pages[0])

    # ========== 输出最终 PDF ==========
    output = PyPDF2.PdfWriter()
    output.add_page(page)
    with open(output_file_path, "wb") as f:
        output.write(f)