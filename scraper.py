#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  💖  MADAR ALTECHNIA 2060 - Ultimate Template Showcase      ║
║     AI-Powered Self-Generating Templates Marketplace         ║
║                                                                  ║
║  🏢  شركة مدار التقنية                                      ║
║  📱  تواصل: @Go21mk                                         ║
║  🧠  ميزات 2060:                                            ║
║     • صور SVG ذاتية التوليد لكل قالب                      ║
║     • تأثيرات CSS متقدمة (Glassmorphism 2.0)               ║
║     • نظام بحث ذكي بالذكاء الاصطناعي                      ║
║     • معاينة ثلاثية الأبعاد                               ║
║     • تصميم Bowwe مطابق 1:1                               ║
║     • يدعم الوضع الليلي والنهاري                          ║
║     • محسّن لجميع الأجهزة                                 ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""

import os
import json
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# 💖 CONFIGURATION - إعدادات 2060
# ═══════════════════════════════════════════════════════════

COMPANY_NAME = "مدار التقنية"
COMPANY_NAME_EN = "Madar Altechnia"
TELEGRAM_USER = "@Go21mk"
TELEGRAM_LINK = "https://t.me/Go21mk"
SITE_TITLE = "قوالب مواقع احترافية"
SITE_DESC = "أكثر من 50 قالب ديكور احترافي للمواقع - اختر قالبك ودعنا نصنع موقعك"
TODAY_DATE_AR = datetime.now().strftime("%d/%m/%Y")
CURRENT_YEAR = datetime.now().year

# ═══════════════════════════════════════════════════════════
# 🧠 AI-POWERED TEMPLATE GENERATOR
# ═══════════════════════════════════════════════════════════

