#!/usr/bin/env python3
"""
🏢 مدار التقني - معرض القوالب الاحترافي
موقع يعرض قوالب المواقع والتطبيقات بتصميم زجاجي عصري
"""

import os
import json
from datetime import datetime
from pathlib import Path

class MadarTechBuilder:
    def __init__(self):
        # معلومات الشركة
        self.company = {
            "name": "مدار التقني",
            "name_en": "Madar Tech",
            "slogan": "قوالب احترافية لمستقبل رقمي أفضل",
            "telegram": "@Go21mk",
            "email": "contact@madar-tech.com",
            "location": "المملكة العربية السعودية",
            "stats": {
                "templates": "500+",
                "clients": "150+",
                "downloads": "10K+",
                "rating": "4.9"
            }
        }
        
        # قوالب المواقع (مثل موقع bowwe)
        self.templates = [
            {
                "id": 1,
                "title": "متجر إلكتروني متكامل",
                "category": "متاجر",
                "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600",
                "description": "قالب متجر متكامل مع نظام دفع وسلة مشتريات ولوحة تحكم",
                "perfect_for": ["رواد الأعمال", "أصحاب المتاجر", "العلامات التجارية"],
                "features": ["سلة مشتريات", "بوابة دفع", "لوحة تحكم", "متجاوب"],
                "rating": 4.9,
                "sales": 1234,
                "price": "199",
                "badge": "الأكثر مبيعاً",
                "tech": ["React", "Node.js", "MongoDB"]
            },
            {
                "id": 2,
                "title": "شركة وأعمال احترافي",
                "category": "شركات",
                "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600",
                "description": "تصميم عصري للشركات والمؤسسات الكبرى مع صفحات متعددة",
                "perfect_for": ["الشركات", "المؤسسات", "وكالات التسويق"],
                "features": ["صفحات متعددة", "مدونة", "معرض أعمال", "SEO"],
                "rating": 4.8,
                "sales": 987,
                "price": "149",
                "badge": "جديد",
                "tech": ["HTML5", "CSS3", "JavaScript"]
            },
            {
                "id": 3,
                "title": "تطبيق جوال عصري",
                "category": "تطبيقات",
                "image": "https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?w=600",
                "description": "واجهة تطبيق جوال عصرية بتصميم زجاجي جذاب",
                "perfect_for": ["مطوري التطبيقات", "الشركات الناشئة", "المصممين"],
                "features": ["واجهة مستخدم", "حركات سلسة", "Dark Mode", "متعدد اللغات"],
                "rating": 4.9,
                "sales": 2341,
                "price": "249",
                "badge": "شائع",
                "tech": ["Flutter", "Dart", "Firebase"]
            },
            {
                "id": 4,
                "title": "لوحة تحكم تحليلات",
                "category": "لوحات تحكم",
                "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",
                "description": "داشبورد احترافي لإدارة البيانات والإحصائيات",
                "perfect_for": ["محللي البيانات", "المدراء", "الشركات التقنية"],
                "features": ["رسوم بيانية", "تقارير", "صلاحيات", "تصدير بيانات"],
                "rating": 4.7,
                "sales": 876,
                "price": "299",
                "badge": "",
                "tech": ["Vue.js", "Chart.js", "Python"]
            },
            {
                "id": 5,
                "title": "بورتفوليو شخصي",
                "category": "شخصي",
                "image": "https://images.unsplash.com/photo-1522199755839-a2bacb67c546?w=600",
                "description": "بورتفوليو شخصي احترافي للمطورين والمصممين",
                "perfect_for": ["المطورين", "المصممين", "المصورين", "الفنانين"],
                "features": ["سيرة ذاتية", "معرض أعمال", "مدونة", "تواصل"],
                "rating": 4.8,
                "sales": 1567,
                "price": "99",
                "badge": "",
                "tech": ["React", "Gatsby", "GraphQL"]
            },
            {
                "id": 6,
                "title": "منصة تعليمية",
                "category": "تعليم",
                "image": "https://images.unsplash.com/photo-1551650975-87deedd944c3?w=600",
                "description": "نظام إدارة تعلم متكامل مع فيديوهات واختبارات",
                "perfect_for": ["المعلمين", "المدربين", "المؤسسات التعليمية"],
                "features": ["دورات", "اختبارات", "شهادات", "بث مباشر"],
                "rating": 4.9,
                "sales": 1890,
                "price": "349",
                "badge": "الأكثر مبيعاً",
                "tech": ["Next.js", "Prisma", "PostgreSQL"]
            },
            {
                "id": 7,
                "title": "مطعم وكافيه",
                "category": "مطاعم",
                "image": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=600",
                "description": "موقع مطعم عصري مع قائمة طعام وطلب أونلاين",
                "perfect_for": ["المطاعم", "المقاهي", "خدمات التوصيل"],
                "features": ["قائمة طعام", "طلب أونلاين", "حجز طاولة", "توصيل"],
                "rating": 4.6,
                "sales": 654,
                "price": "179",
                "badge": "",
                "tech": ["React", "Express", "MySQL"]
            },
            {
                "id": 8,
                "title": "فندق ومنتجع",
                "category": "فنادق",
                "image": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600",
                "description": "موقع فندقي فاخر مع نظام حجز وعرض الغرف",
                "perfect_for": ["الفنادق", "المنتجعات", "بيوت الضيافة"],
                "features": ["حجز غرف", "معرض صور", "عروض", "تقييمات"],
                "rating": 4.7,
                "sales": 432,
                "price": "249",
                "badge": "جديد",
                "tech": ["WordPress", "PHP", "MySQL"]
            },
            {
                "id": 9,
                "title": "مدونة تقنية",
                "category": "مدونات",
                "image": "https://images.unsplash.com/photo-1499750310107-5fef28a66643?w=600",
                "description": "مدونة عصرية للمحتوى التقني مع تصميم نظيف",
                "perfect_for": ["المدونين", "الكتّاب", "المسوقين"],
                "features": ["مقالات", "تصنيفات", "مشاركة", "نشرة بريدية"],
                "rating": 4.5,
                "sales": 765,
                "price": "79",
                "badge": "",
                "tech": ["Gatsby", "Markdown", "Netlify"]
            },
            {
                "id": 10,
                "title": "وكالة تسويق رقمي",
                "category": "وكالات",
                "image": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=600",
                "description": "موقع وكالة تسويقية احترافي مع عرض الخدمات",
                "perfect_for": ["وكالات التسويق", "المسوقين", "الاستشاريين"],
                "features": ["خدمات", "دراسات حالة", "فريق", "عروض أسعار"],
                "rating": 4.8,
                "sales": 543,
                "price": "199",
                "badge": "شائع",
                "tech": ["Next.js", "Tailwind", "Stripe"]
            },
            {
                "id": 11,
                "title": "عيادة طبية",
                "category": "طبي",
                "image": "https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=600",
                "description": "موقع عيادة طبية مع نظام حجز مواعيد",
                "perfect_for": ["الأطباء", "العيادات", "المراكز الطبية"],
                "features": ["حجز مواعيد", "ملف مريض", "أطباء", "خدمات"],
                "rating": 4.7,
                "sales": 321,
                "price": "249",
                "badge": "",
                "tech": ["Laravel", "Vue.js", "MySQL"]
            },
            {
                "id": 12,
                "title": "صالة رياضية",
                "category": "رياضة",
                "image": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48?w=600",
                "description": "موقع صالة رياضية مع جداول تمارين وعضويات",
                "perfect_for": ["الصالات الرياضية", "مدربي اللياقة", "النوادي"],
                "features": ["جداول", "عضويات", "مدربين", "مدونة صحية"],
                "rating": 4.6,
                "sales": 298,
                "price": "179",
                "badge": "",
                "tech": ["React", "Firebase", "Stripe"]
            }
        ]
        
        # فئات القوالب
        self.categories = [
            {"name": "الكل", "icon": "📋", "count": len(self.templates)},
            {"name": "متاجر", "icon": "🛒", "count": 1},
            {"name": "شركات", "icon": "🏢", "count": 1},
            {"name": "تطبيقات", "icon": "📱", "count": 1},
            {"name": "لوحات تحكم", "icon": "📊", "count": 1},
            {"name": "شخصي", "icon": "👤", "count": 1},
            {"name": "تعليم", "icon": "📚", "count": 1},
            {"name": "مطاعم", "icon": "🍽️", "count": 1},
            {"name": "فنادق", "icon": "🏨", "count": 1},
            {"name": "مدونات", "icon": "📝", "count": 1},
            {"name": "وكالات", "icon": "🎯", "count": 1},
            {"name": "طبي", "icon": "🏥", "count": 1},
            {"name": "رياضة", "icon": "💪", "count": 1},
        ]
    
    def generate_html(self):
        """توليد HTML الموقع الكامل"""
        
        # توليد كروت القوالب
        templates_html = ""
        for template in self.templates:
            badge_html = ""
            if template['badge']:
                badge_class = "badge-popular" if "مبيعاً" in template['badge'] or "شائع" in template['badge'] else "badge-new"
                badge_html = f'<span class="template-badge {badge_class}">{template["badge"]}</span>'
            
            stars_html = "★" * int(template['rating']) + "☆" * (5 - int(template['rating']))
            
            features_html = " ".join([f'<span class="feature-tag">{f}</span>' for f in template['features'][:3]])
            
            perfect_for_html = "، ".join(template['perfect_for'])
            
            templates_html += f"""
            <div class="template-card" data-category="{template['category']}" data-aos="fade-up">
                {badge_html}
                <div class="template-image-wrapper">
                    <img src="{template['image']}" alt="{template['title']}" class="template-image" loading="lazy">
                    <div class="template-overlay">
                        <a href="#" class="preview-btn">
                            <i class="fas fa-eye"></i>
                            معاينة
                        </a>
                    </div>
                </div>
                <div class="template-info">
                    <div class="template-header">
                        <span class="template-category">{template['category']}</span>
                        <span class="template-price">{template['price']} ر.س</span>
                    </div>
                    <h3 class="template-title">{template['title']}</h3>
                    <p class="template-desc">{template['description']}</p>
                    
                    <p class="template-perfect"><strong>🔹 مثالي لـ:</strong> {perfect_for_html}</p>
                    
                    <div class="template-features">
                        {features_html}
                    </div>
                    
                    <div class="template-meta">
                        <div class="template-rating">
                            <span class="stars">{stars_html}</span>
                            <span class="rating-number">{template['rating']}</span>
                        </div>
                        <span class="template-sales">
                            <i class="fas fa-shopping-cart"></i>
                            {template['sales']} مبيعاً
                        </span>
                    </div>
                    
                    <div class="template-tech">
                        {" ".join([f'<span class="tech-tag">{t}</span>' for t in template['tech']])}
                    </div>
                </div>
            </div>
            """
        
        # توليد قائمة الفئات
        categories_html = ""
        for cat in self.categories:
            active = "active" if cat['name'] == "الكل" else ""
            categories_html += f"""
            <button class="filter-btn {active}" data-filter="{cat['name']}">
                <span class="filter-icon">{cat['icon']}</span>
                {cat['name']}
                <span class="filter-count">{cat['count']}</span>
            </button>
            """
        
        html = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="مدار التقني - أكثر من 500 قالب احترافي للمواقع والتطبيقات. قوالب مجانية واحترافية بتصميم عصري">
    <meta name="keywords" content="قوالب مواقع, قوالب تطبيقات, مدار التقني, madar tech, templates">
    
    <!-- Open Graph -->
    <meta property="og:title" content="مدار التقني - قوالب احترافية">
    <meta property="og:description" content="أكثر من 500 قالب احترافي لمواقع، هبوط ومحافظ شخصية">
    <meta property="og:image" content="https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1200">
    <meta property="og:type" content="website">
    
    <title>مدار التقني | أكثر من 500 قالب احترافي للمواقع والتطبيقات</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏢</text></svg>">
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    
    <!-- Font Awesome 6 -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <!-- AOS Animation -->
    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
    
    <style>
        :root {{
            --primary: #6366f1;
            --primary-light: #818cf8;
            --primary-dark: #4f46e5;
            --secondary: #8b5cf6;
            --accent: #a78bfa;
            --bg-dark: #0a0a1a;
            --bg-card: #111133;
            --bg-glass: rgba(17, 17, 51, 0.6);
            --text: #ffffff;
            --text-secondary: #94a3b8;
            --border: rgba(99, 102, 241, 0.2);
            --border-hover: rgba(99, 102, 241, 0.5);
            --success: #10b981;
            --warning: #f59e0b;
            --gradient-1: linear-gradient(135deg, #6366f1, #8b5cf6);
            --gradient-2: linear-gradient(135deg, #8b5cf6, #a78bfa);
            --gradient-hero: linear-gradient(135deg, #0a0a1a 0%, #1a1040 50%, #0a0a2a 100%);
            --shadow-glow: 0 0 40px rgba(99, 102, 241, 0.3);
            --shadow-card: 0 20px 60px rgba(0, 0, 0, 0.4);
            --radius: 20px;
            --radius-sm: 12px;
            --transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }}
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html {{
            scroll-behavior: smooth;
        }}
        
        body {{
            font-family: 'Cairo', sans-serif;
            background: var(--bg-dark);
            color: var(--text);
            overflow-x: hidden;
            line-height: 1.7;
        }}
        
        /* جسيمات الخلفية */
        .bg-particles {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 0;
            pointer-events: none;
            background:
                radial-gradient(ellipse at 20% 20%, rgba(99, 102, 241, 0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 80% 80%, rgba(139, 92, 246, 0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 50% 50%, rgba(167, 139, 250, 0.04) 0%, transparent 70%);
        }}
        
        /* نافبار زجاجي */
        .navbar {{
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background: rgba(10, 10, 26, 0.8);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(99, 102, 241, 0.1);
            transition: var(--transition);
            padding: 15px 0;
        }}
        
        .navbar.scrolled {{
            background: rgba(10, 10, 26, 0.95);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        }}
        
        .nav-container {{
            max-width: 1300px;
            margin: 0 auto;
            padding: 0 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
        }}
        
        .logo-icon {{
            width: 45px;
            height: 45px;
            background: var(--gradient-1);
            border-radius: 14px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.4);
        }}
        
        .logo-text {{
            font-size: 22px;
            font-weight: 800;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .nav-actions {{
            display: flex;
            align-items: center;
            gap: 20px;
        }}
        
        .nav-link {{
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
            font-size: 15px;
        }}
        
        .nav-link:hover {{
            color: var(--text);
        }}
        
        .btn-nav {{
            padding: 12px 28px;
            background: var(--gradient-1);
            border: none;
            border-radius: 50px;
            color: white;
            font-weight: 700;
            cursor: pointer;
            transition: var(--transition);
            text-decoration: none;
            font-size: 14px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .btn-nav:hover {{
            transform: translateY(-2px);
            box-shadow: var(--shadow-glow);
        }}
        
        /* هيرو */
        .hero {{
            position: relative;
            z-index: 1;
            padding: 160px 20px 100px;
            text-align: center;
            background: var(--gradient-hero);
        }}
        
        .hero-badge {{
            display: inline-block;
            padding: 8px 22px;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid var(--border);
            border-radius: 50px;
            margin-bottom: 25px;
            font-size: 14px;
            color: var(--primary-light);
            animation: float 3s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
        }}
        
        .hero-title {{
            font-size: 3.5rem;
            font-weight: 900;
            margin-bottom: 20px;
            line-height: 1.3;
            background: linear-gradient(135deg, #fff, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .hero-subtitle {{
            font-size: 1.3rem;
            color: var(--text-secondary);
            max-width: 700px;
            margin: 0 auto 40px;
            line-height: 1.8;
        }}
        
        .hero-stats {{
            display: flex;
            justify-content: center;
            gap: 50px;
            flex-wrap: wrap;
            margin-top: 50px;
        }}
        
        .stat-item {{
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 2.5rem;
            font-weight: 900;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .stat-label {{
            color: var(--text-secondary);
            font-size: 14px;
            margin-top: 5px;
        }}
        
        /* قسم القوالب */
        .templates-section {{
            position: relative;
            z-index: 1;
            padding: 80px 20px;
        }}
        
        .container {{
            max-width: 1300px;
            margin: 0 auto;
        }}
        
        .section-header {{
            text-align: center;
            margin-bottom: 50px;
        }}
        
        .section-title {{
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 15px;
            background: linear-gradient(135deg, #fff, #c4b5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .section-subtitle {{
            color: var(--text-secondary);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
        }}
        
        /* أزرار الفلترة */
        .filter-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            justify-content: center;
            margin-bottom: 40px;
            padding: 20px;
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border);
            border-radius: var(--radius);
        }}
        
        .filter-btn {{
            padding: 10px 20px;
            background: transparent;
            border: 1px solid var(--border);
            border-radius: 50px;
            color: var(--text-secondary);
            cursor: pointer;
            transition: var(--transition);
            font-family: 'Cairo', sans-serif;
            font-size: 14px;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 6px;
            white-space: nowrap;
        }}
        
        .filter-btn:hover {{
            border-color: var(--primary-light);
            color: var(--text);
            background: rgba(99, 102, 241, 0.1);
        }}
        
        .filter-btn.active {{
            background: var(--gradient-1);
            border-color: transparent;
            color: white;
            box-shadow: 0 10px 30px rgba(99, 102, 241, 0.3);
        }}
        
        .filter-count {{
            font-size: 11px;
            background: rgba(255,255,255,0.2);
            padding: 2px 8px;
            border-radius: 20px;
        }}
        
        /* شبكة القوالب */
        .templates-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(370px, 1fr));
            gap: 30px;
        }}
        
        .template-card {{
            background: var(--bg-glass);
            backdrop-filter: blur(10px);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            overflow: hidden;
            transition: var(--transition);
            position: relative;
            display: none;
        }}
        
        .template-card.visible {{
            display: block;
        }}
        
        .template-card:hover {{
            transform: translateY(-12px);
            border-color: var(--border-hover);
            box-shadow: 0 30px 60px rgba(99, 102, 241, 0.2);
        }}
        
        .template-badge {{
            position: absolute;
            top: 15px;
            right: 15px;
            padding: 6px 16px;
            border-radius: 50px;
            font-size: 12px;
            font-weight: 700;
            z-index: 2;
        }}
        
        .badge-popular {{
            background: linear-gradient(135deg, #f59e0b, #ef4444);
            color: white;
        }}
        
        .badge-new {{
            background: linear-gradient(135deg, #10b981, #06b6d4);
            color: white;
        }}
        
        .template-image-wrapper {{
            position: relative;
            height: 240px;
            overflow: hidden;
        }}
        
        .template-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.6s;
        }}
        
        .template-card:hover .template-image {{
            transform: scale(1.08);
        }}
        
        .template-overlay {{
            position: absolute;
            inset: 0;
            background: rgba(10, 10, 26, 0.7);
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            transition: opacity 0.4s;
        }}
        
        .template-card:hover .template-overlay {{
            opacity: 1;
        }}
        
        .preview-btn {{
            padding: 12px 30px;
            background: var(--gradient-1);
            color: white;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: var(--transition);
        }}
        
        .preview-btn:hover {{
            box-shadow: var(--shadow-glow);
            transform: scale(1.05);
        }}
        
        .template-info {{
            padding: 25px;
        }}
        
        .template-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}
        
        .template-category {{
            font-size: 12px;
            padding: 4px 12px;
            background: rgba(99, 102, 241, 0.15);
            border-radius: 20px;
            color: var(--primary-light);
            font-weight: 600;
        }}
        
        .template-price {{
            font-weight: 800;
            font-size: 1.1rem;
            color: var(--success);
        }}
        
        .template-title {{
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 8px;
            color: var(--text);
        }}
        
        .template-desc {{
            color: var(--text-secondary);
            font-size: 14px;
            margin-bottom: 12px;
            line-height: 1.6;
        }}
        
        .template-perfect {{
            color: var(--text-secondary);
            font-size: 13px;
            margin-bottom: 12px;
            line-height: 1.6;
        }}
        
        .template-features {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }}
        
        .feature-tag {{
            font-size: 11px;
            padding: 4px 10px;
            background: rgba(139, 92, 246, 0.1);
            border: 1px solid rgba(139, 92, 246, 0.2);
            border-radius: 20px;
            color: #c4b5fd;
        }}
        
        .template-meta {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 15px;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }}
        
        .stars {{
            color: #f59e0b;
            letter-spacing: 2px;
        }}
        
        .rating-number {{
            color: var(--text-secondary);
            font-size: 14px;
            margin-right: 5px;
        }}
        
        .template-sales {{
            color: var(--text-secondary);
            font-size: 13px;
        }}
        
        .template-tech {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        
        .tech-tag {{
            font-size: 11px;
            padding: 3px 10px;
            background: rgba(255,255,255,0.05);
            border-radius: 15px;
            color: var(--text-secondary);
        }}
        
        /* قسم التواصل */
        .contact-section {{
            position: relative;
            z-index: 1;
            padding: 80px 20px;
            text-align: center;
            background: linear-gradient(180deg, transparent, rgba(99, 102, 241, 0.05), transparent);
        }}
        
        .contact-card {{
            display: inline-block;
            background: var(--bg-glass);
            backdrop-filter: blur(20px);
            border: 1px solid var(--border);
            border-radius: 30px;
            padding: 50px 70px;
            transition: var(--transition);
        }}
        
        .contact-card:hover {{
            border-color: var(--border-hover);
            box-shadow: var(--shadow-glow);
            transform: scale(1.02);
        }}
        
        .contact-icon {{
            font-size: 4rem;
            margin-bottom: 20px;
            animation: float 3s ease-in-out infinite;
        }}
        
        .contact-title {{
            font-size: 1.8rem;
            font-weight: 800;
            margin-bottom: 10px;
        }}
        
        .contact-telegram {{
            font-size: 2rem;
            font-weight: 900;
            color: #0088cc;
            margin: 20px 0;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            text-decoration: none;
            transition: var(--transition);
        }}
        
        .contact-telegram:hover {{
            color: #00a8ff;
            transform: scale(1.05);
        }}
        
        .contact-desc {{
            color: var(--text-secondary);
            margin-bottom: 20px;
            font-size: 1.1rem;
        }}
        
        .btn-telegram {{
            display: inline-flex;
            align-items: center;
            gap: 10px;
            padding: 16px 40px;
            background: linear-gradient(135deg, #0088cc, #00a8ff);
            color: white;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 700;
            font-size: 1.1rem;
            transition: var(--transition);
        }}
        
        .btn-telegram:hover {{
            box-shadow: 0 20px 50px rgba(0, 136, 204, 0.4);
            transform: translateY(-3px);
        }}
        
        /* فوتر */
        .footer {{
            position: relative;
            z-index: 1;
            text-align: center;
            padding: 40px;
            border-top: 1px solid var(--border);
            color: var(--text-secondary);
            background: rgba(10, 10, 26, 0.8);
            backdrop-filter: blur(10px);
        }}
        
        .footer-logo {{
            font-size: 1.5rem;
            font-weight: 800;
            margin-bottom: 10px;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .hero-title {{
                font-size: 2.2rem;
            }}
            .hero-stats {{
                gap: 30px;
            }}
            .stat-number {{
                font-size: 1.8rem;
            }}
            .templates-grid {{
                grid-template-columns: 1fr;
            }}
            .contact-card {{
                padding: 35px 25px;
            }}
            .contact-telegram {{
                font-size: 1.4rem;
            }}
            .navbar {{
                padding: 10px 0;
            }}
            .nav-link {{
                display: none;
            }}
        }}
        
        /* سكرول بار */
        ::-webkit-scrollbar {{
            width: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: var(--bg-dark);
        }}
        ::-webkit-scrollbar-thumb {{
            background: var(--gradient-1);
            border-radius: 10px;
        }}
        
        /* تحميل */
        .loader {{
            text-align: center;
            padding: 40px;
            color: var(--text-secondary);
        }}
    </style>
</head>
<body>
    <div class="bg-particles"></div>
    
    <!-- نافبار -->
    <nav class="navbar" id="navbar">
        <div class="nav-container">
            <a href="#" class="logo">
                <div class="logo-icon">🏢</div>
                <span class="logo-text">مدار التقني</span>
            </a>
            <div class="nav-actions">
                <a href="#templates" class="nav-link">القوالب</a>
                <a href="#contact" class="nav-link">تواصل</a>
                <a href="https://t.me/{self.company['telegram'].replace('@', '')}" class="btn-nav" target="_blank">
                    <i class="fab fa-telegram-plane"></i>
                    تليجرام
                </a>
            </div>
        </div>
    </nav>
    
    <!-- هيرو -->
    <section class="hero">
        <span class="hero-badge">🚀 أكثر من 500 قالب احترافي</span>
        <h1 class="hero-title">اختر أفضل قالب لموقعك<br>الخاص بك</h1>
        <p class="hero-subtitle">
            تعرف على مدى عظيم أعمالك يمكن أن تكون مع <strong>مدار التقني</strong>. 
            قوالب احترافية مصممة بعناية لتناسب جميع المجالات
        </p>
        <a href="#templates" class="btn-nav" style="display: inline-flex; padding: 16px 40px; font-size: 16px;">
            <i class="fas fa-th-large"></i>
            تصفح القوالب
        </a>
        
        <div class="hero-stats">
            <div class="stat-item">
                <div class="stat-number">{self.company['stats']['templates']}</div>
                <div class="stat-label">قالب احترافي</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{self.company['stats']['clients']}</div>
                <div class="stat-label">عميل سعيد</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">{self.company['stats']['downloads']}</div>
                <div class="stat-label">تحميل</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">⭐ {self.company['stats']['rating']}</div>
                <div class="stat-label">تقييم</div>
            </div>
        </div>
    </section>
    
    <!-- قسم القوالب -->
    <section class="templates-section" id="templates">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">🎨 معرض القوالب الاحترافية</h2>
                <p class="section-subtitle">اكتشف مجموعتنا المميزة من القوالب الجاهزة لجميع المجالات</p>
            </div>
            
            <!-- فلتر -->
            <div class="filter-bar" data-aos="fade-up">
                {categories_html}
            </div>
            
            <!-- شبكة القوالب -->
            <div class="templates-grid" id="templatesGrid">
                {templates_html}
            </div>
            
            <div class="loader" id="noResults" style="display: none;">
                <i class="fas fa-search" style="font-size: 3rem; margin-bottom: 15px; opacity: 0.5;"></i>
                <p>لا توجد قوالب في هذه الفئة حالياً</p>
            </div>
        </div>
    </section>
    
    <!-- تواصل -->
    <section class="contact-section" id="contact">
        <div class="container">
            <div class="contact-card" data-aos="zoom-in">
                <div class="contact-icon">💬</div>
                <h3 class="contact-title">تواصل معنا مباشرة</h3>
                <p class="contact-desc">متاحون للمساعدة والاستفسارات على مدار الساعة</p>
                <a href="https://t.me/{self.company['telegram'].replace('@', '')}" class="contact-telegram" target="_blank">
                    <i class="fab fa-telegram"></i>
                    {self.company['telegram']}
                </a>
                <br>
                <a href="https://t.me/{self.company['telegram'].replace('@', '')}" class="btn-telegram" target="_blank">
                    <i class="fab fa-telegram-plane"></i>
                    راسلنا الآن على تليجرام
                </a>
            </div>
        </div>
    </section>
    
    <!-- فوتر -->
    <footer class="footer">
        <div class="footer-logo">🏢 مدار التقني</div>
        <p>جميع الحقوق محفوظة © {datetime.now().year}</p>
        <p style="margin-top: 8px; font-size: 13px;">قوالب احترافية لمستقبل رقمي أفضل</p>
    </footer>
    
    <!-- السكريبتات -->
    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
    <script>
        // تهيئة AOS
        AOS.init({{
            duration: 800,
            once: true,
            offset: 50
        }});
        
        // نافبار سكرول
        window.addEventListener('scroll', () => {{
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {{
                navbar.classList.add('scrolled');
            }} else {{
                navbar.classList.remove('scrolled');
            }}
        }});
        
        // فلترة القوالب
        const filterBtns = document.querySelectorAll('.filter-btn');
        const templateCards = document.querySelectorAll('.template-card');
        const noResults = document.getElementById('noResults');
        
        // إظهار الكل بداية
        templateCards.forEach(card => card.classList.add('visible'));
        
        filterBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                // إزالة active
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filter = btn.getAttribute('data-filter');
                let visibleCount = 0;
                
                templateCards.forEach(card => {{
                    if (filter === 'الكل' || card.getAttribute('data-category') === filter) {{
                        card.classList.add('visible');
                        visibleCount++;
                    }} else {{
                        card.classList.remove('visible');
                    }}
                }});
                
                // إظهار/إخفاء رسالة لا توجد نتائج
                if (visibleCount === 0) {{
                    noResults.style.display = 'block';
                }} else {{
                    noResults.style.display = 'none';
                }}
            }});
        }});
        
        console.log('🏢 مدار التقني - معرض القوالب الاحترافية');
        console.log('💬 تواصل تليجرام: {self.company["telegram"]}');
        console.log('📊 عدد القوالب: {len(self.templates)}');
    </script>
</body>
</html>"""
        
        return html
    
    def build(self):
        """بناء الموقع"""
        print("🏗️ بدء بناء موقع مدار التقني...")
        
        html = self.generate_html()
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        
        # معلومات البناء
        info = {
            'build_time': datetime.now().isoformat(),
            'templates_count': len(self.templates),
            'categories': len(self.categories),
            'company': self.company['name']
        }
        
        Path('data').mkdir(exist_ok=True)
        with open('data/build_info.json', 'w', encoding='utf-8') as f:
            json.dump(info, f, ensure_ascii=False, indent=2)
        
        print("✅ تم بناء موقع مدار التقني بنجاح!")
        print(f"📊 القوالب: {len(self.templates)}")
        print(f"📂 الفئات: {len(self.categories)}")
        return True

if __name__ == "__main__":
    builder = MadarTechBuilder()
    builder.build()
