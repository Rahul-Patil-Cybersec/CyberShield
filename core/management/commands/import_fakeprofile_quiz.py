from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import FAKE PROFILE SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "FAKE PROFILE SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is a fake profile?",
                "option1": "Fake social media account",
                "option2": "Real bank account",
                "option3": "Phone setting",
                "option4": "Email account",
                "answer": 1
            },

            {
                "question": "Where do fake profiles usually exist?",
                "option1": "Social media",
                "option2": "Calculator app",
                "option3": "Camera app",
                "option4": "Phone settings",
                "answer": 1
            },

            {
                "question": "Why do scammers create fake profiles?",
                "option1": "To steal money or data",
                "option2": "To help users",
                "option3": "To improve security",
                "option4": "To fix phone",
                "answer": 1
            },

            {
                "question": "What do scammers use in fake profiles?",
                "option1": "Fake photos and names",
                "option2": "Real bank system",
                "option3": "Phone software",
                "option4": "Antivirus",
                "answer": 1
            },

            {
                "question": "What may scammers ask from fake profile?",
                "option1": "Money or OTP",
                "option2": "Weather info",
                "option3": "Phone model",
                "option4": "Phone color",
                "answer": 1
            },

            {
                "question": "What should you do before trusting profile?",
                "option1": "Verify profile",
                "option2": "Trust immediately",
                "option3": "Share details",
                "option4": "Send money",
                "answer": 1
            },

            {
                "question": "What should you never share?",
                "option1": "Personal information",
                "option2": "News",
                "option3": "Time",
                "option4": "Weather",
                "answer": 1
            },

            {
                "question": "What can fake profiles send?",
                "option1": "Fake links",
                "option2": "Phone updates",
                "option3": "Battery updates",
                "option4": "Screen updates",
                "answer": 1
            },

            {
                "question": "What is safest action?",
                "option1": "Ignore unknown profiles",
                "option2": "Trust strangers",
                "option3": "Share OTP",
                "option4": "Send money",
                "answer": 1
            },

            {
                "question": "How can you stay safe from fake profile scams?",
                "option1": "Verify and avoid unknown profiles",
                "option2": "Trust everyone",
                "option3": "Share personal info",
                "option4": "Send money",
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
            self.style.SUCCESS("FAKE PROFILE SCAM Quiz Imported Successfully")
        )
