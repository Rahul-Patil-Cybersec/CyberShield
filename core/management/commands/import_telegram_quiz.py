from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import TELEGRAM JOB SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "TELEGRAM JOB SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "Where do Telegram job scams usually happen?",
                "option1": "Telegram",
                "option2": "Calculator app",
                "option3": "Camera app",
                "option4": "Phone settings",
                "answer": 1
            },

            {
                "question": "What do scammers offer in Telegram job scams?",
                "option1": "Fake job offers",
                "option2": "Free phone",
                "option3": "Free internet",
                "option4": "Free food",
                "answer": 1
            },

            {
                "question": "Why do scammers pay small money first?",
                "option1": "To gain trust",
                "option2": "To help user",
                "option3": "To increase security",
                "option4": "To improve phone",
                "answer": 1
            },

            {
                "question": "What do scammers ask later?",
                "option1": "Payment or fee",
                "option2": "Phone wallpaper",
                "option3": "Phone brightness",
                "option4": "Phone color",
                "answer": 1
            },

            {
                "question": "What happens after victim pays money?",
                "option1": "Scammer blocks victim",
                "option2": "Job becomes permanent",
                "option3": "Salary increases",
                "option4": "Phone gets faster",
                "answer": 1
            },

            {
                "question": "Do real companies ask for job payment?",
                "option1": "No",
                "option2": "Yes",
                "option3": "Always",
                "option4": "Sometimes",
                "answer": 1
            },

            {
                "question": "What should you do before accepting job offer?",
                "option1": "Verify company",
                "option2": "Pay money",
                "option3": "Share OTP",
                "option4": "Trust blindly",
                "answer": 1
            },

            {
                "question": "What can scammers steal?",
                "option1": "Money and personal data",
                "option2": "Phone color",
                "option3": "Phone size",
                "option4": "Phone sound",
                "answer": 1
            },

            {
                "question": "What is safest action?",
                "option1": "Avoid unknown job offers",
                "option2": "Trust unknown people",
                "option3": "Share bank details",
                "option4": "Pay registration fee",
                "answer": 1
            },

            {
                "question": "How can you stay safe from Telegram job scams?",
                "option1": "Never pay money for job",
                "option2": "Always pay fee",
                "option3": "Share OTP",
                "option4": "Trust strangers",
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
            self.style.SUCCESS("TELEGRAM JOB SCAM Quiz Imported Successfully")
        )
