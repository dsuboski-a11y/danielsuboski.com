import json, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

OUT=Path("fortuna/live.json")
def get(url):
    req=urllib.request.Request(url,headers={"User-Agent":"FortunaDashboard/1.0"})
    with urllib.request.urlopen(req,timeout=20) as r:
        return r.read()

def clean_title(s):
    return re.sub(r"\s+-\s+[^-]{2,40}$","",s).strip()

data={"updatedAt":datetime.now(timezone.utc).isoformat().replace("+00:00","Z"),"locationLabel":"Victoria, BC","headlines":[],"events":[]}
try:
    q=urllib.parse.quote("artificial intelligence when:2d")
    xml=get("https://news.google.com/rss/search?q="+q+"&hl=en-CA&gl=CA&ceid=CA:en")
    root=ET.fromstring(xml)
    for item in root.findall(".//item")[:10]:
        title=item.findtext("title","").strip()
        link=item.findtext("link","").strip()
        pub=item.findtext("pubDate","").strip()
        source=item.find("source")
        source_name=(source.text if source is not None else "AI news").strip()
        data["headlines"].append({"title":clean_title(title),"source":source_name,"date":pub,"url":link})
except Exception as e:
    pass

if OUT.exists():
    try:
        old=json.loads(OUT.read_text(encoding="utf-8"))
        data["events"]=old.get("events",[])
        if not data["headlines"]:
            data["headlines"]=old.get("headlines",[])
    except Exception:
        pass
OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
