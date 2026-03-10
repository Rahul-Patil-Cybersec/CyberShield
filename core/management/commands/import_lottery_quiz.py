from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import FAKE PRIZE & LOTTERY SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "FAKE PRIZE & LOTTERY SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is fake lottery scam?",
                "option1": "Fake message about winning prize",
                "option2": "Real prize message",
                "option3": "Phone update",
                "option4": "App update",
                "answer": 1
            },

            {
                "question": "How do scammers contact victims?",
                "option1": "SMS, call, or email",
                "option2": "Bank branch",
                "option3": "School",
                "option4": "Office",
                "answer": 1
            },

            {
                "question": "What do scammers claim?",
                "option1": "You won a prize",
                "option2": "Phone is broken",
                "option3": "Internet is slow",
                "option4": "App is old",
                "answer": 1
            },

            {
                "question": "What do scammers ask for?",
                "option1": "Fee or payment",
                "option2": "Phone wallpaper",
                "option3": "Phone brightness",
                "option4": "Phone sound",
                "answer": 1
            },

            {
                "question": "Are these prize offers real?",
                "option1": "No",
                "option2": "Yes",
                "option3": "Always",
                "option4": "Sometimes",
                "answer": 1
            },

            {
                "question": "What should you never share?",
                "option1": "Bank details and OTP",
                "option2": "Weather info",
                "option3": "Time",
                "option4": "News",
                "answer": 1
            },

            {
                "question": "What happens if you pay scammers?",
                "option1": "Money loss",
                "option2": "Phone repair",
                "option3": "Free gift",
                "option4": "Faster internet",
                "answer": 1
            },

            {
                "question": "What is safest action?",
                "option1": "Ignore scam messages",
                "option2": "Reply quickly",
                "option3": "Share OTP",
                "option4": "Pay fee",
                "answer": 1
            },

            {
                "question": "How do scammers create trust?",
                "option1": "Pretend official",
                "option2": "Tell truth",
                "option3": "Show real prize",
                "option4": "Give money",
                "answer": 1
            },

            {
                "question": "How can you stay safe?",
                "option1": "Verify prize source",
                "option2": "Trust unknown message",
                "option3": "Pay fee",
                "option4": "Share personal info",
                "answer": 1
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
            self.style.SUCCESS("FAKE PRIZE & LOTTERY SCAM Quiz Imported Successfully")
        )
