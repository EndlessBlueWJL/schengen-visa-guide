class PdfTemplate:
    def __init__(self, template_path, date_of_renewal=None, date_of_expiry=None, qr_code=None,
                 certificate_photo=None, verification_code=None) -> None:
        self.template_path = template_path
        self.date_of_renewal = date_of_renewal
        self.date_of_expiry = date_of_expiry
        self.qr_code = qr_code
        self.certificate_photo = certificate_photo
        self.verification_code = verification_code

    def __str__(self) -> str:
        return "<PdfTemplate: private fields redacted>"


# Personal Information
# class PersonalInformation:
#     def __init__(self, name, sex=None, id_number=None, ethnic_background=None, date_of_birth=None,
#                  higher_education_institution=None, education_level=None, major=None, form_of_learning=None,
#                  start_date=None, length_of_program=None, type_of_education=None, status_of_student_record=None,
#                  anticipated_graduation_date=None) -> None:
#         self.name = name
#         self.sex = sex
#         self.id_number = id_number
#         self.ethnic_background = ethnic_background
#         self.date_of_birth = date_of_birth
#         self.higher_education_institution = higher_education_institution
#         self.education_level = education_level
#         self.major = major
#         self.form_of_learning = form_of_learning
#         self.start_date = start_date
#         self.length_of_program = length_of_program
#         self.type_of_education = type_of_education
#         self.status_of_student_record = status_of_student_record
#         self.anticipated_graduation_date = anticipated_graduation_date

#     def __str__(self) -> str:
#         attribute_str = "\n".join(f"{key}: {value}" for key, value in vars(self).items())
#         return f"============ PersonalInformation ============ \n{attribute_str}"

class PersonalInformation:
    # 严格按照要求的顺序定义参数，移除 id_number
    def __init__(self, name, sex, date_of_birth, ethnic_background,
                 higher_education_institution, education_level, major,
                 length_of_program, type_of_education, form_of_learning,
                 start_date, status_of_student_record, anticipated_graduation_date):
        self.name = name
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.ethnic_background = ethnic_background
        self.higher_education_institution = higher_education_institution
        self.education_level = education_level
        self.major = major
        self.length_of_program = length_of_program
        self.type_of_education = type_of_education
        self.form_of_learning = form_of_learning
        self.start_date = start_date
        self.status_of_student_record = status_of_student_record
        self.anticipated_graduation_date = anticipated_graduation_date

    def __str__(self):
        return "<PersonalInformation: private fields redacted>"
