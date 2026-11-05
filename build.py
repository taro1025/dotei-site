#!/usr/bin/env python3
"""DOTEI の公開ページ（GitHub Pages）と、審査で取り込みを試すための見本ファイルを書き出す。 python3 build.py"""
import json
import os
import shutil

MAIL = "rintaro.sakino@process-craft-ai.com"
DEMO = os.path.expanduser("~/dotei/art/demo")
CSS = """body{margin:0;background:#F3EEE3;color:#1F1D1B;font-family:-apple-system,"Hiragino Sans","Hiragino Kaku Gothic ProN",sans-serif;line-height:1.85}
main{max-width:720px;margin:0 auto;padding:40px 22px 64px}h1,h2{font-family:"Hiragino Mincho ProN","YuMincho",serif}
h1{font-size:1.8em;line-height:1.4}h2{font-size:1.15em;margin-top:2em}a{color:#C43D2B}
.bar{height:6px;background:#C43D2B;border-radius:3px;width:56px;margin:8px 0 24px}footer{margin-top:48px;font-size:.85em;color:#6B655D}
nav a{margin-right:14px}img.icon{width:96px;height:96px;border-radius:22px}.poem{font-family:"Hiragino Mincho ProN",serif;font-size:1.3em}
@media (prefers-color-scheme:dark){body{background:#1C1B19;color:#EEE8DC}a{color:#E2593F}footer{color:#A59E92}}"""

