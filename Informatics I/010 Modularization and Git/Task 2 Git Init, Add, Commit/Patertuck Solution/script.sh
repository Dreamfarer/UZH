# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.
git init
printf "aaa" > a.txt
printf "bbb" > b.txt
git add a.txt b.txt
git commit -m "Add files a.txt and b.txt"
printf "\nb2" >> b.txt
git add b.txt
git commit -m "Add second line to b.txt"
