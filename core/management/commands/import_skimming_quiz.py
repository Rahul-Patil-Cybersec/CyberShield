from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import CARD SKIMMING FRAUD Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "CARD SKIMMING FRAUD"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is card skimming fraud?",
                "option1": "Stealing card information",
                "option2": "Cleaning card",
                "option3": "Charging card",
                "option4": "Blocking card",
                "answer": 1
            },

            {
                "question": "Where do scammers place skimming devices?",
                "option1": "ATM machines",
                "option2": "TV",
                "option3": "Laptop",
                "option4": "Printer",
                "answer": 1
            },

            {
                "question": "What do skimming devices steal?",
                "option1": "Card details",
                "option2": "Phone battery",
                "option3": "Internet speed",
                "option4": "Photos",
                "answer": 1
            },

            {
                "question": "How do scammers capture ATM PIN?",
                "option1": "Hidden cameras or fake keypad",
                "option2": "Asking politely",
                "option3": "Sending email",
                "option4": "Calling bank",
                "answer": 1
            },

            {
                "question": "What should you do while entering ATM PIN?",
                "option1": "Cover keypad",
                "option2": "Show everyone",
                "option3": "Say loudly",
                "option4": "Ignore security",
                "answer": 1
            },

            {
                "question": "What can scammers do with stolen card details?",
                "option1": "Withdraw money",
                "option2": "Improve account",
                "option3": "Increase balance",
                "option4": "Protect account",
                "answer": 1
            },

            {
                "question": "What should you check before using ATM?",
                "option1": "Check for unusual devices",
                "option2": "Check weather",
                "option3": "Check phone",
                "option4": "Check time",
                "answer": 1
            },

            {
                "question": "What is safest ATM to use?",
                "option1": "Trusted and secure ATM",
                "option2": "Broken ATM",
                "option3": "Unknown ATM",
                "option4": "Street ATM",
                "answer": 1
            },

            {
                "question": "How can you detect fraud early?",
                "option1": "Check bank statements",
                "option2": "Ignore account",
                "option3": "Share PIN",
                "option4": "Trust strangers",
                "answer": 1
            },

            {
                "question": "How can you protect from skimming fraud?",
                "option1": "Stay alert and protect PIN",
                "option2": "Share PIN",
                "option3": "Ignore security",
                "option4": "Trust unknown machines",
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
            self.style.SUCCESS("CARD SKIMMING FRAUD Quiz Imported Successfully")
        )