PAGES = {
 "ja": {
  "lang": "ja", "other": "en/", "other_label": "English",
  "nav": ("ホーム", "プライバシーポリシー", "利用規約", "サポート"),
  "index": ("DOTEI", """<p><img class="icon" src="{root}icon.png" alt=""></p>
<p class="poem">僕の前に道はない<br>僕の後ろに道は出来る</p><p>高村光太郎「道程」</p>
<p>DOTEI は、あなたが歩いた道だけを、墨の線で地図に残す iPhone アプリです。</p>
<ul><li>Google マップのタイムライン・ヘルスケアのワークアウト・GPX ファイルから、これまでの道を何年分でも取り込めます</li>
<li>同じ道は墨が重なって濃くなり、はじめて通る道は朱で描かれます</li>
<li>年を選ぶと、その年に歩いた道だけが残ります</li>
<li>記録はこの iPhone の中だけ。アカウント登録もいりません</li>
<li>はじめの 7 日間は無料、そのあとは買い切り（月額はありません）</li></ul>"""),
  "privacy": ("プライバシーポリシー", f"""<p>このポリシーは、iPhone アプリ「DOTEI」（以下「本アプリ」）で運営者が情報をどう扱うかを定めます。</p>
<h2>集める情報</h2><p>運営者は、本アプリから個人を特定できる情報を集めません。本アプリにはアカウント・広告・解析ツール・運営者のサーバーがありません。</p>
<h2>位置情報</h2><p>位置情報は、記録中に歩いた道を地図に描くためにだけ使います。記録した道は端末の中にだけ保存し、外部に送ることはありません。記録中は画面を閉じても位置情報を使い、iPhone の画面上部に使用中の表示が出ます。記録していないときは位置情報を使いません（地図で現在地を表示するときを除く）。</p>
<h2>ヘルスケア</h2><p>ヘルスケアからの取り込みを選んだときだけ、ワークアウトとワークアウトの経路を読み取ります。読み取った経路は地図に描くためにだけ使い、端末の中にだけ保存します。ヘルスケアへの書き込みはしません。ヘルスケアのデータを広告・販売・第三者への提供に使うことはありません。</p>
<h2>取り込んだファイル</h2><p>Google マップのタイムラインや GPX のファイルは、あなたが選んだときだけ読み込み、端末の中で道のりに直して保存します。ファイルの中身を外部に送ることはありません。</p>
<h2>地図</h2><p>実際の地図を重ねて表示するときは、Apple のマップのデータを使います。Apple のマップの扱いは Apple のプライバシーポリシーに従います。</p>
<h2>購入</h2><p>無料体験と買い切りの購入は Apple の App Store で処理されます。運営者は支払いの情報を受け取りません。</p>
<h2>消す方法</h2><p>本アプリの［設定］→［すべての記録を消す］で、記録をすべて消せます。1 本ずつ消すこともできます。本アプリを削除すると、すべてのデータが消えます。</p>
<h2>変更</h2><p>このポリシーを変えるときは、このページで知らせます。</p>
<h2>問い合わせ</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>制定: 2026 年 11 月 3 日</p>"""),
  "terms": ("利用規約", f"""<p>この規約は、iPhone アプリ「DOTEI」（以下「本アプリ」）の利用条件を定めます。本アプリを使うことで、この規約に同意したものとします。</p>
<h2>本アプリの内容</h2><p>本アプリは、歩いた道と取り込んだ記録を地図に描くものです。位置情報の誤差や取り込み元の記録の粗さにより、線が実際の道とずれることがあります。道案内や安全の確認には使わないでください。</p>
<h2>安全</h2><p>歩きながら画面を見続けないでください。交通ルールと周りの安全を守り、私有地や立入禁止の場所に入らないでください。本アプリの利用中に起きたけがや事故について、運営者は責任を負いません。</p>
<h2>無料体験と買い切り</h2><p>はじめの 7 日間は、App Store で ¥0 の「7日間無料トライアル」を購入することで、記録と取り込みをすべて使えます。7 日が過ぎても自動で課金されることはありません。そのあと記録と取り込みを続けるには、買い切りの購入が必要です。買い切りは一度の支払いで、月額や年額の支払いはありません。購入しなくても、それまでに描いた地図と記録は見られます。返金は Apple の規定に従います。</p>
<h2>禁止事項</h2><p>本アプリの改変・再配布・逆コンパイル、法令や公序良俗に反する使い方を禁じます。</p>
<h2>変更と終了</h2><p>運営者は、本アプリの内容やこの規約を変えたり、提供を終えたりすることがあります。</p>
<h2>準拠法</h2><p>この規約は日本の法律に従います。</p>
<h2>問い合わせ</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>制定: 2026 年 11 月 3 日</p>"""),
  "support": ("サポート", f"""<h2>Google マップの記録を取り込むには</h2><ol><li>iPhone の Google マップを開き、右上の自分のアイコンを押します</li><li>［設定］→［個人的なコンテンツ］（または［位置情報とプライバシー］）を開きます</li><li>［タイムラインのデータをエクスポート］を押し、［ファイルに保存］で保存します</li><li>DOTEI の［記録］→［取り込む］→［Google マップのタイムライン］→［ファイルを選ぶ］で選びます</li></ol>
<p>パソコンの Google データエクスポート（Takeout）の Records.json や、Semantic Location History の月ごとのファイルも選べます。zip のときは、ファイルアプリで展開してから選んでください。</p>
<p>試しに取り込める見本: <a href="sample/Timeline.json">Timeline.json</a>・<a href="sample/walk.gpx">walk.gpx</a>（架空の散歩です）</p>
<h2>ヘルスケアの記録が見つからないとき</h2><p>iPhone の設定アプリ →［ヘルスケア］→［データアクセスとデバイス］→［DOTEI］で、ワークアウトとワークアウトの経路をオンにしてください。経路が残るのは、屋外のウォーキング・ランニング・ハイキング・サイクリングなどのワークアウトです。</p>
<h2>画面を閉じても記録を続けるには</h2><p>位置情報を［このAppの使用中のみ許可］にしたまま、［歩きはじめる］を押してから画面を閉じてください。記録中は画面上部に位置情報の表示が出ます。</p>
<h2>購入を復元するには</h2><p>［設定］→［購入を復元］を押してください。</p>
<h2>記録を消すには</h2><p>［記録］から 1 本ずつ、または［設定］→［すべての記録を消す］で消せます。記録はこの iPhone の中にだけあります。</p>
<h2>問い合わせ</h2><p>ご意見・不具合は <a href="mailto:{MAIL}">{MAIL}</a> までお送りください。</p>"""),
 },
 "en": {
  "lang": "en", "other": "../", "other_label": "日本語",
  "nav": ("Home", "Privacy Policy", "Terms", "Support"),
  "index": ("DOTEI", """<p><img class="icon" src="{root}icon.png" alt=""></p>
<p class="poem">There is no road ahead of me.<br>Behind me, a road is made.</p><p>Kōtarō Takamura, “Dōtei (The Journey)”</p>
<p>DOTEI is an iPhone app that draws only the streets you have walked, in ink, on a blank map.</p>
<ul><li>Import years of past walks from Google Maps Timeline, Health workouts and GPX files</li>
<li>Streets you walk again grow darker; streets you walk for the first time turn vermilion</li>
<li>Pick a year to see only the streets you walked that year</li>
<li>Your records stay on your iPhone. No account needed</li>
<li>Free for the first 7 days, then a one-time purchase (no subscription)</li></ul>"""),
  "privacy": ("Privacy Policy", f"""<p>This policy describes how the iPhone app “DOTEI” (the App) handles information.</p>
<h2>What we collect</h2><p>We do not collect any personal information from the App. The App has no accounts, ads, analytics or servers of ours.</p>
<h2>Location</h2><p>Location is used only to draw the streets you walk while recording. Recorded walks are stored only on your device and never sent anywhere. While recording, location is used with the screen off and iPhone shows the location indicator. Location is not used when you are not recording (except to show your position on the map).</p>
<h2>Health</h2><p>Only when you choose to import from Health does the App read your workouts and workout routes. Routes are used only to draw your map and are stored only on the device. The App does not write to Health. Health data is never used for advertising, sold, or shared with third parties.</p>
<h2>Imported files</h2><p>Google Maps Timeline and GPX files are read only when you choose them, converted to walks on the device and stored there. Their contents are never sent anywhere.</p>
<h2>Maps</h2><p>When you show the real map, the App uses Apple Maps data, which is handled under Apple's privacy policy.</p>
<h2>Purchases</h2><p>The free trial and the one-time purchase are processed by Apple's App Store. We do not receive payment information.</p>
<h2>Deleting data</h2><p>Settings &gt; Delete all records removes everything; you can also delete walks one by one. Deleting the App removes all data.</p>
<h2>Changes</h2><p>We will post any changes to this policy on this page.</p>
<h2>Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>Effective: November 3, 2026</p>"""),
  "terms": ("Terms of Use", f"""<p>These terms govern your use of the iPhone app “DOTEI” (the App). By using the App you agree to them.</p>
<h2>What the App does</h2><p>The App draws the streets you walk and the records you import on a map. Lines may differ from the actual streets because of GPS error or coarse source data. Do not use the App for navigation or safety decisions.</p>
<h2>Safety</h2><p>Don't keep looking at the screen while walking. Follow traffic rules, stay aware of your surroundings, and do not enter private or restricted areas. We are not responsible for injuries or accidents while using the App.</p>
<h2>Free trial and one-time purchase</h2><p>For the first 7 days, purchasing the free “7-day Trial” in the App Store unlocks recording and importing. You are never charged automatically when the 7 days end. To keep recording and importing after that, a one-time purchase is required; there are no monthly or yearly fees. Without buying, you can still view the map and records you made. Refunds follow Apple's policies.</p>
<h2>Prohibited use</h2><p>Do not modify, redistribute or decompile the App, or use it unlawfully.</p>
<h2>Changes and termination</h2><p>We may change the App or these terms, or stop providing the App.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of Japan.</p>
<h2>Contact</h2><p><a href="mailto:{MAIL}">{MAIL}</a></p><p>Effective: November 3, 2026</p>"""),
  "support": ("Support", f"""<h2>Importing from Google Maps</h2><ol><li>Open Google Maps on your iPhone and tap your profile picture at the top right</li><li>Open Settings &gt; Personal content (or Location &amp; privacy)</li><li>Tap Export Timeline data and choose Save to Files</li><li>In DOTEI, go to Walks &gt; Import &gt; Google Maps Timeline &gt; Choose a file</li></ol>
<p>Records.json and the monthly Semantic Location History files from Google Takeout work too. If you have a .zip, unzip it in the Files app first.</p>
<p>Samples to try: <a href="../sample/Timeline.json">Timeline.json</a> and <a href="../sample/walk.gpx">walk.gpx</a> (fictional walks)</p>
<h2>If no Health workouts are found</h2><p>Go to Settings &gt; Health &gt; Data Access &amp; Devices &gt; DOTEI and turn on Workouts and Workout Routes. Routes are saved for outdoor walks, runs, hikes and rides.</p>
<h2>Recording with the screen off</h2><p>Keep location access at “While Using the App”, tap Start walking, then lock your phone. The location indicator shows while recording.</p>
<h2>Restoring purchases</h2><p>Settings &gt; Restore Purchases.</p>
<h2>Deleting records</h2><p>Delete walks one by one from Walks, or all at once in Settings &gt; Delete all records. Records exist only on this iPhone.</p>
<h2>Contact</h2><p>Send feedback or bug reports to <a href="mailto:{MAIL}">{MAIL}</a>.</p>"""),
 },
}
FILES = {"index": "index.html", "privacy": "privacy.html", "terms": "terms.html", "support": "support.html"}


