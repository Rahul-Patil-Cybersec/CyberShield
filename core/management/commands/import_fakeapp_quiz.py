from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import FAKE APP INSTALLATION RISK Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "FAKE APP INSTALLATION RISK"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is a fake app?",
                "option1": "App created by scammers",
                "option2": "Official bank app",
                "option3": "Phone settings app",
                "option4": "Calculator app",
                "answer": 1
            },

            {
                "question": "Where should you download apps safely?",
                "option1": "Google Play Store",
                "option2": "Unknown website",
                "option3": "Random link",
                "option4": "Social media",
                "answer": 1
            },

            {
                "question": "What can fake apps steal?",
                "option1": "Personal data",
                "option2": "Phone color",
                "option3": "Phone size",
                "option4": "Battery level",
                "answer": 1
            },

            {
                "question": "How do scammers share fake apps?",
                "option1": "Unknown links",
                "option2": "Bank branch",
                "option3": "TV",
                "option4": "Newspaper",
                "answer": 1
            },

            {
                "question": "What should you check before installing app?",
                "option1": "Reviews and developer",
                "option2": "Phone wallpaper",
                "option3": "Screen brightness",
                "option4": "Phone volume",
                "answer": 1
            },

            {
                "question": "What permission is risky to allow unnecessarily?",
                "option1": "SMS access",
                "option2": "Wallpaper access",
                "option3": "Clock access",
                "option4": "Theme access",
                "answer": 1
            },

            {
                "question": "What can happen if you install fake app?",
                "option1": "Data theft",
                "option2": "Phone cleaning",
                "option3": "Faster internet",
                "option4": "Free gift",
                "answer": 1
            },

            {
                "question": "Should you install apps from unknown sources?",
                "option1": "No",
                "option2": "Yes",
                "option3": "Always",
                "option4": "Sometimes",
                "answer": 1
            },

            {
                "question": "Why do scammers create fake apps?",
                "option1": "To steal information",
                "option2": "To help users",
                "option3": "To improve phone",
                "option4": "To increase battery",
                "answer": 1
            },

            {
                "question": "How can you stay safe from fake apps?",
                "option1": "Install apps from official stores only",
                "option2": "Install any app",
                "option3": "Trust unknown links",
                "option4": "Ignore app details",
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
            self.style.SUCCESS("FAKE APP INSTALLATION RISK Quiz Imported Successfully")
        )
