import subprocess

# Hack some git commands to get csv file available on web site
# On local computer run 'git remote -v' in directory '{mygithubusername}/data'
# and check that you have an origin and a upstream similar to:
# origin git@github.com:{mygithubusername}/data (fetch)
# origin git@github.com:{mygithubusername}/data (push)
# upstream git@github.com:GeoNet/data (fetch)
# upstream git@github.com:GeoNet/data (push)

GIT_WORKING_DIR = '/home/byron/src/mabznz/angular/' # change to your data repo
GIT_CMTFile = 'README.md' # change ot the CMT file for website

change = subprocess.check_output(["git", "diff", GIT_CMTFile], cwd=GIT_WORKING_DIR)
if change:
    # Make sure local fork is in sync with upstream master. The moment tensor files are only updated by one user so shuold not get conflicts
    subprocess.call(["git", "fetch", "upstream"], cwd=GIT_WORKING_DIR)
    subprocess.call(["git", "checkout", "master"], cwd=GIT_WORKING_DIR)
    subprocess.call(["git", "merge", "upstream/master"], stderr=subprocess.STDOUT, cwd=GIT_WORKING_DIR)

    # Commit changes and push to both origin and master without a pull request. Is that possible?
    subprocess.call(["git", "add", GIT_CMTFile], cwd=GIT_WORKING_DIR)
    subprocess.call(["git", "commit", "-m", "Update CMT list", GIT_CMTFile], cwd=GIT_WORKING_DIR)
    subprocess.call(["git", "push", "origin", "master"], cwd=GIT_WORKING_DIR)
else:
    print('no change to', GIT_CMTFile, 'in directory', GIT_WORKING_DIR)
