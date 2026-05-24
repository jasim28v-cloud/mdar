#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                            ║
║  💖  MADAR ALTECHNIA - قوالب مواقع احترافية  💖           ║
║     Website Templates Showcase Generator                   ║
║                                                            ║
║  🏢  شركة مدار التقنية                                    ║
║  📱  تواصل: @Go21mk على تليغرام                          ║
║  📅  تاريخ اليوم مدمج تلقائي                              ║
║  🎨  جميع قوالب الديكور للمواقع                           ║
║                                                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
from datetime import datetime

# ═══════════════════════════════════════════════════════════
# 💖 CONFIGURATION - الإعدادات
# ═══════════════════════════════════════════════════════════

COMPANY_NAME = "مدار التقنية"
COMPANY_NAME_EN = "Madar Altechnia"
TELEGRAM_USER = "@Go21mk"
TELEGRAM_LINK = "https://t.me/Go21mk"
SITE_TITLE = "قوالب مواقع احترافية"
SITE_DESC = "أكثر من 50 قالب ديكور احترافي للمواقع - اختر قالبك ودعنا نصنع موقعك"
TODAY_DATE = datetime.now().strftime("%Y-%m-%d")
TODAY_DATE_AR = datetime.now().strftime("%d/%m/%Y")

# 💖 قائمة القوالب - جميع قوالب الديكور
TEMPLATES = [
    {
        "id": "personal-trainer",
        "name": "مدرب شخصي جمالي",
        "icon": "🏋️",
        "category": "رياضة ولياقة",
        "color": "linear-gradient(135deg, #ec4899, #f97316)",
        "desc": "قالب احترافي للمدربين الشخصيين ومدربي اللياقة البدنية والمراكز الرياضية وأصحاب الصالات الرياضية. يعرض خبرتك في رياضة اللياقة البدنية ويقدم خدماتك بطريقة أنيقة.",
        "tags": ["مدرب شخصي", "لياقة", "رياضة", "جيم", "صالة رياضية"],
        "features": ["عرض الخدمات", "جدول الحصص", "نموذج تواصل", "معرض صور", "تقييمات العملاء"],
        "preview_url": "https://placehold.co/600x400/ec4899/white?text=مدرب+شخصي"
    },
    {
        "id": "tour-guide",
        "name": "المرشدين السياحيين",
        "icon": "✈️",
        "category": "سياحة وسفر",
        "color": "linear-gradient(135deg, #06b6d4, #3b82f6)",
        "desc": "ارفع مستوى حضورك في صناعة السفر. اعرض عروضك المذهلة بسلاسة، وأجب عن استفسارات العملاء من خلال قسم الأسئلة الشائعة المفصل، ونموذج حجز سهل.",
        "tags": ["سياحة", "سفر", "مرشد سياحي", "وكالة سفر", "رحلات"],
        "features": ["عرض العروض", "الأسئلة الشائعة", "نموذج حجز", "معرض الوجهات", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/06b6d4/white?text=مرشد+سياحي"
    },
    {
        "id": "photography",
        "name": "صور احترافية",
        "icon": "📸",
        "category": "فنون وإبداع",
        "color": "linear-gradient(135deg, #8b5cf6, #ec4899)",
        "desc": "نظّم محفظتك في فئات مميزة لسهولة التنقل في المعرض، وسلط الضوء على التقييمات الرائعة لبناء الثقة مع العملاء المحتملين، مع نموذج اتصال مباشر.",
        "tags": ["تصوير", "مصور", "معرض صور", "بورتفوليو", "فوتوغرافي"],
        "features": ["معرض مصنف", "تقييمات", "نموذج تواصل", "عنّي", "الأسعار"],
        "preview_url": "https://placehold.co/600x400/8b5cf6/white?text=تصوير+احترافي"
    },
    {
        "id": "tattoo-studio",
        "name": "استوديو الوشم",
        "icon": "🎨",
        "category": "فنون وإبداع",
        "color": "linear-gradient(135deg, #1a1a2e, #e94560)",
        "desc": "تصميم للتأثير البصري، يتميز بمعرض مذهل لعرض إبداعاتك، وقسم فريقنا، ونموذج اتصال سلس. مثالي للاستوديوهات التي ترغب في الإدلاء ببيان جريء.",
        "tags": ["وشم", "تاتو", "استوديو", "فن", "تجميل"],
        "features": ["معرض الأعمال", "فريق العمل", "نموذج حجز", "الأسعار", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/1a1a2e/white?text=استوديو+وشم"
    },
    {
        "id": "nutritionist",
        "name": "اختصاصي تغذية",
        "icon": "🥗",
        "category": "صحة وتغذية",
        "color": "linear-gradient(135deg, #10b981, #34d399)",
        "desc": "قالب معد لخبراء التغذية. اعرض خبرتك من خلال نبذة عني، وأبرز النتائج الإيجابية للعملاء في قسم المراجعات، واتصل بسهولة باستخدام نموذج اتصال مباشر.",
        "tags": ["تغذية", "صحة", "دايت", "أخصائي", "حمية"],
        "features": ["نبذة عني", "مراجعات", "نموذج تواصل", "الخدمات", "مقالات"],
        "preview_url": "https://placehold.co/600x400/10b981/white?text=اختصاصي+تغذية"
    },
    {
        "id": "ski-lessons",
        "name": "درس التزلج",
        "icon": "⛷️",
        "category": "رياضة ولياقة",
        "color": "linear-gradient(135deg, #3b82f6, #1d4ed8)",
        "desc": "مصمم خصيصًا لمدربي ومدارس التزلج، يوضح عروض الدروس الخاصة بك، ويوفر جدولًا واضحًا للفصول المتاحة، ويتضمن نموذج حجز سلس للمتعلمين.",
        "tags": ["تزلج", "رياضة شتوية", "منتجع", "تدريب", "تزلج على الجليد"],
        "features": ["جدول الدروس", "نموذج حجز", "الأسعار", "المدربون", "معرض"],
        "preview_url": "https://placehold.co/600x400/3b82f6/white?text=درس+تزلج"
    },
    {
        "id": "restaurant",
        "name": "مطعم ساحر",
        "icon": "🍽️",
        "category": "مطاعم وضيافة",
        "color": "linear-gradient(135deg, #dc2626, #991b1b)",
        "desc": "يجسد جوهر تجربة تناول الطعام المبهجة. يتميز بمعرض مذهل لإغراء زبائنك بصريًا، وقائمة مفصلة تعرض عروضك الرائعة في الطهي، ونموذج حجز سهل.",
        "tags": ["مطعم", "كافيه", "طعام", "قائمة", "حجز"],
        "features": ["قائمة الطعام", "معرض الصور", "نموذج حجز", "الموقع", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/dc2626/white?text=مطعم+ساحر"
    },
    {
        "id": "hotel",
        "name": "فندق فاخر",
        "icon": "🏨",
        "category": "فنادق وضيافة",
        "color": "linear-gradient(135deg, #d4a574, #8b6914)",
        "desc": "اجعل ضيوفك ينغمسون في رفاهية فندقك من خلال قالب يعرض خدماتك ومعرض مرافقك بشكل رائع، مع توفير نموذج حجز بسيط ومباشر.",
        "tags": ["فندق", "منتجع", "حجز", "غرف", "ضيافة"],
        "features": ["عرض الغرف", "الخدمات", "نموذج حجز", "معرض", "الأسئلة الشائعة"],
        "preview_url": "https://placehold.co/600x400/d4a574/white?text=فندق+فاخر"
    },
    {
        "id": "real-estate",
        "name": "عقارات فاخرة",
        "icon": "🏠",
        "category": "عقارات",
        "color": "linear-gradient(135deg, #6366f1, #4f46e5)",
        "desc": "قالب احترافي لعرض العقارات والوحدات السكنية والتجارية، مع نظام بحث متقدم، ومعرض صور جذاب، ونموذج تواصل للاستفسارات.",
        "tags": ["عقارات", "شقق", "فلل", "بيع", "إيجار"],
        "features": ["معرض العقارات", "بحث متقدم", "خريطة", "نموذج استفسار", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/6366f1/white?text=عقارات+فاخرة"
    },
    {
        "id": "clinic",
        "name": "عيادة طبية",
        "icon": "🏥",
        "category": "صحة وطب",
        "color": "linear-gradient(135deg, #0891b2, #0e7490)",
        "desc": "قالب احترافي للعيادات والمراكز الطبية، يعرض الخدمات الطبية والأطباء، مع نظام حجز مواعيد ونموذج تواصل سهل.",
        "tags": ["عيادة", "طبيب", "مستشفى", "حجز", "صحة"],
        "features": ["حجز مواعيد", "الأطباء", "الخدمات", "التأمين", "اتصل بنا"],
        "preview_url": "https://placehold.co/600x400/0891b2/white?text=عيادة+طبية"
    },
    {
        "id": "law-firm",
        "name": "مكتب محاماة",
        "icon": "⚖️",
        "category": "قانون وأعمال",
        "color": "linear-gradient(135deg, #1e293b, #334155)",
        "desc": "قالب أنيق لمكاتب المحاماة والاستشارات القانونية، يعرض التخصصات وفريق العمل، مع نموذج استشارة أولية.",
        "tags": ["محامي", "قانون", "استشارة", "محكمة", "شركة"],
        "features": ["التخصصات", "فريق العمل", "استشارة", "مقالات", "اتصل بنا"],
        "preview_url": "https://placehold.co/600x400/1e293b/white?text=مكتب+محاماة"
    },
    {
        "id": "barber-shop",
        "name": "صالون حلاقة",
        "icon": "💈",
        "category": "تجميل وعناية",
        "color": "linear-gradient(135deg, #292524, #44403c)",
        "desc": "قالب عصري لصالونات الحلاقة الرجالية، يعرض الخدمات والأسعار، مع نظام حجز ونموذج تواصل.",
        "tags": ["حلاقة", "صالون", "رجالي", "عناية", "حجز"],
        "features": ["الخدمات", "الأسعار", "نموذج حجز", "معرض", "الموقع"],
        "preview_url": "https://placehold.co/600x400/292524/white?text=صالون+حلاقة"
    },
    {
        "id": "car-dealer",
        "name": "معرض سيارات",
        "icon": "🚗",
        "category": "سيارات",
        "color": "linear-gradient(135deg, #dc2626, #7f1d1d)",
        "desc": "قالب احترافي لمعارض السيارات، يعرض المخزون مع إمكانية البحث والتصفية، ونموذج طلب تجربة قيادة.",
        "tags": ["سيارات", "معرض", "بيع", "جديد", "مستعمل"],
        "features": ["معرض السيارات", "بحث", "تجربة قيادة", "تمويل", "اتصل بنا"],
        "preview_url": "https://placehold.co/600x400/dc2626/white?text=معرض+سيارات"
    },
    {
        "id": "beauty-salon",
        "name": "صالون تجميل",
        "icon": "💅",
        "category": "تجميل وعناية",
        "color": "linear-gradient(135deg, #ec4899, #f472b6)",
        "desc": "قالب أنثوي جذاب لصالونات التجميل والسبا، يعرض الخدمات والباقات مع نظام حجز متكامل.",
        "tags": ["تجميل", "سبا", "نسائي", "عناية", "مكياج"],
        "features": ["الخدمات", "الباقات", "نموذج حجز", "معرض", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/ec4899/white?text=صالون+تجميل"
    },
    {
        "id": "tech-company",
        "name": "شركة تقنية",
        "icon": "💻",
        "category": "تقنية وأعمال",
        "color": "linear-gradient(135deg, #6366f1, #8b5cf6)",
        "desc": "قالب عصري لشركات التقنية والبرمجيات، يعرض الخدمات والمشاريع السابقة، مع نموذج طلب عرض سعر.",
        "tags": ["تقنية", "برمجة", "شركة", "IT", "خدمات"],
        "features": ["الخدمات", "المشاريع", "فريق العمل", "طلب عرض سعر", "المدونة"],
        "preview_url": "https://placehold.co/600x400/6366f1/white?text=شركة+تقنية"
    },
    {
        "id": "coffee-shop",
        "name": "مقهى أنيق",
        "icon": "☕",
        "category": "مطاعم وضيافة",
        "color": "linear-gradient(135deg, #92400e, #78350f)",
        "desc": "قالب دافئ للمقاهي ومحامص القهوة، يعرض قائمة المشروبات والحلويات مع أجواء المقهى المميزة.",
        "tags": ["قهوة", "مقهى", "كافيه", "مشروبات", "حلويات"],
        "features": ["قائمة المشروبات", "معرض", "الموقع", "طلب أونلاين", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/92400e/white?text=مقهى+أنيق"
    },
    {
        "id": "fashion-store",
        "name": "متجر أزياء",
        "icon": "👗",
        "category": "متاجر إلكترونية",
        "color": "linear-gradient(135deg, #ec4899, #a855f7)",
        "desc": "قالب أنيق لمتاجر الأزياء والملابس، مع عرض المنتجات بشكل جذاب ونظام طلب سهل.",
        "tags": ["أزياء", "ملابس", "موضة", "تسوق", "أونلاين"],
        "features": ["كتالوج المنتجات", "سلة التسوق", "المقاسات", "الشحن", "تقييمات"],
        "preview_url": "https://placehold.co/600x400/ec4899/white?text=متجر+أزياء"
    },
    {
        "id": "construction",
        "name": "شركة مقاولات",
        "icon": "🏗️",
        "category": "هندسة وإنشاء",
        "color": "linear-gradient(135deg, #f59e0b, #d97706)",
        "desc": "قالب احترافي لشركات المقاولات والإنشاءات، يعرض المشاريع السابقة والخدمات بتصميم قوي.",
        "tags": ["مقاولات", "بناء", "إنشاء", "هندسة", "مشاريع"],
        "features": ["المشاريع", "الخدمات", "الفريق", "طلب عرض سعر", "اتصل بنا"],
        "preview_url": "https://placehold.co/600x400/f59e0b/white?text=مقاولات"
    },
    {
        "id": "education",
        "name": "مؤسسة تعليمية",
        "icon": "🎓",
        "category": "تعليم وتدريب",
        "color": "linear-gradient(135deg, #2563eb, #1d4ed8)",
        "desc": "قالب مناسب للمدارس والجامعات ومراكز التدريب، يعرض البرامج التعليمية والكادر التدريسي.",
        "tags": ["تعليم", "مدرسة", "جامعة", "دورات", "تدريب"],
        "features": ["البرامج", "الكادر", "التسجيل", "الأخبار", "اتصل بنا"],
        "preview_url": "https://placehold.co/600x400/2563eb/white?text=تعليم"
    },
    {
        "id": "event-planner",
        "name": "منسق فعاليات",
        "icon": "🎉",
        "category": "خدمات",
        "color": "linear-gradient(135deg, #ec4899, #f59e0b)",
        "desc": "قالب مبهج لمنسقي الفعاليات والحفلات، يعرض الخدمات والباقات وصور الفعاليات السابقة.",
        "tags": ["فعاليات", "حفلات", "تنظيم", "أعراس", "مناسبات"],
        "features": ["الباقات", "معرض الفعاليات", "نموذج استفسار", "تقييمات", "الفريق"],
        "preview_url": "https://placehold.co/600x400/ec4899/white?text=فعاليات"
    },
]

# ═══════════════════════════════════════════════════════════
# 💖 UTILITY - دوال مساعدة
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
# 💖 توليد HTML الرئيسي - index.html
# ═══════════════════════════════════════════════════════════

def build_template_card(t):
    return f"""
    <div class="template-card" data-category="{t['category']}" onclick="showTemplateDetail('{t['id']}')">
        <div class="card-image" style="background: {t['color']}">
            <span class="card-icon">{t['icon']}</span>
            <div class="card-overlay">
                <button class="btn-preview" onclick="event.stopPropagation(); showTemplateDetail('{t['id']}')">
                    <i class="fas fa-eye"></i> معاينة
                </button>
            </div>
        </div>
        <div class="card-body">
            <span class="card-category">{t['category']}</span>
            <h3 class="card-title">{t['name']}</h3>
            <p class="card-desc">{t['desc'][:100]}...</p>
            <div class="card-tags">
                {"".join(f'<span class="tag">{tag}</span>' for tag in t['tags'][:3])}
            </div>
        </div>
    </div>"""

def build_template_detail_modal(t):
    return f"""
    <div class="modal-overlay" id="modal-{t['id']}" style="display:none" onclick="if(event.target===this)closeModal('{t['id']}')">
        <div class="modal-content">
            <button class="modal-close" onclick="closeModal('{t['id']}')"><i class="fas fa-times"></i></button>
            <div class="modal-header" style="background: {t['color']}">
                <span class="modal-icon">{t['icon']}</span>
                <h2>{t['name']}</h2>
                <p class="modal-category">{t['category']}</p>
            </div>
            <div class="modal-body">
                <div class="modal-preview">
                    <img src="{t['preview_url']}" alt="{t['name']}" loading="lazy">
                </div>
                <div class="modal-info">
                    <h3>📝 وصف القالب</h3>
                    <p>{t['desc']}</p>
                    
                    <h3>✨ المميزات</h3>
                    <ul class="features-list">
                        {"".join(f'<li><i class="fas fa-check-circle"></i> {f}</li>' for f in t['features'])}
                    </ul>
                    
                    <h3>🏷️ الوسوم</h3>
                    <div class="card-tags">
                        {"".join(f'<span class="tag">{tag}</span>' for tag in t['tags'])}
                    </div>
                    
                    <div class="cta-box">
                        <p>💖 أعجبك هذا القالب؟ تواصل معنا لصنع موقعك!</p>
                        <a href="{TELEGRAM_LINK}" target="_blank" class="btn-telegram">
                            <i class="fab fa-telegram-plane"></i> تواصل عبر تليغرام {TELEGRAM_USER}
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>"""

def build_index():
    cards_html = "\n".join(build_template_card(t) for t in TEMPLATES)
    modals_html = "\n".join(build_template_detail_modal(t) for t in TEMPLATES)
    
    # استخراج الفئات الفريدة
    categories = sorted(set(t['category'] for t in TEMPLATES))
    categories_btns = "\n".join(f'<button class="filter-btn" onclick="filterTemplates(\'{cat}\', this)">{cat}</button>' for cat in categories)
    
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <meta name="description" content="{SITE_DESC}">
    <title>💖 {COMPANY_NAME} | {SITE_TITLE}</title>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{{--glass: rgba(236,72,153,0.03); --border: rgba(236,72,153,0.12); --accent: #ec4899; --accent2: #a855f7; --bg: #0a0508; --card: rgba(30, 15, 30, 0.6)}}
        *{{margin:0;padding:0;box-sizing:border-box}}
        body{{font-family:'Segoe UI',Tahoma,Geneva,Verdana,sans-serif;background:radial-gradient(ellipse at top, #1a0a15, #0a0a0a, #000);color:#fff;min-height:100vh;overflow-x:hidden}}
        .bg-orb{{position:fixed;border-radius:50%;filter:blur(130px);opacity:0.15;z-index:0;animation:orbFloat 20s infinite alternate}}
        .bg-orb:nth-child(1){{width:500px;height:500px;background:#ec4899;top:-100px;left:-100px}}
        .bg-orb:nth-child(2){{width:400px;height:400px;background:#a855f7;bottom:-100px;right:-100px;animation-delay:5s}}
        @keyframes orbFloat{{0%{{transform:translate(0,0)scale(1)}}100%{{transform:translate(50px,-50px)scale(1.3)}}}}

        .container{{position:relative;z-index:10;max-width:1300px;margin:0 auto;padding:15px}}

        /* 💖 NAVBAR */
        .navbar{{display:flex;justify-content:space-between;align-items:center;padding:15px 25px;margin-bottom:25px;background:rgba(10,5,8,0.7);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border:1px solid var(--border);border-radius:50px;box-shadow:0 15px 35px rgba(236,72,153,0.08);position:sticky;top:10px;z-index:100;flex-wrap:wrap;gap:10px}}
        .logo{{display:flex;align-items:center;gap:10px;font-size:22px;font-weight:900;background:linear-gradient(to bottom,#fff,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;white-space:nowrap}}
        .logo i{{font-size:28px;background:linear-gradient(135deg,#ec4899,#a855f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
        .date-badge{{background:rgba(236,72,153,0.15);border:1px solid rgba(236,72,153,0.3);padding:8px 16px;border-radius:25px;font-size:13px;color:#f472b6;display:flex;align-items:center;gap:6px;white-space:nowrap}}

        /* 💖 HERO */
        .hero{{text-align:center;margin-bottom:30px}}
        .hero h1{{font-size:clamp(28px,5vw,48px);font-weight:900;background:linear-gradient(to bottom,#fff,#f472b6,#ec4899);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:12px}}
        .hero p{{font-size:17px;opacity:0.7;max-width:600px;margin:0 auto 20px;line-height:1.6}}
        .hero-stats{{display:flex;justify-content:center;gap:30px;flex-wrap:wrap}}
        .stat-item{{text-align:center;background:var(--card);backdrop-filter:blur(20px);border:1px solid var(--border);border-radius:20px;padding:16px 24px;min-width:120px}}
        .stat-num{{font-size:28px;font-weight:900;color:#f472b6}}
        .stat-label{{font-size:12px;opacity:0.6;margin-top:4px}}

        /* 💖 TELEGRAM BANNER */
        .telegram-banner{{background:linear-gradient(135deg,rgba(0,136,204,0.2),rgba(236,72,153,0.15));border:1px solid rgba(0,136,204,0.3);border-radius:25px;padding:20px;display:flex;align-items:center;justify-content:space-between;margin-bottom:25px;backdrop-filter:blur(20px);flex-wrap:wrap;gap:15px;animation:pulseBanner 2s ease-in-out infinite}}
        @keyframes pulseBanner{{0%,100%{{box-shadow:0 0 20px rgba(0,136,204,0.15)}}50%{{box-shadow:0 0 40px rgba(0,136,204,0.3)}}}}
        .telegram-banner p{{font-size:15px;font-weight:600;margin:0}}
        .btn-telegram{{background:linear-gradient(135deg,#0088cc,#00a8e8);color:#fff;border:none;padding:12px 28px;border-radius:30px;font-size:15px;font-weight:700;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;gap:10px;transition:all 0.3s;box-shadow:0 8px 25px rgba(0,136,204,0.4);white-space:nowrap}}
        .btn-telegram:hover{{transform:translateY(-3px);box-shadow:0 15px 35px rgba(0,136,204,0.6)}}

        /* 💖 FILTERS */
        .filters-wrap{{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:25px;justify-content:center}}
        .filter-btn{{background:rgba(236,72,153,0.06);border:1px solid var(--border);padding:9px 18px;border-radius:25px;color:rgba(255,255,255,0.7);cursor:pointer;font-size:13px;font-weight:500;transition:all 0.3s;white-space:nowrap}}
        .filter-btn:hover,.filter-btn.active{{background:rgba(236,72,153,0.2);border-color:#ec4899;color:#fff;box-shadow:0 0 15px rgba(236,72,153,0.2)}}
        .filter-btn.all{{background:linear-gradient(135deg,#ec4899,#a855f7);border:none;color:#fff;font-weight:700}}

        /* 💖 GRID */
        .templates-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px;margin-bottom:40px}}
        .template-card{{background:var(--card);border:1px solid var(--border);border-radius:20px;overflow:hidden;cursor:pointer;transition:all 0.3s;backdrop-filter:blur(20px);animation:fadeUp 0.5s ease}}
        .template-card:hover{{transform:translateY(-8px);box-shadow:0 25px 50px rgba(236,72,153,0.15);border-color:#ec4899}}
        @keyframes fadeUp{{from{{opacity:0;transform:translateY(30px)}}to{{opacity:1;transform:translateY(0)}}}}
        .card-image{{height:180px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}}
        .card-icon{{font-size:64px;z-index:1;transition:transform 0.3s}}
        .template-card:hover .card-icon{{transform:scale(1.1)}}
        .card-overlay{{position:absolute;inset:0;background:rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity 0.3s}}
        .template-card:hover .card-overlay{{opacity:1}}
        .btn-preview{{background:rgba(255,255,255,0.2);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.3);color:#fff;padding:10px 24px;border-radius:25px;cursor:pointer;font-weight:700;font-size:13px}}
        .card-body{{padding:15px}}
        .card-category{{font-size:11px;opacity:0.5;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;display:block}}
        .card-title{{font-size:16px;font-weight:700;margin-bottom:8px}}
        .card-desc{{font-size:12px;opacity:0.6;line-height:1.5;margin-bottom:10px}}
        .card-tags{{display:flex;flex-wrap:wrap;gap:5px}}
        .tag{{background:rgba(236,72,153,0.1);border:1px solid rgba(236,72,153,0.2);padding:4px 10px;border-radius:15px;font-size:10px;color:#f472b6}}

        /* 💖 MODAL */
        .modal-overlay{{position:fixed;inset:0;background:rgba(0,0,0,0.85);backdrop-filter:blur(20px);z-index:999;display:flex;align-items:center;justify-content:center;padding:20px;overflow-y:auto}}
        .modal-content{{background:linear-gradient(135deg,#1a0a15,#0d0d1a);border:1px solid rgba(236,72,153,0.3);border-radius:24px;max-width:800px;width:100%;max-height:90vh;overflow-y:auto;animation:slideUp 0.4s ease;position:relative}}
        @keyframes slideUp{{from{{opacity:0;transform:translateY(50px)}}to{{opacity:1;transform:translateY(0)}}}}
        .modal-close{{position:absolute;top:15px;right:15px;background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);border:1px solid rgba(236,72,153,0.4);color:#fff;width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;font-size:18px;z-index:10;transition:all 0.3s}}
        .modal-close:hover{{background:rgba(239,68,68,0.4)}}
        .modal-header{{padding:40px 25px 25px;text-align:center;border-radius:24px 24px 0 0}}
        .modal-icon{{font-size:64px;display:block;margin-bottom:10px}}
        .modal-header h2{{font-size:26px;font-weight:900}}
        .modal-category{{font-size:13px;opacity:0.7;margin-top:5px}}
        .modal-body{{padding:25px}}
        .modal-preview{{border-radius:15px;overflow:hidden;margin-bottom:20px;border:1px solid var(--border)}}
        .modal-preview img{{width:100%;height:auto;display:block}}
        .modal-info h3{{font-size:18px;margin:20px 0 10px;color:#f472b6}}
        .modal-info p{{font-size:14px;opacity:0.8;line-height:1.7}}
        .features-list{{list-style:none;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin:12px 0}}
        .features-list li{{display:flex;align-items:center;gap:8px;font-size:13px;background:rgba(236,72,153,0.05);padding:10px 14px;border-radius:12px;border:1px solid rgba(236,72,153,0.1)}}
        .features-list i{{color:#10b981;font-size:16px}}
        .cta-box{{background:rgba(0,136,204,0.1);border:1px solid rgba(0,136,204,0.3);border-radius:16px;padding:20px;text-align:center;margin-top:20px}}
        .cta-box p{{margin-bottom:12px;font-weight:600}}

        /* 💖 FOOTER */
        .footer{{text-align:center;padding:30px 20px;border-top:1px solid var(--border);margin-top:40px}}
        .footer p{{font-size:12px;opacity:0.5;margin:5px 0}}
        .footer a{{color:#f472b6;text-decoration:none}}

        /* 💖 MOBILE */
        @media (max-width:768px){{
            .navbar{{flex-direction:column;text-align:center;border-radius:25px}}
            .hero h1{{font-size:26px}}
            .hero-stats{{gap:10px}}
            .stat-item{{min-width:90px;padding:12px 16px}}
            .stat-num{{font-size:22px}}
            .templates-grid{{grid-template-columns:1fr}}
            .telegram-banner{{flex-direction:column;text-align:center}}
        }}
    </style>
</head>
<body>
    <div class="bg-orb"></div>
    <div class="bg-orb"></div>

    <div class="container">
        <!-- 💖 NAVBAR -->
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

        <!-- 💖 HERO -->
        <header class="hero">
            <h1>💖 {SITE_TITLE}</h1>
            <p>{SITE_DESC} - جميع قوالب الديكور للمواقع في مكان واحد</p>
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

        <!-- 💖 TELEGRAM BANNER -->
        <div class="telegram-banner">
            <div>
                <p style="font-size:18px;margin-bottom:4px">📱 تواصل معنا مباشرة</p>
                <p style="opacity:0.7;font-weight:400">اختر قالبك وسنصنع لك موقعًا احترافيًا كاملاً</p>
            </div>
            <a href="{TELEGRAM_LINK}" target="_blank" class="btn-telegram">
                <i class="fab fa-telegram-plane"></i> {TELEGRAM_USER}
            </a>
        </div>

        <!-- 💖 FILTERS -->
        <div class="filters-wrap">
            <button class="filter-btn all active" onclick="filterTemplates('all', this)">✨ الكل</button>
            {categories_btns}
        </div>

        <!-- 💖 TEMPLATES GRID -->
        <div class="templates-grid" id="templatesGrid">
            {cards_html}
        </div>

        <!-- 💖 MODALS -->
        {modals_html}

        <!-- 💖 FOOTER -->
        <footer class="footer">
            <p>💖 {COMPANY_NAME} © {datetime.now().year} - جميع الحقوق محفوظة</p>
            <p>للتواصل: <a href="{TELEGRAM_LINK}" target="_blank">{TELEGRAM_USER}</a> على تليغرام</p>
            <p style="margin-top:8px">📅 آخر تحديث: {TODAY_DATE_AR}</p>
        </footer>
    </div>

    <script>
        function filterTemplates(cat, btn) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const cards = document.querySelectorAll('.template-card');
            cards.forEach(card => {{
                if (cat === 'all' || card.dataset.category === cat) {{
                    card.style.display = 'block';
                    card.style.animation = 'none';
                    card.offsetHeight;
                    card.style.animation = 'fadeUp 0.5s ease';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}

        function showTemplateDetail(id) {{
            const modal = document.getElementById('modal-' + id);
            if (modal) {{
                modal.style.display = 'flex';
                document.body.style.overflow = 'hidden';
            }}
        }}

        function closeModal(id) {{
            const modal = document.getElementById('modal-' + id);
            if (modal) {{
                modal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }}
        }}

        document.addEventListener('keydown', function(e) {{
            if (e.key === 'Escape') {{
                document.querySelectorAll('.modal-overlay').forEach(m => {{
                    if (m.style.display === 'flex') {{
                        m.style.display = 'none';
                        document.body.style.overflow = 'auto';
                    }}
                }});
            }}
        }});

        console.log('💖 {COMPANY_NAME} | {TODAY_DATE}');
        console.log('📱 تواصل: {TELEGRAM_USER}');
    </script>
</body>
</html>"""

# ═══════════════════════════════════════════════════════════
# 💖 MAIN
# ═══════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  💖  MADAR ALTECHNIA - قوالب مواقع احترافية  ✨     ║
║     Templates Showcase Generator                         ║
║                                                          ║
║  🏢  شركة مدار التقنية                                ║
║  📱  تواصل: @Go21mk                                   ║
║  📅  تاريخ اليوم: """ + TODAY_DATE_AR + """                                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
    """)
    
    section("GENERATING SITE - إنشاء الموقع")
    
    write("index.html", build_index())
    
    print(f"""
{'='*60}
  💖 DONE - تم الإنشاء بنجاح! ✨
{'='*60}

  📊 إحصائيات:
     • {TOTAL_LINES} إجمالي عدد الأسطر
     • ملف واحد: index.html
     • {len(TEMPLATES)} قالب ديكور احترافي
     • {len(set(t['category'] for t in TEMPLATES))} تصنيف مختلف

  💖 القوالب المشمولة:
     {" • ".join(t['name'] for t in TEMPLATES)}

  📱 للتواصل: {TELEGRAM_USER}
  📅 تاريخ اليوم: {TODAY_DATE_AR}

  💖 افتح index.html في المتصفح للمعاينة
  💖 MADAR ALTECHNIA READY! ✨
{'='*60}
    """)

if __name__ == "__main__":
    main()
