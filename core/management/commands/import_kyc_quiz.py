from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import BANK KYC UPDATE SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "BANK KYC UPDATE SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What does KYC stand for?",
                "option1": "Know Your Customer",
                "option2": "Keep Your Cash",
                "option3": "Know Your Code",
                "option4": "Key Your Card",
                "answer": 1
            },

            {
                "question": "Why do banks use KYC?",
                "option1": "To verify identity",
                "option2": "To increase speed",
                "option3": "To play games",
                "option4": "To send ads",
                "answer": 1
            },

            {
                "question": "How do scammers contact users for fake KYC updates?",
                "option1": "Calls or messages",
                "option2": "Bank branch only",
                "option3": "Newspaper",
                "option4": "TV",
                "answer": 1
            },

            {
                "question": "What do scammers ask during KYC scam?",
                "option1": "OTP and bank details",
                "option2": "Your favorite color",
                "option3": "Your hobbies",
                "option4": "Your height",
                "answer": 1
            },

            {
                "question": "Will real bank ask for OTP on call?",
                "option1": "Yes",
                "option2": "No",
                "option3": "Sometimes",
                "option4": "Only at night",
                "answer": 2
            },

            {
                "question": "Where should you update KYC safely?",
                "option1": "Official bank branch or website",
                "option2": "Unknown links",
                "option3": "Social media",
                "option4": "Random apps",
                "answer": 1
            },

            {
                "question": "What should you do if you get fake KYC call?",
                "option1": "Share details",
                "option2": "Ignore and block",
                "option3": "Send OTP",
                "option4": "Reply immediately",
                "answer": 2
            },

            {
                "question": "What happens if you share bank details with scammer?",
                "option1": "Money can be stolen",
                "option2": "Phone gets faster",
                "option3": "Account gets stronger",
                "option4": "Nothing happens",
                "answer": 1
            },

            {
                "question": "How can you identify fake KYC message?",
                "option1": "It asks for personal details urgently",
                "option2": "It comes from bank branch",
                "option3": "It has bank logo",
                "option4": "It is long message",
                "answer": 1
            },

            {
                "question": "What is safest action during KYC update?",
                "option1": "Use official bank channel",
                "option2": "Click unknown link",
                "option3": "Share OTP",
                "option4": "Trust caller",
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
            self.style.SUCCESS("BANK KYC UPDATE SCAM Quiz Imported Successfully")
        )
