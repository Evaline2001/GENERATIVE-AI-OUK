import os, git, json, networkx as nx, matplotlib.pyplot as plt

def clone_repo(repo_url, dest="temp_repo"):
    if os.path.exists(dest):
        os.system(f"rm -rf {dest}")
    git.Repo.clone_from(repo_url, dest)
    return dest

def generate_tree(root_dir):
    structure = {}
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in ['.git','node_modules','__pycache__']]
        rel_path = os.path.relpath(root, root_dir)
        structure[rel_path] = files
    return structure

def simple_analyze(repo_dir):
    graph = nx.DiGraph()
    for root, _, files in os.walk(repo_dir):
        for f in files:
            if f.endswith(".py") or f.endswith(".jac"):
                path = os.path.join(root, f)
                graph.add_node(path)
    nodes = list(graph.nodes)
    for i in range(len(nodes)-1):
        graph.add_edge(nodes[i], nodes[i+1])
    nx.nx_pydot.write_dot(graph, "code_graph.dot")
    plt.figure(figsize=(6,4))
    nx.draw(graph, with_labels=False, node_size=20)
    plt.savefig("graph.png")
    return f"Nodes: {len(nodes)}, Edges: {graph.number_of_edges()}"

def build_docs(file_tree, analysis_summary, output="docs.md"):
    with open(output, "w") as f:
        f.write("# 📘 Auto-Generated Documentation\n\n")
        f.write("## File Structure\n\n```\n")
        for k, v in file_tree.items():
            f.write(f"{k}/ : {', '.join(v)}\n")
        f.write("```\n\n## Code Graph Summary\n")
        f.write(analysis_summary + "\n\n")
        f.write("![Graph](graph.png)\n")
    return output
