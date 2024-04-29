import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz(None, "Quiz", "start date ","due date")
        quiz = self.ctrl.get_quizzes()
        self.assertEquals(len(quiz), 1, "There is exactly one discussion.")
        quiz = self.ctrl.get_quiz_by_id(quiz_id)
        self.ctrl.print_quiz(quiz_id)
        self.assertIsNotNone(quiz, "The quiz can be retrieved.")

    def test_expose_failure_02(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz title", "Quiz", "start date ","due date")
        question_id = self.ctrl.add_question(quiz_id,"Hello"+5,"Question Title")
        question = self.ctrl.get_question_by_id(question_id)
        self.ctrl.print_quiz(quiz_id)
        self.assertIsNotNone(question, "The quiz can be retrieved.")

    def test_expose_failure_03(self):
        """
        Implement this function and two more that
        execute the code and make it fail.
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz title", "Quiz", "start date ","due date")
        question_id = self.ctrl.add_question(quiz_id,"Question Title","Question")
        Answer_id = self.ctrl.add_answer(question_id,"3"+5,True)
        Answer = self.ctrl.print_quiz(quiz_id)
        self.assertIsNone(Answer, "The quiz can be retrieved.")
        
        

if __name__ == '__main__':
    unittest.main()