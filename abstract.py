import os
import requests
from bs4 import BeautifulSoup

def get_abstract(title):
    search_url = "https://scholar.google.com/scholar?q="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0"
    }

    response = requests.get(search_url + title, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        abstract_div = soup.find("div", class_="gs_rs")

        if abstract_div:
            abstract = abstract_div.get_text().strip()
            return abstract
        else:
            return "未找到相关论文摘要。"
    else:
        return "请求失败，请重试。"

def write_to_file(title, abstract):
    with open("abstract.txt", "w", encoding="utf-8") as f:
        f.write("论文标题：\n")
        f.write(title)
        f.write("\n\n论文摘要：\n")
        f.write(abstract)

def open_file(file_path):
    if os.name == "nt":  # Windows
        os.system(f"start {file_path}")
    elif os.name == "posix":  # macOS and Linux
        os.system(f"open {file_path}")

if __name__ == "__main__":
    title = input("请输入论文名字: ")
    abstract = get_abstract(title)
    write_to_file(title, abstract)
    print("已将摘要保存到 abstract.txt 文件中。")
    open_file("abstract.txt")
