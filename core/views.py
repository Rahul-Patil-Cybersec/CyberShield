from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from .models import Question, QuizResult






def home(request):
    return render(request, "core/home.html")
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def login_user(request):

    error = ""

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('/')   # home pe bhejega
        else:
            error = "Invalid Username or Password"

    return render(request, "core/login.html", {"error": error})
def register_user(request):

    error = ""

    if request.method == "POST":

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            error = "Username already exists"
        else:
            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            return redirect('/login/')

    return render(request, "core/register.html", {"error": error})

from .models import AwarenessTopic

def awareness(request):
    topics = AwarenessTopic.objects.all()
    return render(request, "core/awareness.html", {"topics": topics})

from .models import ToolUsage
from django.contrib.auth.decorators import login_required


@login_required
def password_checker(request):

    result = ""
    score = 0

    if request.method == "POST":

        password = request.POST.get("password")

        if len(password) >= 8:
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if any(c.isupper() for c in password):
            score += 1
        if any(c in "!@#$%^&*" for c in password):
            score += 1

        if score <= 1:
            result = "Weak ❌"
        elif score == 2:
            result = "Medium ⚠️"
        else:
            result = "Strong ✅"

        ToolUsage.objects.create(

        user=request.user,

        tool_name="Browser Info Checker",

        input_data="Browser check",

        result="Success"

)


    return render(request, "core/password_checker.html", {
        "result": result,
        "score": score
    })
def tools_home(request):
    return render(request, "core/tools_home.html")

import random
import string
from django.contrib.auth.decorators import login_required


@login_required
def password_generator(request):

    result = ""

    if request.method == "POST":

        length = int(request.POST.get("length", 10))

        chars = string.ascii_letters + string.digits + "!@#$%^&*"

        result = ''.join(random.choice(chars) for _ in range(length))

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Random Password Generator",
            input_data=f"length={length}",
            result=result
        )

    return render(request, "core/password_generator.html", {"result": result})

import hashlib
from django.contrib.auth.decorators import login_required


@login_required
def hash_generator(request):

    result = ""

    if request.method == "POST":

        text = request.POST.get("text")

        result = hashlib.sha256(text.encode()).hexdigest()

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Password Hash Generator",
            input_data=text,
            result=result
        )

    return render(request, "core/hash_generator.html", {"result": result})

@login_required
def password_leak_checker(request):

    result = ""

    leaked_passwords = [
        "123456",
        "password",
        "admin123",
        "qwerty",
        "rahul123",
        "welcome",
        "iloveyou"
    ]

    if request.method == "POST":

        password = request.POST.get("password")

        if password in leaked_passwords:
            result = "❌ This password is leaked! Choose another."
        else:
            result = "✅ Safe! Password not found in leaks."

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Password Leak Checker",
            input_data=password,
            result=result
        )

    return render(request, "core/password_leak_checker.html", {"result": result})

import random


@login_required
def pin_generator(request):

    result = ""

    if request.method == "POST":

        length = int(request.POST.get("length", 4))

        digits = "0123456789"

        result = ''.join(random.choice(digits) for _ in range(length))

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Secure PIN Generator",
            input_data=f"length={length}",
            result=result
        )

    return render(request, "core/pin_generator.html", {"result": result})

@login_required
def phishing_detector(request):

    result = ""

    if request.method == "POST":

        url = request.POST.get("url").lower()

        score = 0

        suspicious_words = ["login", "verify", "free", "bank", "update", "win"]

        if "@" in url:
            score += 2

        if len(url) > 50:
            score += 1

        if not url.startswith("https"):
            score += 1

        for word in suspicious_words:
            if word in url:
                score += 1

        if score >= 3:
            result = "❌ Phishing Link Detected"
        elif score == 2:
            result = "⚠️ Suspicious Link"
        else:
            result = "✅ Safe Link"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Phishing Link Detector",
            input_data=url,
            result=result
        )

    return render(request, "core/phishing_detector.html", {"result": result})

import re


