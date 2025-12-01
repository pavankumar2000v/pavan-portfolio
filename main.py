<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pavan Kumar V - Mechatronics Engineer</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.6.0/css/all.min.css">
  <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
  <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
  <style>
    body { font-family: 'Inter', sans-serif; background: #1a212e; color: #e2e8f0; }
    .top-bar { background: linear-gradient(135deg, #407686f1 0%, #3b82f6 100%); }
    .nav-item { transition: all 0.3s; }
    .nav-item:hover, .nav-item.active { background: rgba(100,255,218,0.2); color: #64ffda; }
    .glass { background: rgba(255,255,255,0.05); backdrop-filter: blur(12px); border: 1px solid rgba(100,255,218,0.2); }
    .card-hover { transition: all 0.3s; }
    .card-hover:hover { transform: translateY(-4px); border-color: rgba(100,255,218,0.5); }
    @media (max-width: 768px) { .nav-item { min-width: 80px; text-align: center; } }
  </style>
</head>
<body>
  <script> AOS.init({ once: true, duration: 800 }); </script>

  <!-- Top Navigation Bar (Fixed, Horizontal like GarudaWNX) -->
  <nav class="top-bar fixed top-0 left-0 right-0 z-50 flex justify-center space-x-1 px-4 py-3 shadow-lg">
    <a href="#about" class="nav-item active px-6 py-2 rounded-lg text-white font-semibold">About</a>
    <a href="#experience" class="nav-item px-6 py-2 rounded-lg text-white font-semibold">Experience</a>
    <a href="#projects" class="nav-item px-6 py-2 rounded-lg text-white font-semibold">Projects</a>
    <a href="#education" class="nav-item px-6 py-2 rounded-lg text-white font-semibold">Education</a>
    <a href="#contact" class="nav-item px-6 py-2 rounded-lg text-white font-semibold">Contact</a>
  </nav>

  <!-- Main Content (Scroll Sections) -->
  <main class="pt-20">  <!-- Padding for top bar -->
    <!-- Hero (About Section) -->
    <section id="about" class="min-h-screen flex items-center justify-center text-center px-6 bg-gradient-to-b from-[#0a192f] to-[#1a365d]" data-aos="fade-up">
      <div class="max-w-4xl">
        <h1 class="text-4xl md:text-6xl font-black mb-4 text-white">Pavan Kumar V</h1>
        <p class="text-2xl md:text-4xl mb-6 text-[#64ffda]">Mechatronics Engineer</p>
        <p class="text-xl md:text-2xl text-pink-300 mb-8">IoT & Automation | EV Battery Manufacturing</p>
        <p class="text-lg md:text-xl max-w-3xl mx-auto leading-relaxed italic text-gray-300 mb-8">
          "Live production experience in <span class="text-[#64ffda] font-bold">EV battery manufacturing</span> — deployed & supported applications connected to <span class="text-green-400 font-bold">PLC-controlled CNC machines</span>, validated real-time data with DBeaver, ensured 100% uptime on plant floor."
        </p>
        <p class="text-base md:text-lg text-pink-300 font-medium mb-6">{{ data.location }} • {{ data.phone }} • {{ data.email }}</p>
        <div class="flex justify-center gap-8 text-3xl mb-8" data-aos="zoom-in">
          <a href="https://www.linkedin.com/in/pavan-kumar-v-/" target="_blank" class="hover:scale-125 transition text-blue-400"><i class="fab fa-linkedin"></i></a>
          <a href="mailto:{{ data.email }}" class="hover:scale-125 transition text-red-400"><i class="fas fa-envelope"></i></a>
          <a href="tel:{{ data.phone }}" class="hover:scale-125 transition text-green-400"><i class="fas fa-phone"></i></a>
        </div>
      </div>
    </section>

    <!-- Professional Summary (Part of About) -->
    <section class="my-20 px-6" data-aos="fade-up">
      <h2 class="text-3xl md:text-4xl font-bold mb-8 text-[#64ffda]">Professional Summary</h2>
      <div class="glass rounded-2xl p-6 md:p-8">
        <ul class="space-y-4 text-base md:text-lg">
          {% for item in data.professional_summary %}
          <li class="flex items-start" data-aos="fade-right" data-aos-delay="{{ loop.index * 100 }}"><span class="text-[#64ffda] mr-4 flex-shrink-0">•</span> <span class="flex-1">{{ item }}</span></li>
          {% endfor %}
        </ul>
      </div>
    </section>

    <!-- Technical Skills (Part of About) -->
    <section class="my-20 px-6" data-aos="fade-up">
      <h2 class="text-3xl md:text-4xl font-bold mb-8 text-purple-400">Technical Skills</h2>
      <div class="glass rounded-2xl p-6 md:p-8 grid md:grid-cols-2 gap-6">
        {% for category, skills in data.technical_skills.items() %}
        <div data-aos="zoom-in" data-aos-delay="{{ loop.index * 100 }}"><strong class="text-purple-300 block mb-1">{{ category }}:</strong> {{ skills }}</div>
        {% endfor %}
      </div>
    </section>

    <!-- Experience -->
    <section id="experience" class="my-20 px-6" data-aos="fade-up">
      <h2 class="text-3xl md:text-4xl font-bold mb-12 text-green-400 text-center">Professional Experience</h2>
      {% for exp in data.professional_experience %}
      <div class="glass rounded-2xl p-6 md:p-10 mb-10 card-hover border-l-4 border-green-400" data-aos="fade-up" data-aos-delay="{{ loop.index * 200 }}">
        <h3 class="text-2xl md:text-3xl font-bold text-green-300 mb-2">{{ exp.title }}</h3>
        <p class="text-xl mb-2 text-white">{{ exp.company }} ({{ exp.duration }})</p>
        {% if exp.client %}<p class="text-lg opacity-80 mb-6 text-gray-300">Client: {{ exp.client }}</p>{% endif %}
        <ul class="space-y-3 text-base md:text-lg">
          {% for point in exp.responsibilities %}
          <li class="flex items-start" data-aos="fade-left" data-aos-delay="{{ loop.index * 100 }}"><span class="text-green-400 mr-4 flex-shrink-0">•</span> <span class="flex-1">{{ point }}</span></li>
          {% endfor %}
        </ul>
      </div>
      {% endfor %}
    </section>

    <!-- Projects -->
    <section id="projects" class="my-20 px-6" data-aos="fade-up">
      <h2 class="text-3xl md:text-4xl font-bold mb-12 text-pink-400 text-center">Project Experience</h2>
      <div class="grid md:grid-cols-2 gap-8">
        {% for proj in data.project_experience %}
        <div class="glass rounded-2xl p-6 md:p-8 card-hover border border-white/20" data-aos="fade-up" data-aos-delay="{{ loop.index * 150 }}">
          <h3 class="text-xl md:text-2xl font-bold mb-4 text-white">{{ proj.title }}</h3>
          <p class="text-base md:text-lg opacity-90 leading-relaxed">{{ proj.description }}</p>
        </div>
        {% endfor %}
      </div>
    </section>

    <!-- Education -->
    <section id="education" class="my-20 px-6 text-center" data-aos="fade-up">
      <h2 class="text-3xl md:text-4xl font-bold mb-12 text-yellow-400">Education</h2>
      <div class="glass rounded-2xl p-6 md:p-12 inline-block max-w-4xl">
        {% for edu in data.education %}
        <div class="mb-8 last:mb-0" data-aos="fade-up" data-aos-delay="{{ loop.index * 100 }}">
          <h3 class="text-2xl font-bold text-white">{{ edu.degree }}</h3>
          <p class="text-xl text-gray-300">{{ edu.institution }} • {{ edu.year }}</p>
          <p class="text-yellow-300 text-2xl font-bold">{{ edu.score }}</p>
        </div>
        {% endfor %}
      </div>
    </section>

    <!-- Contact -->
    <section id="contact" class="my-20 px-6 py-20 text-center" data-aos="fade-up">
      <h2 class="text-3xl md:text-4xl font-bold mb-8 text-[#64ffda]">Let's Connect</h2>
      <div class="glass rounded-2xl p-6 md:p-12 max-w-2xl mx-auto">
        <p class="text-2xl mb-6 text-white">{{ data.location }}</p>
        <p class="text-xl mb-4 text-cyan-400 font-bold">{{ data.phone }}</p>
        <p class="text-lg mb-8 text-white/80">{{ data.email }}</p>
        <div class="flex justify-center gap-8 text-4xl mb-8">
          <a href="https://www.linkedin.com/in/pavan-kumar-v-/" target="_blank" class="hover:scale-125 transition text-blue-400" data-aos="zoom-in"><i class="fab fa-linkedin"></i></a>
          <a href="mailto:{{ data.email }}" class="hover:scale-125 transition text-red-400" data-aos="zoom-in" data-aos-delay="100"><i class="fas fa-envelope"></i></a>
          <a href="tel:{{ data.phone }}" class="hover:scale-125 transition text-green-400" data-aos="zoom-in" data-aos-delay="200"><i class="fas fa-phone"></i></a>
        </div>
        <a href="/static/Pavan_Kumar_Resume.pdf" download class="inline-block bg-gradient-to-r from-[#64ffda] to-blue-600 px-8 py-4 rounded-full text-lg font-bold hover:scale-110 transition shadow-xl text-[#0a192f]">Download Resume</a>
      </div>
    </section>
  </main>

  <footer class="text-center py-8 text-gray-500 border-t border-gray-700">
    © 2025 Pavan Kumar V • All rights reserved.
  </footer>

  <script>
    // Active nav on scroll
    window.addEventListener('scroll', () => {
      const sections = document.querySelectorAll('section[id]');
      let current = '';
      sections.forEach(section => {
        const rect = section.getBoundingClientRect();
        if (rect.top <= 100 && rect.bottom >= 100) {
          current = section.id;
        }
      });
      document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.getAttribute('href') === `#${current}`) {
          item.classList.add('active');
        }
      });
    });

    // Smooth scroll for nav links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  </script>
</body>
</html>
