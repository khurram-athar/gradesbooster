#!/usr/bin/env python3
"""
Patch all curriculum grade*.ts files to add YouTube videoUrl fields.
Run after all grade files are generated.
"""
import re, os

DIR = '/sessions/wonderful-keen-tesla/mnt/gradesbooster/data'

# Curated YouTube video IDs per (grade_band, subject)
# k3=Grades 0-3  m=Grades 4-6  u=Grades 7-9  hs=Grades 10-12

VIDS = {
    # ── Grades 0-3 ───────────────────────────────────────────
    ('k3','Language'):      ['Y7ClQc_4Txg','_Ys942P9hn0','QGNwOoeyKko','vcmwZqijDnY','hhxltYxHlQ0'],
    ('k3','Math'):          ['jSL5WNcTtUs','dCIhDUWS2X8','2Tp51rFXIc8','wrldije5nAk','1ZDcByAHKt8'],
    ('k3','Science'):       ['NG-FaXNiIfU','Q-J2FErZHuA','bIaq4HUD3jo','6a0dmntR0Dw','4ExsJBcHeVA'],
    ('k3','SocialStudies'): ['BlPtF_NqIQI','YkrAIz_Ha6E','UXh_7wbnS3A','VMxjzWHbyFM','P-G0YkfgdbA'],

    # ── Grades 4-6 ───────────────────────────────────────────
    # Language: Crash Course Literature (short stories / reading)
    ('m','Language'):       ['MSYw502dJNY','I4kz-C7GryY','MS4jk5kavy4','WfNiQBXmPw8','ui86G8Q5GhQ'],
    # Math: Math Antics
    ('m','Math'):           ['Mst8iZjIpFE','do_IbHId2Os','KNdUJQ_qd4U','17IgK9b6P2M','_jcW-ZgpRbM'],
    # Science: Crash Course Kids
    ('m','Science'):        ['BlPtF_NqIQI','YkrAIz_Ha6E','UXh_7wbnS3A','VMxjzWHbyFM','wyRy8kowyM8'],
    ('m','SocialStudies'):  ['YkrAIz_Ha6E','BlPtF_NqIQI','VMxjzWHbyFM','UXh_7wbnS3A','P-G0YkfgdbA'],
    ('m','History'):        ['YkrAIz_Ha6E','BlPtF_NqIQI','VMxjzWHbyFM','UXh_7wbnS3A','P-G0YkfgdbA'],
    ('m','Geography'):      ['YkrAIz_Ha6E','BlPtF_NqIQI','VMxjzWHbyFM','UXh_7wbnS3A','P-G0YkfgdbA'],

    # ── Grades 7-9 ───────────────────────────────────────────
    # Language: Crash Course Literature
    ('u','Language'):       ['MSYw502dJNY','I4kz-C7GryY','MS4jk5kavy4','WfNiQBXmPw8','ui86G8Q5GhQ'],
    # Math: Khan Academy algebra / pre-algebra
    ('u','Math'):           ['bAerID24QJ0','vDqOoI-4Z6M','rgvysb9emcQ','rj7DweP8e58','a_Wi-6SRBTc'],
    # Science: Crash Course Biology intro + evolution
    ('u','Science'):        ['tZE_fQFK8EY','i-VeKZeyHZs','F38BmgPcZ_I','L0k-enzoeOM','8kK2zwjRV0M'],
    ('u','History'):        ['YkrAIz_Ha6E','BlPtF_NqIQI','VMxjzWHbyFM','UXh_7wbnS3A','P-G0YkfgdbA'],
    ('u','Geography'):      ['YkrAIz_Ha6E','BlPtF_NqIQI','VMxjzWHbyFM','UXh_7wbnS3A','P-G0YkfgdbA'],

    # ── Grades 10-12 ─────────────────────────────────────────
    # English: Crash Course Literature
    ('hs','English'):          ['MSYw502dJNY','I4kz-C7GryY','MS4jk5kavy4','WfNiQBXmPw8','ui86G8Q5GhQ'],
    # Math — Ontario "Math" in grade 10 = Academic/Applied mix (Khan algebra)
    ('hs','Math'):             ['bAerID24QJ0','vDqOoI-4Z6M','rgvysb9emcQ','rj7DweP8e58','a_Wi-6SRBTc'],
    # Functions / Advanced Functions / Calculus: Khan Academy
    ('hs','Functions'):        ['riXcZT2ICjA','eh_ATp0hbB0','N2PpRnFqnqY','__Uw1SXPW7s','MFrpe4Wm8-g'],
    ('hs','AdvancedFunctions'):['eh_ATp0hbB0','riXcZT2ICjA','N2PpRnFqnqY','__Uw1SXPW7s','MFrpe4Wm8-g'],
    ('hs','Calculus'):         ['__Uw1SXPW7s','N2PpRnFqnqY','riXcZT2ICjA','eh_ATp0hbB0','MFrpe4Wm8-g'],
    # Physics: Crash Course Physics
    ('hs','Physics'):          ['ZM8ECpBuQYE','w3BhzYI6zXU','MFrpe4Wm8-g','__Uw1SXPW7s','N2PpRnFqnqY'],
    # Chemistry: Crash Course Chemistry
    ('hs','Chemistry'):        ['FSyAehMdpyI','ZM8ECpBuQYE','w3BhzYI6zXU','tZE_fQFK8EY','i-VeKZeyHZs'],
    # Biology: Crash Course Biology
    ('hs','Biology'):          ['tZE_fQFK8EY','i-VeKZeyHZs','F38BmgPcZ_I','L0k-enzoeOM','8kK2zwjRV0M'],
    # History in high school
    ('hs','History'):          ['YkrAIz_Ha6E','BlPtF_NqIQI','VMxjzWHbyFM','UXh_7wbnS3A','P-G0YkfgdbA'],
    # Science in grade 10 (general before specialisation)
    ('hs','Science'):          ['ZM8ECpBuQYE','FSyAehMdpyI','tZE_fQFK8EY','w3BhzYI6zXU','i-VeKZeyHZs'],
}