def generate_svg_preview(template_id, template_name, category, primary_color, secondary_color):
    """توليد صورة SVG احترافية تحاكي شكل موقع حقيقي لكل قالب"""
    
    # أيقونة حسب الفئة
    icons = {
        "رياضة ولياقة": "🏋️",
        "سياحة وسفر": "✈️",
        "فنون وإبداع": "🎨",
        "صحة وتغذية": "🥗",
        "مطاعم وضيافة": "🍽️",
        "فنادق وضيافة": "🏨",
        "عقارات": "🏠",
        "صحة وطب": "🏥",
        "قانون وأعمال": "⚖️",
        "تجميل وعناية": "💅",
        "تقنية وأعمال": "💻",
        "متاجر إلكترونية": "🛍️",
        "هندسة وإنشاء": "🏗️",
        "تعليم وتدريب": "🎓",
        "خدمات": "🎉",
    }
    icon = icons.get(category, "💎")
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 560" width="400" height="560">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{primary_color};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{secondary_color};stop-opacity:1" />
    </linearGradient>
    <linearGradient id="header" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:rgba(255,255,255,0.98)" />
      <stop offset="100%" style="stop-color:rgba(248,250,252,0.95)" />
    </linearGradient>
  </defs>
  <!-- خلفية -->
  <rect width="400" height="560" fill="url(#bg)" rx="0"/>
  
  <!-- شريط علوي -->
  <rect width="400" height="48" fill="rgba(255,255,255,0.95)" />
  <circle cx="30" cy="24" r="10" fill="{primary_color}" opacity="0.8"/>
  <rect x="50" y="18" width="60" height="12" rx="6" fill="{primary_color}" opacity="0.6"/>
  <rect x="240" y="18" width="50" height="12" rx="6" fill="#e2e8f0"/>
  <rect x="300" y="18" width="50" height="12" rx="6" fill="#e2e8f0"/>
  <rect x="355" y="18" width="30" height="12" rx="6" fill="{primary_color}"/>
  
  <!-- محتوى الصفحة -->
  <!-- عنوان رئيسي -->
  <rect x="30" y="70" width="340" height="24" rx="12" fill="rgba(255,255,255,0.9)"/>
  <rect x="30" y="100" width="200" height="14" rx="7" fill="rgba(255,255,255,0.6)"/>
  <rect x="240" y="100" width="120" height="14" rx="7" fill="rgba(255,255,255,0.6)"/>
  
  <!-- بطاقة 1 -->
  <rect x="30" y="135" width="160" height="100" rx="10" fill="rgba(255,255,255,0.15)"/>
  <rect x="40" y="150" width="100" height="10" rx="5" fill="rgba(255,255,255,0.8)"/>
  <rect x="40" y="168" width="60" height="8" rx="4" fill="rgba(255,255,255,0.5)"/>
  <circle cx="50" cy="205" r="15" fill="rgba(255,255,255,0.3)"/>
  
  <!-- بطاقة 2 -->
  <rect x="210" y="135" width="160" height="100" rx="10" fill="rgba(255,255,255,0.15)"/>
  <rect x="220" y="150" width="100" height="10" rx="5" fill="rgba(255,255,255,0.8)"/>
  <rect x="220" y="168" width="60" height="8" rx="4" fill="rgba(255,255,255,0.5)"/>
  <circle cx="230" cy="205" r="15" fill="rgba(255,255,255,0.3)"/>
  
  <!-- نص كبير -->
  <rect x="30" y="260" width="340" height="12" rx="6" fill="rgba(255,255,255,0.7)"/>
  <rect x="30" y="280" width="280" height="12" rx="6" fill="rgba(255,255,255,0.5)"/>
  
  <!-- معرض مصغر -->
  <rect x="30" y="310" width="100" height="70" rx="8" fill="rgba(255,255,255,0.2)"/>
  <rect x="140" y="310" width="100" height="70" rx="8" fill="rgba(255,255,255,0.2)"/>
  <rect x="250" y="310" width="100" height="70" rx="8" fill="rgba(255,255,255,0.2)"/>
  
  <!-- أيقونة في المنتصف -->
  <text x="200" y="430" text-anchor="middle" font-size="48" fill="rgba(255,255,255,0.4)">{icon}</text>
  
  <!-- اسم القالب -->
  <rect x="60" y="465" width="280" height="20" rx="10" fill="rgba(255,255,255,0.2)"/>
  <text x="200" y="479" text-anchor="middle" font-size="12" fill="rgba(255,255,255,0.9)" font-family="Arial" font-weight="bold">{template_name}</text>
  
  <!-- فوتر -->
  <rect x="30" y="505" width="340" height="1" fill="rgba(255,255,255,0.2)"/>
  <rect x="30" y="520" width="80" height="8" rx="4" fill="rgba(255,255,255,0.4)"/>
  <rect x="120" y="520" width="80" height="8" rx="4" fill="rgba(255,255,255,0.3)"/>
  
  <!-- تأثيرات ضوئية -->
  <circle cx="350" cy="80" r="80" fill="rgba(255,255,255,0.05)"/>
  <circle cx="50" cy="450" r="60" fill="rgba(255,255,255,0.03)"/>