SITE = "https://dotei.process-craft-ai.com"


def page_url(folder, name):
    path = "" if folder == "." else folder + "/"
    return f"{SITE}/{path}{'' if name == 'index.html' else name}"


APP_STORE = "https://apps.apple.com/jp/app/id6830070527"
META = {
 "ja": {"home": "DOTEI｜歩いた道だけを描く散歩の地図アプリ", "locale": "ja_JP",
        "index": "DOTEI は、歩いた道だけを和紙の地図に墨の線で残す iPhone アプリ。Google マップのタイムライン・ヘルスケア・GPX から過去の道も取り込めます。はじめての道は朱。7 日間無料、そのあとは買い切り。",
        "privacy": "DOTEI のプライバシーポリシー。位置情報・ヘルスケア・取り込んだファイルはすべて端末の中だけで扱います。",
        "terms": "DOTEI の利用規約。7 日間の無料体験と買い切りの購入、安全に使うための注意について。",
        "support": "DOTEI のサポート。Google マップのタイムラインやヘルスケアの記録の取り込み方、購入の復元、記録の消し方。"},
 "en": {"home": "DOTEI | A walking map that draws only the streets you have walked", "locale": "en_US",
        "index": "DOTEI is an iPhone app that draws only the streets you have walked, in ink, on a blank map. Import past walks from Google Maps Timeline, Health and GPX. Free for 7 days, then a one-time purchase.",
        "privacy": "DOTEI privacy policy. Location, Health data and imported files stay on your iPhone.",
        "terms": "DOTEI terms of use, including the 7-day free trial, the one-time purchase and safety.",
        "support": "DOTEI support: importing Google Maps Timeline and Health workouts, restoring purchases and deleting records."},
}


