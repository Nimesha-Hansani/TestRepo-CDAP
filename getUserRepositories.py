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
            try:
                  if(tr.type == "tree"):

                        treeContent=repository.get_contents(tr.path)
                        while len(treeContent) > 0:
                              file_content=treeContent.pop(0)

                              if file_content.type =="dir":
                                    treeContent.extend(repository.get_contents(file_content.path))

                              else:
                                    print(file_content.path)

                                    # rawPath=Avoid_Files(file_content.path,repoName,baseUrl,commitKey)
                            
                                    # if(rawPath != None):
                                    #       print(rawPath)
                                    #       r = requests.get(rawPath)
                               
                                    #       ExtFileName = rawPath.split('/')
                                    #       File_Extension =(ExtFileName[len(ExtFileName)-1]).split('.')
                               
                                    #       Comprehension.CalculateComprehension(br.name,Date[0],Date[1],File_Extension[1],file_content.path,rawPath,repo)

                  

                  
                  elif (tr.type == "blob"):
                        print(tr.path)
                  
                  else:

                        pass
            
            except:

                  pass
           
      



      
                  
            
             