#!/usr/bin/env python3
import os
import argparse
import subprocess
from typing import Dict, List, Set

class GitObject:
    def __init__(self, sha1, obj_type, content):
        self.sha1 = sha1
        self.type = obj_type
        self.content = content.decode('utf-8', errors='replace')

class CommitNode:
    def __init__(self, sha1, parents):
        self.sha1 = sha1
        self.parents = parents

#Извлечение объекта
def read_object(repo_path, sha1):
    result = subprocess.run(
        ['git', 'cat-file', '-p', sha1],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        raise FileNotFoundError(f"Object '{sha1}' not found.")

    type_result = subprocess.run(
        ['git', 'cat-file', '-t', sha1],
        cwd=repo_path,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    obj_type = type_result.stdout.strip()

    return GitObject(sha1, obj_type, result.stdout.encode('utf-8'))

#Извлечение информации о родительских коммитов
def parse_commit(obj):
    lines = obj.content.split('\n')
    parents = []
    for line in lines:
        if line.startswith('parent '):
            parents.append(line[7:])
    return CommitNode(obj.sha1, parents)

#Построение графа (обход в ширину)
def build_commit_graph(repo_path, start_sha1):
    graph = {}
    stack = [start_sha1]
    visited: Set[str] = set()
    while stack:
        sha1 = stack.pop()
        if sha1 in visited:
            continue
        visited.add(sha1)
        obj = read_object(repo_path, sha1)
        if obj.type != 'commit':
            continue
        commit_node = parse_commit(obj)
        graph[sha1] = commit_node
        stack.extend(commit_node.parents)
    return graph

#Генерация dot-строки
def generate_dot(graph):
    dot = 'digraph G {\n'
    dot += '  rankdir=TB;\n'
    dot += '  node [shape=box, style=filled, color="#40e0d0"];\n'
    dot += '  edge [color="#000000"];\n'

    for sha1, node in graph.items():
        dot += f'  "{sha1}" [label="{sha1}"];\n'
        for parent_sha1 in node.parents:
            dot += f'  "{sha1}" -> "{parent_sha1}";\n'
    dot += '}\n'
    return dot

#Запись dot-строки в файл
def write_dot_file(dot_content, dot_path):
    with open(dot_path, 'w') as f:
        f.write(dot_content)

#Генерация png-файла из графа
def generate_graph_image(graphviz_path, dot_path, output_path, layout = 'dot'):
    subprocess.run([graphviz_path, '-K', layout, '-Tpng', dot_path, '-o', output_path], check=True)


def main():
    parser = argparse.ArgumentParser(description='Git Commit Dependency Graph Visualizer')
    parser.add_argument('graphviz_path', help='Path to the Graphviz executable')
    parser.add_argument('repo_path', help='Path to the Git repository')
    parser.add_argument('output_path', help='Path to the output image file')
    parser.add_argument('start_sha1', help='SHA1 of the starting commit')
    args = parser.parse_args()
    graph = build_commit_graph(args.repo_path, args.start_sha1)
    dot_content = generate_dot(graph)
    dot_path = os.path.join(os.path.dirname(args.output_path), 'graph.dot')
    write_dot_file(dot_content, dot_path)
    generate_graph_image(args.graphviz_path, dot_path, args.output_path)
    print("Graph generated successfully.")

if __name__ == '__main__':
    main()