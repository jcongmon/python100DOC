print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
people = float(input("How many people to split the bill? "))
calc = round((round(bill, 2) + (round(bill, 2) * round(tip / 100, 2))) / people, 2)
print(f"Each person should pay: ${calc}")

echo "# python100DOC" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jcongmon/python100DOC.git
git push -u origin main