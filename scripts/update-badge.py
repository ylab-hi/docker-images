from pathlib import Path
from dataclasses import dataclass

BASE_URL = "https://hub.docker.com/repository/docker/yanglabinfo/{}".format


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


def create_table(recipes):
    table = "|Tool | Pull | Stars| Image Size|\n" "|---|---|---|---|\n"
    for recipe in recipes:
        badges = Badge(recipe, get_version(recipe))
        table += f"|[{recipe}]({BASE_URL(recipe)})| {badges.pull}| {badges.star}| {badges.size}|\n"
    return table


def get_recipes():
    recipes = []
    for p in Path("recipes").iterdir():
        if p.is_dir():
            recipes.append(p.name)
    return recipes


def get_version(recipe):
    with open(f"recipes/{recipe}/Dockerfile") as f:
        for line in f:
            if line.startswith("ARG VERSION"):
                return line.split("=")[1].strip()

    return "latest"


def update_badge(recipes):
    table = create_table(recipes)

    start_sep = "<!-- begin badge -->\n"
    end_sep = "<!-- end badge -->\n"

    content = []
    file_name = Path("README.md")

    add = True
    with open(file_name) as f:
        for line in f:
            if line == start_sep:
                add = False
                content.append(line)
                content.append(table)

            if line == end_sep:
                add = True

            if add:
                content.append(line)

    try:
        with open(file_name, "w") as f:
            f.writelines(content)

    except Exception as e:
        print(f"update readme error happen {e}")


def main():
    recipes = get_recipes()
    update_badge(recipes)


if __name__ == "__main__":
    main()
