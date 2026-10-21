"""Remove hidden sample records from an in-memory template, preserving drawing.

The original author asset is never rewritten. This profile is specific to the
reviewed upstream template: unsupported bytes are rejected rather than guessed.
Only hidden text-show operations and the two covered sample images are removed.
Visible labels, vector drawing, cover images, transforms and fonts are retained.
"""
from collections import Counter
from hashlib import sha256
from io import BytesIO
from pathlib import Path

from PyPDF2 import PdfReader
from PyPDF2.generic import ContentStream, DictionaryObject, NameObject
from scripts.upstream_references import AUTHOR_REFERENCE_SHA256

REFERENCE_PATH="data/online_verification_report_template20260809.pdf"
PRIVATE_TEXT_SLOTS=tuple([(178.75,710.78-28*index) for index in range(13)]+[(181.09,745.38),(251.342,202.18)])
PRIVATE_IMAGES={"/Im3":(480,640),"/Im5":(147,147)}
SHOW_TEXT={b"Tj",b"TJ",b"'",b'"'}


class TemplateProfileError(ValueError):
    """The source does not match the reviewed template structure."""


def _private_slot(group):
    matrices=[values for values,operator in group if operator==b"Tm"]
    if len(matrices)!=1:
        return None
    x,y=float(matrices[0][4]),float(matrices[0][5])
    for index,(expected_x,expected_y) in enumerate(PRIVATE_TEXT_SLOTS):
        if abs(x-expected_x)<.001 and abs(y-expected_y)<.001:
            return index
    return None


def load_clean_template(path):
    raw=Path(path).read_bytes()
    if sha256(raw).hexdigest() not in AUTHOR_REFERENCE_SHA256[REFERENCE_PATH]:
        raise TemplateProfileError("Unrecognized template; no unreviewed output was generated.")
    reader=PdfReader(BytesIO(raw))
    if len(reader.pages)!=1:
        raise TemplateProfileError("Unexpected template page count.")
    page=reader.pages[0]
    resources=page["/Resources"]
    xobjects=resources["/XObject"]
    for name,size in PRIVATE_IMAGES.items():
        image=xobjects[name].get_object()
        if image.get("/Subtype")!="/Image" or (image.get("/Width"),image.get("/Height"))!=size:
            raise TemplateProfileError("Unexpected sample image structure.")

    stream=ContentStream(page.get_contents(),reader)
    operations=[]
    text_group=None
    removed_slots=Counter()
    for operands,operator in stream.operations:
        if operator==b"BT":
            if text_group is not None:
                raise TemplateProfileError("Nested text object.")
            text_group=[]
        if text_group is not None:
            text_group.append((operands,operator))
            if operator==b"ET":
                slot=_private_slot(text_group)
                if slot is None:
                    operations.extend(text_group)
                else:
                    if not any(op in SHOW_TEXT for _,op in text_group):
                        raise TemplateProfileError("Expected sample text is missing.")
                    # Keep state operations so subsequent visible drawing is identical.
                    operations.extend((values,op) for values,op in text_group if op not in SHOW_TEXT)
                    removed_slots[slot]+=1
                text_group=None
        else:
            operations.append((operands,operator))
    if text_group is not None or removed_slots!=Counter(range(len(PRIVATE_TEXT_SLOTS))):
        raise TemplateProfileError("Unexpected sample text layout.")

    removed_images=Counter()
    filtered=[]
    for operands,operator in operations:
        if operator==b"Do" and str(operands[0]) in PRIVATE_IMAGES:
            removed_images[str(operands[0])]+=1
        else:
            filtered.append((operands,operator))
    if removed_images!=Counter(PRIVATE_IMAGES.keys()):
        raise TemplateProfileError("Unexpected sample image placement.")
    stream.operations=filtered
    page[NameObject("/Contents")]=stream
    resources[NameObject("/XObject")]=DictionaryObject({name:ref for name,ref in xobjects.items() if str(name) not in PRIVATE_IMAGES})
    return page
