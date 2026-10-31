import argparse,json,re
from pathlib import Path
RULES=[["author","\\b(author|creator|owner)\\s*[:=]","info"],["timestamp","\\b(created|modified|timestamp|date)\\s*[:=]","info"],["location","\\b(gps|latitude|longitude|coordinates)\\s*[:=]","review"]]
def analyze_text(text):
 out=[]
 for rule,pattern,severity in RULES:
  for m in re.finditer(pattern,text,re.I): out.append({"rule":rule,"severity":severity,"line":text.count("\\n",0,m.start())+1,"match":m.group(0)[:120]})
 return out
def main():
 p=argparse.ArgumentParser(description="Review exported text for metadata-like fields");p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args()
 if not a.input.is_file(): p.error("input file not found")
 findings=analyze_text(a.input.read_text(encoding="utf-8",errors="replace"));report={"tool":"metadata-inspector","count":len(findings),"findings":findings};data=json.dumps(report,indent=2,ensure_ascii=False)
 if a.output:a.output.write_text(data+"\\n",encoding="utf-8")
 print(data)
if __name__=="__main__":main()
