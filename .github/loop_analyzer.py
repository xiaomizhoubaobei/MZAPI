import ast
import os
from typing import List

class LoopAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.nested_loops = 0
        self.max_depth = 0
        self.current_file = ""

    def visit_For(self, node):
        self.nested_loops += 1
        self.max_depth = max(self.max_depth, self.nested_loops)
        self.generic_visit(node)
        self.nested_loops -= 1

    def visit_While(self, node):
        self.visit_For(node)

    def report(self):
        print(f'File: {self.current_file}, Maximum loop nesting depth: {self.max_depth}')

def analyze_loops(file_paths: List[str]):
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            print(f"File not found: {file_path}")
            continue

        with open(file_path, 'r', encoding='utf-8') as source:
            tree = ast.parse(source.read(), filename=file_path)

        analyzer = LoopAnalyzer()
        analyzer.current_file = file_path
        analyzer.visit(tree)
        analyzer.report()

def get_python_files(directory: str) -> List[str]:
    """Recursively find all Python files in the given directory."""
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def main():
    # Specify the directory containing your Python files
    directory_to_analyze = '.MB'  # Change this to your target directory

    # Get all Python files in the specified directory
    python_files = get_python_files(directory_to_analyze)

    # Analyze loops in each Python file
    analyze_loops(python_files)

if __name__ == "__main__":
    main()