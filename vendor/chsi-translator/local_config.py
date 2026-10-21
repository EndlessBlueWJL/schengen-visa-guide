"""Local-only configuration. Private inputs and outputs stay outside the checkout."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent
EXAMPLE = ROOT / "configuration.example.yaml"
TEMPLATE = ROOT / "data" / "online_verification_report_template20260809.pdf"


class ConfigurationError(ValueError):
    pass


def external_path(value, base=None):
    if not isinstance(value, (str, Path)) or not str(value).strip():
        raise ConfigurationError("路径不能为空。")
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = (base or Path.cwd()) / path
    path = path.resolve()
    if path.is_relative_to(ROOT):
        raise ConfigurationError("个人配置、照片、二维码和输出必须放在代码仓库之外。")
    return path


def create_configuration(destination):
    path = external_path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        stream.write(EXAMPLE.read_text(encoding="utf-8"))


def read_private_configuration(path):
    path = external_path(path)
    config = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ConfigurationError("配置必须是 YAML 对象。")
    required = yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))
    for key in required:
        value = config.get(key)
        if not isinstance(value, str):
            raise ConfigurationError("配置字段必须存在，且使用引号包裹的字符串。")
        if not value.strip():
            raise ConfigurationError("必填字段不能为空。")
    for key in ("qr_code", "certificate_photo", "output_file_path"):
        config[key] = str(external_path(config[key], path.parent))
    for key in ("qr_code", "certificate_photo"):
        if not Path(config[key]).is_file():
            raise ConfigurationError("照片或二维码文件不存在。")
    if Path(config["output_file_path"]) in [path, Path(config["qr_code"]), Path(config["certificate_photo"])]:
        raise ConfigurationError("输出路径不能覆盖配置或输入图片。")
    config["template_path"] = str(TEMPLATE)
    return config
