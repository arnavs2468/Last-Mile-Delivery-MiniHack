======================================================================
MiniHack: AI Data Intelligence Challenge
Solution: Last-Mile Delivery Delay Root Cause Analysis
======================================================================

Hello Judges! 👋 

Welcome to my submission for the Last-Mile Delivery problem statement. 
This project dives into our 2,080-row dataset to figure out exactly why 
deliveries are running late across our 10 cities, and more importantly, 
how we can fix it.

Author: Arnav Singh 
Institution: Institute of Engineering and Technology, DDU Gorakhpur

----------------------------------------------------------------------
📁 WHAT IS IN THIS FOLDER?
----------------------------------------------------------------------
1. solution.py 
   The main Python script. This single file handles all the data 
   cleaning, runs the statistical T-tests, and generates the final 
   visual dashboard.

2. last_mile_delivery_dataset.csv 
   The original dataset, kept right here so the code runs seamlessly 
   out of the box.

3. README.txt 
   You are reading it right now!

----------------------------------------------------------------------
🚀 HOW TO RUN THE CODE
----------------------------------------------------------------------
I wanted to make testing this as frictionless as possible. 

Step 1: Open your terminal and navigate to this folder.
Step 2: Ensure you have the required libraries installed:
        pip install pandas numpy matplotlib seaborn scipy
Step 3: Run the script:
        python solution.py

What to expect:
- The answers to the first three analytical questions will print 
  directly to your terminal console in plain text.
- A pop-up window will automatically open displaying the 3-panel 
  Matplotlib dashboard for Question 4. (Note: You will need to close 
  this graphical window to fully terminate the script).

----------------------------------------------------------------------
💡 A QUICK SPOILER (The Big Fix)
----------------------------------------------------------------------
If you are short on time, the data made one thing very clear: rain 
absolutely wreaks havoc on grocery deliveries, and veteran riders 
make a statistically massive difference. The biggest operational fix 
is right there in the dashboard!

Thank you for hosting such a great hackathon, and I hope you enjoy 
reviewing my solution!