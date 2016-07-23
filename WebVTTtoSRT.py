import re
from pathlib import Path


def vtt_to_srt(vtt_file: str):
    output_address = vtt_file[:len(vtt_file) - 3] + "srt"
    print("\"" + vtt_file + "\" to \"" + output_address)
    r_sub = re.compile('(?P<a> \d\d:\d\d)\.(?P<b> \d\d\d)', re.VERBOSE)

    with open(vtt_file, "r") as i_file:
        with open(output_address, "w") as o_file:
            content = i_file.read()
            content = content.replace("WEBVTT\n\n", "")
            content = r_sub.sub('\g<a>,\g<b>', content)
            o_file.write(content)


def recursive_file_finder(path: Path):
    if path.is_dir():
        print("Dir: " + path.name)
        for subdir in path.iterdir():
            recursive_file_finder(subdir)
    else:
        if path.name.endswith('.vtt'):
            print(path.name)
            vtt_to_srt(str(path.absolute()))

startingAddress = "D:\\University\\Online Courses\\" \
                  "Fundamentals of Digital Image and Video Processing - Northwestern University"
p = Path(startingAddress)
recursive_file_finder(p)
