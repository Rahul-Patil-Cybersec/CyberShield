from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import OTP SCAM AWARENESS Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "OTP SCAM AWARENESS"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What does OTP stand for?",
                "option1": "One Time Password",
                "option2": "Only Test Password",
                "option3": "Online Text Password",
                "option4": "Open Transfer Password",
                "answer": 1
            },

            {
                "question": "Why is OTP used?",
                "option1": "To decorate phone",
                "option2": "To verify identity",
                "option3": "To increase internet speed",
                "option4": "To delete account",
                "answer": 2
            },

            {
                "question": "Who should you share your OTP with?",
                "option1": "Bank officer on phone",
                "option2": "Friends",
                "option3": "Nobody",
                "option4": "Social media",
                "answer": 3
            },

            {
                "question": "What can scammers do if they get your OTP?",
                "option1": "Access your account",
                "option2": "Improve your security",
                "option3": "Fix your phone",
                "option4": "Charge your battery",
                "answer": 1
            },

            {
                "question": "How do scammers usually ask for OTP?",
                "option1": "Call or message",
                "option2": "Face to face only",
                "option3": "Newspaper",
                "option4": "TV",
                "answer": 1
            },

            {
                "question": "Will bank ever ask for your OTP?",
                "option1": "Yes",
                "option2": "No",
                "option3": "Sometimes",
                "option4": "Only at night",
                "answer": 2
            },

            {
                "question": "What should you do if someone asks for OTP?",
                "option1": "Share it",
                "option2": "Ignore and block",
                "option3": "Post online",
                "option4": "Tell everyone",
                "answer": 2
            },

            {
                "question": "Where do you receive OTP?",
                "option1": "Mobile or email",
                "option2": "TV",
                "option3": "Newspaper",
                "option4": "Radio",
                "answer": 1
            },

            {
                "question": "OTP helps protect:",
                "option1": "Your account",
                "option2": "Your clothes",
                "option3": "Your car",
                "option4": "Your house",
                "answer": 1
            },

            {
                "question": "What is safest action with OTP?",
                "option1": "Share with caller",
                "option2": "Keep it secret",
                "option3": "Send to friends",
                "option4": "Post on social media",
                "answer": 2
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
            self.style.SUCCESS("OTP SCAM Quiz Imported Successfully")
        )