def home_json_ld():
    """トップの構造化データ。Google は WebSite の name を検索結果のサイト名に使う"""
    publisher = {"@type": "Organization", "name": "Process Craft AI", "url": "https://process-craft-ai.com/"}
    graph = [
        {"@type": "WebSite", "name": "DOTEI", "alternateName": ["ドウテイ", "道程", "DOTEI - 歩いた道だけの地図"],
         "url": f"{SITE}/", "inLanguage": "ja", "publisher": publisher},
        {"@type": "SoftwareApplication", "name": "DOTEI", "alternateName": "DOTEI - 歩いた道だけの地図",
         "operatingSystem": "iOS", "applicationCategory": "TravelApplication",
         "offers": {"@type": "Offer", "price": "0", "priceCurrency": "JPY"},
         "url": f"{SITE}/", "downloadUrl": APP_STORE, "sameAs": [APP_STORE],
         "image": f"{SITE}/icon-512.png", "publisher": publisher},
    ]
    data = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)
    return f'<script type="application/ld+json">{data}</script>'


def head_meta(lang, kind, title, url):
    """description・OGP・twitter:card・ファビコン。トップ（日本語）には構造化データも足す"""
    m = META[lang]
    desc = m[kind]
    tags = [f'<meta name="description" content="{desc}">', '<meta property="og:site_name" content="DOTEI">',
            f'<meta property="og:type" content="website"><meta property="og:locale" content="{m["locale"]}">',
            f'<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">',
            f'<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/icon-512.png">',
            '<meta name="twitter:card" content="summary">',
            '<link rel="icon" href="/favicon.ico" sizes="48x48">',
            '<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">',
            '<link rel="apple-touch-icon" href="/apple-touch-icon.png">']
    if lang == "ja" and kind == "index":
        tags.append(home_json_ld())
    return "\n".join(tags)


