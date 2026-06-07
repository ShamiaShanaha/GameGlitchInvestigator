# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

First Bug: I expected the hint text to tell the user to go lower when the guess is too high and to go higher when the guess is too low. But the hint messages are reversed: when the guess is too high, the game tells me to go higher.

Second Bug: I expected the game instructions to match the difficulty range, but when I selected Hard mode, it showed that the range was 1 to 50, but the game kept giving me secret numbers that went above the range.

Third Bug: I expected Hard mode to be more difficult than Normal mode. However, Hard mode uses a range of 1–50 while Normal mode uses a range of 1–100. Because there are fewer possible numbers in Hard mode, it may actually be easier than Normal mode.

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|--------|------------------|-----------------|------------------------|
| Secret = 57, Guess = 60 | Display "Too High" and tell the user to guess lower | Displays "📈 Go HIGHER!" even though the guess is too high | None |
| Select Hard difficulty | Instructions should tell the user to guess a number between 1 and 50 | Instructions still say "Guess a number between 1 and 100" | None |
| Hard mode (1–50) vs. Normal mode (1–100) | Hard mode should be more difficult than Normal mode | Hard mode has a smaller range than Normal mode, making it  easier | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude as my tool for this project. It helped me to understand the code better, fix my logic issues in some areas, and refactor code into separate files. One example of a correct AI suggestion was when it helped me refactor the game logic by moving functions like check_guess into a separate logic_utils.py file. This made the code cleaner and easier to manage because the UI in app.py was no longer mixed with the core game logic. In addition, I also made sure to check the changes by running the app and making sure the game worked correctly after the changes were made. One example of a misleading suggestion was when the AI at the start suggested that I should keep two different types for the secret number, sometimes converting it to a string. I tested this and found it was not needed and actually made the logic more complicated, so I removed it and kept the secret as an integer.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided whether a bug was really fixed by running the app and playing with it to see if it was truly fixed. One test I ran is the pytest, where I checked the check_guess function. For example, I tested guessing 60 when the secret was 50, and it told me that I had passed. This showed that the bug fix worked correctly and the logic behaved as expected. AI helped me design better tests by showing me that my function returns a tuple instead of a single string.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns mean the app rebuilds itself from scratch every time you do something, like clicking a button or entering a guess. Instead of only updating one small part of the screen, it replays the whole program again from top to bottom.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Next time I work with AI, I will verify any suggestions it gives me instead of immediately allowing the changes. Even if the AI sounds confident, I would always test the change before assuming it is correct. This project changed how I think about AI-generated code because it can be very helpful for spotting patterns and fixing bugs, but it still requires human testing and validation to make sure the final logic actually works correctly.
