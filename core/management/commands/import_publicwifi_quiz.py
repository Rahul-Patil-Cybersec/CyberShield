from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import PUBLIC WIFI SECURITY RISK Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "PUBLIC WIFI SECURITY RISK"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is public WiFi?",
                "option1": "Free internet in public places",
                "option2": "Private home internet",
                "option3": "Bank internet",
                "option4": "Office only internet",
                "answer": 1
            },

            {
                "question": "Where is public WiFi commonly available?",
                "option1": "Cafes and airports",
                "option2": "Inside SIM card",
                "option3": "Inside battery",
                "option4": "Inside charger",
                "answer": 1
            },

            {
                "question": "Is public WiFi always secure?",
                "option1": "No",
                "option2": "Yes",
                "option3": "Always",
                "option4": "Only at night",
                "answer": 1
            },

            {
                "question": "What can hackers steal using public WiFi?",
                "option1": "Passwords and bank details",
                "option2": "Phone color",
                "option3": "Phone size",
                "option4": "Screen brightness",
                "answer": 1
            },

            {
                "question": "What should you avoid on public WiFi?",
                "option1": "Online banking",
                "option2": "Watching videos",
                "option3": "Reading news",
                "option4": "Checking weather",
                "answer": 1
            },

            {
                "question": "What is safer than public WiFi?",
                "option1": "Mobile data",
                "option2": "Unknown WiFi",
                "option3": "Fake WiFi",
                "option4": "Random WiFi",
                "answer": 1
            },

            {
                "question": "What should you check before connecting WiFi?",
                "option1": "Network name and trust",
                "option2": "Phone color",
                "option3": "Wallpaper",
                "option4": "Battery",
                "answer": 1
            },

            {
                "question": "What can fake WiFi do?",
                "option1": "Steal your data",
                "option2": "Improve phone",
                "option3": "Charge battery",
                "option4": "Clean storage",
                "answer": 1
            },

            {
                "question": "What should you turn off for safety?",
                "option1": "Auto WiFi connection",
                "option2": "Phone screen",
                "option3": "Phone sound",
                "option4": "Phone light",
                "answer": 1
            },

            {
                "question": "How can you stay safe on public WiFi?",
                "option1": "Avoid sensitive activities",
                "option2": "Share passwords",
                "option3": "Trust all networks",
                "option4": "Ignore security",
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
            self.style.SUCCESS("PUBLIC WIFI SECURITY RISK Quiz Imported Successfully")
        )