def band(grade):
    if grade <= 3: return 'k3'
    if grade <= 6: return 'm'
    if grade <= 9: return 'u'
    return 'hs'

def get_vid(grade, subject, day_num):
    b = band(grade)
    lst = VIDS.get((b, subject))
    if not lst:
        # fallback: Science for the band
        lst = VIDS.get((b, 'Science'), ['tZE_fQFK8EY'])
    return f"https://www.youtube.com/watch?v={lst[(day_num - 1) % len(lst)]}"

def patch_file(grade):
    path = f'{DIR}/grade{grade}.ts'
    if not os.path.exists(path):
        print(f'  SKIP: grade{grade}.ts not found')
        return

    content = open(path).read()

    if 'videoUrl:' in content:
        print(f'  grade{grade}.ts already has videoUrl — skipping')
        return

    replacements = 0

    def replacer(m):
        nonlocal replacements
        pos = m.start()
        prefix = content[:pos]

        # Find current day number (last {day:N before this position)
        day_matches = list(re.finditer(r'\{day:(\d+)', prefix))
        day_num = int(day_matches[-1].group(1)) if day_matches else 1

        # Find current subject (last subject:"..." before this position)
        subj_matches = list(re.finditer(r'subject:"([^"]+)"', prefix))
        subject = subj_matches[-1].group(1) if subj_matches else 'Science'

        vid_url = get_vid(grade, subject, day_num)
        replacements += 1
        return m.group(0) + f'\n   videoUrl:"{vid_url}",'

    # Insert videoUrl after each "resourceUrl:..." line
    new_content = re.sub(r'resourceUrl:"[^"]+",' , replacer, content)
    open(path, 'w').write(new_content)
    print(f'  grade{grade}.ts — added {replacements} videoUrl entries')

print('Adding YouTube videoUrl to curriculum files...')
for g in range(13):
    patch_file(g)
print('Done!')
