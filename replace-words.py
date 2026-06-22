import os
import shutil
import tkinter as tk
from tkinter import simpledialog, messagebox

import win32com.client as win32


def get_input_words():
    root = tk.Tk()
    root.withdraw()

    old_word = simpledialog.askstring("단어 변경", "바꿀 단어를 입력하세요:")
    if not old_word:
        return None, None

    new_word = simpledialog.askstring("단어 변경", "바뀔 단어를 입력하세요:")
    if not new_word:
        return None, None

    return old_word, new_word


def replace_all(hwp, old_word, new_word):
    hwp.HAction.GetDefault("AllReplace", hwp.HParameterSet.HFindReplace.HSet)

    option = hwp.HParameterSet.HFindReplace
    option.FindString = old_word
    option.ReplaceString = new_word
    option.Direction = hwp.FindDir("Forward")
    option.IgnoreMessage = 1
    option.FindType = 1

    hwp.HAction.Execute("AllReplace", option.HSet)


def highlight_word(hwp, word):
    hwp.MovePos(2)  # 문서 처음으로 이동

    while True:
        hwp.HAction.GetDefault("RepeatFind", hwp.HParameterSet.HFindReplace.HSet)

        option = hwp.HParameterSet.HFindReplace
        option.FindString = word
        option.Direction = hwp.FindDir("Forward")
        option.IgnoreMessage = 1
        option.FindType = 1

        found = hwp.HAction.Execute("RepeatFind", option.HSet)

        if not found:
            break

        hwp.HAction.GetDefault("MarkPenShape", hwp.HParameterSet.HMarkPenShape.HSet)

        pen = hwp.HParameterSet.HMarkPenShape
        pen.Color = hwp.RGBColor(255, 255, 0)

        hwp.HAction.Execute("MarkPenShape", pen.HSet)


def process_files(old_word, new_word):
    base_dir = os.path.dirname(os.path.abspath(__file__))

    origin_dir = os.path.join(base_dir, "origin")
    replaced_dir = os.path.join(base_dir, "replaced")

    os.makedirs(origin_dir, exist_ok=True)
    os.makedirs(replaced_dir, exist_ok=True)

    files = [
        f for f in os.listdir(base_dir)
        if f.lower().endswith((".hwp", ".hwpx"))
    ]

    if not files:
        messagebox.showinfo("알림", "같은 폴더에 .hwp 또는 .hwpx 파일이 없습니다.")
        return

    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
    hwp.XHwpWindows.Item(0).Visible = False

    processed_count = 0
    error_files = []

    for filename in files:
        source_path = os.path.join(base_dir, filename)
        origin_path = os.path.join(origin_dir, filename)
        replaced_path = os.path.join(replaced_dir, filename)

        try:
            shutil.copy2(source_path, origin_path)

            hwp.Open(source_path)

            replace_all(hwp, old_word, new_word)
            highlight_word(hwp, new_word)

            hwp.SaveAs(replaced_path)
            hwp.Clear(1)

            processed_count += 1

        except Exception as e:
            error_files.append(f"{filename}: {e}")

            try:
                hwp.Clear(1)
            except:
                pass

    hwp.Quit()

    result_message = f"{processed_count}개 파일 처리 완료\n\n"
    result_message += "원본 파일: origin 폴더\n"
    result_message += "수정 파일: replaced 폴더"

    if error_files:
        result_message += "\n\n오류 파일:\n" + "\n".join(error_files)

    messagebox.showinfo("완료", result_message)


def main():
    old_word, new_word = get_input_words()

    if not old_word or not new_word:
        messagebox.showwarning("취소", "입력이 취소되었습니다.")
        return

    process_files(old_word, new_word)


if __name__ == "__main__":
    main()