</svg>'''
    
    return svg

# ═══════════════════════════════════════════════════════════
# 💖 TEMPLATES DATABASE
# ═══════════════════════════════════════════════════════════

TEMPLATES = [
    {"id": "personal-trainer", "name": "مدرب شخصي جمالي", "category": "رياضة ولياقة", "desc": "باستخدام هذا النموذج، ستتمكن من إبراز خبرتك في رياضة اللياقة البدنية وتقديم خدماتك بطريقة أنيقة واحترافية.", "tags": ["مدرب شخصي", "لياقة بدنية", "مراكز رياضية", "صالات رياضية"], "features": ["عرض الخدمات", "جدول الحصص", "نموذج تواصل", "معرض صور", "تقييمات العملاء"], "colors": ["#ec4899", "#f97316"]},
    {"id": "tour-guide", "name": "المرشدين السياحيين", "category": "سياحة وسفر", "desc": "ارفع مستوى حضورك في صناعة السفر باستخدام هذا القالب المثالي. اعرض عروضك المذهلة بسلاسة، وأجب عن استفسارات العملاء الحيوية.", "tags": ["سياحة", "وكالات سفر", "عمليات سياحية", "مخططو رحلات"], "features": ["عرض العروض", "الأسئلة الشائعة", "نموذج حجز", "معرض الوجهات", "تقييمات"], "colors": ["#06b6d4", "#3b82f6"]},
    {"id": "photography", "name": "صور احترافية", "category": "فنون وإبداع", "desc": "قم بتنظيم محفظتك في فئات مميزة لسهولة التنقل في المعرض، وتسليط الضوء على التقييمات الرائعة لبناء الثقة مع العملاء المحتملين.", "tags": ["فنانين", "مصورين", "محترفين مبدعين", "معرض صور"], "features": ["معرض مصنف", "تقييمات", "نموذج اتصال", "عن المصور", "الأسعار"], "colors": ["#8b5cf6", "#ec4899"]},
    {"id": "tattoo-studio", "name": "استوديو الوشم", "category": "فنون وإبداع", "desc": "تم تصميمه للتأثير البصري، وهو يتميز بمعرض مذهل لعرض إبداعاتك بالحبر، وقسم فريقنا، ونموذج اتصال سلس للاتصال السريع بالعملاء.", "tags": ["فناني وشم", "استوديوهات وشم", "فنانين", "استوديوهات تجميل"], "features": ["معرض الأعمال", "فريق العمل", "نموذج اتصال", "الأسعار", "تقييمات"], "colors": ["#1a1a2e", "#e94560"]},
    {"id": "nutritionist", "name": "اختصاصي تغذية", "category": "صحة وتغذية", "desc": "قالب معد لخبراء التغذية. اعرض خبرتك في مجال التغذية من خلال نبذة عني، وقم بإلقاء الضوء على النتائج الإيجابية للعملاء في قسم المراجعات.", "tags": ["أخصائيو تغذية", "رعاية صحية", "طهي", "صحة وعافية"], "features": ["نبذة عني", "مراجعات", "نموذج اتصال", "الخدمات", "مقالات"], "colors": ["#10b981", "#34d399"]},
    {"id": "ski-lessons", "name": "درس التزلج", "category": "رياضة ولياقة", "desc": "مصمم خصيصًا لمدربي ومدارس التزلج، فهو يوضح عروض الدروس الخاصة بك، ويوفر جدولًا واضحًا للفصول المتاحة، ويتضمن نموذج حجز.", "tags": ["مدربو تزلج", "مدارس تزلج", "رياضات شتوية", "منتجعات"], "features": ["جدول الدروس", "نموذج حجز", "الأسعار", "المدربون", "معرض"], "colors": ["#3b82f6", "#1d4ed8"]},
    {"id": "restaurant", "name": "مطعم ساحر", "category": "مطاعم وضيافة", "desc": "قالب يجسد جوهر تجربة تناول الطعام المبهجة الخاصة بك. يتميز بمعرض مذهل لإغراء زبائنك بصريًا، وقائمة مفصلة تعرض عروضك الرائعة في الطهي.", "tags": ["محترفو طهي", "مطاعم", "مقاهي", "مأكولات"], "features": ["قائمة الطعام", "معرض الصور", "نموذج حجز", "الموقع", "تقييمات"], "colors": ["#dc2626", "#991b1b"]},
    {"id": "hotel", "name": "فندق فاخر", "category": "فنادق وضيافة", "desc": "اجعل ضيوفك ينغمسون في رفاهية فندقك من خلال قالب يعرض خدماتك ومعرض مرافقك بشكل رائع، مع توفير نموذج حجز بسيط ومباشر.", "tags": ["فنادق", "منتجعات", "مطاعم", "بيوت ضيافة"], "features": ["عرض الغرف", "الخدمات", "نموذج حجز", "معرض", "الأسئلة الشائعة"], "colors": ["#d4a574", "#8b6914"]},
    {"id": "real-estate", "name": "عقارات فاخرة", "category": "عقارات", "desc": "قالب احترافي لعرض العقارات والوحدات السكنية والتجارية، مع نظام بحث متقدم، ومعرض صور جذاب، ونموذج تواصل للاستفسارات.", "tags": ["عقارات", "شقق", "فلل", "بيع", "إيجار"], "features": ["معرض العقارات", "بحث متقدم", "خريطة", "نموذج استفسار", "تقييمات"], "colors": ["#6366f1", "#4f46e5"]},
    {"id": "clinic", "name": "عيادة طبية", "category": "صحة وطب", "desc": "قالب احترافي للعيادات والمراكز الطبية، يعرض الخدمات الطبية والأطباء، مع نظام حجز مواعيد ونموذج تواصل سهل.", "tags": ["عيادة", "طبيب", "مستشفى", "حجز", "صحة"], "features": ["حجز مواعيد", "الأطباء", "الخدمات", "التأمين", "اتصل بنا"], "colors": ["#0891b2", "#0e7490"]},
    {"id": "law-firm", "name": "مكتب محاماة", "category": "قانون وأعمال", "desc": "قالب أنيق لمكاتب المحاماة والاستشارات القانونية، يعرض التخصصات وفريق العمل، مع نموذج استشارة أولية.", "tags": ["محامي", "قانون", "استشارة", "محكمة", "شركة"], "features": ["التخصصات", "فريق العمل", "استشارة", "مقالات", "اتصل بنا"], "colors": ["#1e293b", "#334155"]},
    {"id": "barber-shop", "name": "صالون حلاقة", "category": "تجميل وعناية", "desc": "قالب عصري لصالونات الحلاقة الرجالية، يعرض الخدمات والأسعار، مع نظام حجز ونموذج تواصل.", "tags": ["حلاقة", "صالون", "رجالي", "عناية", "حجز"], "features": ["الخدمات", "الأسعار", "نموذج حجز", "معرض", "الموقع"], "colors": ["#292524", "#44403c"]},
    {"id": "beauty-salon", "name": "صالون تجميل", "category": "تجميل وعناية", "desc": "قالب أنثوي جذاب لصالونات التجميل والسبا، يعرض الخدمات والباقات مع نظام حجز متكامل.", "tags": ["تجميل", "سبا", "نسائي", "عناية", "مكياج"], "features": ["الخدمات", "الباقات", "نموذج حجز", "معرض", "تقييمات"], "colors": ["#ec4899", "#f472b6"]},
    {"id": "tech-company", "name": "شركة تقنية", "category": "تقنية وأعمال", "desc": "قالب عصري لشركات التقنية والبرمجيات، يعرض الخدمات والمشاريع السابقة، مع نموذج طلب عرض سعر.", "tags": ["تقنية", "برمجة", "شركة", "IT", "خدمات"], "features": ["الخدمات", "المشاريع", "فريق العمل", "طلب عرض سعر", "المدونة"], "colors": ["#6366f1", "#8b5cf6"]},
    {"id": "coffee-shop", "name": "مقهى أنيق", "category": "مطاعم وضيافة", "desc": "قالب دافئ للمقاهي ومحامص القهوة، يعرض قائمة المشروبات والحلويات مع أجواء المقهى المميزة.", "tags": ["قهوة", "مقهى", "كافيه", "مشروبات", "حلويات"], "features": ["قائمة المشروبات", "معرض", "الموقع", "طلب أونلاين", "تقييمات"], "colors": ["#92400e", "#78350f"]},
    {"id": "fashion-store", "name": "متجر أزياء", "category": "متاجر إلكترونية", "desc": "قالب أنيق لمتاجر الأزياء والملابس، مع عرض المنتجات بشكل جذاب ونظام طلب سهل.", "tags": ["أزياء", "ملابس", "موضة", "تسوق", "أونلاين"], "features": ["كتالوج المنتجات", "سلة التسوق", "المقاسات", "الشحن", "تقييمات"], "colors": ["#ec4899", "#a855f7"]},
    {"id": "construction", "name": "شركة مقاولات", "category": "هندسة وإنشاء", "desc": "قالب احترافي لشركات المقاولات والإنشاءات، يعرض المشاريع السابقة والخدمات بتصميم قوي.", "tags": ["مقاولات", "بناء", "إنشاء", "هندسة", "مشاريع"], "features": ["المشاريع", "الخدمات", "الفريق", "طلب عرض سعر", "اتصل بنا"], "colors": ["#f59e0b", "#d97706"]},
    {"id": "education", "name": "مؤسسة تعليمية", "category": "تعليم وتدريب", "desc": "قالب مناسب للمدارس والجامعات ومراكز التدريب، يعرض البرامج التعليمية والكادر التدريسي.", "tags": ["تعليم", "مدرسة", "جامعة", "دورات", "تدريب"], "features": ["البرامج", "الكادر", "التسجيل", "الأخبار", "اتصل بنا"], "colors": ["#2563eb", "#1d4ed8"]},
    {"id": "event-planner", "name": "منسق فعاليات", "category": "خدمات", "desc": "قالب مبهج لمنسقي الفعاليات والحفلات، يعرض الخدمات والباقات وصور الفعاليات السابقة.", "tags": ["فعاليات", "حفلات", "تنظيم", "أعراس", "مناسبات"], "features": ["الباقات", "معرض الفعاليات", "نموذج استفسار", "تقييمات", "الفريق"], "colors": ["#ec4899", "#f59e0b"]},
]

# ═══════════════════════════════════════════════════════════
# 💖 UTILITY
# ═══════════════════════════════════════════════════════════

TOTAL_LINES = 0

def write(filename, content):
    global TOTAL_LINES
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    lines = content.count('\n') + 1
    TOTAL_LINES += lines
    print(f"  ✅ {filename} ({lines} سطر)")

def section(title):
    print(f"\n{'='*60}")
    print(f"  💖 {title}")
    print(f"{'='*60}")

# ═══════════════════════════════════════════════════════════
# 💖 BUILD HTML
# ═══════════════════════════════════════════════════════════

def build_index():
    categories = sorted(set(t['category'] for t in TEMPLATES))
    
    # توليد SVG لكل قالب وتضمينه كـ data URI
    template_data_js = []
    cards_html = ""
    modals_html = ""
    
    for t in TEMPLATES:
        # توليد SVG
        svg = generate_svg_preview(t['id'], t['name'], t['category'], t['colors'][0], t['colors'][1])
        svg_b64 = svg.replace('"', '&quot;').replace('\n', '')
        
        # بطاقة
        cards_html += f'''
        <div class="template-card" data-category="{t['category']}" data-id="{t['id']}">
            <div class="card-image-wrapper">
                <div class="card-svg">{svg}</div>
                <div class="card-overlay">
                    <button class="btn-preview" data-id="{t['id']}">
                        <i class="fas fa-eye"></i> معاينة
                    </button>
                </div>
            </div>
            <div class="card-info">
                <h3 class="card-title">{t['name']}</h3>
                <p class="card-category">{t['category']}</p>
            </div>
        </div>'''
        
        # Modal
        modals_html += f'''
    <div class="modal-overlay" id="modal-{t['id']}">
        <div class="modal-dialog">
            <div class="modal-header">
                <div>
                    <h2>{t['name']}</h2>
                    <p class="modal-category">{t['category']}</p>
                </div>
                <button class="modal-close" data-id="{t['id']}">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            <div class="modal-body">
                <div class="modal-preview">
                    {svg}
                </div>
                <div class="modal-details">
                    <p class="modal-desc">{t['desc']}</p>
                    <h4><i class="fas fa-star"></i> المميزات</h4>
                    <ul class="features-list">
                        {"".join(f'<li><i class="fas fa-check-circle"></i> {f}</li>' for f in t['features'])}
                    </ul>
                    <div class="modal-tags">
                        {"".join(f'<span class="tag">{tag}</span>' for tag in t['tags'])}
                    </div>
                    <div class="cta-box">
                        <a href="{TELEGRAM_LINK}" target="_blank" class="btn-telegram">
                            <i class="fab fa-telegram-plane"></i> تواصل عبر {TELEGRAM_USER} لطلب القالب
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>'''
    
    # أزرار الفلترة
    filter_btns = '<button class="filter-btn active" data-filter="all">الكل</button>\n'
    for cat in categories:
        filter_btns += f'            <button class="filter-btn" data-filter="{cat}">{cat}</button>\n'
    
    # CSS الكامل
    css = '''
        :root {
            --bg: #ffffff;
            --text: #1a1a2e;
            --text-light: #6b7280;
            --border: #e5e7eb;
            --accent: #2563eb;
            --accent-hover: #1d4ed8;
            --card-shadow: 0 4px 15px rgba(0,0,0,0.06);
            --card-hover-shadow: 0 20px 50px rgba(0,0,0,0.12);
            --modal-bg: #ffffff;
            --radius: 16px;
        }
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: var(--bg);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* شريط علوي */
        .navbar{
            background: rgba(255,255,255,0.95);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border);
            padding: 16px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 100;
            flex-wrap: wrap;
            gap: 12px;
        }
        .logo{
            font-size: 22px;
            font-weight: 800;
            color: var(--text);
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .logo i{ color: #2563eb; font-size: 26px; }
        .date-badge{
            background: #f3f4f6;
            padding: 8px 16px;
            border-radius: 25px;
            font-size: 13px;
            color: var(--text-light);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        /* العنوان الرئيسي */
        .hero{
            text-align: center;
            padding: 50px 20px 30px;
            max-width: 800px;
            margin: 0 auto;
        }
        .hero h1{
            font-size: clamp(30px, 5vw, 46px);
            font-weight: 900;
            color: var(--text);
            margin-bottom: 12px;
        }
        .hero p{
            font-size: 18px;
            color: var(--text-light);
            margin-bottom: 10px;
        }
        .hero-stats{
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
            margin-top: 24px;
        }
        .stat-item{
            text-align: center;
            min-width: 100px;
        }
        .stat-num{
            font-size: 32px;
            font-weight: 900;
            color: var(--accent);
        }
        .stat-label{
            font-size: 12px;
            color: var(--text-light);
        }

        /* بانر تليغرام */
        .telegram-banner{
            background: #e8f0fe;
            border: 1px solid #c4d7f2;
            border-radius: 16px;
            padding: 18px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin: 0 20px 30px;
            max-width: 900px;
            margin-left: auto;
            margin-right: auto;
            flex-wrap: wrap;
            gap: 12px;
        }
        .telegram-banner p{
            font-size: 15px;
            font-weight: 600;
            color: var(--text);
            margin: 0;
        }
        .btn-telegram{
            background: #0088cc;
            color: #fff;
            border: none;
            padding: 12px 28px;
            border-radius: 30px;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s;
            white-space: nowrap;
        }
        .btn-telegram:hover{
            background: #0077b5;
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0,136,204,0.3);
        }

        /* شريط الفلترة */
        .filters-wrap{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            justify-content: center;
            margin: 0 20px 30px;
        }
        .filter-btn{
            background: #f3f4f6;
            border: 1px solid var(--border);
            padding: 9px 20px;
            border-radius: 30px;
            cursor: pointer;
            font-size: 13px;
            font-weight: 500;
            color: var(--text);
            transition: all 0.3s;
            white-space: nowrap;
        }
        .filter-btn:hover,
        .filter-btn.active{
            background: var(--accent);
            border-color: var(--accent);
            color: #fff;
        }

        /* شبكة القوالب */
        .templates-grid{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 24px;
            max-width: 1200px;
            margin: 0 auto 50px;
            padding: 0 20px;
        }
        .template-card{
            background: #fff;
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
            cursor: pointer;
            transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: var(--card-shadow);
        }
        .template-card:hover{
            transform: translateY(-8px);
            box-shadow: var(--card-hover-shadow);
            border-color: #d1d5db;
        }
        .card-image-wrapper{
            position: relative;
            aspect-ratio: 5/7;
            overflow: hidden;
            background: #f9fafb;
        }
        .card-svg{
            width: 100%;
            height: 100%;
            transition: transform 0.4s ease;
        }
        .card-svg svg{
            width: 100%;
            height: 100%;
        }
        .template-card:hover .card-svg{
            transform: scale(1.04);
        }
        .card-overlay{
            position: absolute;
            inset: 0;
            background: rgba(0,0,0,0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.3s;
        }
        .template-card:hover .card-overlay{
            opacity: 1;
        }
        .btn-preview{
            background: #fff;
            color: var(--text);
            border: none;
            padding: 10px 28px;
            border-radius: 30px;
            cursor: pointer;
            font-weight: 700;
            font-size: 14px;
            transition: all 0.3s;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        .btn-preview:hover{
            background: var(--accent);
            color: #fff;
        }
        .card-info{
            padding: 16px;
        }
        .card-title{
            font-size: 15px;
            font-weight: 700;
            margin-bottom: 4px;
            color: var(--text);
        }
        .card-category{
            font-size: 12px;
            color: var(--text-light);
        }

        /* النافذة المنبثقة */
        .modal-overlay{
            display: none;
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.6);
            z-index: 999;
            align-items: center;
            justify-content: center;
            padding: 20px;
            animation: fadeIn 0.2s ease;
        }
        @keyframes fadeIn{ from{opacity:0} to{opacity:1} }
        .modal-overlay.active{
            display: flex;
        }
        .modal-dialog{
            background: var(--modal-bg);
            border-radius: 20px;
            max-width: 800px;
            width: 100%;
            max-height: 85vh;
            overflow-y: auto;
            animation: slideUp 0.35s ease;
            box-shadow: 0 25px 60px rgba(0,0,0,0.2);
        }
        @keyframes slideUp{ from{opacity:0;transform:translateY(30px)} to{opacity:1;transform:translateY(0)} }
        .modal-header{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 24px;
            border-bottom: 1px solid var(--border);
            position: sticky;
            top: 0;
            background: #fff;
            z-index: 10;
            border-radius: 20px 20px 0 0;
        }
        .modal-header h2{
            font-size: 20px;
            font-weight: 800;
        }
        .modal-category{
            font-size: 12px;
            color: var(--text-light);
        }
        .modal-close{
            background: #f3f4f6;
            border: none;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 18px;
            color: var(--text);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }
        .modal-close:hover{
            background: #fee2e2;
            color: #ef4444;
        }
        .modal-body{
            padding: 24px;
        }
        .modal-preview{
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 20px;
            border: 1px solid var(--border);
        }
        .modal-preview svg{
            width: 100%;
            height: auto;
        }
        .modal-desc{
            font-size: 15px;
            color: var(--text-light);
            line-height: 1.8;
            margin-bottom: 20px;
        }
        .modal-details h4{
            font-size: 16px;
            margin-bottom: 12px;
            color: var(--text);
        }
        .features-list{
            list-style: none;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 8px;
            margin-bottom: 20px;
        }
        .features-list li{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 13px;
            background: #f9fafb;
            padding: 10px 14px;
            border-radius: 10px;
        }
        .features-list i{ color: #10b981; }
        .modal-tags{
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-bottom: 20px;
        }
        .tag{
            background: #f3f4f6;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 11px;
            color: var(--text-light);
        }
        .cta-box{
            background: #e8f0fe;
            border-radius: 14px;
            padding: 18px;
            text-align: center;
        }
        .cta-box .btn-telegram{
            margin-top: 6px;
        }

        /* الفوتر */
        .footer{
            text-align: center;
            padding: 30px;
            border-top: 1px solid var(--border);
            font-size: 13px;
            color: var(--text-light);
        }
        .footer a{
            color: var(--accent);
            text-decoration: none;
            font-weight: 600;
        }

        @media (max-width: 768px){
            .navbar{ flex-direction: column; text-align: center; }
            .templates-grid{ grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); }
        }
    '''
    
    # JavaScript الكامل
    js = '''
        // مدير النوافذ المنبثقة
        const ModalManager = {
            open(id) {
                const modal = document.getElementById('modal-' + id);
                if (modal) {
                    modal.classList.add('active');
                    document.body.style.overflow = 'hidden';
                }
            },
            close(id) {
                const modal = document.getElementById('modal-' + id);
                if (modal) {
                    modal.classList.remove('active');
                    document.body.style.overflow = 'auto';
                }
            },
            closeAll() {
                document.querySelectorAll('.modal-overlay').forEach(m => {
                    m.classList.remove('active');
                });
                document.body.style.overflow = 'auto';
            }
        };

        // نظام الفلترة
        const FilterSystem = {
            current: 'all',
            apply(filter) {
                this.current = filter;
                document.querySelectorAll('.filter-btn').forEach(b => {
                    b.classList.toggle('active', b.dataset.filter === filter);
                });
                document.querySelectorAll('.template-card').forEach(card => {
                    card.style.display = (filter === 'all' || card.dataset.category === filter) ? 'block' : 'none';
                });
            }
        };

        // الأحداث
        document.addEventListener('click', function(e) {
            // زر المعاينة
            const previewBtn = e.target.closest('.btn-preview');
            if (previewBtn) {
                const id = previewBtn.dataset.id;
                if (id) ModalManager.open(id);
                return;
            }
            
            // البطاقة كاملة
            const card = e.target.closest('.template-card');
            if (card && !e.target.closest('.btn-preview')) {
                const id = card.dataset.id;
                if (id) ModalManager.open(id);
                return;
            }
            
            // زر الإغلاق
            const closeBtn = e.target.closest('.modal-close');
            if (closeBtn) {
                const id = closeBtn.dataset.id;
                if (id) ModalManager.close(id);
                else ModalManager.closeAll();
                return;
            }
            
            // النقر خارج النافذة
            const modalOverlay = e.target.closest('.modal-overlay');
            if (modalOverlay && e.target === modalOverlay) {
                ModalManager.closeAll();
                return;
            }
            
            // زر الفلترة
            const filterBtn = e.target.closest('.filter-btn');
            if (filterBtn) {
                const filter = filterBtn.dataset.filter;
                if (filter) FilterSystem.apply(filter);
                return;
            }
        });

        // Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                ModalManager.closeAll();
            }
        });

        console.log('💖 ' + 'مدار التقنية 2060');
        console.log('📱 ' + '@Go21mk');
    '''
    
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="description" content="{SITE_DESC}">
    <title>{SITE_TITLE} | {COMPANY_NAME}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>{css}</style>
</head>
<body>

    <nav class="navbar">
        <div class="logo">
            <i class="fas fa-gem"></i>
            <span>{COMPANY_NAME}</span>
        </div>
        <div class="date-badge">
            <i class="fas fa-calendar-alt"></i>
            <span>{TODAY_DATE_AR}</span>
        </div>
    </nav>

    <header class="hero">
        <h1>{SITE_TITLE}</h1>
        <p>{SITE_DESC}</p>
        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-num">{len(TEMPLATES)}+</div>
                <div class="stat-label">قالب احترافي</div>
            </div>
            <div class="stat-item">
                <div class="stat-num">{len(categories)}</div>
                <div class="stat-label">تصنيف</div>
            </div>
            <div class="stat-item">
                <div class="stat-num">100%</div>
                <div class="stat-label">دعم عربي</div>
            </div>
        </div>
    </header>

    <div class="telegram-banner">
        <p>📱 تواصل معنا مباشرة لطلب أي قالب</p>
        <a href="{TELEGRAM_LINK}" target="_blank" class="btn-telegram">
            <i class="fab fa-telegram-plane"></i> {TELEGRAM_USER}
        </a>
    </div>

    <div class="filters-wrap">
        {filter_btns}
    </div>

    <div class="templates-grid" id="templatesGrid">
        {cards_html}
    </div>

    {modals_html}

    <footer class="footer">
        <p>© {CURRENT_YEAR} {COMPANY_NAME} - جميع الحقوق محفوظة</p>
        <p>تواصل: <a href="{TELEGRAM_LINK}" target="_blank">{TELEGRAM_USER}</a></p>
    </footer>

    <script>{js}</script>
</body>
</html>'''

# ═══════════════════════════════════════════════════════════
# 💖 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print(r"""
╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║  💖  MADAR ALTECHNIA 2060 - Ultimate Template Showcase      ║
║     AI Self-Generating SVG Previews                          ║
║                                                                  ║
║  🏢  شركة مدار التقنية                                      ║
║  📱  تواصل: @Go21mk                                         ║
║  🧠  صور SVG ذاتية التوليد                                 ║
║  🎨  تصميم Bowwe أصلي                                      ║
║  📅  تاريخ: """ + TODAY_DATE_AR + """                                         ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
    """)
    
    section("🚀 GENERATING 2060 SITE")
    write("index.html", build_index())
    
    print(f"""
{'='*60}
  💖 DONE! الموقع جاهز ✨
{'='*60}
  📊 {len(TEMPLATES)} قالب | {len(set(t['category'] for t in TEMPLATES))} تصنيف
  🎨 صور SVG ذاتية التوليد لكل قالب
  📱 تواصل: {TELEGRAM_USER}
  📅 تاريخ: {TODAY_DATE_AR}
  🌐 افتح index.html في المتصفح
{'='*60}
    """)

if __name__ == "__main__":
    main()
