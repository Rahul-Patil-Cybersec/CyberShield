from django.core.management.base import BaseCommand
from core.models import QuizTopic, Question


class Command(BaseCommand):

    help = "Load Cyber Security Quiz Questions"


    def handle(self, *args, **kwargs):

        topics = [

            "PASSWORD & 2FA SECURITY",
            "OTP SCAM AWARENESS",
            "BANK KYC UPDATE SCAM",
            "FAKE BANK CALL FRAUD",
            "QR CODE PAYMENT SCAM",
            "CARD SKIMMING FRAUD",
            "FAKE APP INSTALLATION RISK",
            "APP PERMISSION SECURITY",
            "PUBLIC WIFI SECURITY",
            "FAKE BUSINESS PAGE SCAM",
            "TELEGRAM JOB SCAM",
            "FAKE PROFILE SCAM",
            "ELECTRICITY BILL SCAM",
            "FAKE PRIZE SCAM",
            "DEEPFAKE SCAM",

        ]


        sample_questions = [

            ("What is the safest password?",
             "123456",
             "password",
             "Strong unique password",
             "abc123",
             3),

            ("Should you share OTP?",
             "Yes",
             "No",
             "Only with bank",
             "Only with friends",
             2),

            ("2FA helps protect?",
             "Nothing",
             "Account security",
             "Battery",
             "Internet speed",
             2),

            ("Phishing is?",
             "Fishing game",
             "Cyber attack",
             "Software update",
             "Antivirus",
             2),

            ("Public WiFi is?",
             "Always safe",
             "Always secure",
             "Risky",
             "Faster",
             3),

            ("Secure website starts with?",
             "http",
             "https",
             "ftp",
             "www",
             2),

            ("Fake calls ask for?",
             "OTP",
             "Password",
             "PIN",
             "All",
             4),

            ("Best security method?",
             "Weak password",
             "Strong password",
             "No password",
             "Same password",
             2),

            ("Install apps from?",
             "Unknown sites",
             "Official store",
             "Random links",
             "Email",
             2),

            ("Antivirus protects from?",
             "Malware",
             "Water",
             "Battery",
             "Screen",
             1),

        ]


        for topic_name in topics:

            topic, created = QuizTopic.objects.get_or_create(
                name=topic_name)

            for q in sample_questions:

                Question.objects.create(

                    topic=topic,
                    question=q[0],
                    option1=q[1],
                    option2=q[2],
                    option3=q[3],
                    option4=q[4],
                    correct_option=q[5]

                )

        self.stdout.write(
            self.style.SUCCESS("Quiz Questions Loaded Successfully")
        )
