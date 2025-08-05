import os
import subprocess

def clone_and_run():
    repo_url = "https://github.com/github/github-mcp-server.git"
    repo_dir = "github-mcp-server"
    if not os.path.exists(repo_dir):
        subprocess.run(["git", "clone", repo_url], check=True)
    os.chdir(repo_dir)
    subprocess.run(["go", "run", "./cmd/github-mcp-server/main.go"], check=True)

if __name__ == "__main__":
    clone_and_run()
