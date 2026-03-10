import os
import xml.etree.ElementTree as ET

CLASSES = ["apple", "banana", "orange"]

def convert_bbox(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return x * dw, y * dh, w * dw, h * dh

def convert_folder(xml_dir, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    for file in os.listdir(xml_dir):
        if not file.endswith(".xml"):
            continue

        tree = ET.parse(os.path.join(xml_dir, file))
        root = tree.getroot()

        size = root.find("size")
        if size is None:
            print(f"⚠️ Skipped (no size tag): {file}")
            continue

        w = int(size.find("width").text)
        h = int(size.find("height").text)

        if w == 0 or h == 0:
            print(f"⚠️ Skipped (zero size): {file}")
            continue

        with open(os.path.join(out_dir, file.replace(".xml", ".txt")), "w") as f:
            for obj in root.iter("object"):
                cls = obj.find("name").text
                if cls not in CLASSES:
                    continue

                cls_id = CLASSES.index(cls)
                xmlbox = obj.find("bndbox")

                bbox = (
                    float(xmlbox.find("xmin").text),
                    float(xmlbox.find("xmax").text),
                    float(xmlbox.find("ymin").text),
                    float(xmlbox.find("ymax").text),
                )

                bb = convert_bbox((w, h), bbox)
                f.write(f"{cls_id} {' '.join(map(str, bb))}\n")

    print(f"✅ Finished converting: {xml_dir}")

convert_folder("labels_xml/train", "labels/train")
convert_folder("labels_xml/test", "labels/test")
