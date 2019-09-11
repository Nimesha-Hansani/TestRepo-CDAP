from github  import Github


baseUrl='https://raw.githubusercontent.com/'

g = Github('nimeshaamarasingha@gmail.com', '19950525hansani')
repository=g.get_repo('Nimesha-Hansani/TestRepo-CDAP')
branches=repository.get_branches()
    
for br in branches:
   headCommit=br.commit.sha

   commits = repository.get_commits(headCommit)
   for com in commits:
        commitDateTime = com.commit.author.date
        print(commitDateTime)

        tree=repository.get_git_tree(com.sha).tree
        
        for tr in tree :
             
              treeContent=repository.get_contents(tr.path)
              print(treeContent)

              while len(treeContent)> 1:

                      file_content=treeContent.pop(0)
                      print(file_content)