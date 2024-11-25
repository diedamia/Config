import unittest
import os
import subprocess
from main import *

class TestGitGraphVisualizer(unittest.TestCase):

    def setUp(self):
        self.repo_path = 'test_repos'
        self.commit_sha1 = 'dc13c15'
        self.graphviz_path = 'C:/Program Files/Graphviz/bin/dot.exe'
        self.output_image_path = 'output.png'
        self.dot_path = 'graph.dot'

    def test_read_object(self):
        git_object = read_object(self.repo_path, self.commit_sha1)
        self.assertEqual(git_object.sha1, self.commit_sha1)
        self.assertEqual(git_object.type, 'commit')

    def test_parse_commit(self):
        obj = read_object(self.repo_path, self.commit_sha1)
        commit_node = parse_commit(obj)
        self.assertEqual(commit_node.sha1, self.commit_sha1)
        self.assertIsInstance(commit_node.parents, list)
    
    def test_build_commit_graph(self):
        graph = build_commit_graph(self.repo_path, self.commit_sha1)
        self.assertIn(self.commit_sha1, graph)
        self.assertIsInstance(graph[self.commit_sha1], CommitNode)

    def test_generate_dot(self):
        graph = build_commit_graph(self.repo_path, self.commit_sha1)
        dot_content = generate_dot(graph)
        self.assertIn('digraph G {', dot_content) 

    def test_write_dot_file(self):
        dot_content = "digraph G { }"
        write_dot_file(dot_content, self.dot_path)
        self.assertTrue(os.path.exists(self.dot_path)) 
        with open(self.dot_path) as f:
            self.assertEqual(f.read().strip(), dot_content)

    def test_generate_graph_image(self):
        graph = build_commit_graph(self.repo_path, self.commit_sha1)
        dot_content = generate_dot(graph)
        write_dot_file(dot_content, self.dot_path)
        generate_graph_image(self.graphviz_path, self.dot_path, self.output_image_path)
        self.assertTrue(os.path.exists(self.output_image_path)) 


if __name__ == '__main__':
    unittest.main()
