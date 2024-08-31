from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor
import sys

def copy_file(file_path, target_dir):
    ext = file_path.suffix[1:].lower() 
    if not ext:
        ext = 'unknown'
    
    target_subdir = target_dir / ext
    target_subdir.mkdir(parents=True, exist_ok=True)
    
    shutil.copy2(file_path, target_subdir / file_path.name)

def process_directory(src_dir, target_dir):
    with ThreadPoolExecutor() as executor:
        futures = []
        for file_path in src_dir.rglob('*'):
            if file_path.is_file():
                futures.append(executor.submit(copy_file, file_path, target_dir))
        for future in futures:
            future.result()

def main():
    if len(sys.argv) < 2:
        print("Використання: python file_sorter.py <шлях до джерельної директорії> [шлях до цільової директорії]")
        sys.exit(1)
    
    src_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")
    
    if not src_dir.exists() or not src_dir.is_dir():
        print(f"Джерельна директорія не існує або не є директорією: {src_dir}")
        sys.exit(1)

    target_dir.mkdir(parents=True, exist_ok=True)
    process_directory(src_dir, target_dir)
    print("Обробка завершена.")

if __name__ == "__main__":
    main()
