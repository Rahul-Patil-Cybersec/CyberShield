from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import ELECTRICITY BILL SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "ELECTRICITY BILL SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is electricity bill scam?",
                "option1": "Fake message about electricity bill",
                "option2": "Real electricity bill",
                "option3": "Phone battery alert",
                "option4": "Internet message",
                "answer": 1
            },

            {
                "question": "How do scammers contact users?",
                "option1": "SMS or WhatsApp",
                "option2": "Bank branch",
                "option3": "School",
                "option4": "Office",
                "answer": 1
            },

            {
                "question": "What do scammers threaten?",
                "option1": "Electricity disconnection",
                "option2": "Phone shutdown",
                "option3": "Internet removal",
                "option4": "App removal",
                "answer": 1
            },

            {
                "question": "What do fake messages contain?",
                "option1": "Fake payment link",
                "option2": "Phone wallpaper",
                "option3": "Phone brightness",
                "option4": "Phone sound",
                "answer": 1
            },

            {
                "question": "What do scammers ask for?",
                "option1": "OTP or bank details",
                "option2": "Weather info",
                "option3": "Phone color",
                "option4": "Phone size",
                "answer": 1
            },

            {
                "question": "Should you click unknown payment links?",
                "option1": "No",
                "option2": "Yes",
                "option3": "Always",
                "option4": "Sometimes",
                "answer": 1
            },

            {
                "question": "Where should you check electricity bill safely?",
                "option1": "Official website or app",
                "option2": "Unknown link",
                "option3": "Social media",
                "option4": "Random message",
                "answer": 1
            },

            {
                "question": "What can fake apps do?",
                "option1": "Steal personal data",
                "option2": "Improve battery",
                "option3": "Fix phone",
                "option4": "Increase speed",
                "answer": 1
            },

            {
                "question": "What is safest action?",
                "option1": "Verify official source",
                "option2": "Trust unknown message",
                "option3": "Share OTP",
                "option4": "Click fake link",
                "answer": 1
            },

            {
                "question": "How can you stay safe?",
                "option1": "Never share OTP or bank details",
                "option2": "Share personal info",
                "option3": "Trust unknown callers",
                "option4": "Install unknown apps",
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
            self.style.SUCCESS("ELECTRICITY BILL SCAM Quiz Imported Successfully")
        )
