"""Generate a translation from an explicitly selected, external private config."""
import argparse
from pathlib import Path
import sys

import format_date
import model
from local_config import create_configuration, read_private_configuration
from report_translator import save_english_report, translate_to_english


def read_configuration(path):
    config = read_private_configuration(path)
    pdf_template = model.PdfTemplate(
        template_path=config["template_path"],
        date_of_renewal=format_date.get_renewal_date(config["date_of_renewal"]),
        date_of_expiry=format_date.get_expiry_date(config["date_of_renewal"]),
        qr_code=config["qr_code"], certificate_photo=config["certificate_photo"],
        verification_code=config["verification_code"],
    )
    info = model.PersonalInformation(
        name=translate_to_english(config["name"]).upper(),
        sex=translate_to_english(config["sex"]),
        ethnic_background=translate_to_english(config["ethnic_background"]),
        date_of_birth=format_date.format_date(config["date_of_birth"]),
        higher_education_institution=translate_to_english(config["higher_education_institution"]),
        education_level=translate_to_english(config["education_level"]),
        major=translate_to_english(config["major"]),
        length_of_program=translate_to_english(config["length_of_program"]),
        type_of_education=translate_to_english(config["type_of_education"]),
        form_of_learning=translate_to_english(config["form_of_learning"]),
        start_date=format_date.format_date(config["start_date"]),
        status_of_student_record=translate_to_english(config["status_of_student_record"]),
        anticipated_graduation_date=format_date.format_date(config["anticipated_graduation_date"]),
    )
    return config["output_file_path"], pdf_template, info


def cli(argv=None):
    parser = argparse.ArgumentParser(description="本地学籍报告翻译工具；个人材料必须保存在仓库外。")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--config", help="仓库外的个人 YAML 配置")
    mode.add_argument("--init-config", metavar="PATH", help="在仓库外创建空白配置")
    args = parser.parse_args(argv)
    try:
        if args.init_config:
            create_configuration(args.init_config)
            print("已创建空白配置。请在本地填写，勿提交到代码仓库。")
        else:
            output, template, info = read_configuration(args.config)
            Path(output).parent.mkdir(parents=True, exist_ok=True)
            save_english_report(output, template, info)
            print("英文翻译件已生成，请在本地核对。")
    except Exception:
        # Do not echo private values, file contents or tracebacks into logs.
        print("操作失败。请检查配置完整性、日期格式、英文内容及仓库外的输入输出路径。", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
