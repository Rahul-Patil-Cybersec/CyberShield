from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import PASSWORD & 2FA SECURITY Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "PASSWORD & 2FA SECURITY"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is a strong password?",
                "option1": "123456",
                "option2": "password",
                "option3": "P@ssw0rd#2026",
                "option4": "abc",
                "answer": 3
            },

            {
                "question": "Why is 2FA important?",
                "option1": "It makes login faster",
                "option2": "It adds extra security",
                "option3": "It removes password",
                "option4": "It deletes account",
                "answer": 2
            },

            {
                "question": "What should you do if someone asks for your OTP?",
                "option1": "Share it",
                "option2": "Ignore it",
                "option3": "Share with friends",
                "option4": "Post online",
                "answer": 2
            },

            {
                "question": "Which password is weakest?",
                "option1": "Hello@123",
                "option2": "Rahul#2026",
                "option3": "123456",
                "option4": "MySecure@Pass9",
                "answer": 3
            },

            {
                "question": "Where should you enable 2FA?",
                "option1": "Important accounts",
                "option2": "Games only",
                "option3": "Not needed anywhere",
                "option4": "Only email",
                "answer": 1
            },

            {
                "question": "What can hackers do with your password?",
                "option1": "Access your account",
                "option2": "Improve security",
                "option3": "Delete virus",
                "option4": "Increase speed",
                "answer": 1
            },

            {
                "question": "What is OTP?",
                "option1": "One Time Password",
                "option2": "Online Test Password",
                "option3": "Open Text Password",
                "option4": "Only Type Password",
                "answer": 1
            },

            {
                "question": "Should you use same password everywhere?",
                "option1": "Yes",
                "option2": "No",
                "option3": "Sometimes",
                "option4": "Only social media",
                "answer": 2
            },

            {
                "question": "What makes password strong?",
                "option1": "Only letters",
                "option2": "Only numbers",
                "option3": "Letters, numbers, symbols",
                "option4": "Only name",
                "answer": 3
            },

            {
                "question": "What is best way to protect account?",
                "option1": "Share password",
                "option2": "Use weak password",
                "option3": "Enable 2FA and strong password",
                "option4": "Ignore security",
                "answer": 3
            },

        ]

        for q in questions:

            Question.objects.create(
                topic=topic,
                question=q["question"],
                option1=q["option1"],
                option2=q["option2"],
                option3=q["option3"],
                option4=q["option4"],
                correct_option=q["answer"]
            )


        self.stdout.write(
            self.style.SUCCESS("PASSWORD & 2FA Quiz Imported Successfully")
        )
