import os
import shutil

# デスクトップのパスを取得（どのMacでも動くように）
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 元のHTMLファイルがあるフォルダ（デスクトップ上）
source_folder = os.path.join(desktop_path, "hiroyuki_prg_sample1")
# 修正後のHTMLファイルを保存するフォルダ（デスクトップ上）
output_folder = os.path.join(desktop_path, "hiroyuki_prg_sample2")

# 出力フォルダ無ければ→作成
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 全てのHTMLファイルを処理
for filename in os.listdir(source_folder):
    source_path = os.path.join(source_folder, filename)

    # フォルダならスキップ
    if os.path.isdir(source_path):
        print(f" スキップ（フォルダ）: {filename}")
        continue

    # .htmlファイル以外はスキップ
    if not filename.endswith(".html"):
        print(f"スキップ（非HTMLファイル）: {filename}")
        continue

    output_path = os.path.join(output_folder, filename)

    # ファイルを読み込む
    with open(source_path, "r", encoding="utf-8", errors="ignore") as file:
        content = file.read()

    # すでにDOCTYPEがある場合はスキップ（重複防止）
    if "<!DOCTYPE html>" in content:
        print(f"スキップ: {filename}（すでにDOCTYPEあり）")
        shutil.copy(source_path, output_path)  # そのままコピー
        continue

    # 必要なヘッダーを追加
    new_content = f"""<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>{filename}</title>
</head>
<body>
{content}
</body>
</html>
"""

    # 修正後の内容をデスクトップの新フォルダに保存
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print(f"修正完了: {filename} → {output_folder}")

print("全てのHTMLファイルを修正、新しいフォルダにデスクトップ上で保存完了")

