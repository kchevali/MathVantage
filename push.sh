# shopt -s globstar
cd /Users/kevin/Documents/Repos/MathVantage/Exams
for fileToCommit in ./*; do
    # git diff "$fileToCommit" || continue 
    test -f "$fileToCommit" || continue 
    printf "%s\n" "${fileToCommit}"
    git add "${fileToCommit}"
    git commit -m "Auto push ${fileToCommit}" 
done
for fileToCommit in ./**/*; do
    # git diff "$fileToCommit" || continue 
    test -f "$fileToCommit" || continue 
    printf "%s\n" "${fileToCommit}"
    git add "${fileToCommit}"
    git commit -m "Auto push ${fileToCommit}" 
done
for fileToCommit in ./**/**/*; do
    # git diff "$fileToCommit" || continue 
    test -f "$fileToCommit" || continue 
    printf "%s\n" "${fileToCommit}"
    git add "${fileToCommit}"
    git commit -m "Auto push ${fileToCommit}" 
done
git push