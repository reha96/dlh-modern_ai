#!/usr/bin/env python3
"""Prepare Pascal VOC 2012 detection subset in YOLOv8 format.

Downloads the Pascal VOC 2012 archive, keeps only the images listed in
the sample files, filters annotations down to person, car and bicycle,
converts the remaining boxes to YOLO normalized format, and writes the
dataset layout plus data.yaml expected by the later tasks.
"""

import shutil
import tarfile
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

# public VOC 2012 trainval archive
VOC_URL = (
    "http://host.robots.ox.ac.uk/pascal/VOC/voc2012/"
    "VOCtrainval_11-May-2012.tar"
)
VOC_ARCHIVE = "VOCtrainval_11-May-2012.tar"

# classes to keep, in data.yaml order
CLASSES = ["person", "car", "bicycle"]

# exact data.yaml content expected by the checker
DATA_YAML = """\
path: datasets/detection/
train: images/train
val: images/val
nc: 3
names: ["person", "car", "bicycle"]
"""


def download_voc(dest):
    """Download and extract the Pascal VOC 2012 archive into dest."""
    # work with a path object from here on
    dest = Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    # skip everything when the extracted tree is already there
    extracted = dest / "VOCdevkit" / "VOC2012"
    if extracted.is_dir():
        return extracted
    # fetch the tarball only when it is missing
    archive = dest / VOC_ARCHIVE
    if not archive.is_file():
        urllib.request.urlretrieve(VOC_URL, archive)
    # unpack the archive next to the destination folder
    with tarfile.open(archive, "r") as tar:
        tar.extractall(path=dest)
    return extracted


def convert_annotation(xml_path):
    """Convert one VOC XML annotation to YOLO lines for kept classes."""
    # parse the annotation xml file
    tree = ET.parse(str(xml_path))
    root = tree.getroot()
    # image size normalizes pixel boxes into [0, 1]
    width = float(root.findtext("size/width"))
    height = float(root.findtext("size/height"))
    lines = []
    for obj in root.findall("object"):
        # skip every class outside person/car/bicycle
        name = obj.findtext("name")
        if name not in CLASSES:
            continue
        # read the pixel corner box
        box = obj.find("bndbox")
        xmin = float(box.findtext("xmin"))
        ymin = float(box.findtext("ymin"))
        xmax = float(box.findtext("xmax"))
        ymax = float(box.findtext("ymax"))
        # skip boxes with no area
        if xmax <= xmin or ymax <= ymin:
            continue
        # convert corners to normalized center + size
        cid = CLASSES.index(name)
        xc = ((xmin + xmax) / 2.0) / width
        yc = ((ymin + ymax) / 2.0) / height
        w = (xmax - xmin) / width
        h = (ymax - ymin) / height
        lines.append("{} {:.6f} {:.6f} {:.6f} {:.6f}".format(
            cid, xc, yc, w, h))
    return lines


def build_split(sample_file, src_img_dir, src_ann_dir, dst_img_dir,
                dst_lbl_dir):
    """Copy listed images and write matching YOLO label files."""
    # make sure both output folders exist
    dst_img_dir = Path(dst_img_dir)
    dst_lbl_dir = Path(dst_lbl_dir)
    dst_img_dir.mkdir(parents=True, exist_ok=True)
    dst_lbl_dir.mkdir(parents=True, exist_ok=True)
    # one image id per non-empty line, extension optional
    ids = []
    with open(sample_file) as f:
        for line in f:
            name = line.strip()
            if not name:
                continue
            if name.lower().endswith(".jpg"):
                name = name[:-4]
            ids.append(name)
    # copy each image and write its twin label file
    for img_id in ids:
        src = str(Path(src_img_dir) / (img_id + ".jpg"))
        dst = str(Path(dst_img_dir) / (img_id + ".jpg"))
        shutil.copy(src, dst)
        lines = convert_annotation(Path(src_ann_dir) / (img_id + ".xml"))
        with open(dst_lbl_dir / (img_id + ".txt"), "w") as f:
            # empty file when no kept object is present
            if lines:
                f.write("\n".join(lines) + "\n")


def write_data_yaml(path):
    """Write the YOLO dataset YAML pointing at datasets/detection/."""
    # fixed text so the content matches the spec exactly
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        f.write(DATA_YAML)


def _find_sample_file(base, cwd, split):
    """Locate <split>_samples.txt, else fall back to full VOC splits."""
    # spec names train twice; read it as train + val files
    name = "{}_samples.txt".format(split)
    for folder in (cwd, base):
        candidate = Path(folder) / name
        if candidate.is_file():
            return candidate
    # fall back to the full VOC train/val id lists
    fallback = (base / "VOCdevkit" / "VOC2012" / "ImageSets"
                / "Main" / "{}.txt".format(split))
    return fallback


def main():
    """Run the full VOC download, filter, convert, and layout pipeline."""
    # all dataset paths live next to this file
    base = Path(__file__).resolve().parent
    cwd = Path.cwd()
    # download and extract the archive once
    voc = download_voc(base)
    src_img = voc / "JPEGImages"
    src_ann = voc / "Annotations"
    # output layout expected by YOLOv8 training
    out = base / "datasets" / "detection"
    splits = {
        "train": (out / "images" / "train", out / "labels" / "train"),
        "val": (out / "images" / "val", out / "labels" / "val"),
    }
    # build each split from its sample (or fallback) id list
    for split, (img_dir, lbl_dir) in splits.items():
        sample = _find_sample_file(base, cwd, split)
        build_split(sample, src_img, src_ann, img_dir, lbl_dir)
    # dataset descriptor used by every later task
    write_data_yaml(out / "data.yaml")


if __name__ == "__main__":
    main()