@login_required
def url_scanner(request):

    result = ""

    if request.method == "POST":

        url = request.POST.get("url").lower()

        score = 0

        suspicious_words = ["login", "verify", "free", "bank", "update", "win"]

        shorteners = ["bit.ly", "tinyurl", "goo.gl"]

        # checks
        if not url.startswith("https"):
            score += 1

        if any(s in url for s in shorteners):
            score += 2

        if len(url) > 60:
            score += 1

        if re.search(r"\d+\.\d+\.\d+\.\d+", url):  # IP address
            score += 2

        for word in suspicious_words:
            if word in url:
                score += 1

        if score >= 4:
            result = "❌ Dangerous URL"
        elif score >= 2:
            result = "⚠️ Suspicious URL"
        else:
            result = "✅ Safe URL"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="URL Safety Scanner",
            input_data=url,
            result=result
        )

    return render(request, "core/url_scanner.html", {"result": result})

@login_required
def malware_checker(request):

    result = ""

    if request.method == "POST":

        file = request.FILES.get("file")

        filename = file.name.lower()
        size = file.size

        score = 0

        risky_ext = [".exe", ".bat", ".vbs", ".scr", ".cmd"]
        risky_words = ["hack", "crack", "keygen", "patch"]

        if any(filename.endswith(ext) for ext in risky_ext):
            score += 2

        if any(word in filename for word in risky_words):
            score += 2

        if size > 5 * 1024 * 1024:  # 5MB
            score += 1

        if score >= 3:
            result = "❌ Malware Detected"
        elif score >= 1:
            result = "⚠️ Suspicious File"
        else:
            result = "✅ Safe File"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Malware File Checker",
            input_data=filename,
            result=result
        )

    return render(request, "core/malware_checker.html", {"result": result})

import re


@login_required
def email_analyzer(request):

    result = ""
    details = ""

    if request.method == "POST":

        header = request.POST.get("header").lower()

        score = 0

        # count received hops
        hops = header.count("received")

        if hops > 5:
            score += 1

        if "fail" in header:
            score += 2

        if "unknown" in header:
            score += 1

        # extract IP
        ip_match = re.findall(r"\d+\.\d+\.\d+\.\d+", header)
        ip = ip_match[0] if ip_match else "Not found"

        if score >= 2:
            result = "❌ Suspicious Email Header"
        else:
            result = "✅ Safe Email"

        details = f"IP: {ip} | Hops: {hops}"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Email Header Analyzer",
            input_data="Header text",
            result=result
        )

    return render(request, "core/email_analyzer.html", {
        "result": result,
        "details": details
    })

@login_required
def fake_site_detector(request):

    result = ""

    if request.method == "POST":

        url = request.POST.get("url").lower()

        score = 0

        suspicious_words = ["login", "verify", "update", "free", "bank"]

        if "-" in url:
            score += 1

        if any(char.isdigit() for char in url):
            score += 1

        if not url.startswith("https"):
            score += 1

        if len(url) > 50:
            score += 1

        for word in suspicious_words:
            if word in url:
                score += 1

        if score >= 4:
            result = "❌ Fake Website Detected"
        elif score >= 2:
            result = "⚠️ Suspicious Website"
        else:
            result = "✅ Legit Website"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Fake Website Detector",
            input_data=url,
            result=result
        )

    return render(request, "core/fake_site_detector.html", {"result": result})

@login_required
def ip_finder(request):

    result = ""

    if request.method == "POST":

        ip = request.META.get('REMOTE_ADDR')
        browser = request.META.get('HTTP_USER_AGENT')

        result = f"IP: {ip} | Browser: {browser}"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="IP Address Finder",
            input_data="Find IP",
            result=result
        )

    return render(request, "core/ip_finder.html", {"result": result})

@login_required
def ip_location(request):

    result = ""

    if request.method == "POST":

        ip = request.META.get('REMOTE_ADDR')

        # demo static location (safe for offline project)
        city = "Mumbai"
        country = "India"
        timezone = "IST"

        result = f"IP: {ip} | {city}, {country} | {timezone}"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="IP Location Tracker",
            input_data="Detect Location",
            result=result
        )

    return render(request, "core/ip_location.html", {"result": result})