def page(p, kind, root, url):
    title, body = p[kind]
    links = " ".join(f'<a href="{FILES[k]}">{label}</a>' for k, label in zip(FILES, p["nav"]))
    head_title = META[p["lang"]]["home"] if kind == "index" else f"{title} | DOTEI"
    return f"""<!doctype html><html lang="{p['lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{head_title}</title><link rel="canonical" href="{url}">
{head_meta(p["lang"], kind, head_title, url)}
<link rel="stylesheet" href="{root}style.css"></head><body><main>
<nav>{links} <a href="{p['other']}{FILES[kind]}">{p['other_label']}</a></nav>
<h1>{title}</h1><div class="bar"></div>{body.replace('{root}', root)}
<footer>© 2026 Process Craft AI</footer></main></body></html>
"""


def sample_gpx():
    """見本の道のりの 1 本を GPX にする（時刻つき）"""
    from datetime import datetime, timedelta
    walk = json.load(open(os.path.join(DEMO, "walks.json")))[5]
    start = datetime.fromisoformat(walk["start"].replace("Z", "+00:00"))
    span = (datetime.fromisoformat(walk["end"].replace("Z", "+00:00")) - start).total_seconds()
    n = len(walk["points"])
    points = "\n".join(
        f'<trkpt lat="{lat:.7f}" lon="{lon:.7f}"><time>{(start + timedelta(seconds=span * i / max(1, n - 1))).strftime("%Y-%m-%dT%H:%M:%SZ")}</time></trkpt>'
        for i, (lat, lon) in enumerate(walk["points"]))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="DOTEI sample" xmlns="http://www.topografix.com/GPX/1/1">
<trk><name>Sample walk</name><type>walking</type><trkseg>
{points}
</trkseg></trk></gpx>
"""


def main():
    open("style.css", "w").write(CSS)
    os.makedirs("en", exist_ok=True)
    os.makedirs("sample", exist_ok=True)
    for lang, root, folder in (("ja", "", "."), ("en", "../", "en")):
        for kind, name in FILES.items():
            open(os.path.join(folder, name), "w").write(page(PAGES[lang], kind, root, page_url(folder, name)))
    shutil.copy(os.path.join(DEMO, "Timeline.json"), "sample/Timeline.json")
    open("sample/walk.gpx", "w").write(sample_gpx())
    open(".nojekyll", "w").write("")
    write_sitemap()


def write_sitemap():
    """全ページの sitemap.xml と、その場所を書いた robots.txt を出す"""
    urls = [page_url(folder, name) for folder in (".", "en") for name in FILES.values()]
    locs = "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
    open("sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n'
                                   f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{locs}</urlset>\n')
    open("robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    main()
