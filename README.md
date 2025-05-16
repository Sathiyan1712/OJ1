# 🧠 OJ1: Online Judge Platform for Students and Teachers

OJ1 is a Django-based Online Judge platform where **teachers can upload programming problems**, and **students can solve them and get instant code verification**. It promotes practice-based learning, strengthens coding skills, and enables teachers to support student growth.

---

## 📌 Project Goals

- Allow **students** to solve programming problems and receive feedback.
- Allow **teachers** to:
  - Add/edit/delete problems.
  - View student submissions and performance.
- Encourage coding practice through real-world problem solving.

---

## 🏛️ High-Level Architecture


- **Frontend**: Django templates with HTML/CSS/Bootstrap (or React)
- **Backend**: Django Views, Models, and Forms


---

## 🧩 Core Modules

| Module             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| Authentication     | User registration, login, and role-based access (Student, Teacher)          |
| Problem Management | Teachers can add, edit, or delete problems with test cases                  |
| Code Submission    | Students can submit code for problems and get real-time verdicts            |
| Results Feedback   | Verdict: "Correct", "Wrong Answer", "Runtime Error", etc.                   |
| Dashboard          | Teachers can view submissions and performance analytics                    |



## 🛠️ Tech Stack

| Layer      | Technology                      |
|------------|----------------------------------|
| Language   | Python                          |
| Framework  | Django                          |
| Database   | PostgreSQL / SQLite             |
| Frontend   | HTML, CSS, Bootstrap (or React) |
| Judge Engine | Python subprocess / Docker    |
| Authentication | Django's built-in auth system |

