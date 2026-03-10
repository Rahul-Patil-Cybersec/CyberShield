from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import FAKE BUSINESS PAGE SHOPPING SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "FAKE BUSINESS PAGE SHOPPING SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is a fake business page?",
                "option1": "Page created by scammers",
                "option2": "Official bank page",
                "option3": "Government website",
                "option4": "School website",
                "answer": 1
            },

            {
                "question": "Where do fake shopping pages usually appear?",
                "option1": "Social media",
                "option2": "Calculator app",
                "option3": "Camera app",
                "option4": "Phone settings",
                "answer": 1
            },

            {
                "question": "Why do scammers create fake shopping pages?",
                "option1": "To steal money",
                "option2": "To help users",
                "option3": "To improve security",
                "option4": "To give free gifts",
                "answer": 1
            },

            {
                "question": "What do fake pages show to attract users?",
                "option1": "Very low prices",
                "option2": "High security",
                "option3": "Bank protection",
                "option4": "Free internet",
                "answer": 1
            },

            {
                "question": "What happens after payment on fake page?",
                "option1": "No product delivered",
                "option2": "Product delivered fast",
                "option3": "Money returned",
                "option4": "Account secured",
                "answer": 1
            },

            {
                "question": "What should you check before shopping online?",
                "option1": "Reviews and ratings",
                "option2": "Phone wallpaper",
                "option3": "Phone brightness",
                "option4": "Phone battery",
                "answer": 1
            },

            {
                "question": "What is safest place to shop online?",
                "option1": "Trusted websites",
                "option2": "Unknown pages",
                "option3": "Random links",
                "option4": "Fake pages",
                "answer": 1
            },

            {
                "question": "What payment method is safer?",
                "option1": "Secure payment methods",
                "option2": "Direct unknown transfer",
                "option3": "Sharing OTP",
                "option4": "Sharing PIN",
                "answer": 1
            },

            {
                "question": "What can fake pages steal?",
                "option1": "Money and personal data",
                "option2": "Phone color",
                "option3": "Phone size",
                "option4": "Phone sound",
                "answer": 1
            },

            {
                "question": "How can you avoid fake shopping scams?",
                "option1": "Verify seller authenticity",
                "option2": "Trust unknown sellers",
                "option3": "Ignore reviews",
                "option4": "Share bank details",
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
            self.style.SUCCESS("FAKE BUSINESS PAGE SHOPPING SCAM Quiz Imported Successfully")
        )
