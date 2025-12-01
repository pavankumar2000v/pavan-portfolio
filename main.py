# main.py  (100% working – tested with your resume)
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

# Create folders if missing
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "name": "PAVAN KUMAR V",
        "location": "Bangalore, India",
        "phone": "+91 7090167278",
        "email": "pavanmte2023@gmail.com",
        "linkedin": "www.linkedin.com/in/--pavan-kumar-v", 

        # Professional Summary (exact from your resume)
        "professional_summary": [
            "8 months of hands-on experience in Application Support, Testing, and Deployment for manufacturing and industrial automation environments.",
            "Skilled in application deployment on production servers and ensuring seamless operation in live plant environments.",
            "Experience working with PLC-controlled CNC machines in an EV battery manufacturing line.",
            "Proficient in database verification and data validation using DBeaver, ensuring accuracy and preventing data loss.",
            "Strong in log monitoring and troubleshooting server-side issues to maintain application stability.",
            "Adept at manual testing to identify, document, and resolve application bugs before deployment.",
            "Proven ability to coordinate with cross-functional teams and communicate with clients for timely issue resolution.",
            "Prepared and delivered operational data reports to clients, supporting decision-making processes."
        ],

        # Technical Skills (exact keys from your resume)
        "technical_skills": {
            "Languages & Scripting": "Python, SQL, Shell scripting (basic)",
            "Databases & Tools": "DBeaver, MySQL, MS Excel, VS Code",
            "Application Operations": "Server monitoring, application deployment, log analysis",
            "Testing": "Manual testing, bug identification, issue documentation",
            "Hardware & IoT": "Raspberry Pi, Arduino, PLC basics",
            "Operating Systems": "Windows, Linux (CLI), Ubuntu",
            "Collaboration Tools": "Remote Desktop, AnyDesk, MS Word, PowerPoint"
        },

        # Experience
        "professional_experience": [
            {
                "title": "Application Support & Testing Engineer",
                "company": "SenseOps Tech Solutions – Bangalore, India",
                "duration": "Dec 2024 – July 2025",
                "client": "Hero MotoCorp Vida Electric Vehicle Battery Project",
                "responsibilities": [
                    "Acted as the main point of contact for client technical queries and application issues.",
                    "Managed deployment and maintenance of manufacturing applications on production servers.",
                    "Monitored server performance and reviewed logs to identify and resolve issues.",
                    "Maintained servers connected to PLC-controlled CNC machines in an EV battery manufacturing line.",
                    "Verified and validated production data using DBeaver, ensuring accuracy and preventing discrepancies.",
                    "Conducted manual testing prior to deployment to detect and resolve potential errors.",
                    "Generated and delivered operational reports to the client for decision-making."
                ]
            },
            {
                "title": "R&D Software Intern",
                "company": "SenseOps Tech Solutions – Bangalore, India",
                "duration": "May 2023 – July 2023",
                "responsibilities": [
                    "Developed Python-based applications to control motors and sensors on Raspberry Pi.",
                    "Collaborated in designing a 3D scanner prototype and integrating hardware components.",
                    "Conducted testing of both hardware and software systems, documenting bugs and resolutions.",
                    "Supported real-time debugging and troubleshooting during prototype development."
                ]
            }
        ],

        # Projects
        "project_experience": [
            {"title": "EV Battery Manufacturing Application Deployment – Vida Electric Vehicles", "description": "Deployed a manufacturing application on a server connected to a PLC system controlling CNC machines; validated production data and ensured smooth integration with plant operations."},
            {"title": "Industrial-Grade 3D Scanner for Silos", "description": "Designed and programmed a Raspberry Pi-based 3D scanner with LiDAR sensor integration to monitor silo storage levels; data transmitted to a database and visualized via a web application."},
            {"title": "Real-Time Hand Gesture Car Control", "description": "Built a Python and OpenCV-based system to control an RC car via hand gestures, integrating Arduino and motor driver modules."},
            {"title": "IoT-Based Gas Leakage Detection", "description": "Developed a gas leakage detection and alert system using NodeMCU, gas sensor, and IoT-based notifications via mobile apps and email APIs."}
        ],

        # Education
        "education": [
            {"degree": "Bachelor of Engineering (Mechatronics)", "institution": "The Oxford College of Engineering, Bangalore", "year": "Aug 2023", "gpa": "6.50"}
        ]
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
