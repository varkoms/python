from git import Repo

def get_last_10_commits():
    repo = Repo('.')
    commits = list(repo.iter_commits('main'))[:10]
    return commits

print(get_last_10_commits())