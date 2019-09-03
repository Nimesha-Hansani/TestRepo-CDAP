from github import Github
g =  None

def test():
    instance = Github("Nimesha-Hansani", "19950525hansani")
    print(instance)
    global g 
    g = instance
    print(g)
    repos=g.get_user().get_repos()    

    for repo in repos:
        print(repo.name)


def test2():
    print(g)


test()
test2()