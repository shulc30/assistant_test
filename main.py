import subprocess
import time
import os
import sys
import locale

def run_script(script_name):
    """Запускает указанный скрипт через интерпретатор виртуального окружения."""
    project_path = r"C:\Users\Администратор\Desktop\test_2"
    python_path = os.path.join(project_path, "venv", "Scripts", "python.exe")
    script_path = os.path.join(project_path, script_name)

    try:
        result = subprocess.run(
            [python_path, script_path],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            env={**os.environ, "PYTHONUTF8": "1"}  # Принудительная кодировка UTF-8
        )

        # Вывод результатов выполнения скрипта
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            print(f"\n🟢 Вывод {script_name}:\n{stdout}")

        if stderr:
            print(f"\n🔴 Ошибка при выполнении {script_name}:\n{stderr}")

    except Exception as e:
        print(f"\n❌ Произошла ошибка при запуске {script_name}: {e}")

def main():
    scripts = [
        "news.py",
        "news_gen.py",
        "news_gen_slog.py",
        "news_gen_photo.py",
        "move_file.py"
    ]

    for script in scripts:
        print(f"\n🚀 Запуск {script}...")
        run_script(script)
        time.sleep(5)  # Пауза между скриптами

    print("\n✅ Все шаги выполнены успешно.")

if __name__ == "__main__":
    # Устанавливаем кодировку по умолчанию
    locale.setlocale(locale.LC_ALL, "ru_RU.UTF-8")

    # Меняем кодировку консоли на UTF-8 (для Windows)
    if os.name == "nt":
        os.system("chcp 65001 > nul")
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")

    print(f"\n🟢 Текущий интерпретатор Python: {sys.executable}\n")
    main()
