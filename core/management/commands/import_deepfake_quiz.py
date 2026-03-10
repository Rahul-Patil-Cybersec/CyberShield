from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Import FAKE VIDEO / DEEPFAKE SCAM Quiz"


    def handle(self, *args, **kwargs):

        topic_name = "FAKE VIDEO / DEEPFAKE SCAM"

        topic, created = QuizTopic.objects.get_or_create(
            name=topic_name
        )

        questions = [

            {
                "question": "What is a deepfake video?",
                "option1": "Fake video created using AI",
                "option2": "Real video",
                "option3": "Phone camera video",
                "option4": "Security video",
                "answer": 1
            },

            {
                "question": "Who creates deepfake videos?",
                "option1": "Scammers",
                "option2": "Teachers",
                "option3": "Students",
                "option4": "Friends",
                "answer": 1
            },

            {
                "question": "Why do scammers use deepfake videos?",
                "option1": "To trick people",
                "option2": "To help users",
                "option3": "To improve security",
                "option4": "To fix phone",
                "answer": 1
            },

            {
                "question": "What may scammers ask using deepfake video?",
                "option1": "Money or personal info",
                "option2": "Weather info",
                "option3": "Phone model",
                "option4": "Phone color",
                "answer": 1
            },

            {
                "question": "Can deepfake videos look real?",
                "option1": "Yes",
                "option2": "No",
                "option3": "Never",
                "option4": "Impossible",
                "answer": 1
            },

            {
                "question": "What should you do before trusting video?",
                "option1": "Verify source",
                "option2": "Trust immediately",
                "option3": "Share OTP",
                "option4": "Send money",
                "answer": 1
            },

            {
                "question": "What should you never share based on video?",
                "option1": "OTP or bank details",
                "option2": "News",
                "option3": "Weather",
                "option4": "Time",
                "answer": 1
            },

            {
                "question": "Who can scammers impersonate?",
                "option1": "Anyone",
                "option2": "Only police",
                "option3": "Only teacher",
                "option4": "Only student",
                "answer": 1
            },

            {
                "question": "What is safest action?",
                "option1": "Confirm with real person",
                "option2": "Trust video",
                "option3": "Send money",
                "option4": "Share info",
                "answer": 1
            },

            {
                "question": "How can you stay safe from deepfake scams?",
                "option1": "Verify and stay alert",
                "option2": "Trust unknown videos",
                "option3": "Share personal info",
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
            self.style.SUCCESS("FAKE VIDEO / DEEPFAKE SCAM Quiz Imported Successfully")
        )