@login_required
def browser_info(request):

    result = ""

    if request.method == "POST":

        user_agent = request.META.get('HTTP_USER_AGENT')
        ip = request.META.get('REMOTE_ADDR')

        result = f"IP: {ip} | Browser Info: {user_agent}"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Browser Info Checker",
            input_data="Check Browser",
            result=result
        )

    return render(request, "core/browser_info.html", {"result": result})


@login_required
def device_info(request):

    result = ""

    if request.method == "POST":

        user_agent = request.META.get('HTTP_USER_AGENT').lower()
        ip = request.META.get('REMOTE_ADDR')

        device = "Desktop"

        if "mobile" in user_agent:
            device = "Mobile"

        elif "tablet" in user_agent:
            device = "Tablet"

        result = f"IP: {ip} | Device: {device} | Agent: {user_agent}"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Device Info Checker",
            input_data="Check Device",
            result=result
        )

    return render(request, "core/device_info.html", {"result": result})

@login_required
def cookies_viewer(request):

    result = []

    if request.method == "POST":

        cookies = request.COOKIES

        for key, value in cookies.items():
            result.append(f"{key} = {value}")

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Cookies Viewer",
            input_data="View Cookies",
            result=f"{len(result)} cookies found"
        )

    return render(request, "core/cookies_viewer.html", {"cookies": result})

@login_required
def secret_zone(request):
    return render(request, "core/secret_zone.html")



from django.contrib.auth.decorators import login_required
from .models import ToolUsage


@login_required
def secure_keyboard(request):

    result = ""

    if request.method == "POST":

        text = request.POST.get("secure_input")

        result = f"Input received ({len(text)} characters)"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Virtual Secure Keyboard",
            input_data=text,
            result=result
        )

    return render(request, "core/secure_keyboard.html", {
        "result": result
    })


from .models import SecretNote


@login_required
def notepad_locker(request):

    result = ""

    if request.method == "POST":

        note = request.POST.get("note")

        SecretNote.objects.create(
            user=request.user,
            note=note
        )

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Secret Notepad Locker",
            input_data="Secret note saved",
            result="Saved successfully"
        )

        result = "Note saved securely"

    return render(request, "core/notepad_locker.html", {
        "result": result
    })

@login_required
def hacker_terminal(request):

    output = ""

    if request.method == "POST":

        command = request.POST.get("command").lower()

        if command == "help":
            output = "Available commands: help, scan, whoami, access"

        elif command == "scan":
            output = "Scanning network... Access points found"

        elif command == "whoami":
            output = f"User: {request.user.username}"

        elif command == "access":
            output = "Access granted"

        else:
            output = "Command not recognized"

        ToolUsage.objects.create(
            user=request.user,
            tool_name="Hacker Terminal Simulator",
            input_data=command,
            result=output
        )

    return render(request, "core/hacker_terminal.html", {
        "output": output
    })

@login_required
def fake_virus(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Fake Virus Infection Simulator",
        input_data="Simulation started",
        result="Demo run"
    )

    return render(request, "core/fake_virus.html")

@login_required
def adware_simulator(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Adware Attack Simulator",
        input_data="Simulation started",
        result="Adware demo launched"
    )

    return render(request, "core/adware_simulator.html")


@login_required
def fake_virus_alert(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Fake Virus Alert Simulator",
        input_data="Alert triggered",
        result="Simulation executed"
    )

    return render(request, "core/fake_virus_alert.html")

@login_required
def fake_windows_update(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Fake Windows Update Simulator",
        input_data="Update simulation started",
        result="Fake update running"
    )

    return render(request, "core/fake_windows_update.html")

@login_required
def spyware_simulator(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Spyware Attack Simulator",
        input_data="Spyware simulation started",
        result="Fake spyware demo executed"
    )

    return render(request, "core/spyware_simulator.html")

@login_required
def keylogger_simulator(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Keylogger Simulator",
        input_data="Keylogger started",
        result="Simulation active"
    )

    return render(request, "core/keylogger_simulator.html")

@login_required
def spy_camera(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Spy Camera Simulator",
        input_data="Surveillance started",
        result="Simulation active"
    )

    return render(request, "core/spy_camera.html")

