from github import Github
g = Github("mirzaei-ce","Mahdi@1993")
key = open("/home/mahdi/.ssh/hacoin.pub").read()
print g.get_user().create_key("test",key)
