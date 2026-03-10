from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import FAKE BANK CALL FRAUD Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "FAKE BANK CALL FRAUD"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "Who makes fake bank fraud calls?",
                "option1": "Scammers",
                "option2": "Bank manager",
                "option3": "Police",
                "option4": "Teacher",
                "answer": 1
            },

            {
                "question": "What do scammers pretend to be?",
                "option1": "Bank officials",
                "option2": "Doctors",
                "option3": "Drivers",
                "option4": "Shopkeepers",
                "answer": 1
            },

            {
                "question": "What information do scammers ask for?",
                "option1": "OTP and PIN",
                "option2": "Your favorite color",
                "option3": "Your hobbies",
                "option4": "Your age",
                "answer": 1
            },

            {
                "question": "Will real bank ask for OTP on phone?",
                "option1": "Yes",
                "option2": "No",
                "option3": "Sometimes",
                "option4": "Only morning",
                "answer": 2
            },

            {
                "question": "What should you do if you get fake bank call?",
                "option1": "Share OTP",
                "option2": "Disconnect call",
                "option3": "Tell PIN",
                "option4": "Follow instructions",
                "answer": 2
            },

            {
                "question": "Why do scammers ask for OTP?",
                "option1": "To access your account",
                "option2": "To help you",
                "option3": "To increase speed",
                "option4": "To fix phone",
                "answer": 1
            },

            {
                "question": "What should you never share on call?",
                "option1": "Bank details",
                "option2": "Weather",
                "option3": "Time",
                "option4": "News",
                "answer": 1
            },

            {
                "question": "What can happen if you share bank details?",
                "option1": "Money theft",
                "option2": "Phone repair",
                "option3": "Free gift",
                "option4": "Faster internet",
                "answer": 1
            },

            {
                "question": "What is safest action during suspicious call?",
                "option1": "Ignore and report",
                "option2": "Share details",
                "option3": "Trust caller",
                "option4": "Follow instructions",
                "answer": 1
            },

            {
                "question": "How can you protect yourself from fake bank calls?",
                "option1": "Never share OTP or PIN",
                "option2": "Share everything",
                "option3": "Trust unknown callers",
                "option4": "Click unknown links",
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
            self.style.SUCCESS("FAKE BANK CALL FRAUD Quiz Imported Successfully")
        )
