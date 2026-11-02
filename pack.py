"""Packs the registry file (.hnmod): horizon-native.json + mixins/<id>/*.rs|*.toml.
Usage: python3 pack.py  ->  dist/<id>-<version>.hnmod"""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
native = json.loads((ROOT / "horizon-native.json").read_text())
bundle = ROOT / "mixins" / native["id"]
names = ["horizon-native.json"] + [f"mixins/{native['id']}/{p.name}"
                                   for p in bundle.iterdir() if p.suffix in (".rs", ".toml")]
out = ROOT / "dist" / f"{native['id']}-{native['version']}.hnmod"
out.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for name in sorted(names):
        info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        archive.writestr(info, (ROOT / name).read_bytes())
print(f"{out} ({len(names)} files, sha256 {hashlib.sha256(out.read_bytes()).hexdigest()})")
