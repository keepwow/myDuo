DATE=`date +"%Y-%m-%d"`
REMOTE_URL=github.com:keepwow/myDuo.git

gitpush:
	rm -rf .git
	git init .
	git add docs Makefile mkdocs.yml myDuo.py README.md
	git commit -m "$(DATE)"
	git remote add origin "$(REMOTE_URL)"
	git push --set-upstream --force origin main

ghpages:
	mkdocs gh-deploy --force -b gh-pages

all:
	make gitpush
	make ghpages

.PHONY: all gitpush ghpages
