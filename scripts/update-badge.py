import shutil
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Badge:
    name: str
    tag: str

    TABLE = {
        "pull": "![Docker Pulls](https://img.shields.io/docker/pulls/yanglabinfo/{}?style=for-the-badge)".format,
        "star": "![Docker Stars](https://img.shields.io/docker/stars/yanglabinfo/{}?style=for-the-badge)".format,
        "size": "![Docker Image Size (tag)](https://img.shields.io/docker/image-size/yanglabinfo/{}/{}?style=for-the-badge)".format,
    }

    def __post_init__(self):
        self.badges = {}
        for k, v in self.TABLE.items():
            self.badges[k] = v(self.name, self.tag) if k == "size" else v(self.name)

    @property
    def pull(self):
        return self.badges["pull"]

    @property
    def star(self):
        return self.badges["star"]

    @property
    def size(self):
        return self.badges["size"]


# ![Docker Pulls](https://img.shields.io/docker/pulls/yanglabinfo/binder?style=for-the-badge)
# ![Docker Stars](https://img.shields.io/docker/stars/yanglabinfo/binder?style=for-the-badge)
# ![Docker Image Size (tag)](https://img.shields.io/docker/image-size/yanglabinfo/binder/latest)


def create_table(recipes):
    table = "|Tool | Pull | Stars| Image Size|\n" "|---|---|---|---|\n"
    for recipe in recipes:
        badges = Badge(recipe, "latest")
        table += f"|{recipe}| {badges.pull}| {badges.star}| {badges.size}|\n"
    return table


def get_recipes():
    recipes = []
    for p in Path("recipes").iterdir():
        if p.is_dir():
            recipes.append(p.name)
    return recipes


def update_badge(recipes):
    table = create_table(recipes)

    sep1 = "<!-- begin badge -->\n"
    sep2 = "<!-- end badge -->\n"

    content = []
    add = True

    res_name = Path("README.md")
    shutil.copyfile(res_name, res_name.with_suffix(".bak"))

    file_name = Path("README.md")

    with open(file_name) as f:
        for line in f:
            if line == sep1:
                add = False
                content.append(line)
                content.append(table)

            if line == sep2:
                add = True

            if add:
                content.append(line)

    try:
        with open(file_name, "w") as f:
            f.writelines(content)

    except Exception as e:
        print(f"update readme error happend {e}")
