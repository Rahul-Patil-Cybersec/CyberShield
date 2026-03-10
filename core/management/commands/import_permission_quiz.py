from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import APP PERMISSION SECURITY Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "APP PERMISSION SECURITY"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What are app permissions?",
                "option1": "Access given to apps",
                "option2": "Phone color",
                "option3": "Phone battery",
                "option4": "Phone speed",
                "answer": 1
            },

            {
                "question": "Why do apps need permissions?",
                "option1": "To access phone features",
                "option2": "To change wallpaper",
                "option3": "To increase battery",
                "option4": "To clean phone",
                "answer": 1
            },

            {
                "question": "What permission is risky for fake apps?",
                "option1": "SMS access",
                "option2": "Theme access",
                "option3": "Clock access",
                "option4": "Calculator access",
                "answer": 1
            },

            {
                "question": "Should calculator app access contacts?",
                "option1": "No",
                "option2": "Yes",
                "option3": "Always",
                "option4": "Sometimes",
                "answer": 1
            },

            {
                "question": "What can happen if you allow unnecessary permissions?",
                "option1": "Data theft",
                "option2": "Phone repair",
                "option3": "Faster internet",
                "option4": "Free reward",
                "answer": 1
            },

            {
                "question": "Where can you control app permissions?",
                "option1": "Phone settings",
                "option2": "Gallery",
                "option3": "Camera",
                "option4": "Calculator",
                "answer": 1
            },

            {
                "question": "Why do scammers want permissions?",
                "option1": "To steal information",
                "option2": "To help phone",
                "option3": "To clean storage",
                "option4": "To improve battery",
                "answer": 1
            },

            {
                "question": "What should you do before allowing permission?",
                "option1": "Check necessity",
                "option2": "Allow everything",
                "option3": "Ignore permission",
                "option4": "Trust all apps",
                "answer": 1
            },

            {
                "question": "What permission can access OTP?",
                "option1": "SMS permission",
                "option2": "Camera permission",
                "option3": "Wallpaper permission",
                "option4": "Theme permission",
                "answer": 1
            },

            {
                "question": "How can you stay safe?",
                "option1": "Allow only necessary permissions",
                "option2": "Allow all permissions",
                "option3": "Ignore security",
                "option4": "Trust unknown apps",
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
            self.style.SUCCESS("APP PERMISSION SECURITY Quiz Imported Successfully")
        )
