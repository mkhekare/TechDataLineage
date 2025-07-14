class GitService:
    def __init__(self, repo_url, local_path):
        self.repo_url = repo_url
        self.local_path = local_path

    def clone_repository(self):
        import git
        try:
            git.Repo.clone_from(self.repo_url, self.local_path)
            return True
        except Exception as e:
            print(f"Error cloning repository: {e}")
            return False

    def analyze_committed_files(self):
        import git
        try:
            repo = git.Repo(self.local_path)
            committed_files = []
            for commit in repo.iter_commits():
                committed_files.extend(commit.stats.files.keys())
            return list(set(committed_files))  # Return unique file names
        except Exception as e:
            print(f"Error analyzing committed files: {e}")
            return []