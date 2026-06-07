import json
import os
from typing import List, Dict, Any

class QuizEngine:
    def __init__(self, json_file_path: str):
        self.json_file_path = json_file_path
        self.questions: List[Dict[str, Any]] = []
        self.score: int = 0

    def load_questions(self) -> bool:
        """Loads quiz data securely from the JSON file using defensive checks instead of try-except."""
        # Check if file exists
        if not os.path.exists(self.json_file_path):
            print(f"[Error] Target file '{self.json_file_path}' was not found.")
            return False
        
        # Check read permissions defensively
        if not os.access(self.json_file_path, os.R_OK):
            print(f"[Error] Read permission denied for file '{self.json_file_path}'.")
            return False

        # Verify file size is greater than 0 to prevent loading empty streams
        if os.path.getsize(self.json_file_path) == 0:
            print(f"[Error] File '{self.json_file_path}' is empty.")
            return False

        with open(self.json_file_path, "r", encoding="utf-8") as file:
            self.questions = json.load(file)
        return True

    def run_quiz(self) -> None:
        """Starts and manages the main quiz application loop."""
        if not self.questions:
            print("[Warning] No questions loaded in buffer. Exiting.")
            return

        print("\n" + "="*50)
        print("   SENIOR ENGINEER & CYBERSECURITY MASTER QUIZ   ")
        print(f"       Loaded: {len(self.questions)} Advanced Assessment Questions")
        print("="*50 + "\n")

        self.score = 0  # Reset session score tracking

        for index, q in enumerate(self.questions, start=1):
            print(f"Question {index}/{len(self.questions)}:")
            print(f"{q['question']}\n")
            
            # Render choices dynamically
            for opt_idx, option in enumerate(q['options'], start=1):
                print(f"  [{opt_idx}] {option}")
            print("")
            
            # Handle user interaction and input sanitation
            user_choice = self._get_valid_input(len(q['options']))
            selected_answer = q['options'][user_choice - 1]
            
            # Performance verification logic
            if selected_answer == q['answer']:
                print("\n[+] Correct Answer.")
                self.score += 1
            else:
                print(f"\n[-] Incorrect. Target Flag: {q['answer']}")
            
            print("-" * 50 + "\n")

        self._display_metrics()

    def _get_valid_input(self, max_options: int) -> int:
        """Validates user choice parameters strictly using string inspection methods to avoid try-except."""
        while True:
            choice = input("Enter selection index number: ").strip()
            if not choice:
                continue
            
            # Defensive check: Ensure string contains only numeric characters before casting
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= max_options:
                    return idx
                print(f"[!] Alert: Out of bounds. Choose a value between 1 and {max_options}.")
            else:
                print("[!] Alert: Invalid character sequence. Input must be an integer.")

    def _display_metrics(self) -> None:
        """Compiles final metrics and output grades."""
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        
        print("="*50)
        print("                EVALUATION SUMMARY              ")
        print("="*50)
        print(f"Raw Score Output:   {self.score} / {total_questions}")
        print(f"Success Metric:     {percentage:.2f}%")
        
        # Performance Evaluation Grading Block
        print("Status Grade:       ", end="")
        if percentage >= 90:
            print("L33T / Elite Engineer [Pass]")
        elif percentage >= 75:
            print("Senior Engineer [Pass]")
        elif percentage >= 50:
            print("SysAdmin / Associate [Pass]")
        else:
            print("Remediation Recommended [Fail]")
        print("="*50 + "\n")


if __name__ == "__main__":
    DATA_SOURCE = "quiz_data.json"
    
    app = QuizEngine(DATA_SOURCE)
    if app.load_questions():
        app.run_quiz()