@login_required
def matrix_terminal(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Matrix Hacker Terminal",
        input_data="Matrix terminal started",
        result="Simulation running"
    )

    return render(request, "core/matrix_terminal.html")

@login_required
def hacker_typing_test(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Hacker Typing Speed Test",
        input_data="Typing test started",
        result="Simulation active"
    )

    return render(request, "core/hacker_typing_test.html")

@login_required
def ransomware_simulator(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Ransomware Attack Simulator",
        input_data="Ransomware simulation started",
        result="Files locked simulation"
    )

    return render(request, "core/ransomware_simulator.html")

@login_required
def face_scanner(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Face Scanner Simulator",
        input_data="Scan started",
        result="Face scan simulation complete"
    )

    return render(request, "core/face_scanner.html")

@login_required
def target_tracker(request):

    ToolUsage.objects.create(
        user=request.user,
        tool_name="Target Tracker Simulator",
        input_data="Tracking started",
        result="Surveillance simulation active"
    )

    return render(request, "core/target_tracker.html")

from .models import QuizTopic, Question, QuizResult
from django.contrib.auth.decorators import login_required


@login_required
def quiz_topics(request):

    topics = QuizTopic.objects.all()

    return render(request,
                  "core/quiz_topics.html",
                  {"topics": topics})



@login_required
def quiz_page(request, topic_id):

    questions = Question.objects.filter(topic_id=topic_id)

    return render(request,
                  "core/quiz_page.html",
                  {"questions": questions,
                   "topic_id": topic_id})






@login_required
def quiz_result(request):

    if request.method == "POST":

        topic_name = request.POST.get("topic")

        questions = Question.objects.filter(topic=topic_name)

        score = 0

        for q in questions:

            selected = request.POST.get(str(q.id))

            if selected and int(selected) == q.correct_option:
                score += 1


        total = questions.count()

        percentage = int((score / total) * 100) if total > 0 else 0


        if percentage >= 80:
            level = "EXPERT"
        elif percentage >= 60:
            level = "ADVANCED"
        elif percentage >= 40:
            level = "INTERMEDIATE"
        elif percentage >= 20:
            level = "BASIC"
        else:
            level = "BEGINNER"


        QuizResult.objects.create(
            user=request.user,
            topic=topic_name,
            score=score,
            total=total,
            percentage=percentage,
            security_level=level
        )


        return render(request,
                      "core/quiz_result.html",
                      {
                          "score": score,
                          "total": total,
                          "percentage": percentage,
                          "level": level
                      })

    return redirect("quiz_topics")







from django.contrib.auth.decorators import login_required
from .models import ToolUsage, QuizResult
from django.db.models import Sum


@login_required
def user_dashboard(request):

    user = request.user


    # TOOL HISTORY
    tool_history = ToolUsage.objects.filter(
        user=user
    ).order_by('-used_at')[:5]


    total_tools = ToolUsage.objects.filter(
        user=user
    ).count()


    # QUIZ HISTORY
    quiz_history = QuizResult.objects.filter(
        user=user
    ).order_by('-date')[:5]


    total_quiz = quiz_history.count()


    total_score = QuizResult.objects.filter(
        user=user
    ).aggregate(
        Sum('score')
    )['score__sum'] or 0


    avg_score = 0

    if total_quiz > 0:

        avg_score = int(total_score / total_quiz)


    # SECURITY LEVEL
    if avg_score >= 80:
        level = "Expert"
        stars = 5

    elif avg_score >= 60:
        level = "Advanced"
        stars = 4

    elif avg_score >= 40:
        level = "Intermediate"
        stars = 3

    elif avg_score >= 20:
        level = "Basic"
        stars = 2

    else:
        level = "Beginner"
        stars = 1


    context = {

        'user': user,

        'total_tools': total_tools,

        'total_quiz': total_quiz,

        'total_score': total_score,

        'avg_score': avg_score,

        'security_level': level,

        'stars': stars,

        'tool_history': tool_history,

        'quiz_history': quiz_history,

    }



    return render(
        request,
        'core/dashboard.html',
        context
    )


from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def user_logout(request):

    logout(request)

    messages.success(request, "✅ You have been logged out successfully")

    return redirect("login")
